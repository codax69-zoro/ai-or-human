import urllib.request
import ssl
import json
import os

os.makedirs("public/content", exist_ok=True)
ctx = ssl._create_unverified_context()
headers = {'User-Agent': 'PixelpaloozaGame/1.0 (contact@pixelpalooza.in)'}

additional_images = [
    # Real Human Photographs & Artworks
    {
        "filename": "File:Van_Gogh_-_Starry_Night_-_Google_Art_Project.jpg",
        "output": "public/content/human_starry_night.jpg",
        "type": "human"
    },
    {
        "filename": "File:Golden_Gate_Bridge_as_seen_from_Battery_Lancaster.jpg",
        "output": "public/content/human_golden_gate.jpg",
        "type": "human"
    },
    {
        "filename": "File:Bengal_tiger_(Panthera_tigris_tigris)_female_3.jpg",
        "output": "public/content/human_tiger.jpg",
        "type": "human"
    },
    {
        "filename": "File:A_small_cup_of_coffee.JPG",
        "output": "public/content/human_coffee_cup.jpg",
        "type": "human"
    },
    {
        "filename": "File:New_York_City_at_night_HDR.jpg",
        "output": "public/content/human_nyc_night.jpg",
        "type": "human"
    },
    # Verified AI Generations on Wikimedia Commons
    {
        "filename": "File:Cyberpunk_city_street,_AI_generated.png",
        "output": "public/content/ai_cyberpunk_street.png",
        "type": "ai"
    },
    {
        "filename": "File:Deep-fried_rat_and_French_fries_generated_by_Midjourney.png",
        "output": "public/content/ai_viral_food.png",
        "type": "ai"
    },
    {
        "filename": "File:Cat_wearing_sunglasses_sitting_on_a_surfboard_generated_by_Midjourney.png",
        "output": "public/content/ai_surf_cat.png",
        "type": "ai"
    }
]

for item in additional_images:
    fname = item["filename"]
    out_path = item["output"]
    if os.path.exists(out_path):
        print(f"Already exists: {out_path}")
        continue
    try:
        url = f"https://commons.wikimedia.org/w/api.php?action=query&titles={urllib.parse.quote(fname)}&prop=imageinfo&iiprop=url&iiurlwidth=800&format=json"
        req = urllib.request.Request(url, headers=headers)
        res = urllib.request.urlopen(req, context=ctx)
        data = json.loads(res.read().decode('utf-8'))
        pages = data.get("query", {}).get("pages", {})
        page = list(pages.values())[0]
        if "imageinfo" in page:
            thumb_url = page["imageinfo"][0].get("thumburl", page["imageinfo"][0]["url"])
            print(f"Downloading {fname} -> {out_path}...")
            img_req = urllib.request.Request(thumb_url, headers=headers)
            img_data = urllib.request.urlopen(img_req, context=ctx).read()
            with open(out_path, "wb") as f:
                f.write(img_data)
            print(f"Saved {out_path} ({len(img_data)} bytes)")
        else:
            print(f"No imageinfo found for {fname}")
    except Exception as e:
        print(f"Error {fname}: {e}")
