// JavaScript for email validation
const form = document.querySelector('form');
form.addEventListener('submit', function(event) {
    const emailFields = document.querySelectorAll('input[type="text"]');
    emailFields.forEach(field => {
        if (!field.value.includes('@')) {
            event.preventDefault();
            alert('Please enter a valid email address');
        }
    });
});