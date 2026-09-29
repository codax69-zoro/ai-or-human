import React, { useEffect, useState } from 'react';
import confetti from 'canvas-confetti';
import { RotateCcw, Home, Trophy, CheckCircle2, XCircle, Sparkles, Bot, User } from 'lucide-react';
import { sound } from '../utils/sound';

export default function GameOverScreen({
  score,
  totalRounds,
  playedItems,
  userAnswers,
  onPlayAgain,
  onHome
}) {
  const [selectedItemForDetail, setSelectedItemForDetail] = useState(null);
  const percentage = Math.round((score / totalRounds) * 100);

  // Exact dynamic tier quotes specified by user
  const getFunnyResult = () => {
    if (score === totalRounds) {
      return {
        quote: "YOU'RE BASICALLY AN AI DETECTOR. 🤖",
        title: "PERFECT SCORE!",
        color: "text-emerald-400",
        border: "border-emerald-500",
        glow: "shadow-[0_0_40px_rgba(34,197,94,0.3)]"
      };
    }
    if (score >= Math.round(totalRounds * 0.8)) {
      return {
        quote: "OKAY, THAT WAS IMPRESSIVE. 🔥",
        title: "SURVIVED THE SYNTHETIC AGE!",
        color: "text-[#00e5ff]",
        border: "border-[#00e5ff]",
        glow: "shadow-[0_0_40px_rgba(0,229,255,0.3)]"
      };
    }
    if (score >= Math.round(totalRounds * 0.6)) {
      return {
        quote: "NOT BAD. YOU CAUGHT MOST OF THEM.",
        title: "SOLID EFFORT!",
        color: "text-yellow-400",
        border: "border-yellow-500",
        glow: "shadow-[0_0_40px_rgba(234,179,8,0.3)]"
      };
    }
    if (score >= Math.round(totalRounds * 0.4)) {
      return {
        quote: "THE MACHINES GOT YOU A FEW TIMES. 😭",
        title: "ALMOST CAUGHT OUT!",
        color: "text-orange-400",
        border: "border-orange-500",
        glow: "shadow-[0_0_40px_rgba(249,115,22,0.3)]"
      };
    }
    return {
      quote: "AI JUST COOKED YOU. 💀",
      title: "MATRIX CONQUERED YOU!",
      color: "text-rose-500",
      border: "border-rose-500",
      glow: "shadow-[0_0_40px_rgba(244,63,94,0.3)]"
    };
  };

  const result = getFunnyResult();

  useEffect(() => {
    sound.playVictory();
    if (score >= totalRounds * 0.6) {
      confetti({
        particleCount: 90,
        spread: 100,
        origin: { y: 0.5 },
        colors: ['#00e5ff', '#ff007a', '#facc15', '#22c55e']
      });
    }
  }, [score, totalRounds]);

  return (
    <div className="flex flex-col items-center justify-center min-h-[82vh] max-w-4xl mx-auto px-4 py-6 text-center">
      {/* Result Card */}
      <div className={`p-6 sm:p-8 rounded-3xl bg-[#111422] border-2 ${result.border} ${result.glow} w-full mb-6 relative overflow-hidden`}>
        <div className="inline-flex items-center gap-2 px-4 py-1.5 rounded-full bg-white/10 text-white font-mono text-xs font-bold tracking-wider mb-4">
          <Trophy className="w-4 h-4 text-yellow-400" />
          GAME OVER
        </div>

        <h2 className="text-3xl sm:text-5xl font-black text-white tracking-tight mb-2 uppercase">
          {result.title}
        </h2>

        {/* Big Score Display */}
        <div className="my-6">
          <span className="text-xs sm:text-sm font-mono font-bold text-gray-400 uppercase tracking-widest block mb-1">
            YOUR SCORE
          </span>
          <div className="text-7xl sm:text-9xl font-black font-display text-transparent bg-clip-text bg-gradient-to-r from-yellow-300 via-pink-400 to-[#00e5ff] drop-shadow-[0_4px_15px_rgba(0,0,0,0.8)]">
            {score} <span className="text-4xl sm:text-6xl text-gray-500 font-bold">/ {totalRounds}</span>
          </div>
          <div className="mt-3 inline-block px-4 py-1 bg-white/10 rounded-full font-mono text-xs sm:text-sm font-bold text-white">
            {percentage}% ACCURACY
          </div>
        </div>

        {/* Dynamic Fun Quote */}
        <div className={`text-xl sm:text-2xl font-black ${result.color} tracking-wide max-w-xl mx-auto px-6 py-4 bg-black/50 rounded-2xl border border-white/10 mb-8`}>
          "{result.quote}"
        </div>

        {/* Action Buttons */}
        <div className="flex flex-wrap items-center justify-center gap-4">
          <button
            onClick={() => { sound.playBlip(); onPlayAgain(); }}
            className="flex items-center justify-center gap-2 px-8 sm:px-10 py-4 bg-[#00e5ff] hover:bg-[#38e8ff] active:scale-95 text-black font-black text-xl rounded-xl shadow-[0_0_25px_rgba(0,229,255,0.4)] uppercase tracking-wider cursor-pointer transition-all"
          >
            <RotateCcw className="w-5 h-5" />
            PLAY AGAIN
          </button>

          <button
            onClick={() => { sound.playBlip(); onHome(); }}
            className="flex items-center justify-center gap-2 px-6 py-4 bg-white/10 hover:bg-white/20 active:scale-95 text-white font-bold text-base rounded-xl border border-white/20 transition-all cursor-pointer"
          >
            <Home className="w-5 h-5" />
            CHANGE ROUNDS
          </button>
        </div>
      </div>

      {/* Match Recap List */}
      <div className="w-full bg-[#111422] rounded-2xl border border-white/10 p-5 sm:p-6 text-left">
        <div className="flex items-center justify-between mb-4">
          <h4 className="text-base sm:text-lg font-black text-white flex items-center gap-2 uppercase tracking-wider">
            <Sparkles className="w-4 h-4 text-[#00e5ff]" />
            ROUND RECAP
          </h4>
          <span className="text-xs text-gray-400 font-mono">
            Click any row to inspect details
          </span>
        </div>

        <div className="flex flex-col gap-2">
          {playedItems.map((item, idx) => {
            const userChoice = userAnswers[idx];
            const isCorrect = userChoice === item.answer;

            return (
              <div
                key={item.id}
                onClick={() => setSelectedItemForDetail(item)}
                className={`flex items-center justify-between p-3 rounded-xl border cursor-pointer transition-all ${
                  isCorrect
                    ? 'bg-green-500/10 border-green-500/30 hover:bg-green-500/20'
                    : 'bg-rose-500/10 border-rose-500/30 hover:bg-rose-500/20'
                }`}
              >
                <div className="flex items-center gap-3">
                  <span className="font-mono text-xs text-gray-400 font-bold w-6">
                    #{String(idx + 1).padStart(2, '0')}
                  </span>
                  <div>
                    <h5 className="text-sm font-bold text-white">
                      {item.title}
                    </h5>
                    <span className="text-xs font-mono text-gray-400 uppercase">
                      {item.category.replace('_', ' ')} • {item.difficulty}
                    </span>
                  </div>
                </div>

                <div className="flex items-center gap-3">
                  <span className={`px-2.5 py-0.5 rounded-full text-xs font-mono font-bold uppercase flex items-center gap-1 ${
                    item.answer === 'ai' ? 'bg-pink-500/20 text-pink-300 border border-pink-500/40' : 'bg-cyan-500/20 text-cyan-300 border border-cyan-500/40'
                  }`}>
                    {item.answer === 'ai' ? <Bot className="w-3.5 h-3.5" /> : <User className="w-3.5 h-3.5" />}
                    {item.answer}
                  </span>
                  {isCorrect ? (
                    <CheckCircle2 className="w-5 h-5 text-green-400" />
                  ) : (
                    <XCircle className="w-5 h-5 text-rose-400" />
                  )}
                </div>
              </div>
            );
          })}
        </div>
      </div>

      {/* Inspect Item Modal */}
      {selectedItemForDetail && (
        <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/80 backdrop-blur-sm animate-pop">
          <div className="bg-[#111422] border-2 border-white/20 rounded-2xl max-w-lg w-full p-5 text-left relative flex flex-col gap-3">
            <div className="flex items-center justify-between">
              <span className={`px-3 py-1 rounded-full font-mono font-bold text-xs uppercase tracking-wider ${
                selectedItemForDetail.answer === 'ai' ? 'bg-pink-500 text-white' : 'bg-[#00e5ff] text-black'
              }`}>
                ACTUAL: {selectedItemForDetail.answer.toUpperCase()}
              </span>
              <button
                onClick={() => setSelectedItemForDetail(null)}
                className="text-gray-400 hover:text-white font-bold text-lg px-2 cursor-pointer"
              >
                ✕
              </button>
            </div>

            <h4 className="text-base font-bold text-white">
              {selectedItemForDetail.title}
            </h4>

            {selectedItemForDetail.type === 'image' && (
              <div className="w-full h-48 bg-black/80 rounded-xl overflow-hidden flex items-center justify-center p-2">
                <img
                  src={selectedItemForDetail.file}
                  alt={selectedItemForDetail.title}
                  className="max-h-full max-w-full object-contain"
                />
              </div>
            )}

            {selectedItemForDetail.type === 'code' && (
              <pre className="bg-black/60 p-3 rounded-xl border border-white/10 text-xs text-cyan-200 font-mono overflow-x-auto">
                <code>{selectedItemForDetail.content}</code>
              </pre>
            )}

            {selectedItemForDetail.type === 'text' && (
              <p className="bg-black/60 p-3 rounded-xl border border-white/10 text-sm text-gray-200 italic">
                "{selectedItemForDetail.content}"
              </p>
            )}

            <p className="text-xs sm:text-sm text-gray-300 bg-white/5 p-3 rounded-xl border border-white/10 leading-relaxed">
              <strong className="text-yellow-400">Explanation: </strong>
              {selectedItemForDetail.explanation}
            </p>

            <button
              onClick={() => setSelectedItemForDetail(null)}
              className="w-full py-2.5 bg-[#00e5ff] text-black font-black text-sm rounded-xl uppercase tracking-wider cursor-pointer"
            >
              CLOSE
            </button>
          </div>
        </div>
      )}
    </div>
  );
}
