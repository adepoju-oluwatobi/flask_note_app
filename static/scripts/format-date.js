function formatDateTime(datetimeElementId) {
    // Get the datetime string from the paragraph element
    var createdOnString = document.getElementById(datetimeElementId).innerText;

    // Convert the datetime string to a Date object
    var createdOnDate = new Date(createdOnString);

    // Format the Date object into a human-readable string
    var formattedDateTime = createdOnDate.toLocaleString(); // Example format: "1/1/2023, 12:00:00 PM"

    // Update the paragraph element with the formatted datetime
    document.getElementById(datetimeElementId).innerText = "Joined on: " + formattedDateTime;
}

// Call the formatDateTime function with the ID of the datetime element
formatDateTime('created-on');