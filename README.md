# A Little Universe for Us ♡

An elegant, interactive, mobile-friendly monthsary gift website. This is a **static website**: HTML + CSS + JavaScript. Python is used **only as an optional local file server**, not as an application backend. No database and no installation required.

## Quick start (VS Code)

1. Open this project folder in VS Code.
2. Open `script.js`. Edit the `CONFIG` object **at the very top**:
   - `recipient`: your partner's name.
   - `sender`: your name.
   - `monthsaryDate`: your actual date.
   - `monogram` and `copy`: customize the initials and on-page wording.
   - `letter`, `photos`, `reasons`, `songs`, and `finalMessage`: replace sample content with your real story.
   - For each `songs` entry, update `number`, `title`, `artist`, `stage`, `dedication`, `timelineDescription`, `artworkUrl`, and `spotifyTrackId`. Spotify embeds are created only after a visitor opens that song's in-page player and do not autoplay. To use your own legally obtained, web-authorized audio instead, add its local file path (for example, `assets/audio/song-1.mp3`) to that entry's `audioUrl`.
3. Add your own photos in a browser-friendly format such as `.jpg`, `.png`, or `.webp` under `assets/photos/`, then set each `file` in `CONFIG.photos` to its exact name and extension. Browsers do not consistently display `.HEIC` photos, so convert HEIC images to JPG first. Without photos, decorative placeholders display instead.
4. Background music is set in `CONFIG.backgroundMusic` in `script.js`. The current track is “Gymnopedie No. 1” by Kevin MacLeod, licensed under CC BY 4.0; its attribution and license links appear in the footer. Browsers that block autoplay show a welcome button to start playback. iPhone/iPad may require that tap before music can begin, and device volume controls remain in charge. Keep the visible credit if you choose another track with attribution requirements.
5. **Easiest:** double-click `index.html`, or use the VS Code **Live Server** extension.
6. **Optional Python way:** from the project folder run `python serve.py` (or `py serve.py` on Windows). Open `http://localhost:8000` on your laptop.
7. To view it on your phone while testing, connect the phone and laptop to the same Wi-Fi, run the optional server, and open the LAN address it prints (for example, `http://192.168.1.25:8000`). Allow Python through Windows Firewall on private networks if prompted. For access from anywhere, publish the static files using GitHub Pages or Netlify.

## Publish it for your girlfriend

You can publish these static files on GitHub Pages or Netlify. Upload the `index.html`, `style.css`, `script.js`, and `assets` directory together. Python is **not needed** after publishing.

## Note about sample content

The default sample date and messages are placeholders; personalize them before sending. Photo and music files are not included: bring your own. Google Fonts are requested online but fallback fonts work offline.

## Copilot prompt

"Work on my existing static monthsary site, preserving its elegant burgundy/rose design. Use only HTML, CSS and vanilla JavaScript; no Node, frameworks, database or backend. Python may only serve static files locally. Help me personalize the CONFIG object in script.js, improve accessibility/mobile behavior, and add romantic details without breaking existing features. Keep files separate and explain any changes."
