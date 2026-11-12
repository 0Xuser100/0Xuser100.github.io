(() => {
  const root = document.documentElement;
  const reduced = matchMedia('(prefers-reduced-motion: reduce)');
  const observer = 'IntersectionObserver' in window ? new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('in-view');
        observer.unobserve(entry.target);
      }
    });
  }, {threshold: 0.08}) : null;

  function sync() {
    const off = reduced.matches;
    root.dataset.motion = off ? 'off' : 'on';
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
