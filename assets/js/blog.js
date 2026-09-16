(() => {
  'use strict';

  const filters = document.querySelector('.blog-filters');
  const list = document.querySelector('#article-list');
  const status = document.querySelector('.filter-status');
  if (!filters || !list || !status) return;

  const cards = [...list.querySelectorAll('.article-card')];
  const buttons = [...filters.querySelectorAll('button[data-category]')];
  filters.hidden = false;
  status.hidden = false;

  function filterArticles(category) {
    let count = 0;
    cards.forEach(card => {
      const matches = category === 'Todas' || card.dataset.categories.split('|').includes(category);
      card.hidden = !matches;
      if (matches) count += 1;
    });
    buttons.forEach(button => {
      button.setAttribute('aria-pressed', String(button.dataset.category === category));
    });
    status.textContent = `${count} ${count === 1 ? 'artículo' : 'artículos'} · ${category === 'Todas' ? 'Todas las categorías' : category}`;
  }

  buttons.forEach(button => button.addEventListener('click', () => filterArticles(button.dataset.category)));
  filterArticles('Todas');
})();
