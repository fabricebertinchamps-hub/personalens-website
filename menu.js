// Persona Lens site script: mobile nav toggle + sticky "Try it free" bar (phones only)
(function () {
  var STRINGS = {
    en: { btn: 'Try it free', note: 'No download · First reading free · Not stored' },
    fr: { btn: 'Essayer gratuitement', note: "Rien à télécharger · Première lecture gratuite · Rien n'est conservé" },
    es: { btn: 'Probar gratis', note: 'Sin descargas · Primera lectura gratis · No se guarda nada' },
    ru: { btn: 'Попробовать бесплатно', note: 'Без скачивания · Первое прочтение бесплатно · Ничего не хранится' }
  };

  function initNav() {
    var btn = document.querySelector('.nav-toggle');
    var drawer = document.querySelector('.mobile-nav');
    if (!btn || !drawer) return;
    function setOpen(isOpen) {
      drawer.classList.toggle('is-open', isOpen);
      btn.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
      document.body.style.overflow = isOpen ? 'hidden' : '';
      document.body.classList.toggle('nav-open', isOpen);
    }
    btn.addEventListener('click', function (e) {
      e.preventDefault();
      setOpen(!drawer.classList.contains('is-open'));
    });
    drawer.querySelectorAll('a').forEach(function (a) {
      a.addEventListener('click', function () { setOpen(false); });
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && drawer.classList.contains('is-open')) setOpen(false);
    });
  }

  function initSticky() {
    if (document.querySelector('.pl-sticky') || document.body.hasAttribute('data-no-sticky')) return;
    var lang = (document.documentElement.getAttribute('lang') || 'en').slice(0, 2).toLowerCase();
    var t = STRINGS[lang] || STRINGS.en;
    // Reuse the header CTA deep link (it carries lens + lang), swapping the source.
    var href = '/app/?lang=' + lang + '&src=sticky';
    var head = document.querySelector('.header-cta');
    if (head && head.getAttribute('href') && head.getAttribute('href').indexOf('/app/') !== -1) {
      href = head.getAttribute('href').replace(/src=[a-z-]+/, 'src=sticky');
      if (href.indexOf('src=') === -1) href += (href.indexOf('?') === -1 ? '?' : '&') + 'src=sticky';
    }
    var bar = document.createElement('div');
    bar.className = 'pl-sticky';
    bar.setAttribute('role', 'region');
    bar.setAttribute('aria-label', t.btn);
    var a = document.createElement('a');
    a.className = 'btn btn-primary pl-sticky-btn';
    a.href = href;
    a.textContent = t.btn;
    var note = document.createElement('span');
    note.className = 'pl-sticky-note';
    note.textContent = t.note;
    bar.appendChild(a);
    bar.appendChild(note);
    document.body.appendChild(bar);
    document.body.classList.add('has-pl-sticky');

    // Hide while the end-of-page CTA, download section or footer is on screen (avoids two CTAs).
    var targets = document.querySelectorAll('.site-footer, .cta-strip, #download, [data-cta-end]');
    var inView = 0;
    function update() {
      var scrolled = (window.pageYOffset || document.documentElement.scrollTop) > window.innerHeight * 0.4;
      bar.classList.toggle('is-visible', scrolled && inView === 0);
    }
    if ('IntersectionObserver' in window && targets.length) {
      var seen = new Map();
      var io = new IntersectionObserver(function (entries) {
        entries.forEach(function (en) { seen.set(en.target, en.isIntersecting); });
        inView = 0;
        seen.forEach(function (v) { if (v) inView++; });
        update();
      }, { rootMargin: '0px 0px -40px 0px' });
      targets.forEach(function (el) { io.observe(el); });
    }
    window.addEventListener('scroll', update, { passive: true });
    window.addEventListener('resize', update);
    update();
  }

  function init() { initNav(); initSticky(); }
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
