# AI OR HUMAN? — PIXELPALOOZA FESTIVAL GAME 🎮

> **"REAL OR GENERATED? YOU DECIDE."**  
> An interactive, fast-paced festival mini-game built for Pixelpalooza (GDG on Campus × NMIMS Navi Mumbai). Test your ability to distinguish AI-generated creations from genuine human reality across photographs, digital art, code snippets, viral tweets, reviews, emails, and literature.

---

## ⚡ Quick Start

```bash
# 1. Install dependencies
npm install

# 2. Run the game locally
npm run dev
```

Open your browser at:
👉 **`http://localhost:3000`**

---

## 🕹️ Game Overview & Core Mechanic

- **One piece of content per round** (Never show all questions at once).
- **Mixed Content Pool:**
  - 📸 **Photographs & Digital Art** (Real photos & museum masterworks vs Midjourney & Stable Diffusion generations).
  - 💬 **Social Media Posts** (Real viral human tweets vs synthetic corporate/engagement posts).
  - ⭐ **Customer Reviews** (Real idiosyncratic user complaints vs formulaic LLM praise).
  - 💻 **Code Snippets** (Real human hacks with TODOs vs defensive, boilerplate LLM functions).
  - ✍️ **Poems & Short Fiction** (Grounded human verse vs rhyming LLM tropes).
  - 📧 **Emails & Headlines** (Real workplace banter vs AI cold sales copy).

- **Difficulty Progression:**
  - **Rounds 1–3:** *Easy* (distinctive hallmarks).
  - **Rounds 4–7:** *Medium* (requires closer inspection).
  - **Rounds 8–10:** *Hard* (subtle, highly convincing nuances).

---

## 🕹️ Flow

1. **Start Screen:**
   - Select game length: **5 Rounds** or **10 Rounds** (Default: 10).
   - Click **`[ ENTER THE ARENA ⚡ ]`** (or press `Space`).
2. **Gameplay:**
   - The hero content card is displayed with its category and difficulty pill.
   - Question: **`WAS THIS CREATED BY...`**
   - Click **`[ 🤖 AI ]`** (Key: `A`) or **`[ 👤 HUMAN ]`** (Key: `H`).
3. **Instant Feedback (In-Place Transformation):**
   - **Correct:** 🎉 `+1 POINT` with celebratory confetti.
   - **Wrong:** 💀 `+0 POINTS` with comical screen shake.
   - **Why?** Concise explanation highlighting specific visual cues, prompt artifacts, or human quirks, along with source attribution.
   - Click **`[ NEXT → ]`** (or press `Space` / `N`).
4. **Final Result:**
   - Score out of 5 or 10 with accuracy percentage.
   - Dynamic tier commentary based on score:
     - **10/10:** *"YOU'RE BASICALLY AN AI DETECTOR. 🤖"*
     - **8–9:** *"OKAY, THAT WAS IMPRESSIVE. 🔥"*
     - **6–7:** *"NOT BAD. YOU CAUGHT MOST OF THEM."*
     - **4–5:** *"THE MACHINES GOT YOU A FEW TIMES. 😭"*
     - **0–3:** *"AI JUST COOKED YOU. 💀"*
   - **Round Recap:** Inspect each item played during the match to see the full explanation.
   - **`[ PLAY AGAIN ]`** (reshuffles fresh items and restarts without page reload) or **`[ CHANGE ROUNDS ]`**.

---

## ⌨️ Keyboard Controls

| Key | Action |
|:---:|:---|
| <kbd>A</kbd> | Choose **AI** |
| <kbd>H</kbd> | Choose **HUMAN** |
| <kbd>SPACE</kbd> | **START GAME** / Advance to **NEXT** |
| <kbd>N</kbd> | Advance to **NEXT** |
| <kbd>R</kbd> | **RESTART** Game Session |

---

## 📁 Architecture & Local Dataset

- **`/public/content/`** — Authentic offline image assets (verified AI generations + verified human photographs/paintings).
- **`/src/data/content.json` & `/data/content.json`** — 32 handcrafted items with categories, difficulty ratings, correct answers, and educational explanations.
- **`src/components/StartScreen.jsx`** — Pixelpalooza landing page matching the Stitch design.
- **`src/components/GameplayScreen.jsx`** — Dynamic card renderer (images, code, tweets, reviews, poems) with in-place reveal.
- **`src/components/GameOverScreen.jsx`** — Final score and match breakdown.
- **`src/utils/sound.js`** — 100% offline Web Audio API sound synthesizer (no external audio files needed).
