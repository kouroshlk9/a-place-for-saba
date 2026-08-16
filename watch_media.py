from pathlib import Path
import time, subprocess, sys
root=Path(__file__).resolve().parent
media=root/"media"
def snapshot():
    return {(p.as_posix(),p.stat().st_mtime_ns,p.stat().st_size) for p in media.rglob("*") if p.is_file()}
last=None
print("Watching media folders... Ctrl+C to stop.")
while True:
    cur=snapshot()
    if cur!=last:
        subprocess.run([sys.executable,str(root/"update_media.py")])
        last=cur
    time.sleep(2)
