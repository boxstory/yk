/**
 * ============================================================================
 * REALTOR APP - JavaScript Module
 * ============================================================================
 *
 * This file contains JavaScript functionality for the realtor app including:
 * - Dashboard statistics and charts
 * - Inquiry management
 * - Booking calendar
 * - Contact management
 * - Report generation
 *
 * Dependencies: None (vanilla JavaScript)
 * ============================================================================
 */

(function() {
  'use strict';

  /**
   * ========================================================================
   * DASHBOARD STATISTICS
   * ========================================================================
   */
  const DashboardStats = {
    init: function() {
      this.animateCounters();
      this.loadRecentActivity();
    },

    animateCounters: function() {
      const counters = document.querySelectorAll('.stat-counter');

      counters.forEach(counter => {
        const target = parseInt(counter.dataset.count) || 0;
        const duration = 2000; // 2 seconds
        const increment = target / (duration / 16); // 60fps

        let current = 0;
        const timer = setInterval(() => {
          current += increment;
          if (current >= target) {
            counter.textContent = target.toLocaleString();
            clearInterval(timer);
          } else {
            counter.textContent = Math.floor(current).toLocaleString();
          }
        }, 16);
      });
    },

    loadRecentActivity: function() {
      const activityContainer = document.querySelector('#recent-activity');
      if (!activityContainer) return;

      // Activity will be loaded via AJAX in production
      // This is a placeholder for demonstration
      console.log('Loading recent activity...');
    }
  };

  /**
   * ========================================================================
   * INQUIRY MANAGEMENT
   * ========================================================================
   */
  const InquiryManagement = {
    init: function() {
      this.attachStatusChangeListeners();
      this.attachReplyListeners();
      this.setupInquiryFilters();
    },

    attachStatusChangeListeners: function() {
      const statusSelects = document.querySelectorAll('.inquiry-status-select');

      statusSelects.forEach(select => {
        select.addEventListener('change', (e) => {
          const inquiryId = select.dataset.inquiryId;
          const newStatus = select.value;
          this.updateInquiryStatus(inquiryId, newStatus, select);
        });
      });
    },

    updateInquiryStatus: function(inquiryId, status, selectElement) {
      // In production, this would be an AJAX call
      // For now, just update UI
      const row = selectElement.closest('tr');
      if (row) {
        row.classList.add('updating');

        // Simulate API call
        setTimeout(() => {
          row.classList.remove('updating');
          row.classList.add('updated');

          // Show success message
          this.showNotification('Inquiry status updated successfully', 'success');

          setTimeout(() => row.classList.remove('updated'), 2000);
        }, 500);
      }
    },

    attachReplyListeners: function() {
      const replyButtons = document.querySelectorAll('[data-reply-inquiry]');

      replyButtons.forEach(button => {
        button.addEventListener('click', (e) => {
          e.preventDefault();
          const inquiryId = button.dataset.replyInquiry;
          const inquirerEmail = button.dataset.inquirerEmail;
          this.openReplyModal(inquiryId, inquirerEmail);
        });
      });
    },

    openReplyModal: function(inquiryId, inquirerEmail) {
      const modal = document.querySelector('#reply-modal');
      if (!modal) return;

      const emailField = modal.querySelector('#reply-email');
      const inquiryIdField = modal.querySelector('#reply-inquiry-id');

      if (emailField) emailField.value = inquirerEmail;
      if (inquiryIdField) inquiryIdField.value = inquiryId;

      // Show modal
      const bsModal = new bootstrap.Modal(modal);
      bsModal.show();
    },

    setupInquiryFilters: function() {
      const statusFilter = document.querySelector('#inquiry-status-filter');
      const dateFilter = document.querySelector('#inquiry-date-filter');

      if (statusFilter) {
        statusFilter.addEventListener('change', () => this.applyFilters());
      }

      if (dateFilter) {
        dateFilter.addEventListener('change', () => this.applyFilters());
      }
    },

    applyFilters: function() {
      const statusFilter = document.querySelector('#inquiry-status-filter')?.value || '';
      const dateFilter = document.querySelector('#inquiry-date-filter')?.value || '';

      const inquiryRows = document.querySelectorAll('.inquiry-row');

      inquiryRows.forEach(row => {
        let shouldShow = true;

        if (statusFilter && row.dataset.status !== statusFilter) {
          shouldShow = false;
        }

        if (dateFilter && !this.matchesDateFilter(row, dateFilter)) {
          shouldShow = false;
        }

        row.style.display = shouldShow ? '' : 'none';
      });

      this.updateInquiryCount();
    },

    matchesDateFilter: function(row, filter) {
      const rowDate = new Date(row.dataset.date);
      const today = new Date();

      switch(filter) {
        case 'today':
          return rowDate.toDateString() === today.toDateString();
        case 'week':
          const weekAgo = new Date(today.getTime() - 7 * 24 * 60 * 60 * 1000);
          return rowDate >= weekAgo;
        case 'month':
          return rowDate.getMonth() === today.getMonth() &&
                 rowDate.getFullYear() === today.getFullYear();
        default:
          return true;
      }
    },

    updateInquiryCount: function() {
      const visibleRows = document.querySelectorAll('.inquiry-row:not([style*="display: none"])').length;
      const counter = document.querySelector('#inquiry-count');

      if (counter) {
        counter.textContent = `${visibleRows} inquiries`;
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
   * BOOKING CALENDAR
   * ========================================================================
   */
  const BookingCalendar = {
    init: function() {
      this.calendar = document.querySelector('#booking-calendar');
      if (!this.calendar) return;

      this.setupCalendar();
      this.attachBookingListeners();
    },

    setupCalendar: function() {
      // In production, integrate with a calendar library like FullCalendar
      console.log('Booking calendar initialized');
    },

    attachBookingListeners: function() {
      const bookingButtons = document.querySelectorAll('[data-create-booking]');

      bookingButtons.forEach(button => {
        button.addEventListener('click', (e) => {
          e.preventDefault();
          this.openBookingModal();
        });
      });
    },

    openBookingModal: function() {
      const modal = document.querySelector('#booking-modal');
      if (!modal) return;

      const bsModal = new bootstrap.Modal(modal);
      bsModal.show();
    }
  };

  /**
   * ========================================================================
   * CONTACT MANAGEMENT
   * ========================================================================
   */
  const ContactManagement = {
    init: function() {
      this.setupContactSearch();
      this.attachContactActions();
    },

    setupContactSearch: function() {
      const searchInput = document.querySelector('#contact-search');
      if (!searchInput) return;

      let searchTimeout;
      searchInput.addEventListener('input', (e) => {
        clearTimeout(searchTimeout);
        searchTimeout = setTimeout(() => {
          this.searchContacts(e.target.value);
        }, 300);
      });
    },

    searchContacts: function(searchTerm) {
      const contacts = document.querySelectorAll('.contact-item');
      const term = searchTerm.toLowerCase().trim();

      contacts.forEach(contact => {
        const name = contact.dataset.contactName?.toLowerCase() || '';
        const email = contact.dataset.contactEmail?.toLowerCase() || '';
        const phone = contact.dataset.contactPhone?.toLowerCase() || '';

        if (name.includes(term) || email.includes(term) || phone.includes(term)) {
          contact.style.display = '';
        } else {
          contact.style.display = 'none';
        }
      });

      this.updateContactCount();
    },

    attachContactActions: function() {
      const callButtons = document.querySelectorAll('[data-call-contact]');
      const emailButtons = document.querySelectorAll('[data-email-contact]');

      callButtons.forEach(button => {
        button.addEventListener('click', (e) => {
          e.preventDefault();
          const phone = button.dataset.callContact;
          window.location.href = `tel:${phone}`;
        });
      });

      emailButtons.forEach(button => {
        button.addEventListener('click', (e) => {
          e.preventDefault();
          const email = button.dataset.emailContact;
          window.location.href = `mailto:${email}`;
        });
      });
    },

    updateContactCount: function() {
      const visibleContacts = document.querySelectorAll('.contact-item:not([style*="display: none"])').length;
      const counter = document.querySelector('#contact-count');

      if (counter) {
        counter.textContent = `${visibleContacts} contacts`;
      }
    }
  };

  /**
   * ========================================================================
   * REPORT GENERATION
   * ========================================================================
   */
  const ReportGeneration = {
    init: function() {
      this.attachReportListeners();
    },

    attachReportListeners: function() {
      const generateButton = document.querySelector('#generate-report');
      if (!generateButton) return;

      generateButton.addEventListener('click', (e) => {
        e.preventDefault();
        this.generateReport();
      });
    },

    generateReport: function() {
      const reportType = document.querySelector('#report-type')?.value;
      const dateRange = document.querySelector('#report-date-range')?.value;

      if (!reportType) {
        alert('Please select a report type');
        return;
      }

      // Show loading state
      const button = document.querySelector('#generate-report');
      button.disabled = true;
      button.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Generating...';

      // In production, this would be an AJAX call to generate the report
      setTimeout(() => {
        button.disabled = false;
        button.innerHTML = '<i class="fas fa-file-pdf"></i> Generate Report';

        // Simulate download
        alert(`${reportType} report generated successfully!`);
      }, 2000);
    }
  };

  /**
   * ========================================================================
   * PROPERTY LISTING ACTIONS
   * ========================================================================
   */
  const PropertyActions = {
    init: function() {
      this.attachShareListeners();
      this.attachPrintListeners();
    },

    attachShareListeners: function() {
      const shareButtons = document.querySelectorAll('[data-share-property]');

      shareButtons.forEach(button => {
        button.addEventListener('click', (e) => {
          e.preventDefault();
          const propertyId = button.dataset.shareProperty;
          const propertyUrl = button.dataset.propertyUrl;
          this.shareProperty(propertyId, propertyUrl);
        });
      });
    },

    shareProperty: function(propertyId, propertyUrl) {
      if (navigator.share) {
        navigator.share({
          title: 'Property Listing',
          text: 'Check out this property!',
          url: propertyUrl
        }).catch(err => console.log('Error sharing:', err));
      } else {
        // Fallback: Copy to clipboard
        navigator.clipboard.writeText(propertyUrl).then(() => {
          alert('Property link copied to clipboard!');
        });
      }
    },

    attachPrintListeners: function() {
      const printButtons = document.querySelectorAll('[data-print-property]');

      printButtons.forEach(button => {
        button.addEventListener('click', (e) => {
          e.preventDefault();
          window.print();
        });
      });
    }
  };

  /**
   * ========================================================================
   * NOTIFICATIONS
   * ========================================================================
   */
  const Notifications = {
    init: function() {
      this.checkNewNotifications();
      this.attachNotificationListeners();
    },

    checkNewNotifications: function() {
      // In production, this would poll the server for new notifications
      // For now, just update the badge if present
      const badge = document.querySelector('#notification-badge');
      if (badge) {
        const count = parseInt(badge.dataset.count) || 0;
        badge.textContent = count;
        badge.style.display = count > 0 ? 'block' : 'none';
      }
    },

    attachNotificationListeners: function() {
      const notificationBell = document.querySelector('#notification-bell');
      if (!notificationBell) return;

      notificationBell.addEventListener('click', (e) => {
        e.preventDefault();
        this.toggleNotificationDropdown();
      });
    },

    toggleNotificationDropdown: function() {
      const dropdown = document.querySelector('#notification-dropdown');
      if (dropdown) {
        dropdown.classList.toggle('show');
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
    DashboardStats.init();
    InquiryManagement.init();
    BookingCalendar.init();
    ContactManagement.init();
    ReportGeneration.init();
    PropertyActions.init();
    Notifications.init();
  }

  // Start initialization
  init();

})();

/**
 * ============================================================================
 * END OF REALTOR.JS
 * ============================================================================
 */
