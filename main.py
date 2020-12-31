from __future__ import unicode_literals
from os import getenv
from os import system as os_system
from pathlib import Path
from uuid import uuid4
from youtube_dl import YoutubeDL

# TODO: Change this to accept through sys.argv
# Read in playlist url from playlist.url
playlist_url = (Path.cwd() / "playlist.url").open().read()

temp_dir = Path(getenv("TEMP")) if getenv("TEMP") != None else Path.cwd()

output_dir = temp_dir / f"dahlia-{uuid4()}"
yt_dl_output_template = str(temp_dir) + "/%(title)s.%(ext)s"

yt_dl_options = {

}

with YoutubeDL(yt_dl_options) as yt_dl:
	yt_dl.download([playlist_url])

os_system(f"explorer.exe {output_dir}")
