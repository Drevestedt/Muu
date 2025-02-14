document.addEventListener('DOMContentLoaded', () => {
  const form = document.getElementById('book-form');
  const errorElements = form.querySelectorAll('.errorlist');

  if (errorElements.length > 0) {
    form.scrollIntoView({ behavior: 'smooth' });
  }
});
