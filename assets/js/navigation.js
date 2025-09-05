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