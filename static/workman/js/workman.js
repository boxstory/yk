/**
 * ============================================================================
 * WORKMAN APP - JavaScript Module
 * ============================================================================
 *
 * This file contains JavaScript functionality for the workman (service providers) app:
 * - Workman dashboard
 * - Job listings and search
 * - Location-based job filtering
 * - Profile management
 * - Job application tracking
 *
 * Dependencies: None (vanilla JavaScript)
 * ============================================================================
 */

(function() {
  'use strict';

  /**
   * ========================================================================
   * WORKMAN DASHBOARD
   * ========================================================================
   */
  const WorkmanDashboard = {
    init: function() {
      this.loadDashboardData();
      this.setupQuickActions();
    },

    loadDashboardData: function() {
      // Animate statistics
      const stats = document.querySelectorAll('.workman-stat-value');
      stats.forEach(stat => {
        const target = parseInt(stat.dataset.value) || 0;
        this.animateValue(stat, 0, target, 1500);
      });
    },

    animateValue: function(element, start, end, duration) {
      const range = end - start;
      const increment = range / (duration / 16);
      let current = start;

      const timer = setInterval(() => {
        current += increment;
        if (current >= end) {
          element.textContent = end;
          clearInterval(timer);
        } else {
          element.textContent = Math.floor(current);
        }
      }, 16);
    },

    setupQuickActions: function() {
      const quickActionButtons = document.querySelectorAll('[data-quick-action]');

      quickActionButtons.forEach(button => {
        button.addEventListener('click', (e) => {
          const action = button.dataset.quickAction;
          this.handleQuickAction(action);
        });
      });
    },

    handleQuickAction: function(action) {
      switch(action) {
        case 'update-profile':
          window.location.href = '/workman/profile/edit/';
          break;
        case 'view-jobs':
          window.location.href = '/workman/jobs/';
          break;
        case 'view-applications':
          window.location.href = '/workman/applications/';
          break;
        default:
          console.log('Unknown action:', action);
      }
    }
  };

  /**
   * ========================================================================
   * JOB LISTINGS
   * ========================================================================
   */
  const JobListings = {
    init: function() {
      this.setupJobSearch();
      this.setupLocationFilter();
      this.setupServiceTypeFilter();
      this.attachJobActions();
    },

    setupJobSearch: function() {
      const searchInput = document.querySelector('#job-search');
      if (!searchInput) return;

      let searchTimeout;
      searchInput.addEventListener('input', (e) => {
        clearTimeout(searchTimeout);
        searchTimeout = setTimeout(() => {
          this.searchJobs(e.target.value);
        }, 300);
      });
    },

    searchJobs: function(searchTerm) {
      const jobs = document.querySelectorAll('.job-card');
      const term = searchTerm.toLowerCase().trim();

      jobs.forEach(job => {
        const title = job.dataset.jobTitle?.toLowerCase() || '';
        const description = job.dataset.jobDescription?.toLowerCase() || '';
        const location = job.dataset.jobLocation?.toLowerCase() || '';

        if (title.includes(term) || description.includes(term) || location.includes(term)) {
          job.style.display = '';
          job.classList.add('fade-in');
        } else {
          job.style.display = 'none';
        }
      });

      this.updateJobCount();
    },

    setupLocationFilter: function() {
      const locationFilter = document.querySelector('#location-filter');
      if (!locationFilter) return;

      locationFilter.addEventListener('change', () => {
        this.applyFilters();
      });
    },

    setupServiceTypeFilter: function() {
      const serviceFilter = document.querySelector('#service-type-filter');
      if (!serviceFilter) return;

      serviceFilter.addEventListener('change', () => {
        this.applyFilters();
      });
    },

    applyFilters: function() {
      const location = document.querySelector('#location-filter')?.value || '';
      const serviceType = document.querySelector('#service-type-filter')?.value || '';

      const jobs = document.querySelectorAll('.job-card');

      jobs.forEach(job => {
        let shouldShow = true;

        if (location && job.dataset.jobLocation !== location) {
          shouldShow = false;
        }

        if (serviceType && job.dataset.serviceType !== serviceType) {
          shouldShow = false;
        }

        job.style.display = shouldShow ? '' : 'none';
      });

      this.updateJobCount();
    },

    attachJobActions: function() {
      const applyButtons = document.querySelectorAll('[data-apply-job]');
      const saveButtons = document.querySelectorAll('[data-save-job]');

      applyButtons.forEach(button => {
        button.addEventListener('click', (e) => {
          e.preventDefault();
          e.stopPropagation();
          const jobId = button.dataset.applyJob;
          this.applyForJob(jobId, button);
        });
      });

      saveButtons.forEach(button => {
        button.addEventListener('click', (e) => {
          e.preventDefault();
          e.stopPropagation();
          const jobId = button.dataset.saveJob;
          this.saveJob(jobId, button);
        });
      });
    },

    applyForJob: function(jobId, button) {
      if (confirm('Are you sure you want to apply for this job?')) {
        button.disabled = true;
        button.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Applying...';

        // In production, send AJAX request
        setTimeout(() => {
          button.innerHTML = '<i class="fas fa-check"></i> Applied';
          button.classList.add('btn-success');
          this.showNotification('Application submitted successfully!', 'success');
        }, 1000);
      }
    },

    saveJob: function(jobId, button) {
      const isSaved = button.classList.contains('saved');

      if (isSaved) {
        button.classList.remove('saved');
        button.innerHTML = '<i class="far fa-bookmark"></i> Save';
        this.showNotification('Job removed from saved jobs', 'info');
      } else {
        button.classList.add('saved');
        button.innerHTML = '<i class="fas fa-bookmark"></i> Saved';
        this.showNotification('Job saved successfully!', 'success');
      }

      // In production, save to localStorage or server
      this.updateSavedJobsList(jobId, !isSaved);
    },

    updateSavedJobsList: function(jobId, isSaved) {
      let savedJobs = JSON.parse(localStorage.getItem('saved_jobs') || '[]');

      if (isSaved) {
        savedJobs.push(jobId);
      } else {
        savedJobs = savedJobs.filter(id => id !== jobId);
      }

      localStorage.setItem('saved_jobs', JSON.stringify(savedJobs));
    },

    updateJobCount: function() {
      const visibleJobs = document.querySelectorAll('.job-card:not([style*="display: none"])').length;
      const counter = document.querySelector('#job-count');

      if (counter) {
        counter.textContent = `${visibleJobs} jobs available`;
      }
    },

    showNotification: function(message, type = 'info') {
      const notification = document.createElement('div');
      notification.className = `alert alert-${type} notification-toast`;
      notification.textContent = message;
      notification.style.cssText = `
        position: fixed;
        top: 20px;
        right: 20px;
        z-index: 9999;
        min-width: 300px;
        animation: slideIn 0.3s ease-out;
      `;

      document.body.appendChild(notification);

      setTimeout(() => {
        notification.style.animation = 'slideOut 0.3s ease-out';
        setTimeout(() => notification.remove(), 300);
      }, 3000);
    }
  };

  /**
   * ========================================================================
   * PROFILE MANAGEMENT
   * ========================================================================
   */
  const ProfileManagement = {
    init: function() {
      this.setupSkillsManager();
      this.setupPortfolioUpload();
      this.setupAvailabilityToggle();
    },

    setupSkillsManager: function() {
      const addSkillButton = document.querySelector('#add-skill-btn');
      if (!addSkillButton) return;

      addSkillButton.addEventListener('click', () => {
        this.addSkillInput();
      });

      // Remove skill buttons
      document.addEventListener('click', (e) => {
        if (e.target.classList.contains('remove-skill-btn')) {
          e.preventDefault();
          e.target.closest('.skill-item').remove();
        }
      });
    },

    addSkillInput: function() {
      const skillsContainer = document.querySelector('#skills-container');
      if (!skillsContainer) return;

      const skillItem = document.createElement('div');
      skillItem.className = 'skill-item d-flex gap-2 mb-2';
      skillItem.innerHTML = `
        <input type="text" name="skills[]" class="form-control" placeholder="Enter skill">
        <button type="button" class="btn btn-danger remove-skill-btn">
          <i class="fas fa-times"></i>
        </button>
      `;

      skillsContainer.appendChild(skillItem);
    },

    setupPortfolioUpload: function() {
      const portfolioInput = document.querySelector('#portfolio-upload');
      if (!portfolioInput) return;

      portfolioInput.addEventListener('change', (e) => {
        const files = e.target.files;
        this.previewPortfolioFiles(files);
      });
    },

    previewPortfolioFiles: function(files) {
      const preview = document.querySelector('#portfolio-preview');
      if (!preview) return;

      preview.innerHTML = '';

      Array.from(files).forEach((file, index) => {
        const item = document.createElement('div');
        item.className = 'portfolio-item';
        item.innerHTML = `
          <img src="${URL.createObjectURL(file)}" alt="Portfolio ${index + 1}" style="max-width: 150px;">
          <p>${file.name}</p>
        `;
        preview.appendChild(item);
      });
    },

    setupAvailabilityToggle: function() {
      const availabilityToggle = document.querySelector('#availability-toggle');
      if (!availabilityToggle) return;

      availabilityToggle.addEventListener('change', (e) => {
        const isAvailable = e.target.checked;
        this.updateAvailability(isAvailable);
      });
    },

    updateAvailability: function(isAvailable) {
      // In production, send AJAX request to update availability status
      const status = document.querySelector('#availability-status');
      if (status) {
        status.textContent = isAvailable ? 'Available for work' : 'Not available';
        status.className = isAvailable ? 'text-success' : 'text-muted';
      }

      const message = isAvailable ?
        'You are now marked as available for work' :
        'You are now marked as unavailable';

      JobListings.showNotification(message, 'info');
    }
  };

  /**
   * ========================================================================
   * APPLICATION TRACKING
   * ========================================================================
   */
  const ApplicationTracking = {
    init: function() {
      this.setupApplicationFilters();
      this.attachWithdrawListeners();
    },

    setupApplicationFilters: function() {
      const statusFilter = document.querySelector('#application-status-filter');
      if (!statusFilter) return;

      statusFilter.addEventListener('change', () => {
        this.filterApplications();
      });
    },

    filterApplications: function() {
      const status = document.querySelector('#application-status-filter')?.value || '';
      const applications = document.querySelectorAll('.application-item');

      applications.forEach(app => {
        if (status && app.dataset.status !== status) {
          app.style.display = 'none';
        } else {
          app.style.display = '';
        }
      });

      this.updateApplicationCount();
    },

    updateApplicationCount: function() {
      const visibleApps = document.querySelectorAll('.application-item:not([style*="display: none"])').length;
      const counter = document.querySelector('#application-count');

      if (counter) {
        counter.textContent = `${visibleApps} applications`;
      }
    },

    attachWithdrawListeners: function() {
      const withdrawButtons = document.querySelectorAll('[data-withdraw-application]');

      withdrawButtons.forEach(button => {
        button.addEventListener('click', (e) => {
          e.preventDefault();
          const applicationId = button.dataset.withdrawApplication;
          this.withdrawApplication(applicationId);
        });
      });
    },

    withdrawApplication: function(applicationId) {
      if (confirm('Are you sure you want to withdraw this application?')) {
        // In production, send AJAX request
        const applicationItem = document.querySelector(`[data-application-id="${applicationId}"]`);
        if (applicationItem) {
          applicationItem.remove();
          JobListings.showNotification('Application withdrawn successfully', 'info');
        }
      }
    }
  };

  /**
   * ========================================================================
   * LOCATION SERVICES
   * ========================================================================
   */
  const LocationServices = {
    init: function() {
      this.setupLocationDetection();
    },

    setupLocationDetection: function() {
      const detectLocationBtn = document.querySelector('#detect-location-btn');
      if (!detectLocationBtn) return;

      detectLocationBtn.addEventListener('click', () => {
        this.detectCurrentLocation();
      });
    },

    detectCurrentLocation: function() {
      if (!navigator.geolocation) {
        alert('Geolocation is not supported by your browser');
        return;
      }

      const button = document.querySelector('#detect-location-btn');
      button.disabled = true;
      button.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Detecting...';

      navigator.geolocation.getCurrentPosition(
        (position) => {
          this.handleLocationSuccess(position);
          button.disabled = false;
          button.innerHTML = '<i class="fas fa-map-marker-alt"></i> Detect Location';
        },
        (error) => {
          this.handleLocationError(error);
          button.disabled = false;
          button.innerHTML = '<i class="fas fa-map-marker-alt"></i> Detect Location';
        }
      );
    },

    handleLocationSuccess: function(position) {
      const { latitude, longitude } = position.coords;
      console.log('Location detected:', latitude, longitude);

      // In production, reverse geocode to get area name
      // Then filter jobs by nearest location
      JobListings.showNotification('Location detected! Showing nearby jobs', 'success');
    },

    handleLocationError: function(error) {
      console.error('Location error:', error);
      alert('Unable to detect location. Please select manually.');
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
    WorkmanDashboard.init();
    JobListings.init();
    ProfileManagement.init();
    ApplicationTracking.init();
    LocationServices.init();
  }

  // Start initialization
  init();

})();

/**
 * ============================================================================
 * END OF WORKMAN.JS
 * ============================================================================
 */
