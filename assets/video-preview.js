if (location.protocol === 'file:') {
    const player = document.querySelector('iframe');
    if (player) {
        const notice = document.createElement('p');
        notice.className = 'video-fallback';
        notice.textContent = 'Local file preview may not support YouTube playback. Open this page through a web server, or use the YouTube link below.';
        player.before(notice);
    }
}
