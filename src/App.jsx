import React, { useState, useEffect, useCallback } from 'react';
import { ArrowLeft, Cpu, Trophy, User } from 'lucide-react';
import StartScreen from './components/StartScreen';
import GameplayScreen from './components/GameplayScreen';
import GameOverScreen from './components/GameOverScreen';
import contentPool from './data/content.json';

// Fisher-Yates array shuffler
function shuffleArray(array) {
  const arr = [...array];
  for (let i = arr.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [arr[i], arr[j]] = [arr[j], arr[i]];
  }
  return arr;
}

export default function App() {
  const [totalRounds, setTotalRounds] = useState(10);
  const [screen, setScreen] = useState('START'); // 'START' | 'PLAYING' | 'ANSWERED' | 'FINISHED'
  const [selectedItems, setSelectedItems] = useState([]);
  const [currentIndex, setCurrentIndex] = useState(0);
  const [score, setScore] = useState(0);
  const [userAnswers, setUserAnswers] = useState([]);
  const [lastResult, setLastResult] = useState(null);

  // Generate a balanced game with increasing difficulty:
  // Rounds 1-3: Easy, Rounds 4-7: Medium, Rounds 8-10: Hard
  const startNewGame = useCallback((rounds = totalRounds) => {
    const easyItems = shuffleArray(contentPool.filter(i => i.difficulty === 'easy'));
    const mediumItems = shuffleArray(contentPool.filter(i => i.difficulty === 'medium'));
    const hardItems = shuffleArray(contentPool.filter(i => i.difficulty === 'hard'));

    let sessionItems = [];
    if (rounds === 5) {
      sessionItems = [
        ...easyItems.slice(0, 1),
        ...mediumItems.slice(0, 2),
        ...hardItems.slice(0, 2)
      ];
    } else {
      sessionItems = [
        ...easyItems.slice(0, 2),
        ...mediumItems.slice(0, 4),
        ...hardItems.slice(0, 4)
      ];
    }

    // Safety fallback if pool counts differ
    if (sessionItems.length < rounds) {
      const remaining = shuffleArray(contentPool.filter(i => !sessionItems.includes(i)));
      sessionItems = [...sessionItems, ...remaining.slice(0, rounds - sessionItems.length)];
    }

    setSelectedItems(sessionItems);
    setCurrentIndex(0);
    setScore(0);
    setUserAnswers([]);
    setLastResult(null);
    setScreen('PLAYING');
  }, [totalRounds]);

  const handleAnswer = useCallback((choice) => {
    if (screen !== 'PLAYING') return;

    const currentItem = selectedItems[currentIndex];
    const isCorrect = choice === currentItem.answer;

    if (isCorrect) {
      setScore(prev => prev + 1);
    }

    setUserAnswers(prev => [...prev, choice]);
    setLastResult({
      selected: choice,
      isCorrect
    });
    setScreen('ANSWERED');
  }, [screen, selectedItems, currentIndex]);

  const handleNext = useCallback(() => {
    if (currentIndex + 1 >= selectedItems.length) {
      setScreen('FINISHED');
    } else {
      setCurrentIndex(prev => prev + 1);
      setLastResult(null);
      setScreen('PLAYING');
    }
  }, [currentIndex, selectedItems.length]);

  // Global Keyboard Shortcuts
  useEffect(() => {
    const handleKeyDown = (e) => {
      if (['INPUT', 'TEXTAREA'].includes(document.activeElement?.tagName)) return;

      const key = e.key.toLowerCase();

      // Space key
      if (e.code === 'Space') {
        e.preventDefault();
        if (screen === 'START') {
          startNewGame();
        } else if (screen === 'ANSWERED') {
          handleNext();
        }
        return;
      }

      // 'A' key for AI
      if (key === 'a' && screen === 'PLAYING') {
        e.preventDefault();
        handleAnswer('ai');
        return;
      }

      // 'H' key for HUMAN
      if (key === 'h' && screen === 'PLAYING') {
        e.preventDefault();
        handleAnswer('human');
        return;
      }

      // 'N' key for NEXT
      if (key === 'n' && screen === 'ANSWERED') {
        e.preventDefault();
        handleNext();
        return;
      }

      // 'R' key for RESTART
      if (key === 'r') {
        e.preventDefault();
        startNewGame();
        return;
      }
    };

    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, [screen, startNewGame, handleAnswer, handleNext]);

  return (
    <div className="min-h-screen bg-[#080914] text-white flex flex-col justify-between selection:bg-[#ff007a] selection:text-white font-sans antialiased">
      {/* 1. Global Pixelpalooza Top Navbar (Matching Stitch Screenshot) */}
      <header className="w-full border-b border-white/10 bg-black/60 backdrop-blur-md sticky top-0 z-50 px-4 sm:px-8 py-3">
        <div className="max-w-7xl mx-auto flex items-center justify-between">
          {/* Left: Back & Brand */}
          <div className="flex items-center gap-6">
            <button
              onClick={() => setScreen('START')}
              className="text-gray-400 hover:text-white font-bold text-xs flex items-center gap-1.5 transition-colors cursor-pointer"
            >
              <ArrowLeft className="w-3.5 h-3.5" />
              <span className="hidden sm:inline">BACK TO PIXELPALOOZA</span>
            </button>

            <div className="flex items-center gap-2 border-l border-white/10 pl-4 sm:pl-6">
              <span className="font-pixel text-xs sm:text-sm text-white font-black tracking-tight">
                PIXELPAL...
              </span>
              <span className="text-[10px] text-gray-500 font-mono hidden md:inline">
                Where ideas...
              </span>
            </div>

            {/* Navigation Tabs */}
            <nav className="hidden lg:flex items-center gap-1 pl-4">
              <span className="bg-[#00e5ff] text-black font-black text-xs px-3.5 py-1.5 rounded-md tracking-wider">
                ARENA
              </span>
              <span className="text-gray-400 font-bold text-xs px-3 py-1.5 hover:text-white cursor-pointer">
                LEADERBOARD
              </span>
              <span className="text-gray-400 font-bold text-xs px-3 py-1.5 hover:text-white cursor-pointer">
                STAGES
              </span>
              <span className="text-gray-400 font-bold text-xs px-3 py-1.5 hover:text-white cursor-pointer">
                RULES
              </span>
            </nav>
          </div>

          {/* Right: Badges & Profile */}
          <div className="flex items-center gap-3">
            <div className="hidden sm:flex items-center gap-1.5 px-3 py-1 rounded-full bg-white/5 border border-white/10 text-[11px] font-mono text-gray-300">
              <span className="w-2 h-2 rounded-full bg-emerald-400" />
              <span>GDG ON CAMPUS × NMIMS NAVI MUMBAI</span>
            </div>

            <div className="flex items-center gap-1.5 px-3 py-1 rounded-full bg-rose-500/10 border border-rose-500/30 text-[11px] font-mono font-bold text-rose-300">
              <span className="w-2 h-2 rounded-full bg-rose-500 animate-ping" />
              <span>LIVE ARENA</span>
            </div>

            <div className="w-8 h-8 rounded-full bg-gradient-to-tr from-cyan-400 to-pink-500 flex items-center justify-center p-0.5">
              <div className="w-full h-full bg-[#111422] rounded-full flex items-center justify-center text-gray-300">
                <User className="w-4 h-4" />
              </div>
            </div>
          </div>
        </div>
      </header>

      {/* Main Container */}
      <div className="max-w-7xl mx-auto w-full px-4 sm:px-6 py-4 flex-1 flex flex-col justify-start">
        {/* 2. Secondary Attraction HUD Banner (Matching Stitch Screenshot) */}
        <div className="w-full bg-[#111422]/90 border border-white/10 rounded-2xl p-4 sm:p-5 mb-4 flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4 backdrop-blur-md shadow-lg">
          <div className="flex items-center gap-3.5">
            <div className="w-10 h-10 rounded-xl bg-cyan-500/10 border border-cyan-500/30 text-[#00e5ff] flex items-center justify-center">
              <Cpu className="w-5 h-5" />
            </div>
            <div>
              <div className="flex items-center gap-2 mb-0.5">
                <span className="bg-[#ff0055] text-white text-[10px] font-black px-2 py-0.5 rounded tracking-wider uppercase">
                  ATTRACTION 05
                </span>
                <span className="text-[#00e5ff] font-mono text-xs font-bold tracking-wider">
                  TURING BUNKER // ARENA
                </span>
              </div>
              <h2 className="text-white font-extrabold text-base sm:text-lg tracking-tight">
                AI OR HUMAN? — REALITY CHECK
              </h2>
            </div>
          </div>

          <div className="flex items-center gap-3 self-end sm:self-auto">
            {/* Live Score Display */}
            <div className="flex items-center gap-2.5 px-4 py-2 bg-black/60 rounded-xl border border-white/10 text-xs font-mono font-bold">
              <Trophy className="w-4 h-4 text-yellow-400" />
              <span className="text-gray-400 uppercase tracking-widest text-[11px]">SCORE</span>
              <span className="text-xl font-black text-white font-mono leading-none">
                {String(score).padStart(2, '0')}
              </span>
            </div>

            {/* Hotkeys Pill */}
            <div className="hidden md:flex items-center gap-2 px-3 py-2 bg-black/40 rounded-xl border border-white/10 text-xs font-mono text-gray-400">
              <span><strong className="text-white">A</strong> AI</span>
              <span>·</span>
              <span><strong className="text-white">H</strong> Human</span>
              <span>·</span>
              <span><strong className="text-white">Space</strong> Next</span>
            </div>
          </div>
        </div>

        {/* 3. Screen Switcher */}
        <main className="w-full flex-1 flex flex-col items-center justify-center">
          {screen === 'START' && (
            <StartScreen
              totalRounds={totalRounds}
              setTotalRounds={setTotalRounds}
              onStart={() => startNewGame()}
            />
          )}

          {(screen === 'PLAYING' || screen === 'ANSWERED') && selectedItems.length > 0 && (
            <GameplayScreen
              item={selectedItems[currentIndex]}
              currentIndex={currentIndex}
              totalRounds={selectedItems.length}
              score={score}
              onAnswer={handleAnswer}
              onNext={handleNext}
              onRestart={() => startNewGame()}
              gameState={screen}
              lastResult={lastResult}
            />
          )}

          {screen === 'FINISHED' && (
            <GameOverScreen
              score={score}
              totalRounds={selectedItems.length}
              playedItems={selectedItems}
              userAnswers={userAnswers}
              onPlayAgain={() => startNewGame()}
              onHome={() => setScreen('START')}
            />
          )}
        </main>
      </div>

      {/* 4. Global Footer (Matching Stitch Screenshot) */}
      <footer className="w-full border-t border-white/10 bg-black/70 backdrop-blur-md py-3 px-4 sm:px-8 text-xs font-mono text-gray-500">
        <div className="max-w-7xl mx-auto flex flex-col sm:flex-row items-center justify-between gap-2">
          <div className="flex items-center gap-2">
            <span className="font-pixel text-[11px] text-white">PIXELPALOOZA</span>
            <span>•</span>
            <span>POWERED BY GDG ON CAMPUS NMIMS NAVI MUMBAI</span>
          </div>

          <div className="flex items-center gap-3">
            <span className="text-amber-400 font-bold flex items-center gap-1.5">
              <span className="w-1.5 h-1.5 rounded-full bg-amber-400" />
              AI VS HUMAN MINI-GAME ENGINE
            </span>
            <span>•</span>
            <span>© 2025 All Rights Reserved</span>
          </div>
        </div>
      </footer>
    </div>
  );
}
