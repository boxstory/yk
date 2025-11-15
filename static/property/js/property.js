/**
 * ============================================================================
 * PROPERTY APP - JavaScript Module
 * ============================================================================
 *
 * This file contains JavaScript functionality for the property app including:
 * - Property listing interactions
 * - Property card animations
 * - Photo gallery/carousel
 * - Property search and filtering
 * - Map integration
 *
 * Dependencies: None (vanilla JavaScript)
 * ============================================================================
 */

(function() {
  'use strict';

  /**
   * ========================================================================
   * PROPERTY CARD INTERACTIONS
   * ========================================================================
   */
  const PropertyCard = {
    init: function() {
      const cards = document.querySelectorAll('.property-card');
      cards.forEach(card => {
        this.attachEventListeners(card);
      });
    },

    attachEventListeners: function(card) {
      // Card click navigation
      card.addEventListener('click', (e) => {
        // Don't navigate if clicking on buttons or links inside the card
        if (e.target.tagName === 'A' || e.target.tagName === 'BUTTON') {
          return;
        }

        const propertyId = card.dataset.propertyId;
        if (propertyId) {
          window.location.href = `/property/${propertyId}/`;
        }
      });

      // Hover effect enhancement
      card.addEventListener('mouseenter', () => {
        this.onCardHover(card, true);
      });

      card.addEventListener('mouseleave', () => {
        this.onCardHover(card, false);
      });
    },

    onCardHover: function(card, isHovering) {
      const image = card.querySelector('.property-card__image');
      if (image && isHovering) {
        image.style.transform = 'scale(1.05)';
      } else if (image) {
        image.style.transform = 'scale(1)';
      }
    }
  };

  /**
   * ========================================================================
   * PROPERTY SEARCH & FILTERING
   * ========================================================================
   */
  const PropertySearch = {
    init: function() {
      this.searchInput = document.querySelector('#property-search');
      this.zoneFilter = document.querySelector('#zone-filter');
      this.priceFilter = document.querySelector('#price-filter');
      this.bedroomFilter = document.querySelector('#bedroom-filter');

      if (this.searchInput) {
        this.attachSearchListener();
      }

      if (this.zoneFilter || this.priceFilter || this.bedroomFilter) {
        this.attachFilterListeners();
      }
    },

    attachSearchListener: function() {
      let searchTimeout;
      this.searchInput.addEventListener('input', (e) => {
        clearTimeout(searchTimeout);
        searchTimeout = setTimeout(() => {
          this.performSearch(e.target.value);
        }, 500); // Debounce 500ms
      });
    },

    attachFilterListeners: function() {
      [this.zoneFilter, this.priceFilter, this.bedroomFilter].forEach(filter => {
        if (filter) {
          filter.addEventListener('change', () => this.applyFilters());
        }
      });
    },

    performSearch: function(searchTerm) {
      const properties = document.querySelectorAll('.property-card');
      const term = searchTerm.toLowerCase().trim();

      properties.forEach(property => {
        const propertyName = property.dataset.propertyName?.toLowerCase() || '';
        const zone = property.dataset.zone?.toLowerCase() || '';

        if (propertyName.includes(term) || zone.includes(term)) {
          property.style.display = 'block';
          property.classList.add('fade-in');
        } else {
          property.style.display = 'none';
        }
      });

      this.updateResultsCount();
    },

    applyFilters: function() {
      const zone = this.zoneFilter?.value || '';
      const priceRange = this.priceFilter?.value || '';
      const bedrooms = this.bedroomFilter?.value || '';

      const properties = document.querySelectorAll('.property-card');

      properties.forEach(property => {
        let shouldShow = true;

        // Zone filter
        if (zone && property.dataset.zone !== zone) {
          shouldShow = false;
        }

        // Price filter
        if (priceRange && !this.matchesPriceRange(property, priceRange)) {
          shouldShow = false;
        }

        // Bedroom filter
        if (bedrooms && property.dataset.bedrooms !== bedrooms) {
          shouldShow = false;
        }

        property.style.display = shouldShow ? 'block' : 'none';
      });

      this.updateResultsCount();
    },

    matchesPriceRange: function(property, range) {
      const price = parseFloat(property.dataset.price) || 0;

      switch(range) {
        case 'low': return price < 3000;
        case 'mid': return price >= 3000 && price < 6000;
        case 'high': return price >= 6000;
        default: return true;
      }
    },

    updateResultsCount: function() {
      const visibleProperties = document.querySelectorAll('.property-card[style="display: block"]').length;
      const resultsCounter = document.querySelector('#results-count');

      if (resultsCounter) {
        resultsCounter.textContent = `${visibleProperties} properties found`;
      }
    }
  };

  /**
   * ========================================================================
   * PHOTO GALLERY
   * ========================================================================
   */
  const PhotoGallery = {
    init: function() {
      this.galleries = document.querySelectorAll('.property-gallery');
      this.galleries.forEach(gallery => {
        this.setupGallery(gallery);
      });
    },

    setupGallery: function(gallery) {
      const photos = gallery.querySelectorAll('.gallery-photo');
      const mainImage = gallery.querySelector('.main-image');

      if (!mainImage || photos.length === 0) return;

      photos.forEach((photo, index) => {
        photo.addEventListener('click', () => {
          // Update main image
          mainImage.src = photo.src;

          // Update active state
          photos.forEach(p => p.classList.remove('active'));
          photo.classList.add('active');
        });

        // Keyboard navigation
        photo.addEventListener('keypress', (e) => {
          if (e.key === 'Enter' || e.key === ' ') {
            e.preventDefault();
            photo.click();
          }
        });
      });

      // Arrow key navigation
      mainImage.parentElement.addEventListener('keydown', (e) => {
        if (e.key === 'ArrowLeft') this.previousPhoto(photos, mainImage);
        if (e.key === 'ArrowRight') this.nextPhoto(photos, mainImage);
      });
    },

    previousPhoto: function(photos, mainImage) {
      const activeIndex = Array.from(photos).findIndex(p => p.classList.contains('active'));
      const prevIndex = activeIndex > 0 ? activeIndex - 1 : photos.length - 1;
      photos[prevIndex].click();
    },

    nextPhoto: function(photos, mainImage) {
      const activeIndex = Array.from(photos).findIndex(p => p.classList.contains('active'));
      const nextIndex = activeIndex < photos.length - 1 ? activeIndex + 1 : 0;
      photos[nextIndex].click();
    }
  };

  /**
   * ========================================================================
   * PROPERTY FORM ENHANCEMENTS
   * ========================================================================
   */
  const PropertyForm = {
    init: function() {
      this.form = document.querySelector('.property-form');
      if (!this.form) return;

      this.setupPhotoPreview();
      this.setupZoneAutocomplete();
      this.setupFormValidation();
    },

    setupPhotoPreview: function() {
      const photoInputs = this.form.querySelectorAll('input[type="file"][accept*="image"]');

      photoInputs.forEach((input, index) => {
        input.addEventListener('change', (e) => {
          const file = e.target.files[0];
          if (!file) return;

          // Validate file size (max 5MB)
          if (file.size > 5 * 1024 * 1024) {
            alert('Image size must be less than 5MB');
            input.value = '';
            return;
          }

          // Create preview
          const reader = new FileReader();
          reader.onload = (e) => {
            let preview = input.parentElement.querySelector('.photo-preview');
            if (!preview) {
              preview = document.createElement('img');
              preview.className = 'photo-preview';
              preview.style.maxWidth = '200px';
              preview.style.borderRadius = '8px';
              preview.style.marginTop = '10px';
              input.parentElement.appendChild(preview);
            }
            preview.src = e.target.result;
          };
          reader.readAsDataURL(file);
        });
      });
    },

    setupZoneAutocomplete: function() {
      const zoneInput = this.form.querySelector('#zone_name');
      if (!zoneInput) return;

      // Add autocomplete functionality
      zoneInput.addEventListener('input', (e) => {
        const value = e.target.value.toLowerCase();
        const options = zoneInput.querySelectorAll('option');

        options.forEach(option => {
          const text = option.textContent.toLowerCase();
          option.style.display = text.includes(value) ? 'block' : 'none';
        });
      });
    },

    setupFormValidation: function() {
      this.form.addEventListener('submit', (e) => {
        if (!this.validateForm()) {
          e.preventDefault();
          this.showValidationErrors();
        }
      });
    },

    validateForm: function() {
      const requiredFields = this.form.querySelectorAll('[required]');
      let isValid = true;

      requiredFields.forEach(field => {
        if (!field.value.trim()) {
          isValid = false;
          field.classList.add('is-invalid');
        } else {
          field.classList.remove('is-invalid');
        }
      });

      return isValid;
    },

    showValidationErrors: function() {
      const firstInvalid = this.form.querySelector('.is-invalid');
      if (firstInvalid) {
        firstInvalid.scrollIntoView({ behavior: 'smooth', block: 'center' });
        firstInvalid.focus();
      }
    }
  };

  /**
   * ========================================================================
   * INQUIRE MODAL
   * ========================================================================
   */
  const InquireModal = {
    init: function() {
      const inquireButtons = document.querySelectorAll('[data-inquire-property]');

      inquireButtons.forEach(button => {
        button.addEventListener('click', (e) => {
          e.preventDefault();
          const propertyId = button.dataset.inquireProperty;
          const propertyName = button.dataset.propertyName;
          this.openModal(propertyId, propertyName);
        });
      });
    },

    openModal: function(propertyId, propertyName) {
      const modal = document.querySelector('#inquire-modal');
      if (!modal) return;

      // Populate modal with property info
      const propertyNameField = modal.querySelector('#inquire-property-name');
      const propertyIdField = modal.querySelector('#inquire-property-id');

      if (propertyNameField) propertyNameField.textContent = propertyName;
      if (propertyIdField) propertyIdField.value = propertyId;

      // Show modal (Bootstrap 5)
      const bsModal = new bootstrap.Modal(modal);
      bsModal.show();
    }
  };

  /**
   * ========================================================================
   * FAVORITE PROPERTIES
   * ========================================================================
   */
  const FavoriteProperties = {
    init: function() {
      this.favorites = this.loadFavorites();
      this.attachEventListeners();
      this.updateUI();
    },

    loadFavorites: function() {
      const stored = localStorage.getItem('favorite_properties');
      return stored ? JSON.parse(stored) : [];
    },

    saveFavorites: function() {
      localStorage.setItem('favorite_properties', JSON.stringify(this.favorites));
    },

    attachEventListeners: function() {
      const favoriteButtons = document.querySelectorAll('[data-favorite-property]');

      favoriteButtons.forEach(button => {
        button.addEventListener('click', (e) => {
          e.preventDefault();
          e.stopPropagation();
          const propertyId = button.dataset.favoriteProperty;
          this.toggleFavorite(propertyId, button);
        });
      });
    },

    toggleFavorite: function(propertyId, button) {
      const index = this.favorites.indexOf(propertyId);

      if (index > -1) {
        this.favorites.splice(index, 1);
        button.classList.remove('active');
        button.querySelector('i')?.classList.replace('fa-solid', 'fa-regular');
      } else {
        this.favorites.push(propertyId);
        button.classList.add('active');
        button.querySelector('i')?.classList.replace('fa-regular', 'fa-solid');
      }

      this.saveFavorites();
      this.updateFavoriteCount();
    },

    updateUI: function() {
      const favoriteButtons = document.querySelectorAll('[data-favorite-property]');

      favoriteButtons.forEach(button => {
        const propertyId = button.dataset.favoriteProperty;
        if (this.favorites.includes(propertyId)) {
          button.classList.add('active');
          button.querySelector('i')?.classList.replace('fa-regular', 'fa-solid');
        }
      });

      this.updateFavoriteCount();
    },

    updateFavoriteCount: function() {
      const counter = document.querySelector('#favorite-count');
      if (counter) {
        counter.textContent = this.favorites.length;
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
    PropertyCard.init();
    PropertySearch.init();
    PhotoGallery.init();
    PropertyForm.init();
    InquireModal.init();
    FavoriteProperties.init();
  }

  // Start initialization
  init();

})();

/**
 * ============================================================================
 * END OF PROPERTY.JS
 * ============================================================================
 */
