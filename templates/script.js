document.querySelector('.subscribe-button').addEventListener('click', function() {
    // Toggle visibility of hidden section
    document.querySelector('.hidden-section').style.display = 'block';
    // Hide the blurry section and call-to-action
    document.querySelector('.blurry-section').style.display = 'none';
    document.querySelector('.cta').style.display = 'none';
});
