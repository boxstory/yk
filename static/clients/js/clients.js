/**
 * ============================================================================
 * CLIENTS APP - JavaScript Module
 * ============================================================================
 *
 * This file contains JavaScript functionality for the clients (property owners) app:
 * - Client dashboard
 * - Property portfolio management
 * - Portion (unit) management
 * - Financial overview
 * - Tenant management
 *
 * Dependencies: None (vanilla JavaScript)
 * ============================================================================
 */

(function() {
  'use strict';

  /**
   * ========================================================================
   * CLIENT DASHBOARD
   * ========================================================================
   */
  const ClientDashboard = {
    init: function() {
      this.animateStats();
      this.loadRecentActivity();
    },

    animateStats: function() {
      const stats = document.querySelectorAll('.client-stat');

      stats.forEach(stat => {
        const value = parseFloat(stat.dataset.value) || 0;
        const isCurrency = stat.dataset.currency === 'true';
        const duration = 1500;
        const increment = value / (duration / 16);

        let current = 0;
        const timer = setInterval(() => {
          current += increment;
          if (current >= value) {
            stat.textContent = isCurrency ? `QAR ${value.toLocaleString()}` : value;
            clearInterval(timer);
          } else {
            const displayValue = Math.floor(current);
            stat.textContent = isCurrency ? `QAR ${displayValue.toLocaleString()}` : displayValue;
          }
        }, 16);
      });
    },

    loadRecentActivity: function() {
      // Placeholder for loading recent property activity
      console.log('Loading client activity...');
    }
  };

  /**
   * ========================================================================
   * PROPERTY PORTFOLIO
   * ========================================================================
   */
  const PropertyPortfolio = {
    init: function() {
      this.setupViewToggle();
      this.attachPropertyActions();
    },

    setupViewToggle: function() {
      const gridView = document.querySelector('#grid-view-btn');
      const listView = document.querySelector('#list-view-btn');
      const portfolio = document.querySelector('#property-portfolio');

      if (gridView && listView && portfolio) {
        gridView.addEventListener('click', () => {
          portfolio.classList.remove('list-view');
          portfolio.classList.add('grid-view');
          gridView.classList.add('active');
          listView.classList.remove('active');
          localStorage.setItem('portfolio_view', 'grid');
        });

        listView.addEventListener('click', () => {
          portfolio.classList.remove('grid-view');
          portfolio.classList.add('list-view');
          listView.classList.add('active');
          gridView.classList.remove('active');
          localStorage.setItem('portfolio_view', 'list');
        });

        // Load saved preference
        const savedView = localStorage.getItem('portfolio_view') || 'grid';
        if (savedView === 'list') {
          listView.click();
        }
      }
    },

    attachPropertyActions: function() {
      const editButtons = document.querySelectorAll('[data-edit-property]');
      const deleteButtons = document.querySelectorAll('[data-delete-property]');

      editButtons.forEach(button => {
        button.addEventListener('click', (e) => {
          e.preventDefault();
          const propertyId = button.dataset.editProperty;
          window.location.href = `/property/${propertyId}/edit/`;
        });
      });

      deleteButtons.forEach(button => {
        button.addEventListener('click', (e) => {
          e.preventDefault();
          const propertyId = button.dataset.deleteProperty;
          const propertyName = button.dataset.propertyName;
          this.confirmDelete(propertyId, propertyName);
        });
      });
    },

    confirmDelete: function(propertyId, propertyName) {
      if (confirm(`Are you sure you want to delete "${propertyName}"? This action cannot be undone.`)) {
        // In production, this would be an AJAX call
        window.location.href = `/property/${propertyId}/delete/`;
      }
    }
  };

  /**
   * ========================================================================
   * PORTION MANAGEMENT
   * ========================================================================
   */
  const PortionManagement = {
    init: function() {
      this.setupPortionFilters();
      this.attachPortionActions();
      this.setupBulkActions();
    },

    setupPortionFilters: function() {
      const statusFilter = document.querySelector('#portion-status-filter');
      const bedroomFilter = document.querySelector('#portion-bedroom-filter');

      if (statusFilter) {
        statusFilter.addEventListener('change', () => this.applyFilters());
      }

      if (bedroomFilter) {
        bedroomFilter.addEventListener('change', () => this.applyFilters());
      }
    },

    applyFilters: function() {
      const status = document.querySelector('#portion-status-filter')?.value || '';
      const bedrooms = document.querySelector('#portion-bedroom-filter')?.value || '';

      const portions = document.querySelectorAll('.portion-item');

      portions.forEach(portion => {
        let shouldShow = true;

        if (status && portion.dataset.status !== status) {
          shouldShow = false;
        }

        if (bedrooms && portion.dataset.bedrooms !== bedrooms) {
          shouldShow = false;
        }

        portion.style.display = shouldShow ? '' : 'none';
      });

      this.updatePortionCount();
    },

    updatePortionCount: function() {
      const visiblePortions = document.querySelectorAll('.portion-item:not([style*="display: none"])').length;
      const counter = document.querySelector('#portion-count');

      if (counter) {
        counter.textContent = `${visiblePortions} portions`;
      }
    },

    attachPortionActions: function() {
      const viewButtons = document.querySelectorAll('[data-view-portion]');

      viewButtons.forEach(button => {
        button.addEventListener('click', (e) => {
          e.preventDefault();
          const portionId = button.dataset.viewPortion;
          this.showPortionDetails(portionId);
        });
      });
    },

    showPortionDetails: function(portionId) {
      // In production, load portion details via AJAX
      window.location.href = `/portions/${portionId}/`;
    },

    setupBulkActions: function() {
      const selectAll = document.querySelector('#select-all-portions');
      if (!selectAll) return;

      selectAll.addEventListener('change', (e) => {
        const checkboxes = document.querySelectorAll('.portion-checkbox');
        checkboxes.forEach(cb => cb.checked = e.target.checked);
        this.updateBulkActionButton();
      });

      // Individual checkboxes
      const checkboxes = document.querySelectorAll('.portion-checkbox');
      checkboxes.forEach(cb => {
        cb.addEventListener('change', () => this.updateBulkActionButton());
      });
    },

    updateBulkActionButton: function() {
      const checkedCount = document.querySelectorAll('.portion-checkbox:checked').length;
      const bulkButton = document.querySelector('#bulk-action-btn');

      if (bulkButton) {
        bulkButton.textContent = `Actions (${checkedCount} selected)`;
        bulkButton.disabled = checkedCount === 0;
      }
    }
  };

  /**
   * ========================================================================
   * FINANCIAL OVERVIEW
   * ========================================================================
   */
  const FinancialOverview = {
    init: function() {
      this.setupDateRangeFilter();
      this.loadFinancialData();
    },

    setupDateRangeFilter: function() {
      const dateRange = document.querySelector('#financial-date-range');
      if (!dateRange) return;

      dateRange.addEventListener('change', () => {
        this.loadFinancialData();
      });
    },

    loadFinancialData: function() {
      const dateRange = document.querySelector('#financial-date-range')?.value || 'month';

      // In production, this would fetch data from the server
      console.log(`Loading financial data for: ${dateRange}`);

      // Simulate loading
      const container = document.querySelector('#financial-chart');
      if (container) {
        container.innerHTML = '<div class="text-center p-4"><i class="fas fa-spinner fa-spin"></i> Loading...</div>';

        setTimeout(() => {
          container.innerHTML = '<div class="text-center p-4">Financial chart would appear here</div>';
        }, 1000);
      }
    }
  };

  /**
   * ========================================================================
   * TENANT MANAGEMENT
   * ========================================================================
   */
  const TenantManagement = {
    init: function() {
      this.setupTenantSearch();
      this.attachTenantActions();
    },

    setupTenantSearch: function() {
      const searchInput = document.querySelector('#tenant-search');
      if (!searchInput) return;

      let searchTimeout;
      searchInput.addEventListener('input', (e) => {
        clearTimeout(searchTimeout);
        searchTimeout = setTimeout(() => {
          this.searchTenants(e.target.value);
        }, 300);
      });
    },

    searchTenants: function(searchTerm) {
      const tenants = document.querySelectorAll('.tenant-item');
      const term = searchTerm.toLowerCase().trim();

      tenants.forEach(tenant => {
        const name = tenant.dataset.tenantName?.toLowerCase() || '';
        const portionNumber = tenant.dataset.portionNumber?.toLowerCase() || '';

        if (name.includes(term) || portionNumber.includes(term)) {
          tenant.style.display = '';
        } else {
          tenant.style.display = 'none';
        }
      });
    },

    attachTenantActions: function() {
      const contactButtons = document.querySelectorAll('[data-contact-tenant]');

      contactButtons.forEach(button => {
        button.addEventListener('click', (e) => {
          e.preventDefault();
          const tenantId = button.dataset.contactTenant;
          this.openContactModal(tenantId);
        });
      });
    },

    openContactModal: function(tenantId) {
      const modal = document.querySelector('#contact-tenant-modal');
      if (!modal) return;

      // Set tenant ID in modal
      const tenantIdField = modal.querySelector('#contact-tenant-id');
      if (tenantIdField) tenantIdField.value = tenantId;

      // Show modal
      const bsModal = new bootstrap.Modal(modal);
      bsModal.show();
    }
  };

  /**
   * ========================================================================
   * NOTIFICATIONS
   * ========================================================================
   */
  const Notifications = {
    init: function() {
      this.loadNotifications();
      this.attachMarkAsReadListeners();
    },

    loadNotifications: function() {
      const badge = document.querySelector('#notification-badge');
      if (!badge) return;

      // In production, load from server
      const count = parseInt(badge.dataset.count) || 0;
      badge.textContent = count;
      badge.style.display = count > 0 ? 'inline' : 'none';
    },

    attachMarkAsReadListeners: function() {
      const markReadButtons = document.querySelectorAll('[data-mark-read]');

      markReadButtons.forEach(button => {
        button.addEventListener('click', (e) => {
          e.preventDefault();
          const notificationId = button.dataset.markRead;
          this.markAsRead(notificationId);
        });
      });
    },

    markAsRead: function(notificationId) {
      // In production, send AJAX request
      const notification = document.querySelector(`[data-notification-id="${notificationId}"]`);
      if (notification) {
        notification.classList.add('read');
        notification.classList.remove('unread');
      }

      this.updateBadgeCount();
    },

    updateBadgeCount: function() {
      const unreadCount = document.querySelectorAll('.notification.unread').length;
      const badge = document.querySelector('#notification-badge');

      if (badge) {
        badge.textContent = unreadCount;
        badge.style.display = unreadCount > 0 ? 'inline' : 'none';
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
    ClientDashboard.init();
    PropertyPortfolio.init();
    PortionManagement.init();
    FinancialOverview.init();
    TenantManagement.init();
    Notifications.init();
  }

  // Start initialization
  init();

})();

/**
 * ============================================================================
 * END OF CLIENTS.JS
 * ============================================================================
 */
