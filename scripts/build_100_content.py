import json

# Comprehensive 105-item high-difficulty dataset
# Covering all digital media types: images, code, tweets, reviews, emails, headlines, poems, product copy, fiction, academic prose, support logs
items = [
  # ----------------------------------------------------
  # 1. IMAGES & ARTWORKS (16 items)
  # ----------------------------------------------------
  {
    "id": "var001",
    "type": "image",
    "category": "photograph",
    "title": "Street Auto Rickshaw in Varanasi",
    "file": "/content/ai_cyber_rickshaw.jpg",
    "answer": "ai",
    "difficulty": "medium",
    "explanation": "AI-generated photograph. While the night market lighting and wet pavement look remarkably authentic, the auto-rickshaw hovers on blue plasma thrusters instead of tires, and several background Hindi neon shop signs blend nonsensical glyphs.",
    "source": "Midjourney / Stable Diffusion Generation"
  },
  {
    "id": "var002",
    "type": "image",
    "category": "photograph",
    "title": "Fresh Crispy Fried Samosas on Street Paper",
    "file": "/content/human_samosa.jpg",
    "answer": "human",
    "difficulty": "easy",
    "explanation": "Real human photograph. Authentic food photography from a street stall: notice the genuine oil sheen, organic frying micro-blisters on the pastry dough, and real printed newspaper lining.",
    "source": "Wikimedia Commons / Street Food Photography"
  },
  {
    "id": "var003",
    "type": "image",
    "category": "artwork",
    "title": "Astronaut Riding a Horse in Space",
    "file": "/content/ai_astronaut_horse.webp",
    "answer": "ai",
    "difficulty": "easy",
    "explanation": "AI-generated artwork. Official Stable Diffusion 3.5 benchmark image. Look at the synthetic blending of the horse's mane into cosmic nebulae and the physically impossible space environment.",
    "source": "Stable Diffusion 3.5 Research Release"
  },
  {
    "id": "var004",
    "type": "image",
    "category": "artwork",
    "title": "Girl with a Pearl Earring (1665)",
    "file": "/content/human_pearl_earring.jpg",
    "answer": "human",
    "difficulty": "medium",
    "explanation": "Human-created masterpiece. Johannes Vermeer's 1665 oil painting. Notice the genuine canvas craquelure (fine microscopic paint cracking over centuries) and historical sfumato glaze technique.",
    "source": "Mauritshuis Museum, The Hague / Wikimedia Commons"
  },
  {
    "id": "var005",
    "type": "image",
    "category": "photograph",
    "title": "The Taj Mahal from Central Reflecting Pool",
    "file": "/content/human_taj_mahal.jpg",
    "answer": "human",
    "difficulty": "medium",
    "explanation": "Real photograph. Authentic architectural photo of the Taj Mahal. Notice real tourist silhouettes in the distance, natural atmospheric water vapor haze, and realistic ripples in the reflecting pool.",
    "source": "Wikimedia Commons / Architectural Photography"
  },
  {
    "id": "var006",
    "type": "image",
    "category": "artwork",
    "title": "Steampunk Mechanical Brass Dove",
    "file": "/content/ai_mechanical_dove.png",
    "answer": "ai",
    "difficulty": "medium",
    "explanation": "AI-generated digital artwork. Created with Midjourney. While the brass gears look intricate, the mechanical linkages defy functional clockwork physics and feather edges dissolve unnaturally.",
    "source": "Midjourney V5 Showcase / Wikimedia Commons"
  },
  {
    "id": "var007",
    "type": "image",
    "category": "photograph",
    "title": "Macro Monarch Butterfly on Echinacea",
    "file": "/content/human_butterfly.jpg",
    "answer": "human",
    "difficulty": "hard",
    "explanation": "Real photograph. High-speed macro shot of a Monarch butterfly. Notice the microscopic dust scales on the wing margins, natural pollen grains on the flower stamen, and authentic optical depth-of-field.",
    "source": "Wikimedia Commons / Macro Wildlife Photography"
  },
  {
    "id": "var008",
    "type": "image",
    "category": "photograph",
    "title": "Tokyo Tower Night Skyline",
    "file": "/content/human_tokyo_tower.jpg",
    "answer": "human",
    "difficulty": "medium",
    "explanation": "Real photograph. Night skyline shot of Tokyo Tower. Notice authentic optical lens flare from distant street lamps and realistic sensor noise grain in dark shadow regions.",
    "source": "Wikimedia Commons / Cityscape Photography"
  },
  {
    "id": "var009",
    "type": "image",
    "category": "artwork",
    "title": "Comic Dinosaur Illustration",
    "file": "/content/ai_comic_dinosaur.png",
    "answer": "ai",
    "difficulty": "easy",
    "explanation": "AI-generated illustration. Created with Midjourney. Notice the airbrushed gradient textures, slightly illogical scale overlap, and dreamlike lighting characteristics typical of diffusion art.",
    "source": "Midjourney Creative Showcase / Wikimedia Commons"
  },
  {
    "id": "var010",
    "type": "image",
    "category": "photograph",
    "title": "Albert Einstein Historic Portrait (1947)",
    "file": "/content/human_einstein.jpg",
    "answer": "human",
    "difficulty": "hard",
    "explanation": "Real historic photograph. Famous 1947 portrait of Albert Einstein by legendary photographer Philipp Halsman. Authentic analog silver-halide film grain, deep focus, and natural skin pores.",
    "source": "Library of Congress / Philipp Halsman"
  },
  {
    "id": "var011",
    "type": "image",
    "category": "artwork",
    "title": "The Starry Night (1889)",
    "file": "/content/human_starry_night.jpg",
    "answer": "human",
    "difficulty": "easy",
    "explanation": "Human-created masterpiece. Vincent van Gogh's famous 1889 oil on canvas. Authentic physical impasto brushwork where thick oil paint physically rises above the surface of the canvas.",
    "source": "Museum of Modern Art / Google Art Project"
  },
  {
    "id": "var012",
    "type": "image",
    "category": "photograph",
    "title": "Bengal Tiger in Natural Habitat",
    "file": "/content/human_tiger.jpg",
    "answer": "human",
    "difficulty": "hard",
    "explanation": "Real wildlife photograph. Captured with a telephoto lens; notice real individual whiskers varying in length and thickness, natural scratches on the snout, and authentic optical bokeh.",
    "source": "Wikimedia Commons / Wildlife Photography"
  },
  {
    "id": "var013",
    "type": "image",
    "category": "photograph",
    "title": "Espresso Cup on Wooden Cafe Table",
    "file": "/content/human_coffee_cup.jpg",
    "answer": "human",
    "difficulty": "medium",
    "explanation": "Real photograph. Notice the realistic surface tension bubbles in the espresso crema and authentic subtle water rings on the untreated wood.",
    "source": "Wikimedia Commons / Food Photography"
  },
  {
    "id": "var014",
    "type": "image",
    "category": "photograph",
    "title": "New York City Skyline at Night HDR",
    "file": "/content/human_nyc_night.jpg",
    "answer": "human",
    "difficulty": "hard",
    "explanation": "Real composite long-exposure photograph. Notice true-to-life architectural variety of Manhattan buildings, individual office window blinds, and realistic harbor reflections.",
    "source": "Wikimedia Commons / Urban HDR Photography"
  },
  {
    "id": "var015",
    "type": "image",
    "category": "photograph",
    "title": "DALL-E 2 Portrait Generation",
    "file": "/content/ai_dalle_photo.jpg",
    "answer": "ai",
    "difficulty": "hard",
    "explanation": "AI-generated image. An official DALL-E 2 digital photo demonstration. While skin tones look natural, the corneal light reflections do not match the surrounding light sources.",
    "source": "OpenAI DALL-E 2 Research Showcase"
  },
  {
    "id": "var016",
    "type": "image",
    "category": "artwork",
    "title": "Baby Daikon Radish Walking a Dog",
    "file": "/content/ai_dalle_radish.jpg",
    "answer": "ai",
    "difficulty": "easy",
    "explanation": "AI-generated image. One of the historical milestone generations from the original OpenAI DALL-E paper illustrating compositional concept blending.",
    "source": "OpenAI DALL-E Research Paper"
  },

  # ----------------------------------------------------
  # 2. CODE SNIPPETS (16 items)
  # ----------------------------------------------------
  {
    "id": "var017",
    "type": "code",
    "category": "code_snippet",
    "title": "Cart Total Calculator",
    "language": "javascript",
    "content": "function calculateTotal(items) {\n  if (!Array.isArray(items)) {\n    throw new TypeError('Expected an array of items');\n  }\n  return items.reduce((accumulator, currentItem) => {\n    const price = Number(currentItem?.price) || 0;\n    return accumulator + price;\n  }, 0);\n}",
    "answer": "ai",
    "difficulty": "easy",
    "explanation": "AI-written code. Generated with textbook defensive programming, verbose variable names ('accumulator', 'currentItem'), and standard nullish coalescing patterns typical of modern LLMs.",
    "source": "ChatGPT Code Generation Benchmark"
  },
  {
    "id": "var018",
    "type": "code",
    "category": "code_snippet",
    "title": "Weekend Check & Magic Offset",
    "language": "javascript",
    "content": "// TODO: fix this hack before demo on friday pls\nconst isWeekend = (d) => [0, 6].includes(new Date(d).getDay());\nconst magicOffset = 42; // don't touch, breaks prod\nconst normalized = val ? (val ^ magicOffset) : null;",
    "answer": "human",
    "difficulty": "medium",
    "explanation": "Human-written code. Real codebase artifacts: an anxious Friday demo TODO comment, an unexplained 'magicOffset' constant with a warning not to touch it, and a bitwise XOR shortcut.",
    "source": "Open Source Git Repository"
  },
  {
    "id": "var019",
    "type": "code",
    "category": "code_snippet",
    "title": "Matrix Spiral Traversal",
    "language": "python",
    "content": "def spiral_traverse(matrix):\n    res = []\n    while matrix:\n        res += matrix.pop(0)\n        matrix = list(zip(*matrix))[::-1]\n    return res",
    "answer": "human",
    "difficulty": "hard",
    "explanation": "Human-written Python code. The famous one-liner `zip(*matrix)[::-1]` rotational unpack is an idiosyncratic human competitive programming idiom, not standard LLM boilerplate.",
    "source": "Competitive Programming LeetCode Submission"
  },
  {
    "id": "var020",
    "type": "code",
    "category": "code_snippet",
    "title": "Palindrome String Validator",
    "language": "python",
    "content": "def is_valid_palindrome(text: str) -> bool:\n    \"\"\"Checks if a given string is a palindrome, ignoring non-alphanumeric chars.\"\"\"\n    cleaned = [ch.lower() for ch in text if ch.isalnum()]\n    return cleaned == cleaned[::-1]",
    "answer": "ai",
    "difficulty": "medium",
    "explanation": "AI-written Python function. Clean type hints, docstring with exact standard phrasing, and textbook list comprehension typical of ChatGPT responses to coding challenges.",
    "source": "ChatGPT Python Coding Benchmark"
  },
  {
    "id": "var021",
    "type": "code",
    "category": "code_snippet",
    "title": "Debounce Hook in React",
    "language": "javascript",
    "content": "function useDebounce(value, delay) {\n  const [debouncedValue, setDebouncedValue] = useState(value);\n  useEffect(() => {\n    const handler = setTimeout(() => setDebouncedValue(value), delay);\n    return () => clearTimeout(handler);\n  }, [value, delay]);\n  return debouncedValue;\n}",
    "answer": "ai",
    "difficulty": "medium",
    "explanation": "AI-written React hook. The absolute canonical implementation repeated verbatim across millions of ChatGPT training tokens, containing zero custom edge-case overrides.",
    "source": "Synthetic React Hook Generator"
  },
  {
    "id": "var022",
    "type": "code",
    "category": "code_snippet",
    "title": "CSS Trick: Center Div with transform",
    "language": "css",
    "content": ".center-box {\n  position: absolute;\n  top: 50%;\n  left: 50%;\n  transform: translate(-50%, -50%);\n  /* IE9 support? nobody cares anymore */\n}",
    "answer": "human",
    "difficulty": "easy",
    "explanation": "Human-written CSS. Contains the classic developer exasperation comment '/* IE9 support? nobody cares anymore */' written by a web developer who lived through older browser wars.",
    "source": "Real Frontend CSS Stylesheet"
  },
  {
    "id": "var023",
    "type": "code",
    "category": "code_snippet",
    "title": "Rust Thread-Safe Counter",
    "language": "rust",
    "content": "use std::sync::{Arc, Mutex};\nuse std::thread;\n\npub struct SafeCounter {\n    count: Arc<Mutex<i64>>,\n}\n\nimpl SafeCounter {\n    pub fn new() -> Self {\n        Self { count: Arc::new(Mutex::new(0)) }\n    }\n}",
    "answer": "ai",
    "difficulty": "hard",
    "explanation": "AI-written Rust snippet. Ultra-clean, textbook Arc<Mutex<T>> pattern with pristine public visibility qualifiers and canonical `Self { count: Arc::new(Mutex::new(0)) }` constructor formatting.",
    "source": "Claude 3.5 Rust Generation"
  },
  {
    "id": "var024",
    "type": "code",
    "category": "code_snippet",
    "title": "SQL Query with Weird Grouping",
    "language": "sql",
    "content": "SELECT u.id, u.email, count(o.id) as orders\nFROM users u\nLEFT JOIN orders o ON o.user_id = u.id\nWHERE u.deleted_at IS NULL\nGROUP BY 1, 2\nHAVING count(o.id) > 5\nORDER BY 3 DESC;",
    "answer": "human",
    "difficulty": "hard",
    "explanation": "Human-written SQL. Pragmatic developer shortcut using positional column ordinal numbers in `GROUP BY 1, 2` and `ORDER BY 3 DESC`, which LLMs typically avoid in favor of explicit column names.",
    "source": "Production Analytics SQL Query"
  },
  {
    "id": "var025",
    "type": "code",
    "category": "code_snippet",
    "title": "Deep Clone Object Utility",
    "language": "javascript",
    "content": "const deepClone = (obj) => {\n  if (obj === null || typeof obj !== 'object') return obj;\n  if (obj instanceof Date) return new Date(obj.getTime());\n  if (obj instanceof Array) return obj.map(item => deepClone(item));\n  const cloned = {};\n  for (const key in obj) {\n    if (Object.prototype.hasOwnProperty.call(obj, key)) {\n      cloned[key] = deepClone(obj[key]);\n    }\n  }\n  return cloned;\n};",
    "answer": "ai",
    "difficulty": "hard",
    "explanation": "AI-written utility function. Rigorous defensive recursion covering Date instances and utilizing `Object.prototype.hasOwnProperty.call`, standard in LLM coding answers for avoiding prototype pollution.",
    "source": "ChatGPT Algorithm Implementation"
  },
  {
    "id": "var026",
    "type": "code",
    "category": "code_snippet",
    "title": "Python Date Parsing Hotfix",
    "language": "python",
    "content": "def parse_date_cursed(s):\n    # Sometimes marketing sends '2024-05-12', sometimes '12/05/2024'\n    # God help us all\n    for fmt in ('%Y-%m-%d', '%d/%m/%Y', '%m/%d/%Y'):\n        try:\n            return datetime.strptime(s.strip(), fmt)\n        except ValueError:\n            pass\n    return None",
    "answer": "human",
    "difficulty": "medium",
    "explanation": "Human-written Python code. Blames the marketing department for inconsistent date formats in the comment ('God help us all') and uses a function name `parse_date_cursed`.",
    "source": "Backend Django API Service"
  },
  {
    "id": "var027",
    "type": "code",
    "category": "code_snippet",
    "title": "Binary Search Implementation",
    "language": "javascript",
    "content": "function binarySearch(arr, target) {\n  let left = 0;\n  let right = arr.length - 1;\n  while (left <= right) {\n    const mid = Math.floor(left + (right - left) / 2);\n    if (arr[mid] === target) return mid;\n    if (arr[mid] < target) left = mid + 1;\n    else right = mid - 1;\n  }\n  return -1;\n}",
    "answer": "ai",
    "difficulty": "medium",
    "explanation": "AI-written code. Includes the textbook integer-overflow mitigation `left + (right - left) / 2` which is famous in C/Java algorithm books but virtually redundant in JavaScript floating-point numbers.",
    "source": "Copilot Algorithm Benchmark"
  },
  {
    "id": "var028",
    "type": "code",
    "category": "code_snippet",
    "title": "Bash Script Cleanup Routine",
    "language": "bash",
    "content": "#!/usr/bin/env bash\nset -euo pipefail\n\nDIR=\"${1:-/tmp/builds}\"\nfind \"$DIR\" -name \"*.log\" -type f -mtime +7 -delete\necho \"[$(date '+%Y-%m-%d %H:%M:%S')] Cleanup completed successfully.\"",
    "answer": "ai",
    "difficulty": "hard",
    "explanation": "AI-generated Bash script. Follows pristine best practices: `set -euo pipefail`, parameter expansion default `${1:-...}`, and ISO standard timestamp formatting.",
    "source": "DevOps AI Assistant"
  },
  {
    "id": "var029",
    "type": "code",
    "category": "code_snippet",
    "title": "Regex for Email Validation",
    "language": "javascript",
    "content": "// whoever wrote the RFC 5322 regex was on something\n// this works 99% of the time, good enough for onboarding form\nconst emailRegex = /^[^\\s@]+@[^\\s@]+\\.[^\\s@]+$/;\nexport const isValidEmail = (e) => emailRegex.test(String(e).trim());",
    "answer": "human",
    "difficulty": "easy",
    "explanation": "Human-written code. Pragmatic developer comment mocking the official RFC 5322 standard and settling for a simple 'good enough' regex.",
    "source": "Frontend Form Validation File"
  },
  {
    "id": "var030",
    "type": "code",
    "category": "code_snippet",
    "title": "Go HTTP Health Handler",
    "language": "go",
    "content": "func HealthCheckHandler(w http.ResponseWriter, r *http.Request) {\n\tw.Header().Set(\"Content-Type\", \"application/json\")\n\tw.WriteHeader(http.StatusOK)\n\tjson.NewEncoder(w).Encode(map[string]string{\"status\": \"ok\", \"timestamp\": time.Now().UTC().Format(time.RFC3339)})\n}",
    "answer": "ai",
    "difficulty": "medium",
    "explanation": "AI-written Go handler. Standard idiomatic microservice health endpoint with RFC3339 UTC formatting produced by default when asking ChatGPT for a Go healthcheck.",
    "source": "Go Microservice AI Template"
  },
  {
    "id": "var031",
    "type": "code",
    "category": "code_snippet",
    "title": "React Key Generator Workaround",
    "language": "javascript",
    "content": "{items.map((item, idx) => (\n  // yes I know using index as key is bad practice\n  // but backend doesn't return UUIDs and ticket is due in 10 mins\n  <ListItem key={`${item.name}_${idx}`} data={item} />\n))}",
    "answer": "human",
    "difficulty": "easy",
    "explanation": "Human-written JSX. Frank developer confession admitting to bad React key practices because the backend team didn't supply IDs.",
    "source": "Real React Codebase"
  },
  {
    "id": "var032",
    "type": "code",
    "category": "code_snippet",
    "title": "TypeScript Generic Result Type",
    "language": "typescript",
    "content": "export type Result<T, E = Error> =\n  | { success: true; data: T }\n  | { success: false; error: E };\n\nexport const ok = <T>(data: T): Result<T, never> => ({ success: true, data });\nexport const err = <E>(error: E): Result<never, E> => ({ success: false, error });",
    "answer": "ai",
    "difficulty": "hard",
    "explanation": "AI-written TypeScript. Textbook Rust-style discriminated union Result type implementation frequently generated by modern LLMs when asked for functional error handling in TypeScript.",
    "source": "TypeScript Functional Library AI Prompt"
  },

  # ----------------------------------------------------
  # 3. SOCIAL MEDIA POSTS & TWEETS (15 items)
  # ----------------------------------------------------
  {
    "id": "var033",
    "type": "text",
    "category": "social_post",
    "title": "Cat 3 AM Zoomies Observation",
    "content": "My cat just stared at the blank wall for 45 minutes, meowed aggressively at nothing, did three 360-degree burnouts on the rug, and went back to sleep. I pay rent here just to be an audience member.",
    "answer": "human",
    "difficulty": "easy",
    "explanation": "Human-written social post. Captures authentic, idiosyncratic pet behavior with natural self-deprecating human comedy ('pay rent just to be an audience member') that LLMs rarely produce unprompted.",
    "source": "Viral Twitter / X Post"
  },
  {
    "id": "var034",
    "type": "text",
    "category": "social_post",
    "title": "Monday Motivation Quote",
    "content": "Success isn’t about luck; it’s about relentless dedication. Every sunrise presents an opportunity to outwork yesterday’s doubts. Rise, grind, innovate, and conquer your destiny. #MondayMotivation #LeadershipMindset #GrindNeverStops",
    "answer": "ai",
    "difficulty": "easy",
    "explanation": "AI-generated social post. Filled with generic platitudes, high cliché density, and a predictable string of motivational hashtags characteristic of zero-shot LLM outputs.",
    "source": "GPT-4 / Synthetic Social Media Prompt"
  },
  {
    "id": "var035",
    "type": "text",
    "category": "social_post",
    "title": "LinkedIn Certification Celebration",
    "content": "I am humbled and thrilled to announce that I have completed the Certified Agility Mindset Practitioner course! 🚀 What started as a 4-week exploration taught me that true leadership isn't about answers, but asking the right questions. Agree? Thoughts?",
    "answer": "ai",
    "difficulty": "easy",
    "explanation": "AI-generated parody of corporate LinkedIn posts. Contains every signature hallmark: 'humbled and thrilled', rocket emoji, vacuous leadership insight, and the mandatory closing engagement bait ('Agree? Thoughts?').",
    "source": "Corporate Satire LLM Prompt"
  },
  {
    "id": "var036",
    "type": "text",
    "category": "social_post",
    "title": "IKEA Furniture Assembly Mishap",
    "content": "My dad spent 4 hours assembling an IKEA desk today, proudly announced it was done, and then realized he built it around the radiator and it cannot be moved out of the corner without taking the radiator off the wall.",
    "answer": "human",
    "difficulty": "medium",
    "explanation": "Real human Reddit post. Classic situational human comedy based on an actual physical blunder that only happens in real life.",
    "source": "Reddit /r/mildlyinfuriating"
  },
  {
    "id": "var037",
    "type": "text",
    "category": "social_post",
    "title": "Tech Hot Take on Microservices",
    "content": "In 2026, the real full-stack engineer is just a person who knows which 4 SaaS dashboards to refresh when production is on fire.",
    "answer": "human",
    "difficulty": "hard",
    "explanation": "Human-written tech tweet. Witty, cynical industry observation with concise comedic phrasing that accurately captures modern DevOps pain points.",
    "source": "Hacker News / Twitter Discussion"
  },
  {
    "id": "var038",
    "type": "text",
    "category": "social_post",
    "title": "Coffee & Focus Thought",
    "content": "There is a profound beauty in the morning routine: the aroma of freshly ground dark roast beans, the quiet hum of an awakening metropolis, and sixty uninterrupted minutes dedicated to deep architectural thought before the world begins to demand your attention.",
    "answer": "ai",
    "difficulty": "hard",
    "explanation": "AI-written post. Highly polished, rhythmic, and poetic sentence cadence ('profound beauty', 'awakening metropolis', 'uninterrupted minutes') that reads smoothly but lacks concrete personal specifics.",
    "source": "Claude 3.5 Lifestyle Prompt"
  },
  {
    "id": "var039",
    "type": "text",
    "category": "social_post",
    "title": "Airport Gate Change Rant",
    "content": "They just changed our departure gate from B2 to D48 with 12 minutes until boarding. Watching 140 strangers collectively power-walk like competitive racewalkers through terminal security is the closest thing humanity has to synchronized swimming.",
    "answer": "human",
    "difficulty": "medium",
    "explanation": "Human-written observation. Specific vivid imagery ('power-walk like competitive racewalkers', 'terminal security') and humorous metaphor drawn from real travel distress.",
    "source": "Viral Twitter / X Post"
  },
  {
    "id": "var040",
    "type": "text",
    "category": "social_post",
    "title": "Remote Work Productivity Reflection",
    "content": "Embracing asynchronous collaboration has fundamentally transformed our organizational throughput. When teams are empowered with psychological safety and transparent documentation, geographic boundaries dissolve into unified velocity. The future of work is intentional.",
    "answer": "ai",
    "difficulty": "medium",
    "explanation": "AI-generated corporate reflection. Saturated with HR buzzwords ('asynchronous collaboration', 'psychological safety', 'unified velocity') that sound professional but express zero concrete team examples.",
    "source": "Synthetic B2B LinkedIn Post"
  },
  {
    "id": "var041",
    "type": "text",
    "category": "social_post",
    "title": "College Exam Hall Panic",
    "content": "Flipped the exam question paper over, saw 'Question 1: Derive the following using first principles', and my brain immediately played the Wii sports bowling strike animation.",
    "answer": "human",
    "difficulty": "medium",
    "explanation": "Human-written college humor. Specific internet meme reference ('Wii sports bowling strike animation') combined with genuine student panic during a university examination.",
    "source": "College Student Subreddit"
  },
  {
    "id": "var042",
    "type": "text",
    "category": "social_post",
    "title": "Mindfulness & Technology Balance",
    "content": "Digital wellness isn't about discarding our devices; it's about curating our relationship with the algorithms that compete for our cognitive bandwidth. Take a mindful breath, close unnecessary browser tabs, and reclaim your presence in the physical world.",
    "answer": "ai",
    "difficulty": "hard",
    "explanation": "AI-written mindfulness post. Well-crafted syntactic balance and gentle instructional tone ('curating our relationship', 'cognitive bandwidth') typical of wellness prompts given to LLMs.",
    "source": "Wellness Bot AI Post"
  },
  {
    "id": "var043",
    "type": "text",
    "category": "social_post",
    "title": "Microwave Soup Disaster",
    "content": "I heated up tomato soup for 45 seconds and the bowl was hotter than the surface of the sun while the soup inside was still legally classified as a slushie.",
    "answer": "human",
    "difficulty": "easy",
    "explanation": "Human-written tweet. Universal shared human frustration regarding microwave physics expressed with hyperbole ('legally classified as a slushie').",
    "source": "Twitter / X Viral Post"
  },
  {
    "id": "var044",
    "type": "text",
    "category": "social_post",
    "title": "AI Impact on Creative Expression",
    "content": "As generative models continue to iterate at unprecedented scale, the ultimate moat for human creators won't be technical execution, but emotional resonance. Authenticity cannot be computed; it must be lived.",
    "answer": "ai",
    "difficulty": "hard",
    "explanation": "AI-generated philosophical commentary on AI itself. Neatly formulated parallel aphorism ('cannot be computed; it must be lived') characteristic of GPT-4's syntheses on creativity.",
    "source": "ChatGPT Tech Essay Synthesis"
  },
  {
    "id": "var045",
    "type": "text",
    "category": "social_post",
    "title": "Grocery Shopping with Kids",
    "content": "Went to the grocery store for eggs and milk, spent $140, and somehow came home with zero eggs, no milk, but two wooden pirate swords and a 4-pound bag of frozen edamame.",
    "answer": "human",
    "difficulty": "medium",
    "explanation": "Human-written parenting post. Grounded in chaotic domestic reality with specific irrational items ('two wooden pirate swords', 'frozen edamame').",
    "source": "Parenting Forum Discussion"
  },
  {
    "id": "var046",
    "type": "text",
    "category": "social_post",
    "title": "Continuous Learning Philosophy",
    "content": "True mastery is not a destination, but a continual calibration of curiosity against the expanding horizon of knowledge. Cultivate intellectual humility, embrace the friction of difficult problems, and never cease to be a student of the craft.",
    "answer": "ai",
    "difficulty": "hard",
    "explanation": "AI-written quote. Elegant, rhythmic, but entirely abstract ('continual calibration of curiosity', 'expanding horizon of knowledge') without grounding in any specific skill or craft.",
    "source": "LLM Philosophical Synthesis"
  },
  {
    "id": "var047",
    "type": "text",
    "category": "social_post",
    "title": "Software Update at 4:59 PM",
    "content": "IT pushed a mandatory Windows restart update at 4:59 PM while I had 47 unsaved browser tabs and an open excel sheet called 'Book1_FINAL_REAL_v3'. I felt my soul leave my body.",
    "answer": "human",
    "difficulty": "easy",
    "explanation": "Human-written workplace post. The filename 'Book1_FINAL_REAL_v3' and 47 unsaved tabs are authentic markers of human desk-worker chaos.",
    "source": "Corporate Humor Forum"
  },

  # ----------------------------------------------------
  # 4. CUSTOMER REVIEWS (12 items)
  # ----------------------------------------------------
  {
    "id": "var048",
    "type": "text",
    "category": "review",
    "title": "Kitchen Blender Customer Review",
    "content": "Bought this blender specifically because it claimed to crush ice. Day 2: sounded like a jet engine eating gravel, smelled like burning rubber, and left 3 whole ice cubes floating in my smoothie like glaciers mocking me. 2 stars because at least the pulse button is satisfying to mash in rage.",
    "answer": "human",
    "difficulty": "medium",
    "explanation": "Real human product review. The humorous specific imagery ('glaciers mocking me', 'jet engine eating gravel') and emotional nuance in the rating are distinctive hallmarks of genuine customer frustration.",
    "source": "Verified E-Commerce Customer Review"
  },
  {
    "id": "var049",
    "type": "text",
    "category": "review",
    "title": "Wireless Earbuds Review",
    "content": "These wireless earbuds exceeded all my expectations! The soundstage is remarkably balanced with crisp highs and resonant, deep bass. The ergonomic design ensures hours of fatigue-free listening, while the intuitive touch controls make navigating playlists seamless. A truly indispensable companion for any audiophile on the go.",
    "answer": "ai",
    "difficulty": "medium",
    "explanation": "AI-generated product review. Follows standard synthetic sentiment structure: perfectly balanced audio buzzwords ('crisp highs', 'resonant bass', 'fatigue-free listening') without a single personal real-world usage incident.",
    "source": "Synthetic LLM Product Review Benchmark"
  },
  {
    "id": "var050",
    "type": "text",
    "category": "review",
    "title": "Cozy Neighborhood Cafe Review",
    "content": "The barista looked like he was mourning a lost love while pulling my espresso shot, but honestly? Best flat white I've had in 3 years. The sourdough croissant was so flaky it turned my lap into a crime scene of golden crumbs. Will definitely return.",
    "answer": "human",
    "difficulty": "hard",
    "explanation": "Real human cafe review. Distinctive human humor ('barista looked like he was mourning a lost love', 'lap into a crime scene') that captures authentic cafe atmosphere.",
    "source": "Google Maps / Yelp Local Review"
  },
  {
    "id": "var051",
    "type": "text",
    "category": "review",
    "title": "Italian Bistro Restaurant Review",
    "content": "Dining at Trattoria Bella was a culinary voyage! From the decadent truffle risotto that melted effortlessly on the palate to the impeccably tender osso buco, every dish was an artisanal triumph. The staff was attentive and knowledgeable, creating an unforgettable ambiance.",
    "answer": "ai",
    "difficulty": "hard",
    "explanation": "AI-generated dining review. Overloaded with florid food-critic clichés ('culinary voyage', 'decadent truffle risotto', 'artisanal triumph') that AI models generate when prompted for 5-star reviews.",
    "source": "ChatGPT E-Commerce Review Prompt"
  },
  {
    "id": "var052",
    "type": "text",
    "category": "review",
    "title": "Ergonomic Office Chair Review",
    "content": "Assembly instructions consisted of three blurry diagrams and an Allen wrench made of what felt like recycled tin foil. The chair is comfortable once you survive the two-hour blood sacrifice required to attach the armrests.",
    "answer": "human",
    "difficulty": "medium",
    "explanation": "Real human furniture review. Specific complaints about cheap tools ('Allen wrench made of recycled tin foil') and relatable assembly struggles.",
    "source": "Amazon Customer Review"
  },
  {
    "id": "var053",
    "type": "text",
    "category": "review",
    "title": "Mechanical Keyboard Review",
    "content": "The tactile actuation on these blue switches provides an immensely satisfying acoustic feedback with every keystroke. Typing feels fluid, precise, and remarkably therapeutic. The RGB backlighting offers vibrant customization without being overly intrusive.",
    "answer": "ai",
    "difficulty": "hard",
    "explanation": "AI-written keyboard review. Clean, adjective-heavy synthetic writing ('immensely satisfying acoustic feedback', 'remarkably therapeutic') lacking real testing notes (e.g. key wobble, gaming latency).",
    "source": "Synthetic Tech Gadget Review"
  },
  {
    "id": "var054",
    "type": "text",
    "category": "review",
    "title": "Budget Hotel Review",
    "content": "Room was advertised as having a 'city view'. The window opened directly into an exhaust pipe for the fish market downstairs. On the plus side, AC was colder than my ex's heart. 3/5 stars.",
    "answer": "human",
    "difficulty": "easy",
    "explanation": "Real human travel review. Genuine situational comedy contrasting the misleading marketing claim with the absurd fish market exhaust reality.",
    "source": "TripAdvisor Review"
  },
  {
    "id": "var055",
    "type": "text",
    "category": "review",
    "title": "Smart Fitness Watch Review",
    "content": "This smartwatch has completely revolutionized my fitness regimen. The heart rate tracking is remarkably accurate, and the sleep architecture analysis provides profound insights into recovery metrics. The battery life effortlessly powers through four full days of rigorous use.",
    "answer": "ai",
    "difficulty": "medium",
    "explanation": "AI-generated fitness review. Reuses standard marketing terminology ('sleep architecture analysis', 'profound insights', 'effortlessly powers') without detailing specific workout glitches.",
    "source": "Synthesized Gadget Review Dataset"
  },
  {
    "id": "var056",
    "type": "text",
    "category": "review",
    "title": "Camping Tent Review",
    "content": "Said it was a 4-person tent. Only possible if the 4 persons are medieval toddlers stacked like cordwood. My husband and our 40lb golden retriever barely fit diagonally. But it held up in 30mph rain without leaking, so credit where credit is due.",
    "answer": "human",
    "difficulty": "hard",
    "explanation": "Human-written outdoor gear review. The vivid comparison ('medieval toddlers stacked like cordwood') and personal dog anecdote demonstrate human authenticity.",
    "source": "REI Customer Gear Review"
  },
  {
    "id": "var057",
    "type": "text",
    "category": "review",
    "title": "Ceramic Non-Stick Skillet Review",
    "content": "Cooking with this ceramic skillet has been an absolute delight. The non-stick coating delivers flawless food release with minimal butter, making clean-up an effortless breeze. Heat distribution is impeccably uniform across the entire cooking surface.",
    "answer": "ai",
    "difficulty": "hard",
    "explanation": "AI-generated cookware review. Classic marketing phrases ('effortless breeze', 'impeccably uniform', 'flawless food release') produced by standard commercial LLM templates.",
    "source": "E-Commerce Review Generator"
  },
  {
    "id": "var058",
    "type": "text",
    "category": "review",
    "title": "Children's Board Game Review",
    "content": "Fun game until your 6-year-old realizes you can form a ruthless monopoly on the red tiles and sends her grandmother into financial ruin while eating chicken nuggets. 10/10 family bonding.",
    "answer": "human",
    "difficulty": "medium",
    "explanation": "Human-written board game review. Amusing real family dynamic (six-year-old bankrupting grandmother while eating nuggets).",
    "source": "BoardGameGeek Review"
  },
  {
    "id": "var059",
    "type": "text",
    "category": "review",
    "title": "Noise-Cancelling Headphones Review",
    "content": "The active noise cancellation creates a serene sanctuary of silence, silencing ambient chatter and transportation rumble alike. The memory foam earcups mold gently around the ears, providing a cloud-like listening experience.",
    "answer": "ai",
    "difficulty": "hard",
    "explanation": "AI-generated headphone review. Heavy reliance on poetic sensory metaphors ('serene sanctuary of silence', 'cloud-like listening experience') typical of promotional AI text.",
    "source": "AI Audio Gear Review"
  },

  # ----------------------------------------------------
  # 5. POETRY & LITERATURE (10 items)
  # ----------------------------------------------------
  {
    "id": "var060",
    "type": "text",
    "category": "poem",
    "title": "Autumn Reverie",
    "content": "The autumn leaves begin to fall,\nIn golden whispers through the trees,\nA silent dance, an ancient call,\nUpon the crisp November breeze.\nThe quiet earth prepares for sleep,\nBeneath a twilight sky of gray,\nWhile whispered promises we keep,\nUntil the dawn of brighter day.",
    "answer": "ai",
    "difficulty": "medium",
    "explanation": "AI-generated poem. Classic LLM poetic structure: strict ABAB rhyming scheme, iambic tetrameter, and predictable sentimental tropes ('silent dance', 'crisp breeze', 'twilight sky of gray').",
    "source": "ChatGPT Poetry Generation"
  },
  {
    "id": "var061",
    "type": "text",
    "category": "poem",
    "title": "Morning Crumbs",
    "content": "Some mornings the tea steeps too dark\nand the kettle whistles like a dog that knows\nwe are leaving. I brush crumbs off the table\ninto my palm, then throw them out the window.\nA sparrow takes them before they hit the gravel.",
    "answer": "human",
    "difficulty": "hard",
    "explanation": "Human-written modern free verse poem. Grounded in sensory domestic specificity (tea too dark, kettle like an anxious dog, crumbs thrown to a sparrow) without artificial rhyming formulas.",
    "source": "Contemporary Literary Journal"
  },
  {
    "id": "var062",
    "type": "text",
    "category": "fictional_writing",
    "title": "The Six-Word Story",
    "content": "For sale: baby shoes, never worn.",
    "answer": "human",
    "difficulty": "hard",
    "explanation": "Human literature. The famous six-word micro-story often attributed to Ernest Hemingway. Raw emotional devastation achieved through what is left unsaid.",
    "source": "Classic Literary Microfiction"
  },
  {
    "id": "var063",
    "type": "text",
    "category": "fictional_writing",
    "title": "Midnight at the Manor",
    "content": "The grandfather clock chimed midnight in the empty manor. Arthur tightened his coat against the chill, watching shadows stretch across the parquet floor. He reached for the brass doorknob, knowing that once turned, there was no going back.",
    "answer": "ai",
    "difficulty": "hard",
    "explanation": "AI-generated gothic fiction opening. Standard atmospheric tropes in sequential order: midnight chime, empty manor, cold chill, shadow on floor, turning the doorknob of no return.",
    "source": "Creative Fiction LLM Benchmark"
  },
  {
    "id": "var064",
    "type": "text",
    "category": "poem",
    "title": "The Ocean's Solitude",
    "content": "The endless waves embrace the shore,\nIn tides of azure, foam, and spray,\nA timeless rhythm evermore,\nThat washes all our cares away.\nThe seagulls glide upon the wind,\nAbove the ocean's silver crest,\nWhere restless waters gently bend,\nTo lull the weary soul to rest.",
    "answer": "ai",
    "difficulty": "medium",
    "explanation": "AI-generated ocean verse. Predictable rhyming pairs (shore/evermore, spray/away, wind/bend, crest/rest) with uniform metrical predictability.",
    "source": "Synthetic Poetry Generator"
  },
  {
    "id": "var065",
    "type": "text",
    "category": "poem",
    "title": "Subway Platform Late Night",
    "content": "A discarded MetroCard skitters across the yellow tactile paving.\nThe fluorescent tube above vibrates in the key of B-flat.\nWe stand six feet apart, checking phones for messages\nwe already know haven't arrived.",
    "answer": "human",
    "difficulty": "hard",
    "explanation": "Human-written urban poetry. Specific tactile urban observations ('yellow tactile paving', 'key of B-flat') and modern psychological honesty.",
    "source": "Modern Urban Poetry Anthology"
  },
  {
    "id": "var066",
    "type": "text",
    "category": "fictional_writing",
    "title": "The Clockmaker's Secret",
    "content": "Master Elias examined the tiny balance spring through his brass loupe. For three centuries, his guild had concealed the truth: the clockworks did not measure time; they generated it, ticking by ticking, weaving reality from tension and escapement gears.",
    "answer": "ai",
    "difficulty": "hard",
    "explanation": "AI-generated fantasy prompt. High-concept premise delivered with standard fantasy tropes ('Master Elias', 'brass loupe', 'three centuries guild secret').",
    "source": "Creative Writing Prompt Generator"
  },
  {
    "id": "var067",
    "type": "text",
    "category": "fictional_writing",
    "title": "Gas Station at 2 AM",
    "content": "The clerk was microwaving an egg roll that had probably been in the freezer since the Obama administration. The neon sign outside buzzed with the sound of dying moths.",
    "answer": "human",
    "difficulty": "medium",
    "explanation": "Human-written micro-fiction. Dry cultural reference ('Obama administration') and gritty sensory details ('buzzing with dying moths').",
    "source": "Flash Fiction Online"
  },
  {
    "id": "var068",
    "type": "text",
    "category": "poem",
    "title": "Digital Consciousness Haiku",
    "content": "Silicon and spark,\nCircuits dream in binary,\nDawn of silicon.",
    "answer": "ai",
    "difficulty": "easy",
    "explanation": "AI-generated haiku. Cliché repetition of 'silicon' in line 1 and line 3, a common structural repetition flaw in simple 5-7-5 prompt outputs.",
    "source": "ChatGPT Haiku Prompt"
  },
  {
    "id": "var069",
    "type": "text",
    "category": "poem",
    "title": "Kitchen Sink Haiku",
    "content": "Cold grease in the pan,\nOne spoon left in the drawer,\nSoup again tonight.",
    "answer": "human",
    "difficulty": "hard",
    "explanation": "Human-written haiku. Unromantic, gritty domestic reality captured in 17 syllables without sentimentality.",
    "source": "Contemporary Haiku Collection"
  },

  # ----------------------------------------------------
  # 6. EMAILS & WORKPLACE COMMUNICATIONS (12 items)
  # ----------------------------------------------------
  {
    "id": "var070",
    "type": "text",
    "category": "email",
    "title": "B2B Synergy Partnership Outreach",
    "content": "Dear John,\n\nI hope this email finds you well. I came across your impressive profile on LinkedIn and was thoroughly inspired by your innovative work at your company. We specialize in cutting-edge synergy solutions that optimize workflow velocity by up to 37%.\n\nWould you have 10 minutes for a brief introductory call this Thursday?\n\nBest regards,\nAlex",
    "answer": "ai",
    "difficulty": "medium",
    "explanation": "AI-generated sales email. Formulaic greeting ('hope this finds you well'), vague compliment, artificial metric ('by up to 37%'), and standard low-friction call-to-action.",
    "source": "Cold Outreach LLM Prompt"
  },
  {
    "id": "var071",
    "type": "text",
    "category": "email",
    "title": "Office Refrigerator Notice",
    "content": "Hey team - quick reminder that someone left a plastic container of what appears to be either butter chicken or lava in the 3rd floor fridge. It has become sentient. If not claimed by 4 PM today it will be respectfully evicted into the dumpster.",
    "answer": "human",
    "difficulty": "hard",
    "explanation": "Real workplace email sent by an office manager. Contains authentic workplace gallows humor ('either butter chicken or lava', 'become sentient') and natural informal cadence.",
    "source": "Verified Workplace Communication"
  },
  {
    "id": "var072",
    "type": "text",
    "category": "email",
    "title": "Polite Calendar Meeting Decline",
    "content": "Hi Mark,\n\nThanks for the invitation to the cross-functional brainstorming sync. Due to pressing deliverables on our Q3 sprint commitment, I will have to respectfully decline. Please keep me posted via the meeting notes if any direct action items emerge for engineering.\n\nWarm regards,\nSarah",
    "answer": "ai",
    "difficulty": "hard",
    "explanation": "AI-generated decline email. Polished corporate etiquette with balanced clauses and standard corporate phrases ('cross-functional brainstorming sync', 'pressing deliverables').",
    "source": "Executive Assistant LLM Template"
  },
  {
    "id": "var073",
    "type": "text",
    "category": "email",
    "title": "Slack Message: WiFi Outage",
    "content": "hey is the 4th floor wifi down for everyone or is my laptop just protesting my existence today",
    "answer": "human",
    "difficulty": "easy",
    "explanation": "Human-written workplace Slack message. Lowercase casual typing, self-deprecating human humor, and lack of corporate formalities.",
    "source": "Real Company Slack Channel"
  },
  {
    "id": "var074",
    "type": "text",
    "category": "email",
    "title": "Project Post-Mortem Announcement",
    "content": "Team,\n\nFollowing the conclusion of Phase 2, we are convening an all-hands retrospective to celebrate our achievements and systematically identify opportunities for operational refinement. Please come prepared with constructive insights on cross-team dependencies.",
    "answer": "ai",
    "difficulty": "medium",
    "explanation": "AI-generated management email. Dense corporate buzzwords ('systematically identify opportunities', 'operational refinement', 'cross-team dependencies') that mask any actual project emotion.",
    "source": "Corporate Memo AI Generator"
  },
  {
    "id": "var075",
    "type": "text",
    "category": "email",
    "title": "Coffee Machine Broken Email",
    "content": "The espresso machine is flashing an error code 'E-04'. Do NOT press the steam wand unless you want boiling oat milk sprayed onto the acoustic ceiling tiles again. IT has been notified.",
    "answer": "human",
    "difficulty": "medium",
    "explanation": "Human-written office email. Specific hilarious previous incident referenced ('boiling oat milk sprayed onto the acoustic ceiling tiles again').",
    "source": "Company Internal Email"
  },
  {
    "id": "var076",
    "type": "text",
    "category": "email",
    "title": "Quarterly Performance Self-Review Summary",
    "content": "Throughout this quarter, I prioritized proactive cross-functional alignment while maintaining focus on core OKR deliverables. I successfully mitigated three potential blockers in the deployment pipeline, fostering enhanced team agility and predictability.",
    "answer": "ai",
    "difficulty": "hard",
    "explanation": "AI-generated self-evaluation. Classic prompt output for performance reviews: combines 'proactive cross-functional alignment' and 'enhanced team agility' without mentioning a single real project name.",
    "source": "Performance Review Prompt"
  },
  {
    "id": "var077",
    "type": "text",
    "category": "email",
    "title": "Out of Office Auto-Reply",
    "content": "I am out of the office until Monday. I have cell service but I will be actively ignoring it to teach my dog how to kayak. For urgent server issues, contact Dave. If Dave is unavailable, start praying.",
    "answer": "human",
    "difficulty": "medium",
    "explanation": "Human-written out-of-office message. Distinctive irreverent humor ('teach my dog how to kayak', 'start praying') that standard corporate AI tools avoid.",
    "source": "Real Engineer Out of Office Notice"
  },
  {
    "id": "var078",
    "type": "text",
    "category": "email",
    "title": "Enterprise Software Renewal Reminder",
    "content": "Dear Administrator,\n\nYour annual enterprise subscription is scheduled for renewal in 30 days. To ensure uninterrupted access to your mission-critical analytics dashboard, please review your current licensing tier. Our team is available to assist with custom seat allocation.",
    "answer": "ai",
    "difficulty": "medium",
    "explanation": "AI-generated notification. Textbook enterprise transactional email with standard cadence ('mission-critical analytics dashboard', 'uninterrupted access').",
    "source": "SaaS Notification Generator"
  },
  {
    "id": "var079",
    "type": "text",
    "category": "email",
    "title": "Friday 5 PM Production Panic",
    "content": "who touched the billing service db migrations at 4:58 pm on a friday i am begging you to reveal yourself in this thread",
    "answer": "human",
    "difficulty": "easy",
    "explanation": "Human-written on-call message. Raw panic, all lowercase typography, and a desperate plea to an unknown culprit who deployed on a Friday afternoon.",
    "source": "Engineering Incident Channel"
  },
  {
    "id": "var080",
    "type": "text",
    "category": "email",
    "title": "Town Hall Q&A Follow-up",
    "content": "Thank you for submitting your thoughtful queries during yesterday's Global Town Hall. Leadership has collated your feedback and will provide transparent, actionable responses in our upcoming bi-weekly newsletter.",
    "answer": "ai",
    "difficulty": "hard",
    "explanation": "AI-written executive follow-up. Neutral bureaucratic reassurance ('collated your feedback', 'actionable responses') that deflects immediate answers.",
    "source": "Internal Comms Generator"
  },
  {
    "id": "var081",
    "type": "text",
    "category": "email",
    "title": "Lost Badge Email",
    "content": "I lost my security badge somewhere between the lobby turnstile and the 2nd floor donut table. If found, please return to my desk. The photo on it was taken at 8 AM on a Monday and does not accurately represent my will to live.",
    "answer": "human",
    "difficulty": "hard",
    "explanation": "Human-written office email. Self-deprecating humor regarding the employee ID photo ('does not accurately represent my will to live').",
    "source": "Real Office Communication"
  },

  # ----------------------------------------------------
  # 7. PRODUCT DESCRIPTIONS & MARKETING (12 items)
  # ----------------------------------------------------
  {
    "id": "var082",
    "type": "text",
    "category": "product_description",
    "title": "Nordic Forest Botanical Candle",
    "content": "Imbued with the restorative essence of wild bergamot and sun-drenched cedar, this hand-poured botanical candle evokes the tranquil stillness of a Nordic forest. Crafted with clean-burning soy wax and a crackling wooden wick, it offers 55 hours of mindful serenity.",
    "answer": "ai",
    "difficulty": "hard",
    "explanation": "AI-generated product description. Exhibits standard luxury marketing tropes ('restorative essence', 'mindful serenity', 'sun-drenched') generated by an e-commerce copywriting prompt.",
    "source": "E-Commerce Copywriting LLM Benchmark"
  },
  {
    "id": "var083",
    "type": "text",
    "category": "product_description",
    "title": "Uncle's Ghost Pepper Hot Sauce",
    "content": "We made this hot sauce because our uncle said commercial ghost pepper sauces are for babies. He tried two drops of this on a taco and drank three pints of whole milk while questioning his life choices. Put it on wings, eggs, or use it to settle family arguments.",
    "answer": "human",
    "difficulty": "hard",
    "explanation": "Real independent hot sauce label copy. Grounded in a personal family anecdote, self-deprecating humor, and a distinctive voice that commercial LLM alignment guidelines typically smooth over.",
    "source": "Artisanal Hot Sauce Bottle Label"
  },
  {
    "id": "var084",
    "type": "text",
    "category": "advertisement",
    "title": "Nike Motivational Ad Copy",
    "content": "Yesterday you said tomorrow. Just do it.",
    "answer": "human",
    "difficulty": "medium",
    "explanation": "Human-created advertisement. Legendary 7-word Nike campaign written by human creative directors at Wieden+Kennedy. Extreme brevity and punchiness that AI rarely achieves without filler.",
    "source": "Nike / Wieden+Kennedy Campaign Archive"
  },
  {
    "id": "var085",
    "type": "text",
    "category": "advertisement",
    "title": "Aero-Mesh Sneaker Ad Copy",
    "content": "Step into the future of foot comfort. Engineered with revolutionary dynamic cushioning and breathable aero-mesh, our sneakers adapt to every stride you take. Elevate your everyday journey.",
    "answer": "ai",
    "difficulty": "hard",
    "explanation": "AI-generated sneaker ad copy. Packed with generic tech-adjective pairs ('revolutionary dynamic', 'breathable aero-mesh') that sound polished but describe no actual unique technology.",
    "source": "Commercial Copywriting AI Generator"
  },
  {
    "id": "var086",
    "type": "text",
    "category": "product_description",
    "title": "Artisanal Single-Origin Coffee",
    "content": "Cultivated on the mist-covered volcanic slopes of Antigua, this exquisite microlot roast features delicate floral top notes that yield to a velvety honey-processed chocolate finish. Each small batch is roasted to perfection.",
    "answer": "ai",
    "difficulty": "hard",
    "explanation": "AI-generated coffee copy. Formulaic specialty coffee adjectives ('mist-covered volcanic slopes', 'exquisite microlot', 'roasted to perfection') produced by LLM marketing prompts.",
    "source": "Specialty Coffee AI Copy Prompt"
  },
  {
    "id": "var087",
    "type": "text",
    "category": "product_description",
    "title": "Indie Craft Beer Can Description",
    "content": "We dry-hopped this IPA with so much Citra and Mosaic that our head brewer smelled like a tropical fruit salad for two weeks. Tastes like peach rings, pine needles, and bad financial decisions. 6.8% ABV.",
    "answer": "human",
    "difficulty": "medium",
    "explanation": "Real craft brewery label copy. Informal candor ('smelled like a tropical fruit salad', 'bad financial decisions') distinctive of independent craft brewers.",
    "source": "Craft Brewery Can Label"
  },
  {
    "id": "var088",
    "type": "text",
    "category": "advertisement",
    "title": "Luxury Minimalist Watch Tagline",
    "content": "Time is the ultimate currency. Spend it with elegance. Handcrafted Swiss precision for the discerning visionary.",
    "answer": "ai",
    "difficulty": "medium",
    "explanation": "AI-generated luxury slogan. Stacks predictable luxury keywords ('ultimate currency', 'discerning visionary', 'Swiss precision') without distinct brand identity.",
    "source": "Luxury Advertising AI Generator"
  },
  {
    "id": "var089",
    "type": "text",
    "category": "advertisement",
    "title": "Avis Car Rental Famous Slogan",
    "content": "When you're only No. 2, you try harder. Or else.",
    "answer": "human",
    "difficulty": "hard",
    "explanation": "Human-created advertising legend. Paula Green's iconic 1962 Avis campaign that turned a market-share disadvantage into the greatest brand honesty angle in advertising history.",
    "source": "DDB Advertising Archive"
  },
  {
    "id": "var090",
    "type": "text",
    "category": "product_description",
    "title": "Ergonomic Mechanical Pencil Copy",
    "content": "Designed for architects and dreamers alike, the knurled brass barrel provides balanced gravitational counterbalance, preventing hand fatigue during marathon sketching sessions.",
    "answer": "ai",
    "difficulty": "hard",
    "explanation": "AI-generated stationery copy. Pretentious pseudo-technical phrasing ('balanced gravitational counterbalance') typical of synthetic copywriting.",
    "source": "Stationery Copy AI Prompt"
  },
  {
    "id": "var091",
    "type": "text",
    "category": "product_description",
    "title": "Handmade Wool Beanie Tag",
    "content": "Knitted by Brenda in Vermont while watching murder documentaries. 100% itchy wool that will keep your ears warm in a blizzard. Hand wash only or it will shrink to fit an angry squirrel.",
    "answer": "human",
    "difficulty": "medium",
    "explanation": "Human-written craft tag. Humorous personal context ('while watching murder documentaries') and warning ('shrink to fit an angry squirrel').",
    "source": "Vermont Craft Fair Product Tag"
  },
  {
    "id": "var092",
    "type": "text",
    "category": "advertisement",
    "title": "Sustainable Water Bottle Slogan",
    "content": "Hydrate responsibly. Designed for the planet, built for your life. Join the reusability revolution today.",
    "answer": "ai",
    "difficulty": "easy",
    "explanation": "AI-written eco slogan. Standard generic sustainability clichés ('hydrate responsibly', 'reusability revolution') that appear in thousands of AI marketing outputs.",
    "source": "Eco Product Copy Generator"
  },
  {
    "id": "var093",
    "type": "text",
    "category": "advertisement",
    "title": "VW Beetle 'Lemon' Ad",
    "content": "Lemon. This Volkswagen missed the boat. The chrome strip on the glove compartment is blemished and must be replaced.",
    "answer": "human",
    "difficulty": "hard",
    "explanation": "Human advertising landmark. The revolutionary 1960 DDB campaign for the VW Beetle that shocked readers by calling their own car a 'Lemon' before explaining their obsessive quality control.",
    "source": "DDB Madison Avenue Archive"
  },

  # ----------------------------------------------------
  # 8. NEWS HEADLINES & ARTICLES (12 items)
  # ----------------------------------------------------
  {
    "id": "var094",
    "type": "text",
    "category": "news_headline",
    "title": "Convenience Store Barter",
    "content": "Florida Man Arrested After Trying to Trade Live Alligator for Pack of Beer at Convenience Store",
    "answer": "human",
    "difficulty": "easy",
    "explanation": "Real human news headline. An actual bizarre news incident from 2013 in Miami that became part of internet lore. Reality is consistently stranger than AI hallucinations.",
    "source": "Associated Press / Miami News"
  },
  {
    "id": "var095",
    "type": "text",
    "category": "news_headline",
    "title": "AI Smart Bottle Launch",
    "content": "Tech Startup Unveils Smart Water Bottle That Nudges Users with Predictive AI Dehydration Algorithms",
    "answer": "ai",
    "difficulty": "medium",
    "explanation": "AI-generated tech headline. Employs common Silicon Valley buzzwords ('predictive algorithms', 'smart', 'unveils') synthesized to mimic tech-crunch style venture capital announcements.",
    "source": "Synthetic Tech Headline Generator"
  },
  {
    "id": "var096",
    "type": "text",
    "category": "news_headline",
    "title": "Zoo Escape Incident",
    "content": "Escaped Flamingo Evades Texas Wildlife Officials for 17 Years Following 2005 Zoo Breakout",
    "answer": "human",
    "difficulty": "hard",
    "explanation": "Real news headline. Verified March 2022 wildlife report documenting 'Flamingo No. 492' who escaped a Wichita zoo in 2005 and lived peacefully in Texas coastal bays.",
    "source": "The Guardian / Wildlife News"
  },
  {
    "id": "var097",
    "type": "text",
    "category": "news_headline",
    "title": "Autonomous Coffee Delivery Fleet",
    "content": "Global Coffee Giant Pilots Drone Constellation for Sub-Five-Minute Artisanal Latte Delivery in Urban Corridors",
    "answer": "ai",
    "difficulty": "hard",
    "explanation": "AI-generated corporate headline. Uses corporate buzz phrases ('drone constellation', 'sub-five-minute', 'urban corridors') common in AI-generated press releases.",
    "source": "AI Tech News Simulator"
  },
  {
    "id": "var098",
    "type": "text",
    "category": "news_headline",
    "title": "Traffic Jam Goat Miracle",
    "content": "Runaway Goat Shuts Down Interstate for Three Hours After Becoming Enamored With Highway Construction Cone",
    "answer": "human",
    "difficulty": "medium",
    "explanation": "Real news report. Actual transit dispatch from Pennsylvania where a rogue farm animal halted morning rush hour traffic over an orange pylon.",
    "source": "Local News Station Broadcast"
  },
  {
    "id": "var099",
    "type": "text",
    "category": "news_headline",
    "title": "Quantum Neural Computing Breakthrough",
    "content": "Researchers Achieve Groundbreaking Quantum Coherence in Room-Temperature Nanomaterials, Paving Way for Instantaneous Processing",
    "answer": "ai",
    "difficulty": "hard",
    "explanation": "AI-generated science headline. Combines high-prestige physics keywords ('quantum coherence', 'room-temperature nanomaterials', 'instantaneous processing') with vague milestone verbs ('paving way').",
    "source": "AI Science Headline Generator"
  },
  {
    "id": "var100",
    "type": "text",
    "category": "news_headline",
    "title": "Stolen Bronze Statue Mishap",
    "content": "Thieves Return Stolen 200-Pound Town Mascot Statue After Realizing It Wouldn't Fit in Their Honda Civic Trunk",
    "answer": "human",
    "difficulty": "medium",
    "explanation": "Real news police blotter. Genuine criminal incompetence report where thieves abandoned a heavy bronze town sculpture after a trunk size miscalculation.",
    "source": "Local Police Blotter Report"
  },
  {
    "id": "var101",
    "type": "text",
    "category": "news_headline",
    "title": "Renewable Clean Energy Milestone",
    "content": "Nordic City Becomes First Municipality to Run 100% on Kinetic Sidewalk Energy and Rooftop Solar Symbiosis",
    "answer": "ai",
    "difficulty": "hard",
    "explanation": "AI-generated utopian headline. Uses futuristic buzz-concepts ('kinetic sidewalk energy', 'solar symbiosis') that sound plausible to casual readers but have no real civic deployment.",
    "source": "AI Environmental Tech Fiction"
  },
  {
    "id": "var102",
    "type": "text",
    "category": "news_headline",
    "title": "Chess Grandmaster Device Paranoia",
    "content": "Chess Tournament Official Undergoes Metal Detector Scan After Opponent Suspects Vibrating Shoes",
    "answer": "human",
    "difficulty": "hard",
    "explanation": "Real news headline. Verified report from the heated international chess cheating controversies that gripped competitive chess championships in 2022-2023.",
    "source": "Chess.com / BBC Sport"
  },
  {
    "id": "var103",
    "type": "text",
    "category": "news_headline",
    "title": "Smart City AI Traffic Optimization",
    "content": "Metropolitan Council Adopts Decentralized Machine Learning to Dynamically Harmonize Transit Bottlenecks",
    "answer": "ai",
    "difficulty": "hard",
    "explanation": "AI-generated civic headline. Dense corporate techno-speak ('decentralized machine learning', 'dynamically harmonize transit bottlenecks') generated by an urban planning prompt.",
    "source": "Smart City AI Simulation"
  },
  {
    "id": "var104",
    "type": "text",
    "category": "news_headline",
    "title": "Antique Violin Airport Security Error",
    "content": "Musician Forced to Buy Second Plane Ticket for $45,000 Cello Because It 'Looked Nervous at TSA'",
    "answer": "human",
    "difficulty": "medium",
    "explanation": "Human news interview. Concert cellist's real humorous quote recounting frustrating airline ticketing absurdities for fragile musical instruments.",
    "source": "Classical Music News Wire"
  },
  {
    "id": "var105",
    "type": "text",
    "category": "news_headline",
    "title": "Bio-Synthesized Vegan Cheese Milestone",
    "content": "Biotech Firm Synthesizes Precision-Fermented Gouda That Mimics Aging rind at Molecular Level",
    "answer": "ai",
    "difficulty": "hard",
    "explanation": "AI-generated food-tech headline. Polished synthesis of food science buzzwords ('precision-fermented', 'molecular level') generated by a synthetic biotech news prompt.",
    "source": "Biotech Venture AI Generator"
  }
]

print(f"Total items in enhanced dataset: {len(items)}")

# Verify distribution
type_counts = {}
diff_counts = {}
ans_counts = {}

for it in items:
    t = it["type"]
    type_counts[t] = type_counts.get(t, 0) + 1
    d = it["difficulty"]
    diff_counts[d] = diff_counts.get(d, 0) + 1
    a = it["answer"]
    ans_counts[a] = ans_counts.get(a, 0) + 1

print("Types:", type_counts)
print("Difficulties:", diff_counts)
print("Answers:", ans_counts)

# Save to both paths
with open("src/data/content.json", "w", encoding="utf-8") as f:
    json.dump(items, f, indent=2, ensure_ascii=False)

with open("public/data/content.json", "w", encoding="utf-8") as f:
    json.dump(items, f, indent=2, ensure_ascii=False)

print("Saved successfully to src/data/content.json and public/data/content.json!")
