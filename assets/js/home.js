// Back to top functionality
function scrollToTop() {
  window.scrollTo({ top: 0, behavior: 'smooth' });
}

// Show/hide back to top button
window.addEventListener('scroll', function() {
  const backToTop = document.getElementById('backToTop');
  if (backToTop && window.pageYOffset > 300) {
    backToTop.classList.add('visible');
  } else if (backToTop) {
    backToTop.classList.remove('visible');
  }
});

// Smooth scroll to sections (for home page)
function scrollToSection(sectionId) {
  const element = document.getElementById(sectionId);
  if (element) {
    element.scrollIntoView({ behavior: 'smooth' });
  }
}

// Collapsible sidebar sections
function toggleSection(sectionId) {
  const content = document.getElementById(sectionId);
  if (!content) return;

  const header = content.previousElementSibling;
  const icon = header.querySelector('.toggle-icon');

  if (content.classList.contains('open')) {
    content.classList.remove('open');
    header.classList.remove('open');
    icon.textContent = '+';
  } else {
    content.classList.add('open');
    header.classList.add('open');
    icon.textContent = '−';
  }
}