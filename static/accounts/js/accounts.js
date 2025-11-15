/**
 * ============================================================================
 * ACCOUNTS APP - JavaScript Module
 * ============================================================================
 *
 * This file contains JavaScript functionality for the accounts app including:
 * - Login/signup form validation
 * - Profile image upload preview
 * - Password strength meter
 * - Form interactivity
 *
 * Dependencies: None (vanilla JavaScript)
 * ============================================================================
 */

(function() {
  'use strict';

  /**
   * ========================================================================
   * PASSWORD STRENGTH METER
   * ========================================================================
   */
  const PasswordStrength = {
    init: function() {
      const passwordInputs = document.querySelectorAll('input[type="password"]');
      passwordInputs.forEach(input => {
        if (input.id.includes('password1') || input.id.includes('new_password')) {
          this.attachStrengthMeter(input);
        }
      });
    },

    attachStrengthMeter: function(input) {
      const meter = document.createElement('div');
      meter.className = 'password-strength-meter';
      meter.innerHTML = `
        <div class="password-strength-bar">
          <div class="password-strength-fill"></div>
        </div>
        <div class="password-strength-text"></div>
      `;
      input.parentNode.appendChild(meter);

      input.addEventListener('input', () => {
        this.updateStrength(input.value, meter);
      });
    },

    calculateStrength: function(password) {
      let strength = 0;
      if (password.length >= 8) strength += 25;
      if (password.length >= 12) strength += 25;
      if (/[a-z]/.test(password) && /[A-Z]/.test(password)) strength += 25;
      if (/\d/.test(password)) strength += 15;
      if (/[^a-zA-Z0-9]/.test(password)) strength += 10;
      return Math.min(strength, 100);
    },

    updateStrength: function(password, meter) {
      const strength = this.calculateStrength(password);
      const fill = meter.querySelector('.password-strength-fill');
      const text = meter.querySelector('.password-strength-text');

      fill.style.width = strength + '%';

      let strengthText = '';
      let color = '';

      if (strength < 40) {
        strengthText = 'Weak';
        color = '#dc3545';
      } else if (strength < 70) {
        strengthText = 'Medium';
        color = '#ffc107';
      } else {
        strengthText = 'Strong';
        color = '#28a745';
      }

      fill.style.backgroundColor = color;
      text.textContent = strengthText;
      text.style.color = color;
    }
  };

  /**
   * ========================================================================
   * PROFILE IMAGE PREVIEW
   * ========================================================================
   */
  const ProfileImagePreview = {
    init: function() {
      const imageInputs = document.querySelectorAll('input[type="file"][accept*="image"]');
      imageInputs.forEach(input => {
        input.addEventListener('change', (e) => this.handleImageChange(e));
      });
    },

    handleImageChange: function(event) {
      const file = event.target.files[0];
      if (!file) return;

      // Validate file size (max 5MB)
      if (file.size > 5 * 1024 * 1024) {
        alert('Image size must be less than 5MB');
        event.target.value = '';
        return;
      }

      // Validate file type
      if (!file.type.match('image.*')) {
        alert('Please select an image file');
        event.target.value = '';
        return;
      }

      // Show preview
      const reader = new FileReader();
      reader.onload = (e) => {
        let preview = document.querySelector('.image-preview');
        if (!preview) {
          preview = document.createElement('div');
          preview.className = 'image-preview';
          event.target.parentNode.appendChild(preview);
        }
        preview.innerHTML = `<img src="${e.target.result}" alt="Preview" style="max-width: 200px; border-radius: 8px; margin-top: 10px;">`;
      };
      reader.readAsDataURL(file);
    }
  };

  /**
   * ========================================================================
   * FORM VALIDATION
   * ========================================================================
   */
  const FormValidation = {
    init: function() {
      const forms = document.querySelectorAll('.auth-form, .profile-form');
      forms.forEach(form => {
        form.addEventListener('submit', (e) => this.handleSubmit(e));
        this.attachRealTimeValidation(form);
      });
    },

    handleSubmit: function(event) {
      const form = event.target;
      const inputs = form.querySelectorAll('input[required], select[required], textarea[required]');
      let isValid = true;

      inputs.forEach(input => {
        if (!this.validateInput(input)) {
          isValid = false;
        }
      });

      if (!isValid) {
        event.preventDefault();
        this.showError(form, 'Please fill in all required fields correctly');
      }
    },

    attachRealTimeValidation: function(form) {
      const inputs = form.querySelectorAll('input, select, textarea');
      inputs.forEach(input => {
        input.addEventListener('blur', () => {
          this.validateInput(input);
        });

        input.addEventListener('input', () => {
          this.clearError(input);
        });
      });
    },

    validateInput: function(input) {
      // Remove previous error
      this.clearError(input);

      // Skip if not required and empty
      if (!input.required && !input.value) return true;

      // Email validation
      if (input.type === 'email') {
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailRegex.test(input.value)) {
          this.showInputError(input, 'Please enter a valid email address');
          return false;
        }
      }

      // Password confirmation
      if (input.id.includes('password2') || input.id.includes('confirm')) {
        const password1 = document.querySelector('input[id*="password1"]');
        if (password1 && input.value !== password1.value) {
          this.showInputError(input, 'Passwords do not match');
          return false;
        }
      }

      // Required fields
      if (input.required && !input.value.trim()) {
        this.showInputError(input, 'This field is required');
        return false;
      }

      return true;
    },

    showInputError: function(input, message) {
      input.classList.add('is-invalid');
      const errorDiv = document.createElement('div');
      errorDiv.className = 'invalid-feedback';
      errorDiv.textContent = message;
      input.parentNode.appendChild(errorDiv);
    },

    clearError: function(input) {
      input.classList.remove('is-invalid');
      const errorDiv = input.parentNode.querySelector('.invalid-feedback');
      if (errorDiv) {
        errorDiv.remove();
      }
    },

    showError: function(form, message) {
      let alertDiv = form.querySelector('.form-error-alert');
      if (!alertDiv) {
        alertDiv = document.createElement('div');
        alertDiv.className = 'alert alert-error form-error-alert';
        form.insertBefore(alertDiv, form.firstChild);
      }
      alertDiv.textContent = message;
      alertDiv.style.display = 'block';

      setTimeout(() => {
        alertDiv.style.display = 'none';
      }, 5000);
    }
  };

  /**
   * ========================================================================
   * SOCIAL LOGIN
   * ========================================================================
   */
  const SocialLogin = {
    init: function() {
      const socialButtons = document.querySelectorAll('.social-login__button');
      socialButtons.forEach(button => {
        button.addEventListener('click', (e) => this.handleSocialLogin(e));
      });
    },

    handleSocialLogin: function(event) {
      const button = event.currentTarget;
      const provider = button.dataset.provider;

      // Show loading state
      button.disabled = true;
      button.innerHTML = `<i class="fas fa-spinner fa-spin"></i> Connecting...`;

      // The actual redirect will happen via the href
      // This is just for UI feedback
    }
  };

  /**
   * ========================================================================
   * PROFILE TABS
   * ========================================================================
   */
  const ProfileTabs = {
    init: function() {
      const tabs = document.querySelectorAll('[data-tab-target]');
      tabs.forEach(tab => {
        tab.addEventListener('click', (e) => this.switchTab(e));
      });
    },

    switchTab: function(event) {
      event.preventDefault();
      const target = event.currentTarget.dataset.tabTarget;

      // Hide all tab contents
      document.querySelectorAll('[data-tab-content]').forEach(content => {
        content.style.display = 'none';
      });

      // Remove active class from all tabs
      document.querySelectorAll('[data-tab-target]').forEach(tab => {
        tab.classList.remove('active');
      });

      // Show target tab content
      const targetContent = document.querySelector(`[data-tab-content="${target}"]`);
      if (targetContent) {
        targetContent.style.display = 'block';
      }

      // Add active class to clicked tab
      event.currentTarget.classList.add('active');
    }
  };

  /**
   * ========================================================================
   * LANGUAGE SELECTION
   * ========================================================================
   */
  const LanguageSelection = {
    init: function() {
      const languageSelect = document.querySelector('select[name="spoken_languages"]');
      if (languageSelect && languageSelect.multiple) {
        this.enhanceMultiSelect(languageSelect);
      }
    },

    enhanceMultiSelect: function(select) {
      // Add visual feedback for selected items
      select.addEventListener('change', () => {
        const selectedCount = select.selectedOptions.length;
        const label = select.previousElementSibling;
        if (label && label.tagName === 'LABEL') {
          label.textContent = `Languages (${selectedCount} selected)`;
        }
      });
    }
  };

  /**
   * ========================================================================
   * INITIALIZATION
   * ========================================================================
   */
  function init() {
    // Wait for DOM to be fully loaded
    if (document.readyState === 'loading') {
      document.addEventListener('DOMContentLoaded', initializeModules);
    } else {
      initializeModules();
    }
  }

  function initializeModules() {
    PasswordStrength.init();
    ProfileImagePreview.init();
    FormValidation.init();
    SocialLogin.init();
    ProfileTabs.init();
    LanguageSelection.init();
  }

  // Start initialization
  init();

})();

/**
 * ============================================================================
 * END OF ACCOUNTS.JS
 * ============================================================================
 */
