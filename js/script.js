var typedTextSpan = document.querySelector(".interest");
var conjuction = document.querySelector(".conjuction");
var para_text = document.querySelector(".typewriter_p");
const LoveTodo = ["Developer", "Analyst", "Strategist", "Motivator", "Software Engineer","Proud Engineer"]
const typeDelay = 200;
const eraseDelay = 100;
const newtext = 2000;
var index = 0;
var letter_index = 0;

function startTyping() {

    if (isVowel(LoveTodo[index][0])) {
        conjuction.textContent = "n";

    } else {
        conjuction.textContent = "";
    }

    if (letter_index < LoveTodo[index].length) {
        typedTextSpan.textContent += LoveTodo[index].charAt(letter_index);
        letter_index += 1;
        setTimeout(startTyping, typeDelay);
    } else {
        setTimeout(erase, newtext);
    }
}

function erase() {
    if (letter_index > 0) {
        typedTextSpan.textContent = LoveTodo[index].substring(0, letter_index - 1)
        letter_index -= 1
        setTimeout(erase, eraseDelay);


    } else {

        index += 1;
        if (index >= LoveTodo.length)
            index = 0
        setTimeout(startTyping, typeDelay);
    }

    return

}
startTyping()

function isVowel(char) {
    return char === 'A' || char === 'E' || char === 'I' || char === 'O' || char === 'U' || false;
}