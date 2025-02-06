// Typing Effect
const words = ["Truth", "Talk", "Nature"];
let i = 0;
let j = 0;
let currentWord = "";
let isDeleting = false;

function typeEffect() {
    const typingElement = document.querySelector(".typing");

    if (i < words.length) {
        if (!isDeleting && j <= words[i].length) {
            currentWord = words[i].substring(0, j++);
        } else if (isDeleting && j >= 0) {
            currentWord = words[i].substring(0, j--);
        }

        typingElement.textContent = currentWord;

        let speed = isDeleting ? 100 : 200;

        if (!isDeleting && j === words[i].length) {
            speed = 1500;
            isDeleting = true;
        } else if (isDeleting && j === 0) {
            isDeleting = false;
            i++;
            if (i === words.length) i = 0;
            speed = 500;
        }

        setTimeout(typeEffect, speed);
    }
}

// Start Typing Effect
document.addEventListener("DOMContentLoaded", () => {
    setTimeout(typeEffect, 1000);
});
