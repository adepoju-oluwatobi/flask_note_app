// Get the alert element
var alertElement = document.getElementById('alert');

// Call the closeAlert function immediately when the page loads
closeAlert(alertElement);

// JavaScript function to close the alert after 2 seconds
function closeAlert(alertElement) {
    // Hide the alert after 2 seconds
    setTimeout(function() {
        // Add the 'hidden' class to trigger the fade-out effect
        alertElement.classList.add('hidden');
    }, 2000); // 2000 milliseconds = 2 seconds
}
