
// O'zbekcha fayldan matn yuklash
function loadUzbekFile() {
    const file = document.getElementById('uzbekFileInput').files[0];
    loadFile(file, 'uzbekText');
}

// Inglizcha fayldan matn yuklash
function loadEnglishFile() {
    const file = document.getElementById('englishFileInput').files[0];
    loadFile(file, 'englishText');
}

// Faylni o'qish (DOCX yoki TXT)
function loadFile(file, elementId) {
    const reader = new FileReader();

    reader.onload = function (e) {
        if (file.name.endsWith('.txt')) {
            // .txt fayllarni matn sifatida o'qish
            document.getElementById(elementId).value = e.target.result;
        } else if (file.name.endsWith('.docx')) {
            // .docx fayllarni ArrayBuffer orqali o'qish
            mammoth.extractRawText({ arrayBuffer: e.target.result })
                .then(result => document.getElementById(elementId).value = result.value)
                .catch(err => console.error("DOCX o'qishda xato:", err));
        }
    };

    if (file.name.endsWith('.txt')) {
        reader.readAsText(file); // .txt faylni to'g'ridan-to'g'ri matn sifatida o'qish
    } else {
        reader.readAsArrayBuffer(file); // .docx faylni ArrayBuffer sifatida o'qish
    }
}


async function alignText() {
    const uzbekText = document.getElementById('uzbekText').value;
    const englishText = document.getElementById('englishText').value;
    const alignmentOption = document.getElementById('alignmentOption').value;

    if (!uzbekText || !englishText) {
        alert("Iltimos, ikkala matnni ham kiriting yoki yuklang.");
        return;
    }

    if (alignmentOption === "paragraph") {
        alignParagraphs(englishText, uzbekText);
    } else if (alignmentOption === "sentence") {
        alignSentences(englishText, uzbekText);
    } else if (alignmentOption === "phrase") {
        console.log("Bu qism hali tayyor emas");
    }
}

function alignParagraphs(englishText, uzbekText) {
    const englishParagraphs = englishText.split('\n').filter(p => p.trim());
    const uzbekParagraphs = uzbekText.split('\n').filter(p => p.trim());

    displayAlignedText(englishParagraphs, uzbekParagraphs);
}

function alignSentences(englishText, uzbekText) {
    const englishSentences = englishText.split('.').filter(s => s.trim());
    const uzbekSentences = uzbekText.split('.').filter(s => s.trim());

    displayAlignedText(englishSentences, uzbekSentences);
}

function displayAlignedText(englishArray, uzbekArray) {
    const maxLength = Math.max(englishArray.length, uzbekArray.length);
    const resultTable = document.getElementById('resultTable').getElementsByTagName('tbody')[0];
    resultTable.innerHTML = '';

    for (let i = 0; i < maxLength; i++) {
        const row = resultTable.insertRow();
        const englishCell = row.insertCell(0);
        const uzbekCell = row.insertCell(1);
        englishCell.textContent = englishArray[i] || '';
        uzbekCell.textContent = uzbekArray[i] || '';
    }
}

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