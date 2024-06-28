function deleteNote(noteId) {
    fetch(`/delete-note/${noteId}`, {
        method: "DELETE",
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Failed to delete note');
        }
        return response.json();  // Parse response JSON
    })
    .then(data => {
        // Handle successful deletion
        console.log(data.message);
        alert('Note deleted successfully!')
        // Redirect to homepage or desired location
        window.location.href = "/";
    })
    .catch(error => {
        // Handle errors
        console.error('Error deleting note:', error);
        alert('error deleting note!')
    });
}
