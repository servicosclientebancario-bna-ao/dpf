function displayToast(title, message, type) {
    const toastContainer = document.getElementById('toast-container');
    
    const toast = document.createElement('div');
    toast.className = `toast toast-${type}`;

    const toastTitle = document.createElement('div');
    toastTitle.className = 'toast-title';
    toastTitle.textContent = title;

    const toastMessage = document.createElement('div');
    toastMessage.className = 'toast-message';
    toastMessage.textContent = message;

    const closeButton = document.createElement('button');
    closeButton.className = 'toast-close-button';
    closeButton.textContent = '×';
    closeButton.onclick = function() {
        toastContainer.removeChild(toast);
    };

    toast.appendChild(toastTitle);
    toast.appendChild(toastMessage);
    toast.appendChild(closeButton);

    toastContainer.appendChild(toast);

    setTimeout(function() {
        if (toastContainer.contains(toast)) {
            toastContainer.removeChild(toast);
        }
    }, 5000);
}
