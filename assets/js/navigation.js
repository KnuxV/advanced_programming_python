// Global floating navigation toggle
function toggleGlobalNav() {
  const nav = document.getElementById('globalFloatingNav');
  if (nav) {
    nav.classList.toggle('open');
  }
}

// Close global nav when clicking outside
document.addEventListener('click', function(e) {
  const nav = document.getElementById('globalFloatingNav');
  if (nav && !nav.contains(e.target)) {
    nav.classList.remove('open');
  }
});

// Collapsible sidebar sections
function toggleSection(sectionId) {
  const content = document.getElementById(sectionId);
  if (!content) return;

  const header = content.previousElementSibling;
  const icon = header ? header.querySelector('.toggle-icon') : null;

  if (content.classList.contains('open')) {
    content.classList.remove('open');
    if (header) header.classList.remove('open');
    if (icon) icon.textContent = '+';
  } else {
    content.classList.add('open');
    if (header) header.classList.add('open');
    if (icon) icon.textContent = '−';
  }
}

// Initialize sidebar on page load
document.addEventListener('DOMContentLoaded', function() {
  // Auto-expand sections that contain the current page
  const currentLinks = document.querySelectorAll('.sidebar-list li.current a');
  currentLinks.forEach(function(link) {
    const listItem = link.closest('li');
    const content = listItem.closest('.collapsible-content');
    if (content) {
      content.classList.add('open');
      const header = content.previousElementSibling;
      if (header && header.classList.contains('collapsible-header')) {
        header.classList.add('open');
        const icon = header.querySelector('.toggle-icon');
        if (icon) icon.textContent = '−';
      }
    }
  });

  // For lesson pages, auto-expand the lessons section by default if it exists
  const lessonsSection = document.getElementById('lessons-section');
  if (lessonsSection && !lessonsSection.classList.contains('open')) {
    lessonsSection.classList.add('open');
    const header = lessonsSection.previousElementSibling;
    if (header && header.classList.contains('collapsible-header')) {
      header.classList.add('open');
      const icon = header.querySelector('.toggle-icon');
      if (icon) icon.textContent = '−';
    }
  }
});