(() => {
  'use strict';

  const root = document.documentElement;
  const themeButton = document.querySelector('.theme-toggle');
  const menuButton = document.querySelector('.menu-toggle');
  const navigation = document.querySelector('#navegacion');
  const links = [...navigation.querySelectorAll('a')];
  const sectionLinks = links.filter(link => {
    const href = link.getAttribute('href');
    return href.startsWith('#') && href.length > 1 && document.getElementById(href.slice(1));
  });
  const mobileViewport = window.matchMedia('(max-width: 980px)');
  root.classList.add('js');
  themeButton.hidden = false;
  menuButton.hidden = false;

  function setTheme(theme) {
    root.dataset.theme = theme;
    const isDark = theme === 'dark';
    themeButton.setAttribute('aria-pressed', String(isDark));
    themeButton.setAttribute('aria-label', isDark ? 'Activar modo claro' : 'Activar modo oscuro');
  }

  let savedTheme;
  try {
    savedTheme = localStorage.getItem('theme');
  } catch {
    // El sitio sigue funcionando si el navegador bloquea el almacenamiento.
  }
  setTheme(savedTheme === 'dark' ? 'dark' : 'light');

  themeButton.addEventListener('click', () => {
    const theme = root.dataset.theme === 'dark' ? 'light' : 'dark';
    setTheme(theme);
    try {
      localStorage.setItem('theme', theme);
    } catch {
      // El tema se mantiene durante esta visita aunque no pueda guardarse.
    }
  });

  function setMenu(open) {
    navigation.classList.toggle('is-open', open);
    menuButton.setAttribute('aria-expanded', String(open));
    menuButton.setAttribute('aria-label', open ? 'Cerrar menú' : 'Abrir menú');
  }

  menuButton.addEventListener('click', () => {
    setMenu(menuButton.getAttribute('aria-expanded') !== 'true');
  });
  links.forEach(link => link.addEventListener('click', () => {
    if (mobileViewport.matches) {
      setMenu(false);
      if (!sectionLinks.includes(link)) return;
      const section = document.getElementById(link.getAttribute('href').slice(1));
      section.setAttribute('tabindex', '-1');
      section.focus({ preventScroll: true });
      section.addEventListener('blur', () => section.removeAttribute('tabindex'), { once: true });
    }
  }));
  document.addEventListener('keydown', event => {
    if (event.key === 'Escape' && menuButton.getAttribute('aria-expanded') === 'true') {
      setMenu(false);
      menuButton.focus();
    }
  });
  document.addEventListener('click', event => {
    if (!event.target.closest('.site-header')) setMenu(false);
  });
  mobileViewport.addEventListener('change', () => setMenu(false));

  if ('IntersectionObserver' in window && sectionLinks.length) {
    const observer = new IntersectionObserver(entries => {
      const visible = entries.filter(entry => entry.isIntersecting);
      if (!visible.length) return;
      const section = visible.sort((a, b) => a.boundingClientRect.top - b.boundingClientRect.top)[0].target;
      sectionLinks.forEach(link => {
        if (link.getAttribute('href') === `#${section.id}`) {
          link.setAttribute('aria-current', 'location');
        } else {
          link.removeAttribute('aria-current');
        }
      });
    }, { rootMargin: '-15% 0px -55% 0px', threshold: 0 });
    sectionLinks.forEach(link => observer.observe(document.getElementById(link.getAttribute('href').slice(1))));
  }
})();
