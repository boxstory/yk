/**
 * ============================================================================
 * WEBPAGES APP - JavaScript Module
 * ============================================================================
 *
 * This file contains JavaScript functionality for public-facing pages:
 * - Homepage animations and interactions
 * - Contact form validation and submission
 * - Careers/Jobs application
 * - Newsletter subscription
 * - Smooth scrolling and navigation
 *
 * Dependencies: None (vanilla JavaScript)
 * ============================================================================
 */

(function() {
  'use strict';

  /**
   * ========================================================================
   * HOMEPAGE ANIMATIONS
   * ========================================================================
   */
  const HomepageAnimations = {
    init: function() {
      this.setupHeroAnimation();
      this.setupCounterAnimation();
      this.setupScrollAnimations();
    },

    setupHeroAnimation: function() {
      const heroSection = document.querySelector('.hero-section');
      if (!heroSection) return;

      // Fade in hero content
      setTimeout(() => {
        heroSection.classList.add('animated');
      }, 100);
    },

    setupCounterAnimation: function() {
      const counters = document.querySelectorAll('.counter');
      if (counters.length === 0) return;

      const observerOptions = {
        threshold: 0.5
      };

      const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
          if (entry.isIntersecting && !entry.target.classList.contains('counted')) {
            this.animateCounter(entry.target);
            entry.target.classList.add('counted');
          }
        });
      }, observerOptions);

      counters.forEach(counter => observer.observe(counter));
    },

    animateCounter: function(element) {
      const target = parseInt(element.dataset.count) || 0;
      const suffix = element.dataset.suffix || '';
      const duration = 2000;
      const increment = target / (duration / 16);

      let current = 0;
      const timer = setInterval(() => {
        current += increment;
        if (current >= target) {
          element.textContent = target.toLocaleString() + suffix;
          clearInterval(timer);
        } else {
          element.textContent = Math.floor(current).toLocaleString() + suffix;
        }
      }, 16);
    },

    setupScrollAnimations: function() {
      const animatedElements = document.querySelectorAll('.animate-on-scroll');
      if (animatedElements.length === 0) return;

      const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -100px 0px'
      };

      const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
          if (entry.isIntersecting) {
            entry.target.classList.add('animated');
          }
        });
      }, observerOptions);

      animatedElements.forEach(el => observer.observe(el));
    }
  };

  /**
   * ========================================================================
   * CONTACT FORM
   * ========================================================================
   */
  const ContactForm = {
    init: function() {
      this.form = document.querySelector('#contact-form');
      if (!this.form) return;

      this.attachSubmitListener();
      this.attachFieldValidation();
    },

    attachSubmitListener: function() {
      this.form.addEventListener('submit', (e) => {
        e.preventDefault();

        if (this.validateForm()) {
          this.submitForm();
        }
      });
    },

    validateForm: function() {
      const nameField = this.form.querySelector('#contact-name');
      const emailField = this.form.querySelector('#contact-email');
      const messageField = this.form.querySelector('#contact-message');

      let isValid = true;

      // Clear previous errors
      this.clearErrors();

      // Name validation
      if (!nameField.value.trim()) {
        this.showError(nameField, 'Name is required');
        isValid = false;
      }

      // Email validation
      if (!emailField.value.trim()) {
        this.showError(emailField, 'Email is required');
        isValid = false;
      } else if (!this.isValidEmail(emailField.value)) {
        this.showError(emailField, 'Please enter a valid email address');
        isValid = false;
      }

      // Message validation
      if (!messageField.value.trim()) {
        this.showError(messageField, 'Message is required');
        isValid = false;
      } else if (messageField.value.trim().length < 10) {
        this.showError(messageField, 'Message must be at least 10 characters');
        isValid = false;
      }

      return isValid;
    },

    isValidEmail: function(email) {
      const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      return emailRegex.test(email);
    },

    showError: function(field, message) {
      field.classList.add('is-invalid');

      const errorDiv = document.createElement('div');
      errorDiv.className = 'invalid-feedback';
      errorDiv.textContent = message;

      field.parentNode.appendChild(errorDiv);
    },

    clearErrors: function() {
      const invalidFields = this.form.querySelectorAll('.is-invalid');
      invalidFields.forEach(field => field.classList.remove('is-invalid'));

      const errorMessages = this.form.querySelectorAll('.invalid-feedback');
      errorMessages.forEach(msg => msg.remove());
    },

    submitForm: function() {
      const submitBtn = this.form.querySelector('button[type="submit"]');
      const originalText = submitBtn.innerHTML;

      // Disable button and show loading
      submitBtn.disabled = true;
      submitBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Sending...';

      // In production, this would be an AJAX POST request
      const formData = new FormData(this.form);

      setTimeout(() => {
        // Reset button
        submitBtn.disabled = false;
        submitBtn.innerHTML = originalText;

        // Show success message
        this.showSuccessMessage();

        // Reset form
        this.form.reset();
      }, 1500);
    },

    showSuccessMessage: function() {
      const successDiv = document.createElement('div');
      successDiv.className = 'alert alert-success alert-dismissible fade show mt-3';
      successDiv.innerHTML = `
        <strong>Thank you!</strong> Your message has been sent successfully. We'll get back to you soon.
        <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
      `;

      this.form.parentNode.insertBefore(successDiv, this.form);

      // Auto-dismiss after 5 seconds
      setTimeout(() => {
        successDiv.remove();
      }, 5000);
    },

    attachFieldValidation: function() {
      const fields = this.form.querySelectorAll('input, textarea');

      fields.forEach(field => {
        field.addEventListener('blur', () => {
          // Clear error on blur if field now has valid value
          if (field.value.trim()) {
            field.classList.remove('is-invalid');
            const error = field.parentNode.querySelector('.invalid-feedback');
            if (error) error.remove();
          }
        });
      });
    }
  };

  /**
   * ========================================================================
   * CAREERS/JOBS APPLICATION
   * ========================================================================
   */
  const CareersApplication = {
    init: function() {
      this.setupJobListings();
      this.setupApplicationForm();
    },

    setupJobListings: function() {
      const applyButtons = document.querySelectorAll('[data-apply-job]');

      applyButtons.forEach(button => {
        button.addEventListener('click', (e) => {
          e.preventDefault();
          const jobId = button.dataset.applyJob;
          const jobTitle = button.dataset.jobTitle;
          this.openApplicationModal(jobId, jobTitle);
        });
      });
    },

    openApplicationModal: function(jobId, jobTitle) {
      const modal = document.querySelector('#application-modal');
      if (!modal) return;

      const jobTitleField = modal.querySelector('#application-job-title');
      const jobIdField = modal.querySelector('#application-job-id');

      if (jobTitleField) jobTitleField.textContent = jobTitle;
      if (jobIdField) jobIdField.value = jobId;

      // Show modal
      const bsModal = new bootstrap.Modal(modal);
      bsModal.show();
    },

    setupApplicationForm: function() {
      const form = document.querySelector('#career-application-form');
      if (!form) return;

      form.addEventListener('submit', (e) => {
        e.preventDefault();

        if (this.validateApplicationForm(form)) {
          this.submitApplication(form);
        }
      });

      // CV file upload validation
      const cvInput = form.querySelector('#cv-upload');
      if (cvInput) {
        cvInput.addEventListener('change', (e) => {
          this.validateCVFile(e.target);
        });
      }
    },

    validateApplicationForm: function(form) {
      const requiredFields = form.querySelectorAll('[required]');
      let isValid = true;

      requiredFields.forEach(field => {
        if (!field.value.trim()) {
          field.classList.add('is-invalid');
          isValid = false;
        } else {
          field.classList.remove('is-invalid');
        }
      });

      return isValid;
    },

    validateCVFile: function(fileInput) {
      const file = fileInput.files[0];
      if (!file) return true;

      // Check file size (max 5MB)
      if (file.size > 5 * 1024 * 1024) {
        alert('CV file must be less than 5MB');
        fileInput.value = '';
        return false;
      }

      // Check file type
      const allowedTypes = ['.pdf', '.doc', '.docx'];
      const fileExtension = '.' + file.name.split('.').pop().toLowerCase();

      if (!allowedTypes.includes(fileExtension)) {
        alert('CV must be in PDF or Word format');
        fileInput.value = '';
        return false;
      }

      return true;
    },

    submitApplication: function(form) {
      const submitBtn = form.querySelector('button[type="submit"]');
      submitBtn.disabled = true;
      submitBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Submitting...';

      // In production, send via AJAX with FormData
      setTimeout(() => {
        submitBtn.disabled = false;
        submitBtn.innerHTML = 'Submit Application';

        // Close modal and show success
        const modal = bootstrap.Modal.getInstance(document.querySelector('#application-modal'));
        if (modal) modal.hide();

        alert('Application submitted successfully! We will review your application and get back to you soon.');

        form.reset();
      }, 2000);
    }
  };

  /**
   * ========================================================================
   * NEWSLETTER SUBSCRIPTION
   * ========================================================================
   */
  const Newsletter = {
    init: function() {
      this.form = document.querySelector('#newsletter-form');
      if (!this.form) return;

      this.form.addEventListener('submit', (e) => {
        e.preventDefault();
        this.subscribe();
      });
    },

    subscribe: function() {
      const emailInput = this.form.querySelector('#newsletter-email');
      const email = emailInput.value.trim();

      if (!email) {
        this.showMessage('Please enter your email address', 'error');
        return;
      }

      if (!this.isValidEmail(email)) {
        this.showMessage('Please enter a valid email address', 'error');
        return;
      }

      const submitBtn = this.form.querySelector('button[type="submit"]');
      submitBtn.disabled = true;
      submitBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i>';

      // In production, send AJAX request
      setTimeout(() => {
        submitBtn.disabled = false;
        submitBtn.innerHTML = 'Subscribe';

        this.showMessage('Thank you for subscribing!', 'success');
        this.form.reset();
      }, 1000);
    },

    isValidEmail: function(email) {
      const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      return emailRegex.test(email);
    },

    showMessage: function(message, type) {
      const messageDiv = document.createElement('div');
      messageDiv.className = `alert alert-${type === 'error' ? 'danger' : 'success'} mt-2`;
      messageDiv.textContent = message;

      this.form.appendChild(messageDiv);

      setTimeout(() => messageDiv.remove(), 3000);
    }
  };

  /**
   * ========================================================================
   * SMOOTH SCROLLING
   * ========================================================================
   */
  const SmoothScrolling = {
    init: function() {
      this.setupAnchorLinks();
      this.setupBackToTop();
    },

    setupAnchorLinks: function() {
      const anchorLinks = document.querySelectorAll('a[href^="#"]');

      anchorLinks.forEach(link => {
        link.addEventListener('click', (e) => {
          const targetId = link.getAttribute('href');
          if (targetId === '#') return;

          const targetElement = document.querySelector(targetId);
          if (targetElement) {
            e.preventDefault();
            targetElement.scrollIntoView({
              behavior: 'smooth',
              block: 'start'
            });

            // Update URL without triggering scroll
            history.pushState(null, null, targetId);
          }
        });
      });
    },

    setupBackToTop: function() {
      const backToTopBtn = document.querySelector('#back-to-top');
      if (!backToTopBtn) return;

      // Show/hide button based on scroll position
      window.addEventListener('scroll', () => {
        if (window.scrollY > 300) {
          backToTopBtn.style.display = 'block';
        } else {
          backToTopBtn.style.display = 'none';
        }
      });

      // Scroll to top on click
      backToTopBtn.addEventListener('click', (e) => {
        e.preventDefault();
        window.scrollTo({
          top: 0,
          behavior: 'smooth'
        });
      });
    }
  };

  /**
   * ========================================================================
   * PROPERTY SEARCH (HOMEPAGE)
   * ========================================================================
   */
  const PropertySearch = {
    init: function() {
      this.form = document.querySelector('#homepage-search-form');
      if (!this.form) return;

      this.form.addEventListener('submit', (e) => {
        e.preventDefault();
        this.performSearch();
      });
    },

    performSearch: function() {
      const zone = this.form.querySelector('#search-zone')?.value || '';
      const bedrooms = this.form.querySelector('#search-bedrooms')?.value || '';
      const priceRange = this.form.querySelector('#search-price')?.value || '';

      // Build query string
      const params = new URLSearchParams();
      if (zone) params.append('zone', zone);
      if (bedrooms) params.append('bedrooms', bedrooms);
      if (priceRange) params.append('price', priceRange);

      // Redirect to property listing page with filters
      window.location.href = `/property/?${params.toString()}`;
    }
  };

  /**
   * ========================================================================
   * TESTIMONIALS CAROUSEL
   * ========================================================================
   */
  const Testimonials = {
    init: function() {
      this.carousel = document.querySelector('#testimonials-carousel');
      if (!this.carousel) return;

      // Bootstrap carousel is handled automatically
      // Add custom navigation if needed
      this.setupCustomNavigation();
    },

    setupCustomNavigation: function() {
      const prevBtn = document.querySelector('#testimonials-prev');
      const nextBtn = document.querySelector('#testimonials-next');

      if (prevBtn && nextBtn) {
        const carouselInstance = new bootstrap.Carousel(this.carousel);

        prevBtn.addEventListener('click', () => carouselInstance.prev());
        nextBtn.addEventListener('click', () => carouselInstance.next());
      }
    }
  };

  /**
   * ========================================================================
   * INITIALIZATION
   * ========================================================================
   */
  function init() {
    if (document.readyState === 'loading') {
      document.addEventListener('DOMContentLoaded', initializeModules);
    } else {
      initializeModules();
    }
  }

  function initializeModules() {
    HomepageAnimations.init();
    ContactForm.init();
    CareersApplication.init();
    Newsletter.init();
    SmoothScrolling.init();
    PropertySearch.init();
    Testimonials.init();
  }

  // Start initialization
  init();

})();

/**
 * ============================================================================
 * END OF WEBPAGES.JS
 * ============================================================================
 */
