document.addEventListener('DOMContentLoaded', function() {
  const form = document.querySelector('form');
  const inputs = form.querySelectorAll('input');

  inputs.forEach(input => {
    const label = input.previousElementSibling;
    if (label && label.tagName === 'LABEL') {
      input.setAttribute('placeholder', label.textContent);
    }

    input.addEventListener('focus', function() {
      this.parentElement.classList.add('focused');
    });

    input.addEventListener('blur', function() {
      if (this.value === '') {
        this.parentElement.classList.remove('focused');
      }
    });
  });

  form.addEventListener('submit', function(e) {
    const button = this.querySelector('button[type="submit"]');
    button.textContent = 'Processing...';
    button.disabled = true;

    // The form will be submitted normally, no need to prevent default
    // Django will handle the form submission and redirects
  });
});