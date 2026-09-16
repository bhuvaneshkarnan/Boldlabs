/**
 * SERENITY SANCTUARY — JAVASCRIPT CONTROLLER
 * Full clone interactivity for Wix Spiritual Center template
 */

document.addEventListener('DOMContentLoaded', () => {
  // Initialize Lucide Icons
  if (window.lucide) {
    lucide.createIcons();
  }

  // Initialize AOS (Animate on Scroll)
  if (window.AOS) {
    AOS.init({
      duration: 850,
      once: true,
      offset: 70,
      easing: 'cubic-bezier(0.25, 0.46, 0.45, 0.94)'
    });
  }

  // Preloader Dismiss
  const preloader = document.getElementById('preloader');
  if (preloader) {
    window.addEventListener('load', () => {
      setTimeout(() => {
        preloader.classList.add('hidden');
      }, 700);
    });
    // Fallback dismiss
    setTimeout(() => {
      preloader.classList.add('hidden');
    }, 2500);
  }

  // Navbar Scroll State & Back to Top
  const navbar = document.getElementById('navbar');
  const backToTopBtn = document.getElementById('backToTopBtn');
  const heroBg = document.getElementById('heroBg');

  window.addEventListener('scroll', () => {
    const scrollY = window.scrollY;

    if (navbar) {
      if (scrollY > 50) {
        navbar.classList.add('scrolled');
      } else {
        navbar.classList.remove('scrolled');
      }
    }

    if (backToTopBtn) {
      if (scrollY > 500) {
        backToTopBtn.classList.add('visible');
      } else {
        backToTopBtn.classList.remove('visible');
      }
    }

    // Parallax Hero effect
    if (heroBg && scrollY < window.innerHeight) {
      heroBg.style.transform = `scale(1.08) translateY(${scrollY * 0.25}px)`;
    }
  }, { passive: true });

  if (backToTopBtn) {
    backToTopBtn.addEventListener('click', () => {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    });
  }

  // Mobile Drawer Navigation
  const hamburgerBtn = document.getElementById('hamburgerBtn');
  const mobileDrawer = document.getElementById('mobileDrawer');
  const drawerClose = document.getElementById('drawerClose');
  const drawerLinks = document.querySelectorAll('.drawer-link');

  if (hamburgerBtn && mobileDrawer) {
    hamburgerBtn.addEventListener('click', () => {
      mobileDrawer.classList.add('open');
    });
  }

  if (drawerClose && mobileDrawer) {
    drawerClose.addEventListener('click', () => {
      mobileDrawer.classList.remove('open');
    });
  }

  drawerLinks.forEach(link => {
    link.addEventListener('click', () => {
      if (mobileDrawer) mobileDrawer.classList.remove('open');
    });
  });

  // Offerings Category Filter Tabs
  const filterBtns = document.querySelectorAll('.filter-btn');
  const offeringCards = document.querySelectorAll('.offering-card');

  filterBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      filterBtns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');

      const filter = btn.getAttribute('data-filter');

      offeringCards.forEach(card => {
        const category = card.getAttribute('data-category');
        if (filter === 'all' || category === filter) {
          card.style.display = 'flex';
          setTimeout(() => { card.style.opacity = '1'; card.style.transform = 'translateY(0)'; }, 50);
        } else {
          card.style.opacity = '0';
          card.style.transform = 'translateY(15px)';
          setTimeout(() => { card.style.display = 'none'; }, 300);
        }
      });
    });
  });

  // Dynamic Animated Stats Counters
  const statFigures = document.querySelectorAll('.stat-figure[data-target]');
  let statsCounted = false;

  const countUp = (el) => {
    const target = parseInt(el.getAttribute('data-target'), 10);
    const duration = 2000;
    const startTime = performance.now();

    const update = (currentTime) => {
      const elapsed = currentTime - startTime;
      const progress = Math.min(elapsed / duration, 1);
      const easeProgress = 1 - Math.pow(1 - progress, 3);
      const current = Math.floor(easeProgress * target);

      el.textContent = current.toLocaleString() + (target >= 100 ? '+' : (target === 99 ? '%' : '+'));

      if (progress < 1) {
        requestAnimationFrame(update);
      } else {
        el.textContent = target.toLocaleString() + (target >= 100 ? '+' : (target === 99 ? '%' : '+'));
      }
    };
    requestAnimationFrame(update);
  };

  const statObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting && !statsCounted) {
        statsCounted = true;
        statFigures.forEach(fig => countUp(fig));
      }
    });
  }, { threshold: 0.4 });

  if (statFigures.length > 0) {
    statObserver.observe(statFigures[0].parentElement.parentElement);
  }﻿  // Pricing Monthly vs Annual Billing Toggle
  const pricingBillingToggle = document.getElementById('pricingBillingToggle');
  const monthlyToggleLabel = document.getElementById('monthlyToggleLabel');
  const annualToggleLabel = document.getElementById('annualToggleLabel');
  const priceAmounts = document.querySelectorAll('.pricing-card .amount');

  if (pricingBillingToggle) {
    pricingBillingToggle.addEventListener('change', () => {
      const isAnnual = pricingBillingToggle.checked;

      if (monthlyToggleLabel && annualToggleLabel) {
        monthlyToggleLabel.classList.toggle('active', !isAnnual);
        annualToggleLabel.classList.toggle('active', isAnnual);
      }

      priceAmounts.forEach(amt => {
        const monthlyVal = amt.getAttribute('data-monthly');
        const annualVal = amt.getAttribute('data-annual');

        amt.style.opacity = '0';
        amt.style.transform = 'translateY(-10px)';

        setTimeout(() => {
          amt.textContent = isAnnual ? annualVal : monthlyVal;
          amt.style.opacity = '1';
          amt.style.transform = 'translateY(0)';
        }, 180);
      });
    });
  }

  // Testimonials Carousel Slider
  const testimonialsTrack = document.getElementById('testimonialsTrack');
  const slides = document.querySelectorAll('.testimonial-slide');
  const dots = document.querySelectorAll('.carousel-dots .dot');
  const prevBtn = document.getElementById('tPrevBtn');
  const nextBtn = document.getElementById('tNextBtn');
  let currentSlide = 0;
  let carouselInterval;

  const goToSlide = (index) => {
    if (!slides.length) return;
    currentSlide = (index + slides.length) % slides.length;
    slides.forEach((slide) => {
      slide.style.transform = `translateX(-${currentSlide * 100}%)`;
    });
    dots.forEach((dot, idx) => {
      dot.classList.toggle('active', idx === currentSlide);
    });
  };

  if (prevBtn && nextBtn) {
    prevBtn.addEventListener('click', () => {
      goToSlide(currentSlide - 1);
      resetCarouselTimer();
    });

    nextBtn.addEventListener('click', () => {
      goToSlide(currentSlide + 1);
      resetCarouselTimer();
    });
  }

  dots.forEach(dot => {
    dot.addEventListener('click', () => {
      const idx = parseInt(dot.getAttribute('data-index'), 10);
      goToSlide(idx);
      resetCarouselTimer();
    });
  });

  const startCarousel = () => {
    carouselInterval = setInterval(() => {
      goToSlide(currentSlide + 1);
    }, 5500);
  };

  const resetCarouselTimer = () => {
    clearInterval(carouselInterval);
    startCarousel();
  };

  if (slides.length > 0) {
    startCarousel();
  }

  // Web Audio API 432Hz Ambient Sound Generator
  let audioCtx = null;
  let osc1 = null, osc2 = null, gainNode = null;
  let isAudioPlaying = false;
  let audioTimerInterval = null;
  let audioProgressSeconds = 0;
  const audioDurationSeconds = 180; // 3 minutes

  const soundPlayerToggle = document.getElementById('soundPlayerToggle');
  const floatingAudioBar = document.getElementById('floatingAudioBar');
  const playAudioBtn = document.getElementById('playAudioBtn');
  const closeAudioBar = document.getElementById('closeAudioBar');
  const audioWaveAnim = document.getElementById('audioWaveAnim');
  const heroPlayBtn = document.getElementById('heroPlayBtn');
  const heroPlayIcon = document.getElementById('heroPlayIcon');
  const heroPlayText = document.getElementById('heroPlayText');
  const playerProgressFill = document.getElementById('playerProgressFill');
  const timerCurrent = document.getElementById('timerCurrent');

  const startAmbientAudio = () => {
    try {
      const AudioContext = window.AudioContext || window.webkitAudioContext;
      if (!audioCtx) audioCtx = new AudioContext();

      if (audioCtx.state === 'suspended') {
        audioCtx.resume();
      }

      // 432Hz Root and 216Hz Sub-harmonic with soothing sine waves
      osc1 = audioCtx.createOscillator();
      osc2 = audioCtx.createOscillator();
      const lfo = audioCtx.createOscillator();
      const lfoGain = audioCtx.createGain();

      gainNode = audioCtx.createGain();

      osc1.type = 'sine';
      osc1.frequency.setValueAtTime(432, audioCtx.currentTime); // 432Hz Healing Frequency

      osc2.type = 'triangle';
      osc2.frequency.setValueAtTime(216, audioCtx.currentTime); // Sub-octave

      // Gentle pulsating LFO
      lfo.type = 'sine';
      lfo.frequency.setValueAtTime(0.15, audioCtx.currentTime);
      lfoGain.gain.setValueAtTime(0.04, audioCtx.currentTime);
      lfo.connect(gainNode.gain);

      gainNode.gain.setValueAtTime(0.001, audioCtx.currentTime);
      gainNode.gain.exponentialRampToValueAtTime(0.12, audioCtx.currentTime + 2.5);

      osc1.connect(gainNode);
      osc2.connect(gainNode);
      gainNode.connect(audioCtx.destination);

      osc1.start();
      osc2.start();
      lfo.start();

      isAudioPlaying = true;
      updateAudioUiState(true);
      startAudioProgress();
    } catch (e) {
      console.log('Audio init error or autoplay restrictions:', e);
    }
  };

  const stopAmbientAudio = () => {
    if (gainNode && audioCtx) {
      gainNode.gain.exponentialRampToValueAtTime(0.0001, audioCtx.currentTime + 0.8);
      setTimeout(() => {
        if (osc1) osc1.stop();
        if (osc2) osc2.stop();
        osc1 = null;
        osc2 = null;
      }, 900);
    }
    isAudioPlaying = false;
    updateAudioUiState(false);
    clearInterval(audioTimerInterval);
  };

  const toggleAmbientAudio = () => {
    if (isAudioPlaying) {
      stopAmbientAudio();
    } else {
      startAmbientAudio();
    }
  };

  const updateAudioUiState = (playing) => {
    if (floatingAudioBar) floatingAudioBar.classList.add('active');
    if (audioWaveAnim) audioWaveAnim.classList.toggle('playing', playing);

    const playIcon = document.getElementById('playIcon');
    if (playIcon) {
      playIcon.setAttribute('data-lucide', playing ? 'pause' : 'play');
    }

    if (heroPlayIcon) {
      heroPlayIcon.setAttribute('data-lucide', playing ? 'pause' : 'play');
    }
    if (heroPlayText) {
      heroPlayText.textContent = playing ? 'Pause Frequency Flow' : 'Play Frequency Sample';
    }

    if (window.lucide) lucide.createIcons();
  };

  const formatTime = (secs) => {
    const m = Math.floor(secs / 60);
    const s = Math.floor(secs % 60);
    return `${m < 10 ? '0' : ''}${m}:${s < 10 ? '0' : ''}${s}`;
  };

  const startAudioProgress = () => {
    clearInterval(audioTimerInterval);
    audioTimerInterval = setInterval(() => {
      audioProgressSeconds++;
      if (audioProgressSeconds > audioDurationSeconds) {
        audioProgressSeconds = 0;
      }
      if (timerCurrent) timerCurrent.textContent = formatTime(audioProgressSeconds);
      if (playerProgressFill) {
        const pct = (audioProgressSeconds / audioDurationSeconds) * 100;
        playerProgressFill.style.width = `${pct}%`;
      }
    }, 1000);
  };

  if (soundPlayerToggle) soundPlayerToggle.addEventListener('click', toggleAmbientAudio);
  if (playAudioBtn) playAudioBtn.addEventListener('click', toggleAmbientAudio);
  if (heroPlayBtn) heroPlayBtn.addEventListener('click', toggleAmbientAudio);

  if (closeAudioBar) {
    closeAudioBar.addEventListener('click', () => {
      stopAmbientAudio();
      if (floatingAudioBar) floatingAudioBar.classList.remove('active');
    });
  }
});

// Universal Modal & Form Handlers
function openBookingModal(itemTitle) {
  const modal = document.getElementById('universalModal');
  const modalTitle = document.getElementById('modalTitle');
  const modalSubtitle = document.getElementById('modalSubtitle');
  const modalInput = document.getElementById('modalSelectionInput');

  if (modal) {
    if (modalTitle) modalTitle.textContent = `Reserve: ${itemTitle}`;
    if (modalSubtitle) modalSubtitle.textContent = `Confirming your space for "${itemTitle}". Complete the form below to reserve.`;
    if (modalInput) modalInput.value = itemTitle;
    modal.classList.add('open');
  }
}

function closeModal() {
  const modal = document.getElementById('universalModal');
  if (modal) modal.classList.remove('open');
}

function showToast(title, msg) {
  const toast = document.getElementById('toastNotification');
  const toastTitle = document.getElementById('toastTitle');
  const toastMsg = document.getElementById('toastMsg');

  if (toast) {
    if (toastTitle) toastTitle.textContent = title;
    if (toastMsg) toastMsg.textContent = msg;
    toast.classList.add('show');
    setTimeout(() => {
      toast.classList.remove('show');
    }, 4500);
  }
}

function handleBookingSubmit(e) {
  e.preventDefault();
  closeModal();
  showToast('Sacred Reservation Received ✧', 'Thank you! Your space has been noted. Our concierge will send confirmation shortly.');
  e.target.reset();
}

function handleContactSubmit(e) {
  e.preventDefault();
  showToast('Message Sent with Grace 🕊️', 'We have received your heartfelt message and will reply within 24 hours.');
  e.target.reset();
}

function handleNewsletterSubmit(e) {
  e.preventDefault();
  showToast('Welcome to Wisdom Circle 🌿', 'You are now subscribed to our weekly Sunday reflections and event previews.');
  e.target.reset();
}