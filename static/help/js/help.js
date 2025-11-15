/**
 * ============================================================================
 * HELP APP - JavaScript Module
 * ============================================================================
 *
 * This file contains JavaScript functionality for the help system:
 * - Help article navigation
 * - Search functionality
 * - FAQ accordion
 * - Video tutorial player
 * - Feedback system
 *
 * Dependencies: None (vanilla JavaScript)
 * ============================================================================
 */

(function() {
  'use strict';

  /**
   * ========================================================================
   * HELP SEARCH
   * ========================================================================
   */
  const HelpSearch = {
    init: function() {
      this.setupSearchInput();
      this.setupSearchSuggestions();
    },

    setupSearchInput: function() {
      const searchInput = document.querySelector('#help-search');
      if (!searchInput) return;

      let searchTimeout;
      searchInput.addEventListener('input', (e) => {
        clearTimeout(searchTimeout);
        searchTimeout = setTimeout(() => {
          this.performSearch(e.target.value);
        }, 300);
      });
    },

    performSearch: function(searchTerm) {
      const articles = document.querySelectorAll('.help-article');
      const term = searchTerm.toLowerCase().trim();

      if (!term) {
        articles.forEach(article => article.style.display = '');
        this.clearResults();
        return;
      }

      let foundCount = 0;

      articles.forEach(article => {
        const title = article.dataset.title?.toLowerCase() || '';
        const content = article.dataset.content?.toLowerCase() || '';
        const tags = article.dataset.tags?.toLowerCase() || '';

        if (title.includes(term) || content.includes(term) || tags.includes(term)) {
          article.style.display = '';
          this.highlightSearchTerm(article, term);
          foundCount++;
        } else {
          article.style.display = 'none';
        }
      });

      this.displayResults(foundCount, term);
    },

    highlightSearchTerm: function(article, term) {
      // In production, implement text highlighting
      console.log('Highlighting:', term, 'in', article);
    },

    displayResults: function(count, term) {
      const resultsDiv = document.querySelector('#search-results');
      if (!resultsDiv) return;

      if (count === 0) {
        resultsDiv.innerHTML = `
          <div class="alert alert-info">
            No results found for "<strong>${term}</strong>".
            Try different keywords or browse categories below.
          </div>
        `;
      } else {
        resultsDiv.innerHTML = `
          <div class="alert alert-success">
            Found <strong>${count}</strong> article${count !== 1 ? 's' : ''} for "<strong>${term}</strong>"
          </div>
        `;
      }
    },

    clearResults: function() {
      const resultsDiv = document.querySelector('#search-results');
      if (resultsDiv) {
        resultsDiv.innerHTML = '';
      }
    },

    setupSearchSuggestions: function() {
      const searchInput = document.querySelector('#help-search');
      if (!searchInput) return;

      searchInput.addEventListener('focus', () => {
        this.showPopularSearches();
      });
    },

    showPopularSearches: function() {
      const suggestionsDiv = document.querySelector('#search-suggestions');
      if (!suggestionsDiv) return;

      const popularSearches = [
        'How to add property',
        'Managing portions',
        'Realtor collaboration',
        'Payment methods',
        'Account settings'
      ];

      suggestionsDiv.innerHTML = `
        <div class="popular-searches">
          <h6>Popular searches:</h6>
          <div class="d-flex flex-wrap gap-2">
            ${popularSearches.map(search => `
              <button class="btn btn-sm btn-outline-primary suggestion-btn" data-search="${search}">
                ${search}
              </button>
            `).join('')}
          </div>
        </div>
      `;

      // Attach click listeners
      suggestionsDiv.querySelectorAll('.suggestion-btn').forEach(btn => {
        btn.addEventListener('click', (e) => {
          e.preventDefault();
          const searchTerm = btn.dataset.search;
          document.querySelector('#help-search').value = searchTerm;
          this.performSearch(searchTerm);
        });
      });
    }
  };

  /**
   * ========================================================================
   * FAQ ACCORDION
   * ========================================================================
   */
  const FAQAccordion = {
    init: function() {
      this.setupAccordion();
      this.setupVoting();
    },

    setupAccordion: function() {
      const faqItems = document.querySelectorAll('.faq-item');

      faqItems.forEach(item => {
        const question = item.querySelector('.faq-question');
        if (!question) return;

        question.addEventListener('click', () => {
          this.toggleItem(item);
        });
      });
    },

    toggleItem: function(item) {
      const answer = item.querySelector('.faq-answer');
      const icon = item.querySelector('.faq-icon');

      if (item.classList.contains('active')) {
        item.classList.remove('active');
        answer.style.maxHeight = '0';
        if (icon) icon.style.transform = 'rotate(0deg)';
      } else {
        // Close other items
        document.querySelectorAll('.faq-item.active').forEach(activeItem => {
          if (activeItem !== item) {
            this.toggleItem(activeItem);
          }
        });

        item.classList.add('active');
        answer.style.maxHeight = answer.scrollHeight + 'px';
        if (icon) icon.style.transform = 'rotate(180deg)';
      }
    },

    setupVoting: function() {
      const helpfulButtons = document.querySelectorAll('[data-vote-helpful]');
      const notHelpfulButtons = document.querySelectorAll('[data-vote-not-helpful]');

      helpfulButtons.forEach(button => {
        button.addEventListener('click', (e) => {
          e.preventDefault();
          const articleId = button.dataset.voteHelpful;
          this.submitVote(articleId, true);
        });
      });

      notHelpfulButtons.forEach(button => {
        button.addEventListener('click', (e) => {
          e.preventDefault();
          const articleId = button.dataset.voteNotHelpful;
          this.submitVote(articleId, false);
        });
      });
    },

    submitVote: function(articleId, isHelpful) {
      // In production, send AJAX request
      const feedback = document.querySelector(`#feedback-${articleId}`);
      if (feedback) {
        feedback.innerHTML = `
          <div class="alert alert-success">
            Thank you for your feedback!
          </div>
        `;
      }
    }
  };

  /**
   * ========================================================================
   * VIDEO TUTORIALS
   * ========================================================================
   */
  const VideoTutorials = {
    init: function() {
      this.setupVideoPlayers();
      this.trackVideoProgress();
    },

    setupVideoPlayers: function() {
      const videos = document.querySelectorAll('.tutorial-video');

      videos.forEach(video => {
        video.addEventListener('play', () => {
          this.onVideoPlay(video);
        });

        video.addEventListener('ended', () => {
          this.onVideoEnd(video);
        });
      });
    },

    onVideoPlay: function(video) {
      const videoId = video.dataset.videoId;
      console.log('Started watching:', videoId);

      // In production, track analytics
    },

    onVideoEnd: function(video) {
      const videoId = video.dataset.videoId;
      console.log('Completed watching:', videoId);

      // Mark as watched
      const videoCard = video.closest('.video-card');
      if (videoCard) {
        videoCard.classList.add('watched');

        const badge = document.createElement('span');
        badge.className = 'badge bg-success ms-2';
        badge.textContent = 'Watched';
        videoCard.querySelector('.video-title')?.appendChild(badge);
      }

      // Save to localStorage
      this.saveWatchedVideo(videoId);
    },

    saveWatchedVideo: function(videoId) {
      let watchedVideos = JSON.parse(localStorage.getItem('watched_videos') || '[]');
      if (!watchedVideos.includes(videoId)) {
        watchedVideos.push(videoId);
        localStorage.setItem('watched_videos', JSON.stringify(watchedVideos));
      }
    },

    trackVideoProgress: function() {
      const videos = document.querySelectorAll('.tutorial-video');

      videos.forEach(video => {
        video.addEventListener('timeupdate', () => {
          const progress = (video.currentTime / video.duration) * 100;
          const progressBar = video.closest('.video-card')?.querySelector('.progress-bar');

          if (progressBar) {
            progressBar.style.width = progress + '%';
          }
        });
      });
    }
  };

  /**
   * ========================================================================
   * HELP NAVIGATION
   * ========================================================================
   */
  const HelpNavigation = {
    init: function() {
      this.setupCategoryFilter();
      this.setupBreadcrumbs();
      this.setupTableOfContents();
    },

    setupCategoryFilter: function() {
      const categoryButtons = document.querySelectorAll('[data-category]');

      categoryButtons.forEach(button => {
        button.addEventListener('click', (e) => {
          e.preventDefault();
          const category = button.dataset.category;
          this.filterByCategory(category);

          // Update active state
          categoryButtons.forEach(btn => btn.classList.remove('active'));
          button.classList.add('active');
        });
      });
    },

    filterByCategory: function(category) {
      const articles = document.querySelectorAll('.help-article');

      articles.forEach(article => {
        if (category === 'all' || article.dataset.category === category) {
          article.style.display = '';
        } else {
          article.style.display = 'none';
        }
      });
    },

    setupBreadcrumbs: function() {
      const breadcrumbLinks = document.querySelectorAll('.breadcrumb a');

      breadcrumbLinks.forEach(link => {
        link.addEventListener('click', (e) => {
          // Allow normal navigation
          console.log('Navigating to:', link.href);
        });
      });
    },

    setupTableOfContents: function() {
      const tocLinks = document.querySelectorAll('.table-of-contents a');

      tocLinks.forEach(link => {
        link.addEventListener('click', (e) => {
          e.preventDefault();
          const targetId = link.getAttribute('href').substring(1);
          const targetElement = document.getElementById(targetId);

          if (targetElement) {
            targetElement.scrollIntoView({
              behavior: 'smooth',
              block: 'start'
            });

            // Highlight section temporarily
            targetElement.classList.add('highlighted');
            setTimeout(() => {
              targetElement.classList.remove('highlighted');
            }, 2000);
          }
        });
      });
    }
  };

  /**
   * ========================================================================
   * FEEDBACK SYSTEM
   * ========================================================================
   */
  const FeedbackSystem = {
    init: function() {
      this.setupFeedbackForm();
    },

    setupFeedbackForm: function() {
      const feedbackForm = document.querySelector('#help-feedback-form');
      if (!feedbackForm) return;

      feedbackForm.addEventListener('submit', (e) => {
        e.preventDefault();
        this.submitFeedback(feedbackForm);
      });
    },

    submitFeedback: function(form) {
      const formData = new FormData(form);
      const submitBtn = form.querySelector('button[type="submit"]');

      // Disable button
      submitBtn.disabled = true;
      submitBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Sending...';

      // In production, send AJAX request
      setTimeout(() => {
        submitBtn.disabled = false;
        submitBtn.innerHTML = 'Submit Feedback';

        // Show success message
        const successMsg = document.createElement('div');
        successMsg.className = 'alert alert-success mt-3';
        successMsg.textContent = 'Thank you for your feedback! We appreciate your input.';
        form.appendChild(successMsg);

        // Reset form
        form.reset();

        // Remove success message after 5 seconds
        setTimeout(() => successMsg.remove(), 5000);
      }, 1000);
    }
  };

  /**
   * ========================================================================
   * ROLE-SPECIFIC HELP
   * ========================================================================
   */
  const RoleSpecificHelp = {
    init: function() {
      this.detectUserRole();
      this.showRoleRelevantContent();
    },

    detectUserRole: function() {
      const roleElement = document.querySelector('[data-user-role]');
      this.userRole = roleElement?.dataset.userRole || 'guest';
    },

    showRoleRelevantContent: function() {
      const allContent = document.querySelectorAll('[data-role-content]');

      allContent.forEach(content => {
        const allowedRoles = content.dataset.roleContent.split(',');

        if (allowedRoles.includes(this.userRole) || allowedRoles.includes('all')) {
          content.style.display = '';
        } else {
          content.style.display = 'none';
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
    if (document.readyState === 'loading') {
      document.addEventListener('DOMContentLoaded', initializeModules);
    } else {
      initializeModules();
    }
  }

  function initializeModules() {
    HelpSearch.init();
    FAQAccordion.init();
    VideoTutorials.init();
    HelpNavigation.init();
    FeedbackSystem.init();
    RoleSpecificHelp.init();
  }

  // Start initialization
  init();

})();

/**
 * ============================================================================
 * END OF HELP.JS
 * ============================================================================
 */
