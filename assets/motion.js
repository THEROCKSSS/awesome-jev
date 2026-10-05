'use strict';

// One scroll-derived playhead owns the desktop chapter. No wheel interception or
// time-based smoothing: the same scroll position always produces the same pose.
(() => {
  const story = document.getElementById('story');
  const hero = document.getElementById('top');
  const stage = story?.querySelector('.story-sticky');
  const steps = [...(story?.querySelectorAll('.story-steps article') || [])];
  if (!story || !hero || !stage || steps.length !== 3) return;

  const canAnimate = window.matchMedia('(min-width: 901px) and (prefers-reduced-motion: no-preference)');
  const clamp = x => Math.max(0, Math.min(1, x));
  const segment = (p, a, b) => clamp((p - a) / (b - a));
  let frame = 0;

  function applyPose() {
    frame = 0;
    if (!canAnimate.matches) return;
    const top = document.querySelector('.topnav')?.offsetHeight || 76;
    const travel = Math.max(1, story.offsetHeight - window.innerHeight);
    const p = clamp((top - story.getBoundingClientRect().top) / travel);
    const wire = segment(p, .1, .58);
    const nodes = segment(p, .12, .53);
    const card = segment(p, .67, .86);
    const sceneScale = .78 + .44 * segment(p, .03, .61) - .08 * segment(p, .75, 1);
    const sceneRotation = -17 + 35 * segment(p, 0, .65) - 18 * segment(p, .7, 1);

    story.style.setProperty('--story-progress', p.toFixed(4));
    story.style.setProperty('--rail-height', (p * 100).toFixed(2) + '%');
    story.style.setProperty('--wire-offset', (1 - wire).toFixed(4));
    story.style.setProperty('--node-opacity', (.27 + .73 * nodes).toFixed(3));
    story.style.setProperty('--node-shift', (18 * (1 - nodes)).toFixed(1) + 'px');
    story.style.setProperty('--scene-scale', sceneScale.toFixed(4));
    story.style.setProperty('--scene-rotate', sceneRotation.toFixed(2) + 'deg');
    story.style.setProperty('--scene-shift', (-55 * segment(p, .7, 1)).toFixed(1) + 'px');
    story.style.setProperty('--halo-outer', (115 * p).toFixed(2) + 'deg');
    story.style.setProperty('--halo-inner', (-155 * p).toFixed(2) + 'deg');
    story.style.setProperty('--core-scale', (1 - .48 * segment(p, .7, .92)).toFixed(3));
    story.style.setProperty('--card-opacity', card.toFixed(3));
    story.style.setProperty('--card-shift', (65 * (1 - card)).toFixed(1) + 'px');
    story.style.setProperty('--card-scale', (.8 + .2 * card).toFixed(3));
    story.style.setProperty('--card-rotate', (6 * (1 - card)).toFixed(2) + 'deg');
    story.style.setProperty('--backdrop-shift', (-190 * p).toFixed(1) + 'px');

    const visibility = [
      1 - segment(p, .25, .37),
      segment(p, .25, .37) * (1 - segment(p, .59, .71)),
      segment(p, .59, .71),
    ];
    steps.forEach((step, i) => {
      const v = visibility[i];
      step.style.opacity = v.toFixed(3);
      step.style.transform = `translateY(${((1 - v) * 28).toFixed(1)}px)`;
    });

    const heroP = clamp(window.scrollY / Math.max(1, hero.offsetHeight));
    hero.style.setProperty('--hero-shift', (heroP * 105).toFixed(1) + 'px');
    hero.style.setProperty('--hero-rotate', (heroP * 28).toFixed(1) + 'deg');
    hero.style.setProperty('--hero-scale', (1 + heroP * .12).toFixed(3));
    hero.style.setProperty('--hero-grid-shift', (heroP * 70).toFixed(1) + 'px');
  }

  function schedule() {
    if (!frame && canAnimate.matches) frame = requestAnimationFrame(applyPose);
  }
  function syncMode() {
    const enabled = canAnimate.matches;
    story.classList.toggle('motion-ready', enabled);
    hero.classList.toggle('motion-ready', enabled);
    if (enabled) schedule();
    else {
      if (frame) cancelAnimationFrame(frame);
      frame = 0;
      steps.forEach(step => { step.style.opacity = ''; step.style.transform = ''; });
      story.removeAttribute('style');
      hero.removeAttribute('style');
    }
  }
  window.addEventListener('scroll', schedule, {passive: true});
  window.addEventListener('resize', schedule, {passive: true});
  window.addEventListener('pageshow', schedule);
  canAnimate.addEventListener('change', syncMode);
  syncMode();
})();
