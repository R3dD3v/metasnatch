# metasnatch
iHeart Radio Metadata Grabber
-- Written in Python

-----------------------------

So I was using Tizonia to listen to iHeart radio
but I noticed that it doesn't tell me what's playing.
Like any sensible person, I decided to do it myself

-----------------------------

Currently
- You can freely choose your radio station
- Uses the song history from iHeart's API to work globally across all stations

TODO
- Pull radio station data
- Add Station search so we aren't relying on IDs
- Write install script, because even though it's easy to install, some people are lazy

----------------------------

Installation
- `python -m pip install requests`
- `git clone https://github.com/r3dd3v/metasnatch.git`
- `cd metasnatch-main`
- `python3 metasnatch.py`
  If you'd like, you can add an alias to ~/.bashrc as metasnatch
  `alias metasnatch="python3 /home/metasnatch-main/metasnatch.py"`
