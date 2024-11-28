
document.addEventListener('keydown', function (e) {
    // Ctrl+Shift+I uchun
    if (e.ctrlKey && e.shiftKey && e.key === 'I') {
        e.preventDefault();
        alert("Developer Tools ni ochish cheklangan!");
    }

    // F12 uchun
    if (e.key === 'F12') {
        e.preventDefault();
        alert("Developer Tools ni ochish cheklangan!");
    }

    // Ctrl+U uchun
    if (e.ctrlKey && e.key === 'u') {
        e.preventDefault();
        alert("ushbu sahifaning kodini ko‘rish cheklangan!");
    }

    // Ctrl+Shift+J (Console) uchun
    if (e.ctrlKey && e.shiftKey && e.key === 'J') {
        e.preventDefault();
        alert("Developer Tools ni ochish cheklangan!");
    }

    // Ctrl+Shift+C (Element Inspect) uchun
    if (e.ctrlKey && e.shiftKey && e.key === 'C') {
        e.preventDefault();
        alert("Developer Tools ni ochish cheklangan!");
    }
});

// Sichqoncha o'ng tugmasini bloklash
document.addEventListener('contextmenu', function (e) {
    e.preventDefault();
    alert("Manba kodini ko‘rish cheklangan!");
});