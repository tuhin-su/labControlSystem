document.addEventListener('contextmenu', function(e) {
    e.preventDefault();  // Prevents right-click menu
});

document.addEventListener('keydown', function(event) {
    // Disable F12 (DevTools), Ctrl+I, Ctrl+U, etc.
    if (event.key === 'F12' || (event.ctrlKey && (event.key === 'I' || event.key === 'U'))) {
        event.preventDefault();
    }

    // Block Ctrl+R (Reload)
    if (event.ctrlKey && event.key === 'r') {
        event.preventDefault();
    }
});