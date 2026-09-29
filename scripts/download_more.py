import urllib.request
import ssl
import json
import os

os.makedirs("public/content", exist_ok=True)
ctx = ssl._create_unverified_context()
headers = {'User-Agent': 'PixelpaloozaGame/1.0 (contact@pixelpalooza.in)'}

files = [
    {
        "filename": "File:A_mechanical_dove_8274822e-52fe-40fa-ac4d-f3cde5a332ae.png",
        "output": "public/content/ai_mechanical_dove.png"
    },
    {
        "filename": "File:Midjourney_-_Comic_Dinosaur.png",
        "output": "public/content/ai_comic_dinosaur.png"
    },
    {
        "filename": "File:Tokyo_Tower_and_around_Skyscrapers.jpg",
        "output": "public/content/human_tokyo_tower.jpg"
    },
    {
        "filename": "File:Albert_Einstein_Head.jpg",
        "output": "public/content/human_einstein.jpg"
    }
]

for item in files:
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
    except Exception as e:
        print(f"Error {fname}: {e}")
