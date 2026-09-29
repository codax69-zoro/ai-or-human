import urllib.request
import ssl
import json
import os

os.makedirs("public/content", exist_ok=True)
ctx = ssl._create_unverified_context()
headers = {'User-Agent': 'PixelpaloozaGame/1.0 (contact@pixelpalooza.in)'}

# Target Wikimedia files to download (800px thumbnails)
files_to_download = [
    # Human photographs & artworks
    {
        "filename": "File:Samosa_13.jpg",
        "output": "public/content/human_samosa.jpg",
        "type": "human",
        "desc": "Real food photography of crispy fried Indian samosas"
    },
    {
        "filename": "File:Auto_rickshaw_in_Delhi.jpg",
        "output": "public/content/human_autorickshaw.jpg",
        "type": "human",
        "desc": "Real candid photograph of an auto rickshaw on a street in Delhi"
    },
    {
        "filename": "File:Girl_with_a_Pearl_Earring.jpg",
        "output": "public/content/human_pearl_earring.jpg",
        "type": "human",
        "desc": "Johannes Vermeer's authentic 1665 oil painting masterpiece"
    },
    {
        "filename": "File:Taj_Mahal_(Edited).jpeg",
        "output": "public/content/human_taj_mahal.jpg",
        "type": "human",
        "desc": "Real photograph of the Taj Mahal taken from the central reflecting pool"
    },
    {
        "filename": "File:Monarch_In_May.jpg",
        "output": "public/content/human_butterfly.jpg",
        "type": "human",
        "desc": "Real wildlife macro photograph of a Monarch butterfly on a flower"
    },
    {
        "filename": "File:Old_man_in_Varanasi.jpg",
        "output": "public/content/human_elderly_portrait.jpg",
        "type": "human",
        "desc": "Real candid portrait of an elder in Varanasi with genuine skin texture and wrinkles"
    },
    # AI generated images
    {
        "filename": "File:Astronaut_Riding_a_Horse_(SD3.5).webp",
        "output": "public/content/ai_astronaut_horse.webp",
        "type": "ai",
        "desc": "AI generation benchmark created with Stable Diffusion 3.5"
    }
]

for item in files_to_download:
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
        print(f"Error downloading {fname}: {e}")
