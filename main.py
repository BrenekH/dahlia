import subprocess
from os import getenv
from os import system as os_system
from pathlib import Path
from sys import argv as sys_argv
from uuid import uuid4

try:
	playlist_url = sys_argv[1]
except IndexError:
	f = Path(getenv("APPDATA")) / "brenekh-Dahlia/url.config" # APPDATA gives Windows "Roaming" data
	if not f.exists():
		raise RuntimeError(f"Could not locate playlist url to download. Either pass it on the command line or setup {f}")
	playlist_url = f.open().read()

temp_dir = Path(getenv("TEMP")) if getenv("TEMP") != None else Path.cwd()
output_dir = temp_dir / f"dahlia-{uuid4()}"
output_dir.mkdir(parents=True, exist_ok=True)

yt_dl_output_template = str(output_dir) + "/%(title)s.%(ext)s"

ran_process = subprocess.run(["youtube-dl", "-o", str(yt_dl_output_template), "-x", "--audio-format", "mp3", str(playlist_url)])

if ran_process.returncode == 0:
	os_system(f"explorer {output_dir}")

input("Press enter to exit...")
