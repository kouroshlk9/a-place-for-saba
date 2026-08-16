from pathlib import Path
import json, re

ROOT = Path(__file__).resolve().parent
MEDIA = ROOT / "media"
EXT = {
    "music": {".mp3",".m4a",".ogg",".wav",".flac",".aac"},
    "photos": {".jpg",".jpeg",".png",".webp",".gif"},
    "voices": {".ogg",".mp3",".m4a",".wav",".aac"},
}
IGNORE = {"put_music_here.txt","put_songs_here.txt","put_photos_here.txt","put_voices_here.txt"}

def clean(stem):
    s = stem.replace("_"," ").replace("-"," ")
    s = re.sub(r"\b(128|192|256|320)\b","",s,flags=re.I)
    s = re.sub(r"\s+"," ",s).strip()
    return s

def files(kind):
    p=MEDIA/kind
    return sorted([x for x in p.rglob("*") if x.is_file() and x.suffix.lower() in EXT[kind] and x.name.lower() not in IGNORE],
                  key=lambda x:x.name.casefold())

def music_item(p):
    title=clean(p.stem); artist=""
    # filename convention "Artist - Title"
    raw=p.stem.replace("_"," ")
    if " - " in raw:
        artist, title0 = raw.split(" - ",1)
        artist=clean(artist); title=clean(title0)
    return {"title":title,"artist":artist,"path":p.relative_to(ROOT).as_posix()}

def item(p):
    return {"title":clean(p.stem),"path":p.relative_to(ROOT).as_posix()}

data={
 "music":[music_item(p) for p in files("music")],
 "photos":[item(p) for p in files("photos")],
 "voices":[item(p) for p in files("voices")]
}
(ROOT/"media-manifest.json").write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding="utf-8")
print(f"Updated: {len(data['music'])} music | {len(data['photos'])} photos | {len(data['voices'])} voices")
