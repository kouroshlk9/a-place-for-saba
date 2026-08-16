A PLACE FOR SABA — Gift Hub

1) Copy your files into:
   media/music
   media/photos
   media/voices

2) Double-click UPDATE_MEDIA.bat.
   It regenerates media-manifest.json automatically.

3) For automatic local watching, double-click WATCH_MEDIA.bat.
   Leave that window open while adding/removing media.

4) Open index.html through a local web server (recommended), e.g.:
   py -m http.server 8000
   then visit localhost:8000

5) For GitHub Pages:
   run UPDATE_MEDIA.bat, then commit/push index.html, media-manifest.json,
   and whichever media files you actually want hosted.
   Local files that are not pushed cannot be played by the public website.

The site never needs manual HTML edits just to add/remove media.
