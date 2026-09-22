(() => {
  'use strict';

  const gallery = document.querySelector('.mesa-gallery');
  const dialog = document.querySelector('#mesa-lightbox');
  if (!gallery || !dialog || typeof dialog.showModal !== 'function') return;

  const enlargedImage = dialog.querySelector('img');
  const caption = dialog.querySelector('figcaption');
  const closeButton = dialog.querySelector('.mesa-lightbox-close');
  let trigger = null;
  let activeHistoryMarker = null;
  let nextHistoryMarker = 0;

  function closeLightbox(goBack) {
    if (!dialog.open) return;
    dialog.close();
    enlargedImage.removeAttribute('src');
    const shouldPop = goBack && activeHistoryMarker !== null &&
      history.state?.mesaSteamLightbox === activeHistoryMarker;
    activeHistoryMarker = null;
    if (shouldPop) history.back();
    trigger?.focus();
    trigger = null;
  }

  gallery.addEventListener('click', event => {
    const link = event.target.closest('a[data-lightbox]');
    if (!link || !gallery.contains(link)) return;
    const thumbnail = link.querySelector('img');
    if (!thumbnail) return;

    event.preventDefault();
    trigger = link;
    enlargedImage.src = link.href;
    enlargedImage.alt = thumbnail.alt;
    caption.textContent = link.closest('figure')?.querySelector('figcaption')?.textContent || '';
    dialog.showModal();
    activeHistoryMarker = ++nextHistoryMarker;
    history.pushState({ ...history.state, mesaSteamLightbox: activeHistoryMarker }, '');
  });

  closeButton.addEventListener('click', () => closeLightbox(true));
  dialog.addEventListener('cancel', event => {
    event.preventDefault();
    closeLightbox(true);
  });
  dialog.addEventListener('click', event => {
    if (event.target === dialog) closeLightbox(true);
  });
  window.addEventListener('popstate', () => closeLightbox(false));
})();
