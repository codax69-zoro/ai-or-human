import os

os.makedirs("public/memes", exist_ok=True)

memes = [
    {
        "id": "meme001",
        "bg": ["#0f0c1b", "#2b1055"],
        "badge": "🤖 PROMPT: CYBERPUNK 2077 VARANASI",
        "title": "NEO-VARANASI HOVER-AUTO",
        "elements": """
        <!-- Cyber Ganga River & Temple Skyline -->
        <path d="M0,450 C300,420 500,480 800,440 L800,600 L0,600 Z" fill="#070b19" />
        <path d="M0,480 C200,460 600,520 800,490 L800,600 L0,600 Z" fill="#0d1b3e" />
        <!-- Cyber Temples with Neon Silhouettes -->
        <polygon points="120,440 160,310 200,440" fill="#1b143f" stroke="#ff007a" stroke-width="2"/>
        <polygon points="145,310 160,250 175,310" fill="#ff007a" />
        <polygon points="220,440 250,340 280,440" fill="#141a45" stroke="#00f0ff" stroke-width="2"/>
        <polygon points="620,450 670,300 720,450" fill="#1b143f" stroke="#ff007a" stroke-width="2"/>
        <!-- Flying Auto-Rickshaw -->
        <g transform="translate(240, 160)">
          <!-- Neon Thrusters -->
          <ellipse cx="60" cy="190" rx="35" ry="12" fill="#00f0ff" filter="drop-shadow(0 0 15px #00f0ff)"/>
          <ellipse cx="260" cy="190" rx="35" ry="12" fill="#00f0ff" filter="drop-shadow(0 0 15px #00f0ff)"/>
          <path d="M40,195 L60,270 L80,195 Z" fill="url(#cyanFlame)"/>
          <path d="M240,195 L260,270 L280,195 Z" fill="url(#cyanFlame)"/>
          <!-- Yellow-Green Auto Body -->
          <path d="M50,150 L270,150 L290,100 L250,30 L90,30 L30,100 Z" fill="#facc15" stroke="#000" stroke-width="6"/>
          <path d="M40,150 L280,150 L270,185 L50,185 Z" fill="#15803d" stroke="#000" stroke-width="6"/>
          <!-- Windshield & Cyber HUD -->
          <polygon points="95,40 245,40 275,95 70,95" fill="#1e293b" opacity="0.85" stroke="#38bdf8" stroke-width="3"/>
          <circle cx="170" cy="70" r="18" fill="none" stroke="#ff007a" stroke-width="2" stroke-dasharray="4 2"/>
          <text x="170" y="74" fill="#ff007a" font-family="monospace" font-size="10" text-anchor="middle">HUD 2077</text>
          <!-- Headlight Beam -->
          <polygon points="50,120 0,220 0,160 30,115" fill="#fef08a" opacity="0.6"/>
          <!-- Digital Meter Sign -->
          <rect x="110" y="110" width="100" height="30" rx="5" fill="#000" stroke="#ef4444" stroke-width="2"/>
          <text x="160" y="130" fill="#22c55e" font-family="monospace" font-weight="bold" font-size="14" text-anchor="middle">METER: 9999 ₹</text>
        </g>
        <!-- Hinglish Comic Caption -->
        <rect x="220" y="490" width="360" height="48" rx="24" fill="#000" stroke="#00f0ff" stroke-width="3"/>
        <text x="400" y="522" fill="#fff" font-family="'Outfit', sans-serif" font-weight="900" font-size="18" text-anchor="middle">"BHAIYA GANGA CROSS KAROGE?"</text>
        """
    },
    {
        "id": "meme002",
        "bg": ["#111827", "#1f2937"],
        "badge": "🤖 MIDJOURNEY V6 GENERATION",
        "title": "ROBOT VS SABZIWALA BARGAIN",
        "elements": """
        <!-- Wooden Thela (Vegetable Cart) -->
        <rect x="80" y="320" width="640" height="180" rx="10" fill="#78350f" stroke="#000" stroke-width="5"/>
        <rect x="100" y="340" width="600" height="20" fill="#92400e"/>
        <!-- Veggies on Cart -->
        <circle cx="160" cy="305" r="28" fill="#ef4444" stroke="#000" stroke-width="3"/>
        <circle cx="205" cy="310" r="25" fill="#ef4444" stroke="#000" stroke-width="3"/>
        <circle cx="180" cy="275" r="24" fill="#dc2626" stroke="#000" stroke-width="3"/>
        <text x="180" y="345" fill="#fff" font-weight="bold" font-size="12" text-anchor="middle">TAMATAR</text>
        <!-- Coriander Bundle -->
        <ellipse cx="320" cy="290" rx="45" ry="30" fill="#15803d" stroke="#14532d" stroke-width="3"/>
        <text x="320" y="345" fill="#86efac" font-weight="bold" font-size="12" text-anchor="middle">FREE DHANIYA</text>
        <!-- Robot Figure (Left) with 7 Fingers -->
        <g transform="translate(180, 80)">
          <!-- Head -->
          <rect x="40" y="30" width="80" height="70" rx="15" fill="#94a3b8" stroke="#000" stroke-width="4"/>
          <circle cx="65" cy="65" r="10" fill="#00f0ff"/>
          <circle cx="95" cy="65" r="10" fill="#00f0ff"/>
          <rect x="60" y="85" width="40" height="5" fill="#000"/>
          <!-- 7-Fingered Metallic Hand Pointing -->
          <path d="M120,130 C150,140 180,180 200,200" stroke="#64748b" stroke-width="12" stroke-linecap="round"/>
          <!-- Multi fingers AI Glitch -->
          <line x1="200" y1="200" x2="225" y2="180" stroke="#94a3b8" stroke-width="4"/>
          <line x1="200" y1="200" x2="230" y2="190" stroke="#94a3b8" stroke-width="4"/>
          <line x1="200" y1="200" x2="232" y2="200" stroke="#94a3b8" stroke-width="4"/>
          <line x1="200" y1="200" x2="230" y2="210" stroke="#94a3b8" stroke-width="4"/>
          <line x1="200" y1="200" x2="225" y2="220" stroke="#94a3b8" stroke-width="4"/>
          <line x1="200" y1="200" x2="218" y2="230" stroke="#94a3b8" stroke-width="4"/>
          <line x1="200" y1="200" x2="210" y2="238" stroke="#94a3b8" stroke-width="4"/>
          <text x="250" y="180" fill="#ef4444" font-weight="900" font-size="13">⚠️ 7 FINGERS</text>
        </g>
        <!-- Dialogue Bubble -->
        <rect x="360" y="80" width="360" height="110" rx="16" fill="#fff" stroke="#000" stroke-width="4"/>
        <polygon points="410,190 390,230 440,190" fill="#fff" stroke="#000" stroke-width="4"/>
        <rect x="400" y="185" width="40" height="10" fill="#fff"/>
        <text x="540" y="125" fill="#000" font-family="'Outfit', sans-serif" font-weight="800" font-size="18" text-anchor="middle">"ERROR 404: DHANIYA MIRCHI</text>
        <text x="540" y="155" fill="#b91c1c" font-family="'Outfit', sans-serif" font-weight="900" font-size="20" text-anchor="middle">FREE NAHI DIYA TOH RIOT HO JAYEGA"</text>
        """
    },
    {
        "id": "meme003",
        "bg": ["#2e1065", "#172554"],
        "badge": "🤖 STABLE DIFFUSION XL DESI ART",
        "title": "MONA LISA IN BANARASI SAREE",
        "elements": """
        <!-- Ornate Mughal Arch Background -->
        <path d="M250,550 L250,220 C250,120 400,60 400,60 C400,60 550,120 550,220 L550,550 Z" fill="#4c1d95" stroke="#f59e0b" stroke-width="6"/>
        <!-- Saree & Portrait Silhouette -->
        <g transform="translate(280, 110)">
          <!-- Hair & Face -->
          <ellipse cx="120" cy="120" rx="60" ry="75" fill="#fed7aa" stroke="#000" stroke-width="4"/>
          <path d="M50,110 C50,40 190,40 190,110 C190,150 170,180 170,180 L70,180 Z" fill="#1e1b4b"/>
          <!-- Mona Lisa Face Features -->
          <ellipse cx="120" cy="120" rx="45" ry="55" fill="#ffedd5"/>
          <!-- Traditional Red Bindi -->
          <circle cx="120" cy="98" r="6" fill="#dc2626" stroke="#991b1b" stroke-width="1"/>
          <!-- Classic Smirk Eyes -->
          <ellipse cx="102" cy="115" rx="8" ry="4" fill="#000"/>
          <ellipse cx="138" cy="115" rx="8" ry="4" fill="#000"/>
          <!-- Signature Smirk Smile -->
          <path d="M106,145 Q120,155 136,143" fill="none" stroke="#7c2d12" stroke-width="3" stroke-linecap="round"/>
          <!-- Heavy Desi Gold Jhumkas (Earrings) -->
          <g fill="#fbbf24" stroke="#d97706" stroke-width="1.5">
            <circle cx="68" cy="135" r="8"/>
            <polygon points="60,145 76,145 68,165"/>
            <circle cx="172" cy="135" r="8"/>
            <polygon points="164,145 180,145 172,165"/>
          </g>
          <!-- Banarasi Crimson Red & Gold Pallu -->
          <path d="M40,175 C90,160 170,170 210,195 L230,340 L10,340 Z" fill="#b91c1c" stroke="#f59e0b" stroke-width="5"/>
          <path d="M60,190 L210,290" stroke="#fde047" stroke-width="8" stroke-dasharray="8 6"/>
          <!-- Gold Temple Necklace -->
          <path d="M90,165 Q120,190 150,165" fill="none" stroke="#f59e0b" stroke-width="6"/>
        </g>
        <rect x="200" y="480" width="400" height="50" rx="25" fill="#000" stroke="#f59e0b" stroke-width="3"/>
        <text x="400" y="512" fill="#fde047" font-family="'Outfit', sans-serif" font-weight="900" font-size="18" text-anchor="middle">"LE LOUVRE ❌ CHANDNI CHOWK ✔️"</text>
        """
    },
    {
        "id": "meme004",
        "bg": ["#082f49", "#0c4a6e"],
        "badge": "🤖 GENERATIVE AI: ABSURD PROMPT",
        "title": "UNDERWATER SCUBA BARAAT",
        "elements": """
        <!-- Ocean Floor & Bubbles -->
        <circle cx="120" cy="200" r="14" fill="#38bdf8" opacity="0.4"/>
        <circle cx="220" cy="140" r="22" fill="#38bdf8" opacity="0.5"/>
        <circle cx="680" cy="180" r="18" fill="#38bdf8" opacity="0.4"/>
        <circle cx="580" cy="110" r="28" fill="#38bdf8" opacity="0.6"/>
        <!-- Coral & Seaweed -->
        <path d="M0,520 Q60,450 120,530 T240,510 T400,540 T600,500 T800,530 L800,600 L0,600 Z" fill="#0369a1"/>
        <!-- Scuba Dhol Wala Center -->
        <g transform="translate(280, 160)">
          <!-- Oxygen Tank on Back -->
          <rect x="25" y="70" width="30" height="90" rx="12" fill="#facc15" stroke="#000" stroke-width="3"/>
          <!-- Orange Wedding Turban with Diving Mask -->
          <ellipse cx="120" cy="65" rx="55" ry="30" fill="#f97316" stroke="#000" stroke-width="4"/>
          <!-- Diving Goggles over Face -->
          <rect x="90" y="75" width="60" height="28" rx="8" fill="#38bdf8" stroke="#000" stroke-width="3" opacity="0.9"/>
          <!-- Oxygen Hose -->
          <path d="M45,90 C45,130 90,130 115,105" fill="none" stroke="#000" stroke-width="4"/>
          <!-- Traditional Kurta -->
          <path d="M60,110 L180,110 L200,230 L40,230 Z" fill="#ea580c" stroke="#000" stroke-width="4"/>
          <!-- Floating Underwater Dhol Drum -->
          <ellipse cx="120" cy="180" rx="70" ry="40" fill="#b45309" stroke="#000" stroke-width="5"/>
          <ellipse cx="60" cy="180" rx="15" ry="38" fill="#fde68a" stroke="#000" stroke-width="4"/>
          <ellipse cx="180" cy="180" rx="15" ry="38" fill="#fde68a" stroke="#000" stroke-width="4"/>
          <line x1="70" y1="145" x2="170" y2="215" stroke="#fef08a" stroke-width="3"/>
          <line x1="70" y1="215" x2="170" y2="145" stroke="#fef08a" stroke-width="3"/>
        </g>
        <!-- Floating Samosa with Air Bubbles -->
        <polygon points="620,240 680,240 650,200" fill="#f59e0b" stroke="#000" stroke-width="3"/>
        <text x="650" y="270" fill="#fef08a" font-weight="bold" font-size="12" text-anchor="middle">FLOATING SAMOSA</text>
        <rect x="180" y="490" width="440" height="50" rx="25" fill="#000" stroke="#38bdf8" stroke-width="3"/>
        <text x="400" y="522" fill="#fff" font-family="'Outfit', sans-serif" font-weight="900" font-size="18" text-anchor="middle">"NAAGIN DANCE AT 50 METERS DEPTH 🤿"</text>
        """
    },
    {
        "id": "meme005",
        "bg": ["#450a0a", "#7f1d1d"],
        "badge": "🤖 MIDJOURNEY GAMING CROSSOVER",
        "title": "SUPER MARIO AT DADAR STATION",
        "elements": """
        <!-- Station Platform Sign -->
        <rect x="220" y="50" width="360" height="60" fill="#1e3a8a" stroke="#ffffff" stroke-width="4"/>
        <text x="400" y="90" fill="#ffffff" font-family="'Outfit', sans-serif" font-weight="900" font-size="24" text-anchor="middle">दादर DADAR दादर</text>
        <!-- Mario Figure -->
        <g transform="translate(260, 140)">
          <!-- Red Cap -->
          <path d="M70,70 C70,10 200,10 210,70 L240,75 L230,95 L60,95 Z" fill="#dc2626" stroke="#000" stroke-width="4"/>
          <circle cx="140" cy="50" r="18" fill="#fff" stroke="#000" stroke-width="2"/>
          <text x="140" y="58" fill="#dc2626" font-family="'Outfit', sans-serif" font-weight="900" font-size="22" text-anchor="middle">M</text>
          <!-- Face & Big Nose -->
          <ellipse cx="145" cy="115" rx="45" ry="40" fill="#fbcfe8" stroke="#000" stroke-width="3"/>
          <ellipse cx="165" cy="115" rx="18" ry="14" fill="#f472b6" stroke="#000" stroke-width="3"/>
          <!-- Legendary Mustache -->
          <path d="M120,130 C135,115 155,145 175,130 C195,145 210,120 220,135 C205,155 130,155 120,130 Z" fill="#000"/>
          <!-- Blue Dungarees & Hand holding Vada Pav -->
          <rect x="80" y="160" width="120" height="110" fill="#2563eb" stroke="#000" stroke-width="4"/>
          <!-- Vada Pav held high -->
          <g transform="translate(190, 140)">
            <!-- Pav (Bread) -->
            <ellipse cx="40" cy="40" rx="36" ry="26" fill="#d97706" stroke="#000" stroke-width="3"/>
            <!-- Fried Vada Inside -->
            <circle cx="40" cy="43" r="22" fill="#eab308" stroke="#000" stroke-width="3"/>
            <!-- Spicy Green Chutney Drips -->
            <path d="M30,48 C30,62 38,62 38,48" fill="#16a34a"/>
            <path d="M46,47 C46,65 54,65 54,47" fill="#16a34a"/>
            <!-- Fried Green Chilli -->
            <path d="M55,30 Q75,10 65,5" stroke="#15803d" stroke-width="5" fill="none" stroke-linecap="round"/>
          </g>
        </g>
        <rect x="200" y="480" width="400" height="50" rx="25" fill="#000" stroke="#f59e0b" stroke-width="3"/>
        <text x="400" y="512" fill="#fbbf24" font-family="'Outfit', sans-serif" font-weight="900" font-size="18" text-anchor="middle">"MAMMA MIA! EXTRA SUKHA CHUTNEY DOH!"</text>
        """
    },
    {
        "id": "meme006",
        "bg": ["#022c22", "#064e3b"],
        "badge": "🤖 GENERATIVE AI: CODE MEETS DESI",
        "title": "DADI DEBUGGING PYTORCH AT 3 AM",
        "elements": """
        <!-- Matrix Code Waterfall in Background -->
        <g opacity="0.3" font-family="monospace" font-size="12" fill="#4ade80">
          <text x="80" y="80">loss.backward()</text>
          <text x="80" y="110">optimizer.step()</text>
          <text x="80" y="140">cuda:0 out of memory</text>
          <text x="600" y="90">epochs = 100</text>
          <text x="600" y="120">lr = 0.0001</text>
          <text x="600" y="150">batch_size = 64</text>
        </g>
        <!-- Dadi Profile -->
        <g transform="translate(240, 130)">
          <!-- Maroon Saree & Head Pallu -->
          <path d="M50,110 C50,20 180,20 200,110 L230,300 L30,300 Z" fill="#831843" stroke="#000" stroke-width="4"/>
          <circle cx="120" cy="110" r="50" fill="#fed7aa" stroke="#000" stroke-width="3"/>
          <!-- Silver Grey Hair Bun -->
          <circle cx="80" cy="65" r="22" fill="#cbd5e1" stroke="#000" stroke-width="2"/>
          <!-- Big Reading Glasses with Code Reflection -->
          <circle cx="105" cy="110" r="18" fill="#1e293b" stroke="#f59e0b" stroke-width="3"/>
          <circle cx="145" cy="110" r="18" fill="#1e293b" stroke="#f59e0b" stroke-width="3"/>
          <line x1="123" y1="110" x2="127" y2="110" stroke="#f59e0b" stroke-width="3"/>
          <text x="105" y="114" fill="#4ade80" font-family="monospace" font-size="9" text-anchor="middle">&gt;loss</text>
          <text x="145" y="114" fill="#4ade80" font-family="monospace" font-size="9" text-anchor="middle">&gt;0.01</text>
          <!-- Glowing Steel Glass of Cutting Chai -->
          <g transform="translate(240, 180)">
            <polygon points="10,20 35,20 30,70 15,70" fill="#cbd5e1" stroke="#000" stroke-width="2"/>
            <polygon points="13,30 32,30 29,65 16,65" fill="#b45309"/>
            <path d="M22,15 Q26,5 22,-5" stroke="#f59e0b" stroke-width="2" fill="none"/>
            <text x="23" y="85" fill="#fde047" font-size="10" font-weight="bold" text-anchor="middle">CHAI</text>
          </g>
        </g>
        <!-- Mechanical Keyboard on desk -->
        <rect x="180" y="410" width="440" height="60" rx="8" fill="#0f172a" stroke="#22c55e" stroke-width="3"/>
        <rect x="220" y="480" width="360" height="50" rx="25" fill="#000" stroke="#22c55e" stroke-width="3"/>
        <text x="400" y="512" fill="#4ade80" font-family="'Outfit', sans-serif" font-weight="900" font-size="18" text-anchor="middle">"BETA, OVERFITTING HO GAYA TERA"</text>
        """
    },
    {
        "id": "meme007",
        "bg": ["#030712", "#0f172a"],
        "badge": "🤖 DALL-E 3 ZERO-G BIRYANI",
        "title": "ASTRONAUT BIRYANI IN ZERO GRAVITY",
        "elements": """
        <!-- Earth View from Space Station Window -->
        <circle cx="400" cy="240" r="160" fill="#0284c7" stroke="#38bdf8" stroke-width="8" opacity="0.6"/>
        <path d="M300,160 Q380,180 430,220 Q480,260 410,360" fill="#15803d" opacity="0.7"/>
        <!-- Steel Tiffin Box in Space -->
        <g transform="translate(260, 160)">
          <!-- Tier 1 -->
          <ellipse cx="140" cy="70" rx="70" ry="24" fill="#cbd5e1" stroke="#000" stroke-width="3"/>
          <rect x="70" y="70" width="140" height="40" fill="#94a3b8" stroke="#000" stroke-width="3"/>
          <ellipse cx="140" cy="110" rx="70" ry="24" fill="#cbd5e1" stroke="#000" stroke-width="3"/>
          <!-- Dum Biryani Spilling Out in Zero G -->
          <ellipse cx="140" cy="68" rx="60" ry="18" fill="#d97706"/>
          <!-- Floating Spiced Rice Grains & Elaichi -->
          <ellipse cx="60" cy="-20" rx="14" ry="5" fill="#fef08a" stroke="#000" stroke-width="1.5" transform="rotate(-30 60 -20)"/>
          <ellipse cx="220" cy="-10" rx="15" ry="6" fill="#fef08a" stroke="#000" stroke-width="1.5" transform="rotate(45 220 -10)"/>
          <ellipse cx="150" cy="-50" rx="12" ry="5" fill="#f59e0b" stroke="#000" stroke-width="1.5"/>
          <!-- Floating Chicken Leg Piece Defying Physics -->
          <g transform="translate(230, 40) rotate(-25)">
            <ellipse cx="30" cy="20" rx="25" ry="16" fill="#9a3412" stroke="#000" stroke-width="2"/>
            <rect x="50" y="16" width="25" height="8" rx="4" fill="#f1f5f9" stroke="#000" stroke-width="2"/>
            <text x="30" y="45" fill="#f97316" font-weight="900" font-size="11">LEG PIECE</text>
          </g>
          <!-- Floating Rogue Cardamom (Elaichi) -->
          <ellipse cx="90" cy="-45" rx="8" ry="14" fill="#15803d" stroke="#000" stroke-width="2"/>
          <text x="90" y="-60" fill="#ef4444" font-weight="bold" font-size="11" text-anchor="middle">⚠️ ELAICHI</text>
        </g>
        <rect x="180" y="480" width="440" height="50" rx="25" fill="#000" stroke="#f59e0b" stroke-width="3"/>
        <text x="400" y="512" fill="#fbbf24" font-family="'Outfit', sans-serif" font-weight="900" font-size="18" text-anchor="middle">"NASA CANNOT PREVENT ELAICHI IN BITE"</text>
        """
    },
    {
        "id": "meme008",
        "bg": ["#18002e", "#2c0054"],
        "badge": "🤖 CYBER-DESI CONCEPT ART",
        "title": "CYBER SADHU FLOATING AT 2099 GHATS",
        "elements": """
        <!-- Neon Varanasi River & Holographic Pillars -->
        <rect x="0" y="420" width="800" height="180" fill="#080014"/>
        <line x1="0" y1="450" x2="800" y2="450" stroke="#a855f7" stroke-width="2" stroke-dasharray="12 6"/>
        <line x1="0" y1="500" x2="800" y2="500" stroke="#06b6d4" stroke-width="2" stroke-dasharray="20 10"/>
        <!-- Floating Cyber Sadhu in Padmasana -->
        <g transform="translate(270, 120)">
          <!-- Quantum Levitation Rings -->
          <ellipse cx="130" cy="270" rx="140" ry="25" fill="none" stroke="#00f0ff" stroke-width="4" opacity="0.8" filter="drop-shadow(0 0 10px #00f0ff)"/>
          <ellipse cx="130" cy="290" rx="100" ry="18" fill="none" stroke="#d946ef" stroke-width="3" opacity="0.6"/>
          <!-- Orange Robe Body -->
          <polygon points="130,120 70,250 190,250" fill="#ea580c" stroke="#000" stroke-width="4"/>
          <!-- Head & Beard -->
          <circle cx="130" cy="85" r="35" fill="#fed7aa" stroke="#000" stroke-width="3"/>
          <path d="M100,85 C100,150 160,150 160,85 Z" fill="#f8fafc" stroke="#000" stroke-width="3"/>
          <!-- Third Eye Hologram -->
          <polygon points="130,60 135,70 130,80 125,70" fill="#00f0ff" filter="drop-shadow(0 0 8px #00f0ff)"/>
          <!-- Holographic Rudraksha Mala floating around -->
          <circle cx="90" cy="140" r="7" fill="#fb923c" stroke="#00f0ff" stroke-width="2"/>
          <circle cx="105" cy="160" r="7" fill="#fb923c" stroke="#00f0ff" stroke-width="2"/>
          <circle cx="130" cy="170" r="8" fill="#fb923c" stroke="#00f0ff" stroke-width="2"/>
          <circle cx="155" cy="160" r="7" fill="#fb923c" stroke="#00f0ff" stroke-width="2"/>
          <circle cx="170" cy="140" r="7" fill="#fb923c" stroke="#00f0ff" stroke-width="2"/>
        </g>
        <rect x="200" y="480" width="400" height="50" rx="25" fill="#000" stroke="#a855f7" stroke-width="3"/>
        <text x="400" y="512" fill="#f0abfc" font-family="'Outfit', sans-serif" font-weight="900" font-size="18" text-anchor="middle">"PING 0.001 MS TO UNIVERSE SERVER"</text>
        """
    },
    {
        "id": "meme009",
        "bg": ["#2e1065", "#4c1d95"],
        "badge": "🤖 DEEPFAKE AI GENERATION",
        "title": "ELON MUSK IN PUNJABI KURTA",
        "elements": """
        <!-- Punjabi Wedding Marigold Garland Backdrop -->
        <g stroke="#f59e0b" stroke-width="8" stroke-dasharray="10 15">
          <line x1="80" y1="0" x2="80" y2="400"/>
          <line x1="200" y1="0" x2="200" y2="400"/>
          <line x1="600" y1="0" x2="600" y2="400"/>
          <line x1="720" y1="0" x2="720" y2="400"/>
        </g>
        <!-- Elon Figure Dancing Bhangra -->
        <g transform="translate(260, 110)">
          <!-- Golden Sherwani -->
          <path d="M90,130 L190,130 L220,310 L60,310 Z" fill="#eab308" stroke="#000" stroke-width="5"/>
          <line x1="140" y1="130" x2="140" y2="310" stroke="#ca8a04" stroke-width="6"/>
          <!-- Elon Face with Smug Smile -->
          <rect x="100" y="45" width="80" height="90" rx="35" fill="#ffedd5" stroke="#000" stroke-width="3"/>
          <ellipse cx="120" cy="75" rx="6" ry="4" fill="#1e293b"/>
          <ellipse cx="160" cy="75" rx="6" ry="4" fill="#1e293b"/>
          <path d="M125,100 Q140,112 155,100" stroke="#000" stroke-width="3" fill="none"/>
          <!-- Bhangra Hands Raised (AI Weird Extra Thumb) -->
          <!-- Left Arm -->
          <path d="M90,140 L30,60" stroke="#eab308" stroke-width="22" stroke-linecap="round"/>
          <circle cx="30" cy="50" r="14" fill="#fed7aa" stroke="#000" stroke-width="2"/>
          <!-- Right Arm with 6 fingers glitch -->
          <path d="M190,140 L250,60" stroke="#eab308" stroke-width="22" stroke-linecap="round"/>
          <circle cx="250" cy="50" r="14" fill="#fed7aa" stroke="#000" stroke-width="2"/>
          <text x="270" y="35" fill="#ef4444" font-weight="900" font-size="12">⚠️ AI EXTRA THUMB</text>
        </g>
        <rect x="180" y="480" width="440" height="50" rx="25" fill="#000" stroke="#eab308" stroke-width="3"/>
        <text x="400" y="512" fill="#fde047" font-family="'Outfit', sans-serif" font-weight="900" font-size="18" text-anchor="middle">"TUNAK TUNAK TUN ON MARS CONFIRMED"</text>
        """
    },
    {
        "id": "meme010",
        "bg": ["#1e293b", "#0f172a"],
        "badge": "🤖 BENGALURU SCI-FI AI MEME",
        "title": "FLYING CAR AT SILK BOARD JUNCTION",
        "elements": """
        <!-- Silk Board Signpost -->
        <rect x="200" y="40" width="400" height="70" rx="8" fill="#15803d" stroke="#fff" stroke-width="4"/>
        <text x="400" y="75" fill="#fff" font-family="'Outfit', sans-serif" font-weight="900" font-size="20" text-anchor="middle">SILK BOARD JUNCTION • 2099 AD</text>
        <text x="400" y="98" fill="#fde047" font-family="monospace" font-size="13" text-anchor="middle">AVERAGE WAIT TIME: 4 HOURS 32 MINS</text>
        <!-- Flying DeLorean Hovering in Gridlock -->
        <g transform="translate(250, 160)">
          <!-- Hover Jets -->
          <ellipse cx="60" cy="180" rx="40" ry="12" fill="#38bdf8" filter="drop-shadow(0 0 10px #38bdf8)"/>
          <ellipse cx="240" cy="180" rx="40" ry="12" fill="#38bdf8" filter="drop-shadow(0 0 10px #38bdf8)"/>
          <!-- Car Body -->
          <polygon points="30,150 270,150 250,80 80,80" fill="#94a3b8" stroke="#000" stroke-width="4"/>
          <!-- Windshield -->
          <polygon points="90,85 240,85 220,120 70,120" fill="#0284c7" opacity="0.7"/>
          <!-- Red BMTC Flying Bus Behind It -->
          <rect x="-120" y="40" width="160" height="90" rx="10" fill="#dc2626" stroke="#000" stroke-width="4"/>
          <text x="-40" y="90" fill="#fff" font-weight="bold" font-size="14" text-anchor="middle">BMTC 500-D</text>
        </g>
        <rect x="200" y="480" width="400" height="50" rx="25" fill="#000" stroke="#38bdf8" stroke-width="3"/>
        <text x="400" y="512" fill="#fff" font-family="'Outfit', sans-serif" font-weight="900" font-size="18" text-anchor="middle">"EVEN TIME TRAVEL CANNOT BEAT BENGALURU"</text>
        """
    },
    {
        "id": "meme011",
        "bg": ["#271206", "#451a03"],
        "badge": "🤖 HYPER-REALISTIC AI GENERATION",
        "title": "TEMPLE CARVED OF MELTING CHOCOLATE",
        "elements": """
        <!-- Melting Chocolate Gopuram -->
        <g transform="translate(260, 100)">
          <!-- Tiered Temple Structure in Glossy Brown -->
          <polygon points="140,40 180,90 100,90" fill="#3b1d11" stroke="#78350f" stroke-width="3"/>
          <polygon points="140,90 210,160 70,160" fill="#451a03" stroke="#78350f" stroke-width="3"/>
          <polygon points="140,160 250,260 30,260" fill="#3b1d11" stroke="#78350f" stroke-width="3"/>
          <!-- Impossible AI Liquid Drips -->
          <path d="M70,260 C70,330 90,330 90,260" fill="#78350f"/>
          <path d="M140,260 C140,360 170,360 170,260" fill="#78350f"/>
          <path d="M210,260 C210,320 230,320 230,260" fill="#78350f"/>
          <!-- Unnatural AI Sheen Highlights -->
          <ellipse cx="140" cy="120" rx="30" ry="10" fill="#fed7aa" opacity="0.3"/>
          <ellipse cx="160" cy="200" rx="40" ry="14" fill="#fed7aa" opacity="0.25"/>
        </g>
        <rect x="180" y="480" width="440" height="50" rx="25" fill="#000" stroke="#b45309" stroke-width="3"/>
        <text x="400" y="512" fill="#fed7aa" font-family="'Outfit', sans-serif" font-weight="900" font-size="18" text-anchor="middle">"100% CADBURY SILK ARCHITECTURE"</text>
        """
    },
    {
        "id": "meme012",
        "bg": ["#1c1917", "#292524"],
        "badge": "🤖 AI ANIMAL REALISM",
        "title": "CAT NEGOTIATING GURGAON RENT",
        "elements": """
        <!-- Landlord Office Desk -->
        <rect x="100" y="320" width="600" height="180" fill="#44403c" stroke="#000" stroke-width="4"/>
        <!-- Persian Cat in Suit & Glasses -->
        <g transform="translate(270, 90)">
          <!-- Cat Head & Fluffy Ears -->
          <polygon points="60,60 80,10 110,60" fill="#f8fafc" stroke="#000" stroke-width="3"/>
          <polygon points="150,60 180,10 200,60" fill="#f8fafc" stroke="#000" stroke-width="3"/>
          <ellipse cx="130" cy="110" rx="70" ry="60" fill="#f1f5f9" stroke="#000" stroke-width="3"/>
          <!-- Nerd Specs -->
          <circle cx="105" cy="105" r="22" fill="#e0f2fe" opacity="0.6" stroke="#000" stroke-width="3"/>
          <circle cx="155" cy="105" r="22" fill="#e0f2fe" opacity="0.6" stroke="#000" stroke-width="3"/>
          <line x1="127" y1="105" x2="133" y2="105" stroke="#000" stroke-width="3"/>
          <!-- Suit Collar & Red Tie -->
          <polygon points="70,170 190,170 170,260 90,260" fill="#1e293b" stroke="#000" stroke-width="4"/>
          <polygon points="120,170 140,170 135,240 125,240" fill="#dc2626"/>
        </g>
        <!-- Rent Agreement Stamp Paper on Table -->
        <g transform="translate(420, 310) rotate(8)">
          <rect x="0" y="0" width="110" height="130" fill="#fef08a" stroke="#000" stroke-width="2"/>
          <text x="55" y="30" fill="#713f12" font-size="9" font-weight="bold" text-anchor="middle">₹100 STAMP PAPER</text>
          <text x="55" y="60" fill="#dc2626" font-size="12" font-weight="900" text-anchor="middle">NO REFUND</text>
        </g>
        <rect x="180" y="490" width="440" height="50" rx="25" fill="#000" stroke="#f43f5e" stroke-width="3"/>
        <text x="400" y="522" fill="#fff" font-family="'Outfit', sans-serif" font-weight="900" font-size="18" text-anchor="middle">"MAINTENANCE 15K? BRO I AM A CAT"</text>
        """
    },
    {
        "id": "meme013",
        "bg": ["#1e1b4b", "#312e81"],
        "badge": "🤖 ABSURD PRODUCT AI PROMPT",
        "title": "IPHONE 25 PRO SAMOSA EDITION",
        "elements": """
        <!-- Golden Fried Samosa Phone Body -->
        <g transform="translate(240, 100)">
          <!-- Triangular Crispy Samosa -->
          <polygon points="160,30 290,280 30,280" fill="#d97706" stroke="#78350f" stroke-width="8"/>
          <!-- Fried Bubbles & Crispy Shading -->
          <circle cx="120" cy="180" r="10" fill="#b45309"/>
          <circle cx="170" cy="160" r="14" fill="#b45309"/>
          <circle cx="210" cy="220" r="8" fill="#b45309"/>
          <!-- Apple Pro Camera Bump on Samosa Corner -->
          <rect x="120" y="70" width="80" height="80" rx="18" fill="#000" stroke="#d97706" stroke-width="4"/>
          <!-- Triple Lenses -->
          <circle cx="140" cy="90" r="12" fill="#1e293b" stroke="#38bdf8" stroke-width="3"/>
          <circle cx="180" cy="90" r="12" fill="#1e293b" stroke="#38bdf8" stroke-width="3"/>
          <circle cx="160" cy="125" r="12" fill="#1e293b" stroke="#38bdf8" stroke-width="3"/>
          <!-- USB-C Mint Chutney Port at Bottom -->
          <rect x="140" y="270" width="40" height="12" rx="6" fill="#15803d" stroke="#000" stroke-width="2"/>
          <text x="160" y="260" fill="#22c55e" font-weight="bold" font-size="10" text-anchor="middle">CHUTNEY-C</text>
        </g>
        <rect x="180" y="480" width="440" height="50" rx="25" fill="#000" stroke="#f59e0b" stroke-width="3"/>
        <text x="400" y="512" fill="#fde047" font-family="'Outfit', sans-serif" font-weight="900" font-size="18" text-anchor="middle">"STARTING AT ₹1,89,999 (CHUTNEY EXTRA)"</text>
        """
    },
    {
        "id": "meme014",
        "bg": ["#1e293b", "#334155"],
        "badge": "🤖 SURREAL MIDJOURNEY BLEND",
        "title": "ROMAN GLADIATORS IN MUMBAI LOCAL",
        "elements": """
        <!-- Mumbai Local Compartment Interior -->
        <rect x="100" y="60" width="600" height="400" fill="#0f172a" stroke="#cbd5e1" stroke-width="4"/>
        <!-- Grab Rails (Handles) -->
        <line x1="120" y1="120" x2="680" y2="120" stroke="#94a3b8" stroke-width="8"/>
        <!-- Hanging Handles -->
        <circle cx="200" cy="160" r="16" fill="none" stroke="#94a3b8" stroke-width="4"/>
        <circle cx="360" cy="160" r="16" fill="none" stroke="#94a3b8" stroke-width="4"/>
        <circle cx="520" cy="160" r="16" fill="none" stroke="#94a3b8" stroke-width="4"/>
        <circle cx="640" cy="160" r="16" fill="none" stroke="#94a3b8" stroke-width="4"/>
        <!-- Centurion with Red Plumed Helmet & Shield -->
        <g transform="translate(280, 140)">
          <!-- Red Helmet Plume -->
          <path d="M100,20 C100,-20 160,-20 160,20 Z" fill="#dc2626"/>
          <!-- Bronze Helmet -->
          <polygon points="100,20 160,20 150,80 110,80" fill="#ca8a04" stroke="#000" stroke-width="3"/>
          <rect x="115" y="45" width="30" height="15" fill="#000"/>
          <!-- Roman Armor & Red Cape -->
          <path d="M80,80 L180,80 L190,260 L70,260 Z" fill="#78350f" stroke="#ca8a04" stroke-width="4"/>
          <!-- Giant Golden Scutum Shield -->
          <rect x="160" y="100" width="100" height="180" rx="15" fill="#b91c1c" stroke="#facc15" stroke-width="6"/>
          <circle cx="210" cy="190" r="20" fill="#facc15"/>
        </g>
        <rect x="160" y="480" width="480" height="50" rx="25" fill="#000" stroke="#facc15" stroke-width="3"/>
        <text x="400" y="512" fill="#fff" font-family="'Outfit', sans-serif" font-weight="900" font-size="18" text-anchor="middle">"DADAR AANE PAR DHAKKA APNE AAP MILEGA"</text>
        """
    },
    {
        "id": "meme015",
        "bg": ["#14532d", "#052e16"],
        "badge": "🤖 PHOTOREALISTIC AI ANIMAL",
        "title": "STREET DOG AS CHIEF GUEST IN NEHRU JACKET",
        "elements": """
        <!-- Velvet VIP Stage Chair -->
        <rect x="220" y="160" width="360" height="280" rx="20" fill="#7f1d1d" stroke="#f59e0b" stroke-width="6"/>
        <!-- Indie Dog in Silk Jacket -->
        <g transform="translate(290, 100)">
          <!-- Dog Head & Floppy Ears -->
          <polygon points="40,90 20,40 60,60" fill="#d97706"/>
          <polygon points="180,90 200,40 160,60" fill="#d97706"/>
          <ellipse cx="110" cy="95" rx="55" ry="45" fill="#f59e0b" stroke="#000" stroke-width="3"/>
          <ellipse cx="110" cy="115" rx="22" ry="16" fill="#000"/>
          <ellipse cx="90" cy="85" rx="8" ry="6" fill="#000"/>
          <ellipse cx="130" cy="85" rx="8" ry="6" fill="#000"/>
          <!-- Silk Royal Blue Nehru Jacket -->
          <path d="M50,140 L170,140 L190,280 L30,280 Z" fill="#1d4ed8" stroke="#f59e0b" stroke-width="4"/>
          <!-- Mandarin Collar -->
          <rect x="85" y="130" width="50" height="20" rx="4" fill="#1e40af" stroke="#f59e0b" stroke-width="2"/>
          <!-- Marigold Flower Garland -->
          <ellipse cx="110" cy="180" rx="50" ry="25" fill="none" stroke="#f59e0b" stroke-width="12" stroke-dasharray="10 8"/>
        </g>
        <rect x="180" y="480" width="440" height="50" rx="25" fill="#000" stroke="#f59e0b" stroke-width="3"/>
        <text x="400" y="512" fill="#fde047" font-family="'Outfit', sans-serif" font-weight="900" font-size="18" text-anchor="middle">"CHIEF GUEST FOR BISCUIT DISTRIBUTION"</text>
        """
    },
    {
        "id": "meme016",
        "bg": ["#1e1b4b", "#0f172a"],
        "badge": "🤖 GIGACHAD DESI AI RENDER",
        "title": "GIGACHAD SIPPING FILTER COFFEE",
        "elements": """
        <!-- Traditional South Indian Pillar Background -->
        <rect x="120" y="80" width="40" height="380" fill="#78350f" stroke="#000" stroke-width="3"/>
        <rect x="640" y="80" width="40" height="380" fill="#78350f" stroke="#000" stroke-width="3"/>
        <!-- GigaChad Figure -->
        <g transform="translate(270, 80)">
          <!-- Impossible Sharp Jawline Face -->
          <polygon points="80,110 130,40 180,110 170,190 130,220 90,190" fill="#fed7aa" stroke="#000" stroke-width="4"/>
          <!-- Aviator Sunglasses -->
          <rect x="95" y="95" width="30" height="20" rx="6" fill="#000"/>
          <rect x="135" y="95" width="30" height="20" rx="6" fill="#000"/>
          <line x1="125" y1="105" x2="135" y2="105" stroke="#f59e0b" stroke-width="3"/>
          <!-- Chiseled Stubble & Smirk -->
          <line x1="115" y1="160" x2="145" y2="160" stroke="#000" stroke-width="4"/>
          <!-- Traditional Gold Zari Kasavu Dhoti / Angavastram -->
          <path d="M50,220 L210,220 L220,340 L40,340 Z" fill="#fefce8" stroke="#ca8a04" stroke-width="6"/>
          <!-- Brass Filter Coffee Davarah Tumbler held up -->
          <g transform="translate(180, 180)">
            <polygon points="10,10 40,10 35,50 15,50" fill="#eab308" stroke="#a16207" stroke-width="2"/>
            <!-- Frothy Filter Coffee -->
            <ellipse cx="25" cy="10" rx="14" ry="5" fill="#fde68a"/>
            <path d="M25,0 Q30,-15 25,-25" stroke="#f59e0b" stroke-width="2" fill="none"/>
          </g>
        </g>
        <rect x="180" y="480" width="440" height="50" rx="25" fill="#000" stroke="#facc15" stroke-width="3"/>
        <text x="400" y="512" fill="#fff" font-family="'Outfit', sans-serif" font-weight="900" font-size="18" text-anchor="middle">"AVERAGE DEGREE FILTER COFFEE ENJOYER"</text>
        """
    },
    {
        "id": "meme017",
        "bg": ["#831843", "#500724"],
        "badge": "👤 HUMAN: HERA PHERI (2000)",
        "title": "BABURAO APTE: 'YEH BABURAO KA STYLE HAI'",
        "elements": """
        <!-- Star Garage Setting & Vintage Rotary Phone -->
        <rect x="140" y="80" width="520" height="380" fill="#3f132b" stroke="#f43f5e" stroke-width="3"/>
        <!-- Baburao Apte Drawing / Silhouette -->
        <g transform="translate(270, 90)">
          <!-- White Dhoti Kurta Silhouette -->
          <path d="M70,140 L190,140 L210,310 L50,310 Z" fill="#ffffff" stroke="#000" stroke-width="4"/>
          <!-- Head with Receding Hair -->
          <circle cx="130" cy="90" r="45" fill="#fed7aa" stroke="#000" stroke-width="3"/>
          <path d="M85,90 C85,50 100,50 130,50 C160,50 175,50 175,90" fill="#1e293b"/>
          <!-- Iconic Thick Square Glasses -->
          <rect x="95" y="75" width="30" height="25" fill="#e2e8f0" stroke="#000" stroke-width="4"/>
          <rect x="135" y="75" width="30" height="25" fill="#e2e8f0" stroke="#000" stroke-width="4"/>
          <line x1="125" y1="85" x2="135" y2="85" stroke="#000" stroke-width="4"/>
          <!-- Wide Laugh Smile -->
          <ellipse cx="130" cy="118" rx="18" ry="10" fill="#dc2626"/>
          <!-- Star Garage Vintage Red Telephone in Hand -->
          <g transform="translate(-40, 160)">
            <rect x="20" y="40" width="50" height="40" rx="8" fill="#dc2626" stroke="#000" stroke-width="3"/>
            <path d="M10,25 C30,10 60,10 80,25" stroke="#dc2626" stroke-width="12" stroke-linecap="round"/>
          </g>
        </g>
        <!-- Dialogue Bubble -->
        <rect x="140" y="480" width="520" height="56" rx="28" fill="#fbbf24" stroke="#000" stroke-width="4"/>
        <text x="400" y="516" fill="#000" font-family="'Outfit', sans-serif" font-weight="900" font-size="22" text-anchor="middle">"YEH BABURAO KA STYLE HAI!"</text>
        """
    },
    {
        "id": "meme018",
        "bg": ["#1e3a8a", "#172554"],
        "badge": "👤 HUMAN: TMKOC TV COMEDY",
        "title": "JETHALAL SHOCKED REACTION",
        "elements": """
        <!-- Gokuldham Balcony Backdrop -->
        <rect x="100" y="60" width="600" height="380" fill="#1e293b" stroke="#60a5fa" stroke-width="3"/>
        <line x1="100" y1="360" x2="700" y2="360" stroke="#64748b" stroke-width="8"/>
        <!-- Jethalal Champaklal Gada Drawing -->
        <g transform="translate(270, 90)">
          <!-- Iconic Colorful Geometric Shirt -->
          <path d="M60,150 L200,150 L220,320 L40,320 Z" fill="#f59e0b" stroke="#000" stroke-width="4"/>
          <path d="M80,150 L120,320 M140,150 L180,320" stroke="#ef4444" stroke-width="4"/>
          <!-- Round Expressive Face -->
          <circle cx="130" cy="95" r="55" fill="#fed7aa" stroke="#000" stroke-width="3"/>
          <!-- Classic Sleek Side Hair -->
          <path d="M80,80 C80,35 180,35 180,80 Z" fill="#0f172a"/>
          <!-- Signature Trim Mustache -->
          <rect x="110" y="115" width="40" height="8" rx="4" fill="#000"/>
          <!-- Wide Open Shocked Eyes -->
          <ellipse cx="105" cy="85" rx="14" ry="18" fill="#fff" stroke="#000" stroke-width="3"/>
          <circle cx="105" cy="85" r="6" fill="#000"/>
          <ellipse cx="155" cy="85" rx="14" ry="18" fill="#fff" stroke="#000" stroke-width="3"/>
          <circle cx="155" cy="85" r="6" fill="#000"/>
          <!-- Hands on Head Panic Pose -->
          <circle cx="70" cy="90" r="14" fill="#fed7aa" stroke="#000" stroke-width="3"/>
          <circle cx="190" cy="90" r="14" fill="#fed7aa" stroke="#000" stroke-width="3"/>
        </g>
        <rect x="180" y="480" width="440" height="54" rx="27" fill="#ef4444" stroke="#000" stroke-width="4"/>
        <text x="400" y="515" fill="#fff" font-family="'Outfit', sans-serif" font-weight="900" font-size="22" text-anchor="middle">"HEY MAA! MATAJI! BABITAJI!!"</text>
        """
    },
    {
        "id": "meme019",
        "bg": ["#14532d", "#166534"],
        "badge": "👤 HUMAN: PANCHAYAT / TVF",
        "title": "BANRAKAS: 'GAJAB BEIZZATI HAI YAAR'",
        "elements": """
        <!-- Phulera Rural Village Setting -->
        <path d="M0,380 Q400,320 800,380 L800,600 L0,600 Z" fill="#854d0e"/>
        <!-- Wooden Charpai (Cot) -->
        <rect x="180" y="320" width="440" height="40" fill="#a16207" stroke="#000" stroke-width="4"/>
        <line x1="220" y1="360" x2="220" y2="420" stroke="#78350f" stroke-width="8"/>
        <line x1="580" y1="360" x2="580" y2="420" stroke="#78350f" stroke-width="8"/>
        <!-- Banrakas / Vinod Sitting in Kurta -->
        <g transform="translate(280, 110)">
          <!-- Kurta Silhouette -->
          <path d="M70,120 L170,120 L190,260 L50,260 Z" fill="#fef08a" stroke="#000" stroke-width="4"/>
          <!-- Face with Unimpressed Squint -->
          <circle cx="120" cy="80" r="40" fill="#fed7aa" stroke="#000" stroke-width="3"/>
          <!-- Mustache & Skeptical Eyebrow -->
          <path d="M100,100 Q120,110 140,100" stroke="#000" stroke-width="4" fill="none"/>
          <line x1="95" y1="65" x2="115" y2="70" stroke="#000" stroke-width="3"/>
          <line x1="125" y1="70" x2="145" y2="65" stroke="#000" stroke-width="3"/>
          <!-- Gamchha (Towel) around neck -->
          <path d="M75,115 C85,190 155,190 165,115" fill="none" stroke="#dc2626" stroke-width="12"/>
        </g>
        <rect x="160" y="480" width="480" height="54" rx="27" fill="#000" stroke="#facc15" stroke-width="4"/>
        <text x="400" y="515" fill="#fef08a" font-family="'Outfit', sans-serif" font-weight="900" font-size="22" text-anchor="middle">"DEKH RAHA HAI BINOD? GAJAB BEIZZATI HAI"</text>
        """
    },
    {
        "id": "meme020",
        "bg": ["#1e293b", "#0f172a"],
        "badge": "👤 HUMAN: MUNNA BHAI MBBS (2003)",
        "title": "MUNNA BHAI DEADPAN: 'NAHI'",
        "elements": """
        <!-- Clinic Background -->
        <rect x="140" y="70" width="520" height="380" fill="#334155" stroke="#94a3b8" stroke-width="3"/>
        <!-- Munna Bhai Portrait -->
        <g transform="translate(280, 90)">
          <!-- Blue Silk Shirt & Thick Gold Chain -->
          <path d="M60,140 L180,140 L200,310 L40,310 Z" fill="#0284c7" stroke="#000" stroke-width="4"/>
          <!-- Big Chunky Gold Chain -->
          <path d="M90,140 Q120,180 150,140" fill="none" stroke="#fbbf24" stroke-width="8"/>
          <!-- Rugged Face & Buzzcut -->
          <circle cx="120" cy="85" r="45" fill="#fed7aa" stroke="#000" stroke-width="3"/>
          <path d="M75,70 C75,35 165,35 165,70" fill="#0f172a"/>
          <!-- Deadpan Straight-faced Expression -->
          <line x1="105" y1="115" x2="135" y2="115" stroke="#000" stroke-width="4"/>
          <!-- Stethoscope dangling -->
          <path d="M70,150 C70,240 170,240 170,150" fill="none" stroke="#94a3b8" stroke-width="6"/>
          <circle cx="120" cy="230" r="14" fill="#cbd5e1" stroke="#000" stroke-width="2"/>
        </g>
        <rect x="240" y="480" width="320" height="54" rx="27" fill="#ef4444" stroke="#000" stroke-width="4"/>
        <text x="400" y="516" fill="#fff" font-family="'Outfit', sans-serif" font-weight="900" font-size="28" text-anchor="middle">"NAHI."</text>
        """
    },
    {
        "id": "meme021",
        "bg": ["#7c2d12", "#431407"],
        "badge": "👤 HUMAN: WELCOME (2007)",
        "title": "MAJNU BHAI: 'CONTROL MAJNU CONTROL!'",
        "elements": """
        <!-- Art Studio Canvas with Donkey Painting -->
        <g transform="translate(140, 140)">
          <rect x="0" y="0" width="160" height="180" fill="#fff" stroke="#ca8a04" stroke-width="4"/>
          <!-- Majestic Horse with Donkey on Top Painting -->
          <ellipse cx="80" cy="110" rx="40" ry="25" fill="#78350f"/>
          <ellipse cx="80" cy="65" rx="25" ry="18" fill="#94a3b8"/>
          <text x="80" y="160" fill="#b91c1c" font-size="10" font-weight="bold" text-anchor="middle">WORLD CLASS ART</text>
        </g>
        <!-- Majnu Bhai (Anil Kapoor) in Orange Shirt -->
        <g transform="translate(360, 90)">
          <!-- Bright Orange Shirt -->
          <path d="M50,140 L170,140 L190,320 L30,320 Z" fill="#ea580c" stroke="#000" stroke-width="4"/>
          <!-- Face & Moustache -->
          <circle cx="110" cy="85" r="45" fill="#fed7aa" stroke="#000" stroke-width="3"/>
          <path d="M90,110 Q110,120 130,110" stroke="#000" stroke-width="5" fill="none"/>
          <!-- Dark Aviators -->
          <rect x="85" y="75" width="22" height="16" rx="4" fill="#000"/>
          <rect x="113" y="75" width="22" height="16" rx="4" fill="#000"/>
          <line x1="107" y1="82" x2="113" y2="82" stroke="#ca8a04" stroke-width="2"/>
          <!-- Gripping Hands Pose -->
          <circle cx="40" cy="140" r="14" fill="#fed7aa" stroke="#000" stroke-width="2"/>
          <circle cx="180" cy="140" r="14" fill="#fed7aa" stroke="#000" stroke-width="2"/>
        </g>
        <rect x="140" y="480" width="520" height="54" rx="27" fill="#f97316" stroke="#000" stroke-width="4"/>
        <text x="400" y="515" fill="#000" font-family="'Outfit', sans-serif" font-weight="900" font-size="22" text-anchor="middle">"CONTROL MAJNU... CONTROL!!"</text>
        """
    },
    {
        "id": "meme022",
        "bg": ["#064e3b", "#022c22"],
        "badge": "👤 HUMAN: 3 IDIOTS (2009)",
        "title": "3 IDIOTS: 'JAHANPANAH TUSSI GREAT HO'",
        "elements": """
        <!-- ICE College Hostel Rooftop -->
        <rect x="100" y="80" width="600" height="370" fill="#0f172a" stroke="#10b981" stroke-width="3"/>
        <!-- Raju & Farhan Bowing Down -->
        <g transform="translate(180, 160)">
          <!-- Raju Bowing -->
          <ellipse cx="60" cy="120" rx="30" ry="40" fill="#dc2626" stroke="#000" stroke-width="3"/>
          <circle cx="90" cy="140" r="18" fill="#fed7aa" stroke="#000" stroke-width="2"/>
          <!-- Farhan Bowing -->
          <ellipse cx="140" cy="120" rx="30" ry="40" fill="#2563eb" stroke="#000" stroke-width="3"/>
          <circle cx="170" cy="140" r="18" fill="#fed7aa" stroke="#000" stroke-width="2"/>
        </g>
        <!-- Rancho Smiling Cool -->
        <g transform="translate(450, 120)">
          <path d="M40,110 L120,110 L130,260 L30,260 Z" fill="#facc15" stroke="#000" stroke-width="4"/>
          <circle cx="80" cy="65" r="35" fill="#fed7aa" stroke="#000" stroke-width="3"/>
          <path d="M55,55 C55,25 105,25 105,55" fill="#000"/>
          <ellipse cx="80" cy="80" rx="10" ry="5" fill="#dc2626"/>
        </g>
        <rect x="120" y="480" width="560" height="54" rx="27" fill="#10b981" stroke="#000" stroke-width="4"/>
        <text x="400" y="515" fill="#000" font-family="'Outfit', sans-serif" font-weight="900" font-size="21" text-anchor="middle">"JAHANPANAH! TUSSI GREAT HO! TOHFA QUBOOL KARO!"</text>
        """
    },
    {
        "id": "meme023",
        "bg": ["#172554", "#1e1b4b"],
        "badge": "👤 HUMAN: SHARK TANK INDIA S1",
        "title": "ASHNEER GROVER: 'YEH SAB DOGLAPAN HAI'",
        "elements": """
        <!-- Pitcher Spotlight & Shark Tank Decor -->
        <polygon points="400,0 200,450 600,450" fill="#3b82f6" opacity="0.1"/>
        <!-- Ashneer Grover Shark Chair Silhouette -->
        <rect x="220" y="160" width="360" height="260" rx="16" fill="#0f172a" stroke="#2563eb" stroke-width="5"/>
        <g transform="translate(280, 100)">
          <!-- Black Blazer & Formal Shirt -->
          <path d="M50,130 L190,130 L200,280 L40,280 Z" fill="#1e293b" stroke="#000" stroke-width="4"/>
          <polygon points="100,130 140,130 120,200" fill="#fff"/>
          <!-- Square Frame Specs & Blunt Expression -->
          <circle cx="120" cy="80" r="45" fill="#fed7aa" stroke="#000" stroke-width="3"/>
          <rect x="95" y="70" width="22" height="18" fill="#e0f2fe" opacity="0.7" stroke="#000" stroke-width="3"/>
          <rect x="123" y="70" width="22" height="18" fill="#e0f2fe" opacity="0.7" stroke="#000" stroke-width="3"/>
          <line x1="117" y1="78" x2="123" y2="78" stroke="#000" stroke-width="3"/>
          <!-- Unimpressed Frown -->
          <line x1="105" y1="110" x2="135" y2="108" stroke="#000" stroke-width="4"/>
        </g>
        <rect x="160" y="480" width="480" height="54" rx="27" fill="#ef4444" stroke="#000" stroke-width="4"/>
        <text x="400" y="515" fill="#fff" font-family="'Outfit', sans-serif" font-weight="900" font-size="22" text-anchor="middle">"YEH SAB DOGLAPAN HAI!"</text>
        """
    },
    {
        "id": "meme024",
        "bg": ["#451a03", "#271206"],
        "badge": "👤 HUMAN: MIRZAPUR / PRIME VIDEO",
        "title": "KALEEN BHAIYA: 'YE BHI THEEK HAI'",
        "elements": """
        <!-- Haveli Antique Sofa & Carpet -->
        <rect x="120" y="160" width="560" height="260" rx="15" fill="#3b1d11" stroke="#ca8a04" stroke-width="4"/>
        <!-- Pankaj Tripathi (Kaleen Bhaiya) Drawing -->
        <g transform="translate(280, 90)">
          <!-- Royal Brown Silk Kurta -->
          <path d="M50,140 L190,140 L210,310 L30,310 Z" fill="#78350f" stroke="#000" stroke-width="4"/>
          <!-- Calm Peaceful Face & Grey-Tinted Hair -->
          <circle cx="120" cy="85" r="45" fill="#fed7aa" stroke="#000" stroke-width="3"/>
          <path d="M75,70 C75,30 165,30 165,70" fill="#475569"/>
          <!-- Dignified Mustache & Calm Slight Smile -->
          <path d="M100,108 Q120,118 140,108" stroke="#000" stroke-width="4" fill="none"/>
          <line x1="108" y1="120" x2="132" y2="120" stroke="#000" stroke-width="3"/>
        </g>
        <rect x="200" y="480" width="400" height="54" rx="27" fill="#ca8a04" stroke="#000" stroke-width="4"/>
        <text x="400" y="515" fill="#000" font-family="'Outfit', sans-serif" font-weight="900" font-size="24" text-anchor="middle">"YE BHI THEEK HAI."</text>
        """
    },
    {
        "id": "meme025",
        "bg": ["#0f172a", "#1e293b"],
        "badge": "👤 HUMAN: REAL HOSTEL PHONE CAMERA",
        "title": "2 AM ELECTRIC KETTLE MAGGI BEFORE EXAM",
        "elements": """
        <!-- Messy Hostel Table -->
        <rect x="80" y="180" width="640" height="280" fill="#334155" stroke="#000" stroke-width="5"/>
        <!-- Blue Plastic Electric Kettle -->
        <g transform="translate(180, 160)">
          <rect x="20" y="20" width="100" height="140" rx="15" fill="#0284c7" stroke="#000" stroke-width="4"/>
          <rect x="100" y="40" width="30" height="90" rx="10" fill="#0f172a" stroke="#000" stroke-width="3"/>
          <!-- Yellow Maggi Noodles Boiling Inside -->
          <ellipse cx="70" cy="40" rx="35" ry="15" fill="#facc15" stroke="#ca8a04" stroke-width="2"/>
          <path d="M50,45 Q70,55 90,45" stroke="#b45309" stroke-width="3" fill="none"/>
          <!-- Steam coming out -->
          <path d="M60,15 Q65,0 60,-15" stroke="#cbd5e1" stroke-width="3" fill="none"/>
          <path d="M80,15 Q85,0 80,-15" stroke="#cbd5e1" stroke-width="3" fill="none"/>
        </g>
        <!-- Scattered Xerox Notes & Highlighter -->
        <g transform="translate(380, 220) rotate(-6)">
          <rect x="0" y="0" width="160" height="110" fill="#fff" stroke="#000" stroke-width="2"/>
          <line x1="20" y1="30" x2="140" y2="30" stroke="#facc15" stroke-width="8"/>
          <line x1="20" y1="50" x2="110" y2="50" stroke="#64748b" stroke-width="3"/>
          <line x1="20" y1="70" x2="130" y2="70" stroke="#64748b" stroke-width="3"/>
          <text x="80" y="95" fill="#ef4444" font-weight="900" font-size="12" text-anchor="middle">SYLLABUS 90% REMAINING</text>
        </g>
        <rect x="180" y="480" width="440" height="54" rx="27" fill="#facc15" stroke="#000" stroke-width="4"/>
        <text x="400" y="515" fill="#000" font-family="'Outfit', sans-serif" font-weight="900" font-size="20" text-anchor="middle">"ENGINEERING SURVIVAL KIT 🍜"</text>
        """
    },
    {
        "id": "meme026",
        "bg": ["#1e1b4b", "#0f172a"],
        "badge": "👤 HUMAN: CLASSIC MEME TEMPLATE",
        "title": "SWOLE DOGE VS CHEEMS (ENGINEERING EDITION)",
        "elements": """
        <!-- Left: Swole Doge (Buff Doge) -->
        <g transform="translate(100, 120)">
          <!-- Buff Torso & Muscles -->
          <ellipse cx="140" cy="180" rx="80" ry="70" fill="#f59e0b" stroke="#000" stroke-width="4"/>
          <!-- Buff Arms -->
          <circle cx="50" cy="150" r="35" fill="#d97706" stroke="#000" stroke-width="4"/>
          <circle cx="230" cy="150" r="35" fill="#d97706" stroke="#000" stroke-width="4"/>
          <!-- Doge Head -->
          <circle cx="140" cy="80" r="40" fill="#fde68a" stroke="#000" stroke-width="3"/>
          <text x="140" y="290" fill="#facc15" font-family="'Outfit', sans-serif" font-weight="900" font-size="18" text-anchor="middle">1ST SEMESTER:</text>
          <text x="140" y="315" fill="#fff" font-size="13" text-anchor="middle">"I WILL FOUND NEXT GOOGLE"</text>
        </g>
        <!-- Center Divider -->
        <line x1="400" y1="60" x2="400" y2="440" stroke="#475569" stroke-width="4" stroke-dasharray="10 6"/>
        <!-- Right: Small Crying Cheems -->
        <g transform="translate(480, 190)">
          <ellipse cx="120" cy="130" rx="55" ry="45" fill="#d97706" stroke="#000" stroke-width="3"/>
          <circle cx="110" cy="80" r="30" fill="#fde68a" stroke="#000" stroke-width="3"/>
          <text x="120" y="220" fill="#f43f5e" font-family="'Outfit', sans-serif" font-weight="900" font-size="18" text-anchor="middle">8TH SEMESTER:</text>
          <text x="120" y="245" fill="#fff" font-size="13" text-anchor="middle">"Sir 75% attendance dedo plij"</text>
        </g>
        <rect x="180" y="480" width="440" height="54" rx="27" fill="#000" stroke="#facc15" stroke-width="4"/>
        <text x="400" y="515" fill="#facc15" font-family="'Outfit', sans-serif" font-weight="900" font-size="19" text-anchor="middle">"CANON EVENT OF EVERY B.TECH STUDENT"</text>
        """
    },
    {
        "id": "meme027",
        "bg": ["#064e3b", "#022c22"],
        "badge": "👤 HUMAN: ICC WORLD CUP 2019",
        "title": "DISAPPOINTED CRICKET FAN (HANDS ON HIPS)",
        "elements": """
        <!-- Cricket Stadium Crowd Floodlights -->
        <rect x="100" y="60" width="600" height="380" fill="#0f172a" stroke="#22c55e" stroke-width="3"/>
        <circle cx="200" cy="100" r="16" fill="#fff" opacity="0.8"/>
        <circle cx="600" cy="100" r="16" fill="#fff" opacity="0.8"/>
        <!-- Muhammad Sarim Akhtar Figure -->
        <g transform="translate(280, 90)">
          <!-- Chequered Shirt / Windcheater -->
          <path d="M50,140 L190,140 L210,320 L30,320 Z" fill="#047857" stroke="#000" stroke-width="4"/>
          <!-- Hands Firmly Planted on Hips -->
          <path d="M50,150 L10,210 L45,240" stroke="#047857" stroke-width="18" fill="none" stroke-linecap="round"/>
          <path d="M190,150 L230,210 L195,240" stroke="#047857" stroke-width="18" fill="none" stroke-linecap="round"/>
          <!-- Head with Round Bald Crown & Deadpan Stare -->
          <circle cx="120" cy="85" r="45" fill="#fed7aa" stroke="#000" stroke-width="3"/>
          <path d="M80,75 C80,40 160,40 160,75" fill="#1e293b"/>
          <!-- Deep Deadpan Disappointment Mouth -->
          <ellipse cx="100" cy="80" rx="6" ry="6" fill="#000"/>
          <ellipse cx="140" cy="80" rx="6" ry="6" fill="#000"/>
          <line x1="108" y1="112" x2="132" y2="112" stroke="#000" stroke-width="4"/>
        </g>
        <rect x="160" y="480" width="480" height="54" rx="27" fill="#047857" stroke="#fff" stroke-width="3"/>
        <text x="400" y="515" fill="#fff" font-family="'Outfit', sans-serif" font-weight="900" font-size="22" text-anchor="middle">"WHEN HE DROPS A SITTER AT THIRD MAN"</text>
        """
    },
    {
        "id": "meme028",
        "bg": ["#713f12", "#451a03"],
        "badge": "👤 HUMAN: CHUP CHUP KE (2006)",
        "title": "RAJPAL YADAV: 'MUJHE SAB PATA HAI'",
        "elements": """
        <!-- Haveli Washing Courtyard -->
        <rect x="100" y="60" width="600" height="380" fill="#292524" stroke="#eab308" stroke-width="3"/>
        <!-- Rajpal Yadav (Bandya) Drawing -->
        <g transform="translate(280, 90)">
          <!-- Yellow Faded Kurta -->
          <path d="M60,140 L180,140 L195,310 L45,310 Z" fill="#eab308" stroke="#000" stroke-width="4"/>
          <!-- Face with Bandage on Forehead -->
          <circle cx="120" cy="85" r="42" fill="#fed7aa" stroke="#000" stroke-width="3"/>
          <!-- Bandage -->
          <rect x="95" y="55" width="45" height="14" rx="4" fill="#f8fafc" stroke="#000" stroke-width="2"/>
          <!-- Wide Staring Eyes & Pointing Finger -->
          <ellipse cx="105" cy="85" rx="10" ry="12" fill="#fff" stroke="#000" stroke-width="2"/>
          <circle cx="105" cy="85" r="4" fill="#000"/>
          <ellipse cx="135" cy="85" rx="10" ry="12" fill="#fff" stroke="#000" stroke-width="2"/>
          <circle cx="135" cy="85" r="4" fill="#000"/>
          <!-- Raised Warning Finger -->
          <g transform="translate(180, 120)">
            <rect x="0" y="0" width="16" height="60" rx="8" fill="#fed7aa" stroke="#000" stroke-width="3"/>
          </g>
        </g>
        <rect x="140" y="480" width="520" height="54" rx="27" fill="#eab308" stroke="#000" stroke-width="4"/>
        <text x="400" y="515" fill="#000" font-family="'Outfit', sans-serif" font-weight="900" font-size="22" text-anchor="middle">"MUJHE SAB PATA HAI! MAIN NAHI BATAUNGA!"</text>
        """
    },
    {
        "id": "meme029",
        "bg": ["#1c1917", "#292524"],
        "badge": "👤 HUMAN: REAL DELHI KIRANA SHOP",
        "title": "KIRANA STORE: 'UDHAAR MANG KAR SHARMINDA NA KAREIN'",
        "elements": """
        <!-- Rusted Shop Tin Wall -->
        <rect x="80" y="70" width="640" height="370" fill="#44403c" stroke="#000" stroke-width="4"/>
        <!-- Iconic Vintage Painted Tin Board -->
        <g transform="translate(160, 100)">
          <!-- Red Tin Plate with Rusted Corners -->
          <rect x="0" y="0" width="480" height="260" rx="10" fill="#b91c1c" stroke="#facc15" stroke-width="6"/>
          <!-- Rivet screws in 4 corners -->
          <circle cx="20" cy="20" r="6" fill="#475569"/>
          <circle cx="460" cy="20" r="6" fill="#475569"/>
          <circle cx="20" cy="240" r="6" fill="#475569"/>
          <circle cx="460" cy="240" r="6" fill="#475569"/>
          <!-- Traditional Sign Painter Hindi Script -->
          <text x="240" y="70" fill="#facc15" font-family="'Outfit', sans-serif" font-weight="900" font-size="34" text-anchor="middle">आज नकद कल उधार</text>
          <line x1="60" y1="95" x2="420" y2="95" stroke="#facc15" stroke-width="4"/>
          <text x="240" y="150" fill="#ffffff" font-family="'Outfit', sans-serif" font-weight="800" font-size="22" text-anchor="middle">कृपया उधार मांग कर</text>
          <text x="240" y="195" fill="#facc15" font-family="'Outfit', sans-serif" font-weight="900" font-size="28" text-anchor="middle">शर्मिंदा ना करें!</text>
          <text x="240" y="235" fill="#fecaca" font-size="13" font-weight="bold" text-anchor="middle">QR CODE SE SCAN KARKE PAYMENT KAREIN</text>
        </g>
        <rect x="180" y="480" width="440" height="54" rx="27" fill="#000" stroke="#facc15" stroke-width="4"/>
        <text x="400" y="515" fill="#facc15" font-family="'Outfit', sans-serif" font-weight="900" font-size="20" text-anchor="middle">"UNIVERSAL INDIAN DUKAN RULE 🚫"</text>
        """
    },
    {
        "id": "meme030",
        "bg": ["#1e3a8a", "#1e1b4b"],
        "badge": "👤 HUMAN: 1967 CLASSIC CARTOON FORMAT",
        "title": "TWO SPIDER-MEN POINTING AT EACH OTHER",
        "elements": """
        <!-- Vintage 60s Comic Backdrop -->
        <rect x="80" y="60" width="640" height="380" fill="#0f172a" stroke="#ef4444" stroke-width="3"/>
        <!-- Left Spiderman -->
        <g transform="translate(160, 140)">
          <!-- Red & Blue Body -->
          <ellipse cx="60" cy="140" rx="40" ry="60" fill="#2563eb" stroke="#000" stroke-width="3"/>
          <circle cx="60" cy="65" r="30" fill="#dc2626" stroke="#000" stroke-width="3"/>
          <!-- Pointing Arm Right -->
          <line x1="60" y1="120" x2="160" y2="120" stroke="#dc2626" stroke-width="14" stroke-linecap="round"/>
          <text x="60" y="230" fill="#facc15" font-weight="900" font-size="16" text-anchor="middle">"YOU COPIED"</text>
        </g>
        <!-- Right Spiderman -->
        <g transform="translate(520, 140) scale(-1, 1)">
          <!-- Red & Blue Body -->
          <ellipse cx="60" cy="140" rx="40" ry="60" fill="#2563eb" stroke="#000" stroke-width="3"/>
          <circle cx="60" cy="65" r="30" fill="#dc2626" stroke="#000" stroke-width="3"/>
          <!-- Pointing Arm Right (mirrored Left) -->
          <line x1="60" y1="120" x2="160" y2="120" stroke="#dc2626" stroke-width="14" stroke-linecap="round"/>
          <text x="60" y="230" fill="#facc15" font-weight="900" font-size="16" text-anchor="middle" transform="scale(-1, 1)">"BRO FROM YOU"</text>
        </g>
        <rect x="180" y="480" width="440" height="54" rx="27" fill="#dc2626" stroke="#000" stroke-width="4"/>
        <text x="400" y="515" fill="#fff" font-family="'Outfit', sans-serif" font-weight="900" font-size="20" text-anchor="middle">"TWO BACKBENCHERS IN LAB VIVA"</text>
        """
    },
    {
        "id": "meme031",
        "bg": ["#3f132b", "#1e1b4b"],
        "badge": "👤 HUMAN: KRANTIVEER (1994)",
        "title": "NANA PATEKAR: 'ACCHA KHASA CHAL RAHA THA'",
        "elements": """
        <!-- Dramatic 90s Spotlight Cinema Hall Frame -->
        <rect x="100" y="60" width="600" height="380" fill="#1c1917" stroke="#e11d48" stroke-width="4"/>
        <!-- Nana Patekar Profile with Finger to Head -->
        <g transform="translate(280, 90)">
          <!-- Simple Cotton Kurta -->
          <path d="M50,140 L190,140 L200,310 L40,310 Z" fill="#f8fafc" stroke="#000" stroke-width="4"/>
          <!-- Intense Focused Face -->
          <circle cx="120" cy="85" r="45" fill="#fed7aa" stroke="#000" stroke-width="3"/>
          <!-- Salt and Pepper Hair -->
          <path d="M75,70 C75,30 165,30 165,70" fill="#334155"/>
          <!-- Hand pointing to temple / brain -->
          <g transform="translate(50, 60)">
            <rect x="0" y="20" width="35" height="14" rx="6" fill="#fed7aa" stroke="#000" stroke-width="2"/>
          </g>
          <!-- Deep intense frown lines -->
          <line x1="105" y1="70" x2="135" y2="70" stroke="#000" stroke-width="3"/>
        </g>
        <rect x="140" y="480" width="520" height="54" rx="27" fill="#e11d48" stroke="#000" stroke-width="4"/>
        <text x="400" y="515" fill="#fff" font-family="'Outfit', sans-serif" font-weight="900" font-size="20" text-anchor="middle">"ACCHA KHASA CHAL RAHA THA... PHIR SWAAD AA GAYA!"</text>
        """
    },
    {
        "id": "meme032",
        "bg": ["#1e293b", "#0f172a"],
        "badge": "👤 HUMAN: BANGALORE REAL AUTO METER",
        "title": "BENGALURU AUTO METER ERROR 9999",
        "elements": """
        <!-- Real Auto Dashboard Texture -->
        <rect x="80" y="80" width="640" height="360" rx="16" fill="#18181b" stroke="#3f3f46" stroke-width="5"/>
        <!-- Digital Fare Meter Box -->
        <g transform="translate(180, 120)">
          <rect x="0" y="0" width="440" height="200" rx="12" fill="#09090b" stroke="#ef4444" stroke-width="4"/>
          <text x="220" y="40" fill="#a1a1aa" font-family="monospace" font-size="14" font-weight="bold" text-anchor="middle">ELECTRONIC DIGITAL FARE METER</text>
          <!-- Glowing Red 7-Segment LED Display -->
          <rect x="40" y="60" width="360" height="85" fill="#18181b" stroke="#27272a" stroke-width="2"/>
          <text x="220" y="125" fill="#ef4444" font-family="monospace" font-weight="900" font-size="52" text-anchor="middle" filter="drop-shadow(0 0 10px #ef4444)">₹ 9999.00</text>
          <text x="220" y="175" fill="#fbbf24" font-family="monospace" font-size="13" text-anchor="middle">DISTANCE: 1.2 KM • INDIRANAGAR</text>
        </g>
        <rect x="180" y="480" width="440" height="54" rx="27" fill="#000" stroke="#ef4444" stroke-width="4"/>
        <text x="400" y="515" fill="#facc15" font-family="'Outfit', sans-serif" font-weight="900" font-size="20" text-anchor="middle">"ONE AND A HALF LAGEGA SAAR"</text>
        """
    }
]

template = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 600" width="100%" height="100%">
  <defs>
    <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{bg1}"/>
      <stop offset="100%" stop-color="{bg2}"/>
    </linearGradient>
    <linearGradient id="cyanFlame" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#00f0ff" stop-opacity="0.9"/>
      <stop offset="100%" stop-color="#00f0ff" stop-opacity="0"/>
    </linearGradient>
    <filter id="glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="6" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>
  </defs>

  <!-- Background -->
  <rect width="800" height="600" fill="url(#bgGrad)"/>

  <!-- Subtle Pixelpalooza Grid lines -->
  <g stroke="rgba(255,255,255,0.06)" stroke-width="1">
    <line x1="0" y1="100" x2="800" y2="100" />
    <line x1="0" y1="200" x2="800" y2="200" />
    <line x1="0" y1="300" x2="800" y2="300" />
    <line x1="0" y1="400" x2="800" y2="400" />
    <line x1="0" y1="500" x2="800" y2="500" />
    <line x1="200" y1="0" x2="200" y2="600" />
    <line x1="400" y1="0" x2="400" y2="600" />
    <line x1="600" y1="0" x2="600" y2="600" />
  </g>

  <!-- Top Badge -->
  <g transform="translate(40, 24)">
    <rect x="0" y="0" width="340" height="28" rx="14" fill="#000000" stroke="rgba(255,255,255,0.3)" stroke-width="1.5"/>
    <text x="170" y="19" fill="#f8fafc" font-family="monospace" font-weight="bold" font-size="11" text-anchor="middle">{badge}</text>
  </g>

  <!-- Elements -->
  {elements}

  <!-- Watermark border corner accents -->
  <rect x="15" y="15" width="20" height="4" fill="#ff007a"/>
  <rect x="15" y="15" width="4" height="20" fill="#ff007a"/>
  <rect x="765" y="15" width="20" height="4" fill="#00f0ff"/>
  <rect x="781" y="15" width="4" height="20" fill="#00f0ff"/>
  <rect x="15" y="581" width="20" height="4" fill="#00f0ff"/>
  <rect x="15" y="565" width="4" height="20" fill="#00f0ff"/>
  <rect x="765" y="581" width="20" height="4" fill="#ff007a"/>
  <rect x="781" y="565" width="4" height="20" fill="#ff007a"/>
</svg>
'''

for m in memes:
    content = template.format(
        bg1=m["bg"][0],
        bg2=m["bg"][1],
        badge=m["badge"],
        title=m["title"],
        elements=m["elements"]
    )
    with open(f"public/memes/{m['id']}.svg", "w", encoding="utf-8") as f:
        f.write(content)

print(f"Successfully generated {len(memes)} meme SVGs!")
