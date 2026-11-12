(() => {
  const root = document.documentElement;
  const reduced = matchMedia('(prefers-reduced-motion: reduce)');
  const button = document.querySelector('#motion-control');
  let preferred = null;
  try { preferred = localStorage.getItem('portfolio-motion'); } catch {}
  let paused = preferred === 'off' || (preferred === null && reduced.matches);
  const observer = 'IntersectionObserver' in window ? new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('in-view');
        observer.unobserve(entry.target);
      }
    });
  }, {threshold: 0.08}) : null;

  function sync() {
    const ar = root.lang === 'ar';
    const off = paused || reduced.matches;
    root.dataset.motion = off ? 'off' : 'on';
    button.innerHTML = `<span aria-hidden="true">${off ? '▷' : 'Ⅱ'}</span>`;
    const label = reduced.matches
      ? (ar ? 'تقليل الحركة مفعّل من إعدادات جهازك' : 'Reduced motion is enabled in your device settings')
      : off ? (ar ? 'تشغيل الحركة' : 'Enable animations') : (ar ? 'إيقاف الحركة' : 'Pause animations');
    button.setAttribute('aria-label', label);
    button.setAttribute('title', label);
    button.setAttribute('aria-pressed', String(off));
    button.disabled = reduced.matches;
    if (off) {
      document.querySelectorAll('.reveal-ready').forEach(el => el.classList.add('in-view'));
    } else if (observer) {
      document.querySelectorAll('.case-study,.section-head,.timeline article,.skill-grid article,.education').forEach(el => {
        if (!el.classList.contains('reveal-ready')) {
          el.classList.add('reveal-ready');
          observer.observe(el);
        }
      });
    }
  }
  button.addEventListener('click', () => {
    paused = !paused;
    try { localStorage.setItem('portfolio-motion', paused ? 'off' : 'on'); } catch {}
    sync();
  });
  reduced.addEventListener('change', sync);
  document.addEventListener('portfolio:render', sync);
  let scheduled = false;
  function progress() {
    const span = root.scrollHeight - root.clientHeight;
    document.querySelector('.reading-progress').style.transform = `scaleX(${span > 0 ? root.scrollTop / span : 0})`;
    scheduled = false;
  }
  addEventListener('scroll', () => {
    if (!scheduled) { scheduled = true; requestAnimationFrame(progress); }
  }, {passive: true});
  addEventListener('resize', progress);
  sync();
  progress();
})();
