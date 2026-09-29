import React, { useState, useEffect } from 'react';
import confetti from 'canvas-confetti';
import { Bot, User, ArrowRight, RotateCcw, Sparkles, Star, Terminal, Mail, MessageSquare, Newspaper, BookOpen, Image as ImageIcon } from 'lucide-react';
import { sound } from '../utils/sound';

export default function GameplayScreen({
  item,
  currentIndex,
  totalRounds,
  score,
  onAnswer,
  onNext,
  onRestart,
  gameState, // 'PLAYING' | 'ANSWERED'
  lastResult // { selected: 'ai'|'human', isCorrect: boolean }
}) {
  const [imageLoaded, setImageLoaded] = useState(false);

  useEffect(() => {
    setImageLoaded(false);
  }, [currentIndex]);

  const handleSelect = (choice) => {
    if (gameState !== 'PLAYING') return;
    const isCorrect = choice === item.answer;

    if (isCorrect) {
      sound.playCorrect();
      confetti({
        particleCount: 70,
        spread: 80,
        origin: { y: 0.65 },
        colors: ['#00e5ff', '#ff007a', '#facc15', '#22c55e']
      });
    } else {
      sound.playWrong();
    }

    onAnswer(choice);
  };

  const handleNextClick = () => {
    sound.playBlip();
    onNext();
  };

  // Helper to get category icon
  const getCategoryIcon = (category) => {
    switch (category) {
      case 'photograph':
      case 'artwork':
        return <ImageIcon className="w-4 h-4" />;
      case 'code_snippet':
        return <Terminal className="w-4 h-4" />;
      case 'social_post':
        return <MessageSquare className="w-4 h-4" />;
      case 'review':
        return <Star className="w-4 h-4 fill-amber-400 text-amber-400" />;
      case 'email':
        return <Mail className="w-4 h-4" />;
      case 'news_headline':
        return <Newspaper className="w-4 h-4" />;
      case 'poem':
      case 'fictional_writing':
      case 'product_description':
        return <BookOpen className="w-4 h-4" />;
      default:
        return <Sparkles className="w-4 h-4" />;
    }
  };

  return (
    <div className="flex flex-col items-center justify-between min-h-[82vh] max-w-4xl mx-auto px-4 py-3 w-full">
      {/* Top Status & Segmented Progress Bar */}
      <div className="w-full bg-[#111422]/90 backdrop-blur-md rounded-2xl border border-white/10 p-3 sm:p-4 mb-4 flex flex-col gap-3">
        <div className="flex items-center justify-between text-xs sm:text-sm font-black">
          {/* Round Indicator */}
          <div className="flex items-center gap-2">
            <span className="font-mono text-[#00e5ff] text-xs sm:text-sm tracking-wider uppercase">
              ROUND {String(currentIndex + 1).padStart(2, '0')} / {String(totalRounds).padStart(2, '0')}
            </span>
          </div>

          {/* Score Counter */}
          <div className="flex items-center gap-3">
            <div className="flex items-center gap-2 px-3 py-1 bg-yellow-500/10 border border-yellow-500/30 rounded-xl text-yellow-300 font-mono font-bold">
              <span>SCORE</span>
              <span className="text-white text-base font-black">{String(score).padStart(2, '0')}</span>
            </div>

            {/* Quick Restart */}
            <button
              onClick={() => { sound.playBlip(); onRestart(); }}
              className="p-1.5 rounded-lg bg-white/5 border border-white/10 hover:bg-white/15 text-gray-400 hover:text-white transition-all cursor-pointer"
              title="Restart Game (R)"
            >
              <RotateCcw className="w-4 h-4" />
            </button>
          </div>
        </div>

        {/* Segmented Progress Bar */}
        <div className="grid gap-1.5 w-full" style={{ gridTemplateColumns: `repeat(${totalRounds}, minmax(0, 1fr))` }}>
          {Array.from({ length: totalRounds }).map((_, idx) => {
            const isCompleted = idx < currentIndex;
            const isCurrent = idx === currentIndex;
            return (
              <div
                key={idx}
                className={`h-2 rounded-full transition-all duration-300 ${
                  isCurrent
                    ? 'bg-[#00e5ff] shadow-[0_0_10px_#00e5ff]'
                    : isCompleted
                    ? 'bg-white/40'
                    : 'bg-white/10'
                }`}
              />
            );
          })}
        </div>
      </div>

      {/* Main Content Card */}
      <div className="w-full flex-1 flex flex-col items-center justify-center max-w-3xl relative">
        <div className="relative w-full bg-[#111422] rounded-2xl border-2 border-white/15 shadow-2xl overflow-hidden flex flex-col">
          {/* Card Header Pills */}
          <div className="flex items-center justify-between px-5 py-3 bg-black/60 border-b border-white/10 text-xs font-bold">
            <div className="flex items-center gap-2 text-[#00e5ff] uppercase tracking-wider font-mono">
              {getCategoryIcon(item.category)}
              <span>{item.category.replace('_', ' ')}</span>
            </div>
            <div className="flex items-center gap-2">
              <span className={`px-2.5 py-0.5 rounded-full text-[10px] font-mono font-bold uppercase tracking-wider ${
                item.difficulty === 'easy' ? 'bg-green-500/20 text-green-300 border border-green-500/40' :
                item.difficulty === 'medium' ? 'bg-yellow-500/20 text-yellow-300 border border-yellow-500/40' :
                'bg-rose-500/20 text-rose-300 border border-rose-500/40'
              }`}>
                {item.difficulty}
              </span>
            </div>
          </div>

          {/* Content Body */}
          <div className="p-5 sm:p-7 flex flex-col items-center justify-center min-h-[260px] sm:min-h-[300px]">
            {/* 1. IMAGE CONTENT */}
            {item.type === 'image' && (
              <div className="relative w-full h-[40vh] sm:h-[44vh] flex items-center justify-center bg-black/80 rounded-xl overflow-hidden p-2">
                <img
                  src={item.file}
                  alt={item.title}
                  onLoad={() => setImageLoaded(true)}
                  className={`max-h-full max-w-full object-contain rounded-lg transition-all duration-300 ${
                    imageLoaded ? 'opacity-100 scale-100' : 'opacity-0 scale-95'
                  }`}
                />
                {!imageLoaded && (
                  <div className="absolute inset-0 flex items-center justify-center text-gray-500 font-mono text-xs">
                    Loading content...
                  </div>
                )}
              </div>
            )}

            {/* 2. CODE SNIPPET CONTENT */}
            {item.type === 'code' && (
              <div className="w-full bg-[#0a0d18] rounded-xl border border-white/15 overflow-hidden text-left font-mono">
                <div className="flex items-center justify-between px-4 py-2 bg-black/50 border-b border-white/10 text-xs text-gray-400">
                  <div className="flex items-center gap-1.5">
                    <span className="w-2.5 h-2.5 rounded-full bg-red-500/80" />
                    <span className="w-2.5 h-2.5 rounded-full bg-yellow-500/80" />
                    <span className="w-2.5 h-2.5 rounded-full bg-green-500/80" />
                  </div>
                  <span className="text-[11px] uppercase tracking-wider font-bold text-gray-400">
                    {item.language || 'code'}
                  </span>
                </div>
                <pre className="p-4 sm:p-5 text-sm sm:text-base text-cyan-200 overflow-x-auto leading-relaxed">
                  <code>{item.content}</code>
                </pre>
              </div>
            )}

            {/* 3. TEXT / SOCIAL / REVIEW / EMAIL CONTENT */}
            {item.type === 'text' && (
              <div className="w-full text-left">
                {/* Social Post Styling */}
                {item.category === 'social_post' && (
                  <div className="bg-black/50 border border-white/10 rounded-2xl p-5">
                    <div className="flex items-center gap-3 mb-3">
                      <div className="w-10 h-10 rounded-full bg-gradient-to-tr from-cyan-500 to-pink-500 flex items-center justify-center font-bold text-white text-sm">
                        @
                      </div>
                      <div>
                        <div className="flex items-center gap-1.5 font-bold text-white text-sm">
                          <span>User</span>
                          <span className="text-[#00e5ff] text-xs">✓</span>
                        </div>
                        <span className="text-gray-400 text-xs font-mono">@user_feed</span>
                      </div>
                    </div>
                    <p className="text-base sm:text-lg text-white font-medium leading-relaxed">
                      "{item.content}"
                    </p>
                  </div>
                )}

                {/* Product Review Styling */}
                {item.category === 'review' && (
                  <div className="bg-black/50 border border-white/10 rounded-2xl p-5">
                    <div className="flex items-center gap-1 mb-3">
                      {Array.from({ length: 5 }).map((_, i) => (
                        <Star key={i} className="w-4 h-4 fill-amber-400 text-amber-400" />
                      ))}
                      <span className="ml-2 text-xs font-bold text-gray-400 font-mono">Verified Purchase</span>
                    </div>
                    <p className="text-base sm:text-lg text-gray-100 font-medium leading-relaxed">
                      "{item.content}"
                    </p>
                  </div>
                )}

                {/* Email Styling */}
                {item.category === 'email' && (
                  <div className="bg-black/50 border border-white/10 rounded-2xl p-5 font-sans">
                    <div className="border-b border-white/10 pb-3 mb-3 text-xs text-gray-400 flex flex-col gap-1 font-mono">
                      <div><strong className="text-gray-300">Subject:</strong> {item.title}</div>
                    </div>
                    <div className="text-sm sm:text-base text-gray-200 whitespace-pre-line leading-relaxed">
                      {item.content}
                    </div>
                  </div>
                )}

                {/* News Headline Styling */}
                {item.category === 'news_headline' && (
                  <div className="bg-black/60 border border-white/10 rounded-2xl p-6 text-center">
                    <span className="inline-block px-3 py-1 bg-red-600/30 border border-red-500/50 text-red-300 rounded text-xs font-mono font-bold uppercase tracking-wider mb-4">
                      BREAKING NEWS
                    </span>
                    <h3 className="text-xl sm:text-2xl md:text-3xl font-black text-white font-display leading-snug">
                      "{item.content}"
                    </h3>
                  </div>
                )}

                {/* Poem / Literature Styling */}
                {(item.category === 'poem' || item.category === 'fictional_writing') && (
                  <div className="bg-black/40 border border-white/10 rounded-2xl p-6 text-center">
                    <p className="text-base sm:text-lg md:text-xl text-gray-100 italic leading-relaxed whitespace-pre-line font-serif">
                      "{item.content}"
                    </p>
                  </div>
                )}

                {/* Advertisement / Product Description Styling */}
                {(item.category === 'advertisement' || item.category === 'product_description') && (
                  <div className="bg-black/50 border border-white/10 rounded-2xl p-6">
                    <span className="text-xs font-mono font-bold text-[#00e5ff] uppercase tracking-wider block mb-2">
                      MARKETING COPY
                    </span>
                    <p className="text-base sm:text-lg text-white font-medium leading-relaxed">
                      "{item.content}"
                    </p>
                  </div>
                )}
              </div>
            )}
          </div>
        </div>
      </div>

      {/* Decision / Reveal Area */}
      <div className="w-full max-w-3xl mt-4">
        {gameState === 'PLAYING' ? (
          <div className="flex flex-col items-center gap-3">
            <h3 className="text-lg sm:text-xl font-black text-white tracking-widest uppercase">
              WAS THIS CREATED BY...
            </h3>

            {/* Two HUGE Choice Buttons */}
            <div className="grid grid-cols-2 gap-4 sm:gap-6 w-full">
              {/* 🤖 AI Button */}
              <button
                onClick={() => handleSelect('ai')}
                className="group relative flex flex-col sm:flex-row items-center justify-center gap-2 sm:gap-3 py-5 sm:py-6 px-4 bg-[#ff007a] hover:bg-[#ff1493] text-white font-black text-2xl sm:text-3xl rounded-2xl shadow-[0_0_25px_rgba(255,0,122,0.4)] cursor-pointer active:scale-95 transition-all"
              >
                <Bot className="w-8 h-8 transition-transform group-hover:scale-110" />
                <span>AI</span>
                <span className="hidden sm:inline-block ml-1 px-2 py-0.5 bg-black/30 rounded text-xs font-mono text-pink-200 border border-pink-300/30">
                  KEY: A
                </span>
              </button>

              {/* 👤 HUMAN Button */}
              <button
                onClick={() => handleSelect('human')}
                className="group relative flex flex-col sm:flex-row items-center justify-center gap-2 sm:gap-3 py-5 sm:py-6 px-4 bg-[#00e5ff] hover:bg-[#38e8ff] text-black font-black text-2xl sm:text-3xl rounded-2xl shadow-[0_0_25px_rgba(0,229,255,0.4)] cursor-pointer active:scale-95 transition-all"
              >
                <User className="w-8 h-8 transition-transform group-hover:scale-110" />
                <span>HUMAN</span>
                <span className="hidden sm:inline-block ml-1 px-2 py-0.5 bg-black/20 rounded text-xs font-mono text-slate-900 border border-black/20">
                  KEY: H
                </span>
              </button>
            </div>
          </div>
        ) : (
          /* ANSWERED State Reveal */
          <div className={`w-full rounded-2xl border-2 p-5 sm:p-6 flex flex-col gap-3 transition-all ${
            lastResult?.isCorrect
              ? 'bg-gradient-to-r from-emerald-950/90 to-green-950/90 border-green-500 shadow-[0_0_30px_rgba(34,197,94,0.3)]'
              : 'bg-gradient-to-r from-rose-950/90 to-red-950/90 border-rose-500 shadow-[0_0_30px_rgba(244,63,94,0.3)] animate-shake'
          }`}>
            <div className="flex flex-col sm:flex-row items-start sm:items-center justify-between gap-3">
              <div className="flex items-center gap-3">
                <span className="text-3xl sm:text-4xl">
                  {lastResult?.isCorrect ? '🎉' : '💀'}
                </span>
                <div>
                  <h4 className={`text-2xl sm:text-3xl font-black tracking-tight ${
                    lastResult?.isCorrect ? 'text-green-400' : 'text-rose-400'
                  }`}>
                    {lastResult?.isCorrect ? 'CORRECT!' : 'GOT FOOLED!'}
                  </h4>
                  <p className="text-xs sm:text-sm text-gray-200 font-semibold mt-0.5">
                    {lastResult?.isCorrect
                      ? `This was ${item.answer.toUpperCase()}-${item.answer === 'ai' ? 'GENERATED' : 'CREATED'}.`
                      : `This was actually ${item.answer.toUpperCase()}-${item.answer === 'ai' ? 'GENERATED' : 'CREATED'}.`
                    }
                  </p>
                </div>
              </div>

              {/* Point Badge */}
              <div className={`px-4 py-1.5 rounded-xl font-mono font-black text-base sm:text-lg border ${
                lastResult?.isCorrect ? 'bg-green-400 text-black border-green-300' : 'bg-rose-500 text-white border-rose-400'
              }`}>
                {lastResult?.isCorrect ? '+1 POINT' : '+0 POINTS'}
              </div>
            </div>

            {/* Explanation Box */}
            <div className="bg-black/60 rounded-xl p-3.5 border border-white/10 text-sm text-gray-200 font-medium leading-relaxed">
              <span className="font-bold text-yellow-400 font-mono uppercase text-xs tracking-wider block mb-1">
                WHY?
              </span>
              {item.explanation}
              {item.source && (
                <span className="block text-xs font-mono text-gray-400 mt-2">
                  Source: {item.source}
                </span>
              )}
            </div>

            {/* NEXT Button */}
            <button
              onClick={handleNextClick}
              className="w-full flex items-center justify-center gap-3 py-4 px-6 bg-[#00e5ff] hover:bg-[#38e8ff] active:scale-98 text-black font-black text-xl sm:text-2xl rounded-xl shadow-[0_0_20px_rgba(0,229,255,0.4)] uppercase tracking-wider cursor-pointer transition-all"
            >
              <span>{currentIndex + 1 >= totalRounds ? 'SEE FINAL SCORE' : 'NEXT'}</span>
              <ArrowRight className="w-6 h-6" />
              <span className="hidden sm:inline-block text-xs font-mono font-bold bg-black/20 px-2.5 py-0.5 rounded">
                SPACE / N
              </span>
            </button>
          </div>
        )}
      </div>
    </div>
  );
}
