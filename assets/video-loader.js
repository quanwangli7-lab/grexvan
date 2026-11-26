/* No player, thumbnail, cookies or analytics until an explicit visitor action. */
'use strict';
document.querySelectorAll('.r-video-mount[data-video-id]').forEach((mount) => {
  const button = mount.querySelector('button');
  if (!button) return;
  button.addEventListener('click', () => {
    const id = mount.dataset.videoId;
    if (!/^[A-Za-z0-9_-]{11}$/.test(id)) return;
    const frame = document.createElement('iframe');
    frame.src = `https://www.youtube-nocookie.com/embed/${id}`;
    frame.title = mount.dataset.videoTitle || 'GREXVAN installation video';
    frame.allow = 'accelerometer; encrypted-media; gyroscope; picture-in-picture; fullscreen';
    frame.allowFullscreen = true;
    frame.referrerPolicy = 'strict-origin-when-cross-origin';
    frame.tabIndex = 0;
    mount.replaceChildren(frame);
    const status = mount.parentElement.querySelector('.r-video-status');
    if (status) status.textContent = 'YouTube player requested. Use its controls to start playback. If it does not load, use the external link below.';
    frame.focus();
  }, { once: true });
});
