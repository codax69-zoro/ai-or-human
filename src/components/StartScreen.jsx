import React from 'react';
import { Zap, Bot, MonitorPlay, Sparkles } from 'lucide-react';
import { sound } from '../utils/sound';

export default function StartScreen({
  totalRounds,
  setTotalRounds,
  onStart
}) {
  const handleSelectRounds = (rounds) => {
    sound.playBlip();
    setTotalRounds(rounds);
  };

  const handleStart = () => {
    sound.playBlip();
    onStart();
  };

  return (
    <div className="flex flex-col items-center justify-center min-h-[75vh] py-6 px-4 text-center max-w-4xl mx-auto w-full">
      {/* College / Organization Pill Badge */}
      <div className="inline-flex items-center gap-2 px-4 py-1.5 rounded-full bg-amber-500/10 border border-amber-500/40 text-amber-300 font-mono text-xs sm:text-sm tracking-wider mb-6">
        <span className="w-2 h-2 rounded-full bg-amber-400 animate-ping" />
        <span className="font-bold">GDG ON CAMPUS NMIMS NAVI MUMBAI</span>
      </div>

      {/* Main Massive Title */}
      <h1 className="text-6xl sm:text-8xl md:text-9xl font-black tracking-tight text-white mb-3 font-display uppercase leading-none drop-shadow-[0_10px_25px_rgba(0,0,0,0.8)]">
        AI OR HUMAN?
      </h1>

      {/* Subtitle */}
      <p className="text-xl sm:text-2xl md:text-3xl font-extrabold text-[#00e5ff] tracking-widest mb-6 uppercase drop-shadow-[0_0_15px_rgba(0,229,255,0.4)]">
        REAL OR GENERATED? YOU DECIDE.
      </p>

      {/* Description Paragraph */}
      <p className="text-sm sm:text-base md:text-lg text-gray-300 max-w-2xl leading-relaxed mb-8 font-medium">
        Can you spot what was synthesized by Midjourney, ChatGPT & Claude vs raw human reality? 
        From photographs and digital artwork to code snippets, viral tweets, poems, and everyday internet text.
      </p>

      {/* Round Selection */}
      <div className="flex flex-col items-center gap-3 mb-8">
        <span className="text-xs font-mono font-bold tracking-widest text-gray-400 uppercase">
          SELECT GAME LENGTH
        </span>
        <div className="inline-flex items-center gap-3 p-1.5 bg-black/60 backdrop-blur-md rounded-2xl border border-white/10">
          <button
            onClick={() => handleSelectRounds(5)}
            className={`px-6 py-2.5 rounded-xl font-black text-sm tracking-wider transition-all cursor-pointer ${
              totalRounds === 5
                ? 'bg-[#00e5ff] text-black shadow-[0_0_20px_rgba(0,229,255,0.4)] scale-105'
                : 'text-gray-400 hover:text-white hover:bg-white/5'
            }`}
          >
            5 ROUNDS
          </button>
          <button
            onClick={() => handleSelectRounds(10)}
            className={`px-6 py-2.5 rounded-xl font-black text-sm tracking-wider transition-all cursor-pointer ${
              totalRounds === 10
                ? 'bg-[#00e5ff] text-black shadow-[0_0_20px_rgba(0,229,255,0.4)] scale-105'
                : 'text-gray-400 hover:text-white hover:bg-white/5'
            }`}
          >
            10 ROUNDS
          </button>
        </div>
      </div>

      {/* Big Action CTA Button */}
      <button
        onClick={handleStart}
        className="group relative inline-flex items-center justify-center gap-3 px-12 sm:px-16 py-5 sm:py-6 bg-[#00e5ff] hover:bg-[#38e8ff] active:scale-95 text-black font-black text-2xl sm:text-3xl rounded-2xl shadow-[0_0_35px_rgba(0,229,255,0.6)] cursor-pointer transition-all uppercase tracking-wider mb-3"
      >
        <span>ENTER THE ARENA</span>
        <Zap className="w-7 h-7 sm:w-8 sm:h-8 fill-black transition-transform group-hover:rotate-12" />
      </button>

      <span className="text-xs font-mono font-bold text-gray-500 tracking-widest uppercase mb-12">
        OR PRESS [SPACEBAR] TO LAUNCH
      </span>

      {/* 3 Bottom Feature Cards (Matching Pixelpalooza screenshot) */}
      <div className="grid grid-cols-1 sm:grid-cols-3 gap-4 w-full max-w-4xl text-left">
        <div className="flex items-start gap-4 p-5 rounded-2xl bg-[#111422]/90 border border-white/10 backdrop-blur-md">
          <div className="p-2.5 rounded-xl bg-amber-500/10 text-amber-400 border border-amber-500/20">
            <Zap className="w-5 h-5" />
          </div>
          <div>
            <h4 className="text-white font-extrabold text-sm sm:text-base uppercase tracking-wide">
              1 PT PER CALL
            </h4>
            <p className="text-xs text-gray-400 mt-0.5 leading-relaxed">
              Instant score calculations & verdicts after each guess.
            </p>
          </div>
        </div>

        <div className="flex items-start gap-4 p-5 rounded-2xl bg-[#111422]/90 border border-white/10 backdrop-blur-md">
          <div className="p-2.5 rounded-xl bg-pink-500/10 text-pink-400 border border-pink-500/20">
            <Bot className="w-5 h-5" />
          </div>
          <div>
            <h4 className="text-white font-extrabold text-sm sm:text-base uppercase tracking-wide">
              100+ CHALLENGES
            </h4>
            <p className="text-xs text-gray-400 mt-0.5 leading-relaxed">
              Massive pool of photographs, digital art, code, tweets & prose.
            </p>
          </div>
        </div>

        <div className="flex items-start gap-4 p-5 rounded-2xl bg-[#111422]/90 border border-white/10 backdrop-blur-md">
          <div className="p-2.5 rounded-xl bg-cyan-500/10 text-cyan-400 border border-cyan-500/20">
            <MonitorPlay className="w-5 h-5" />
          </div>
          <div>
            <h4 className="text-white font-extrabold text-sm sm:text-base uppercase tracking-wide">
              AUDITORIUM READY
            </h4>
            <p className="text-xs text-gray-400 mt-0.5 leading-relaxed">
              Optimized for stage projector, desktop & mobile gameplay.
            </p>
          </div>
        </div>
      </div>
    </div>
  );
}
