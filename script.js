/**
 * ANJANA SURESH - PORTFOLIO INTERACTIVE LOGIC
 * Vanilla JavaScript (ES6+) - Zero external runtime dependencies
 */

document.addEventListener('DOMContentLoaded', () => {
  'use strict';

  // --------------------------------------------------
  // 1. DOM Elements
  // --------------------------------------------------
  const header = document.getElementById('header');
  const mobileToggle = document.getElementById('mobileToggle');
  const mobileNav = document.getElementById('mobileNav');
  const mobileNavLinks = document.querySelectorAll('.mobile-nav-link');
  const navLinks = document.querySelectorAll('.desktop-nav .nav-link');
  const sections = document.querySelectorAll('section[id]');
  const backToTopBtn = document.getElementById('backToTopBtn');
  const copyEmailBtn = document.getElementById('copyEmailBtn');
  const toastNotification = document.getElementById('toastNotification');
  const toastMessage = document.getElementById('toastMessage');
  const filterTabs = document.querySelectorAll('.filter-tab');
  const skillCards = document.querySelectorAll('.skill-category-card');
  const contactForm = document.getElementById('contactForm');
  const currentYearSpan = document.getElementById('currentYear');

  // Update dynamic year in footer
  if (currentYearSpan) {
    currentYearSpan.textContent = new Date().getFullYear();
  }

  // --------------------------------------------------
  // 2. Mobile Navigation Toggle
  // --------------------------------------------------
  const toggleMobileNav = (forceState) => {
    const isCurrentlyOpen = mobileNav.classList.contains('open');
    const newState = typeof forceState === 'boolean' ? forceState : !isCurrentlyOpen;

    if (newState) {
      mobileNav.classList.add('open');
      mobileToggle.classList.add('active');
      mobileToggle.setAttribute('aria-expanded', 'true');
      mobileNav.setAttribute('aria-hidden', 'false');
      document.body.style.overflow = 'hidden'; // prevent scrolling background
    } else {
      mobileNav.classList.remove('open');
      mobileToggle.classList.remove('active');
      mobileToggle.setAttribute('aria-expanded', 'false');
      mobileNav.setAttribute('aria-hidden', 'true');
      document.body.style.overflow = '';
    }
  };

  if (mobileToggle && mobileNav) {
    mobileToggle.addEventListener('click', (e) => {
      e.stopPropagation();
      toggleMobileNav();
    });

    // Close when clicking any mobile link
    mobileNavLinks.forEach((link) => {
      link.addEventListener('click', () => {
        toggleMobileNav(false);
      });
    });

    // Close on outside click
    document.addEventListener('click', (e) => {
      if (
        mobileNav.classList.contains('open') &&
        !mobileNav.contains(e.target) &&
        !mobileToggle.contains(e.target)
      ) {
        toggleMobileNav(false);
      }
    });

    // Close on Escape key press
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape' && mobileNav.classList.contains('open')) {
        toggleMobileNav(false);
        mobileToggle.focus();
      }
    });
  }

  // --------------------------------------------------
  // 3. Header Scrolled State & Back-to-Top Button
  // --------------------------------------------------
  const handleScrollEffects = () => {
    const scrollY = window.pageYOffset || document.documentElement.scrollTop;

    // Header styling on scroll
    if (header) {
      if (scrollY > 50) {
        header.classList.add('scrolled');
      } else {
        header.classList.remove('scrolled');
      }
    }

    // Back to top visibility
    if (backToTopBtn) {
      if (scrollY > 400) {
        backToTopBtn.classList.add('visible');
      } else {
        backToTopBtn.classList.remove('visible');
      }
    }
  };

  window.addEventListener('scroll', handleScrollEffects, { passive: true });
  handleScrollEffects(); // Initial check

  if (backToTopBtn) {
    backToTopBtn.addEventListener('click', () => {
      window.scrollTo({
        top: 0,
        behavior: 'smooth'
      });
    });
  }

  // --------------------------------------------------
  // 4. Active Section Highlighting in Desktop Nav
  // --------------------------------------------------
  const sectionObserverOptions = {
    root: null,
    rootMargin: '-20% 0px -60% 0px',
    threshold: 0
  };

  const sectionObserver = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        const id = entry.target.getAttribute('id');
        navLinks.forEach((link) => {
          if (link.getAttribute('href') === `#${id}`) {
            link.classList.add('active');
          } else {
            link.classList.remove('active');
          }
        });
      }
    });
  }, sectionObserverOptions);

  sections.forEach((section) => {
    sectionObserver.observe(section);
  });

  // --------------------------------------------------
  // 5. Scroll Reveal Animations
  // --------------------------------------------------
  const revealElements = document.querySelectorAll('.fade-in');

  if ('IntersectionObserver' in window) {
    const revealObserver = new IntersectionObserver((entries, observer) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-visible');
          observer.unobserve(entry.target);
        }
      });
    }, {
      root: null,
      threshold: 0.1,
      rootMargin: '0px 0px -40px 0px'
    });

    revealElements.forEach((el) => {
      revealObserver.observe(el);
    });
  } else {
    // Fallback if browser doesn't support IntersectionObserver
    revealElements.forEach((el) => {
      el.classList.add('is-visible');
    });
  }

  // --------------------------------------------------
  // 6. Skills Category Filter Tabs
  // --------------------------------------------------
  if (filterTabs.length > 0 && skillCards.length > 0) {
    filterTabs.forEach((tab) => {
      tab.addEventListener('click', () => {
        // Update active tab styling & aria
        filterTabs.forEach((t) => {
          t.classList.remove('active');
          t.setAttribute('aria-selected', 'false');
        });
        tab.classList.add('active');
        tab.setAttribute('aria-selected', 'true');

        const filterValue = tab.getAttribute('data-filter');

        skillCards.forEach((card) => {
          const cardCategory = card.getAttribute('data-category');

          if (filterValue === 'all' || filterValue === cardCategory) {
            card.style.display = 'flex';
            setTimeout(() => {
              card.style.opacity = '1';
              card.style.transform = 'translateY(0)';
            }, 20);
          } else {
            card.style.opacity = '0';
            card.style.transform = 'translateY(10px)';
            setTimeout(() => {
              card.style.display = 'none';
            }, 200);
          }
        });
      });
    });
  }

  // --------------------------------------------------
  // 7. Toast Notification Utility
  // --------------------------------------------------
  let toastTimeout;
  const showToast = (message, duration = 3000) => {
    if (!toastNotification || !toastMessage) return;

    toastMessage.textContent = message;
    toastNotification.classList.add('show');

    clearTimeout(toastTimeout);
    toastTimeout = setTimeout(() => {
      toastNotification.classList.remove('show');
    }, duration);
  };

  // --------------------------------------------------
  // 8. Copy Email to Clipboard
  // --------------------------------------------------
  if (copyEmailBtn) {
    copyEmailBtn.addEventListener('click', async () => {
      const emailToCopy = copyEmailBtn.getAttribute('data-email') || 'anjanasuresh3535@gmail.com';

      try {
        if (navigator.clipboard && window.isSecureContext) {
          await navigator.clipboard.writeText(emailToCopy);
        } else {
          // Fallback for older browsers
          const textArea = document.createElement('textarea');
          textArea.value = emailToCopy;
          textArea.style.position = 'fixed';
          textArea.style.opacity = '0';
          document.body.appendChild(textArea);
          textArea.select();
          document.execCommand('copy');
          document.body.removeChild(textArea);
        }

        const copyTextSpan = copyEmailBtn.querySelector('.copy-text');
        if (copyTextSpan) {
          copyTextSpan.textContent = 'Copied!';
          setTimeout(() => {
            copyTextSpan.textContent = 'Copy';
          }, 2000);
        }

        showToast(`Copied ${emailToCopy} to clipboard!`);
      } catch (err) {
        showToast(`Email: ${emailToCopy}`);
      }
    });
  }

  // --------------------------------------------------
  // 9. Contact Form (Mailto Builder with Validation)
  // --------------------------------------------------
  if (contactForm) {
    contactForm.addEventListener('submit', (e) => {
      e.preventDefault();

      const senderName = document.getElementById('senderName');
      const senderSubject = document.getElementById('senderSubject');
      const senderMessage = document.getElementById('senderMessage');

      const nameError = document.getElementById('nameError');
      const subjectError = document.getElementById('subjectError');
      const messageError = document.getElementById('messageError');

      let isValid = true;

      // Reset errors
      if (nameError) nameError.textContent = '';
      if (subjectError) subjectError.textContent = '';
      if (messageError) messageError.textContent = '';

      if (!senderName.value.trim()) {
        if (nameError) nameError.textContent = 'Please provide your name or organization.';
        isValid = false;
      }

      if (!senderSubject.value.trim()) {
        if (subjectError) subjectError.textContent = 'Please enter a subject.';
        isValid = false;
      }

      if (!senderMessage.value.trim()) {
        if (messageError) messageError.textContent = 'Please provide a message or opportunity summary.';
        isValid = false;
      }

      if (!isValid) return;

      // Construct Gmail web composer and mailto links
      const recipient = 'anjanasuresh3535@gmail.com';
      const subject = encodeURIComponent(`[Portfolio Inquiry] ${senderSubject.value.trim()} - from ${senderName.value.trim()}`);
      const body = encodeURIComponent(
        `Hello Anjana,\n\n${senderMessage.value.trim()}\n\n---\nSender: ${senderName.value.trim()}\nSent via Portfolio Contact Form`
      );

      const gmailComposeUrl = `https://mail.google.com/mail/?view=cm&fs=1&to=${recipient}&su=${subject}&body=${body}`;
      const mailtoUrl = `mailto:${recipient}?subject=${subject}&body=${body}`;
      
      showToast('Opening Gmail composer...');
      
      const newTab = window.open(gmailComposeUrl, '_blank');
      if (!newTab || newTab.closed || typeof newTab.closed === 'undefined') {
        window.location.href = mailtoUrl;
      }
    });
  }
});
