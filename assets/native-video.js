/* Native same-origin video only. No persistent progress storage, requests to YouTube or analytics. */
'use strict';
document.querySelectorAll('video[data-native-video]').forEach((video) => {
 const status = video.closest('.r-video-card').querySelector('.r-video-status');
 const setStatus = (message) => { if (status) status.textContent = message; };
 video.addEventListener('playing', () => setStatus('Playing. Use the player controls to pause, seek or enter full screen.'));
 video.addEventListener('pause', () => setStatus('Paused. Press Play to continue.'));
 video.addEventListener('waiting', () => setStatus('Loading video… If playback does not continue, use the YouTube backup or written guide.'));
 video.addEventListener('ended', () => setStatus('Playback completed. The written guide and support links remain available below.'));
 video.addEventListener('error', () => setStatus('The video could not be loaded. Try again, or use the YouTube backup or written guide below.'));
 video.querySelectorAll('source').forEach(source => source.addEventListener('error', () => setStatus('The video could not be loaded. Use the YouTube backup or written guide below.')));
});
