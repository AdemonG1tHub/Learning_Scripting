function askQuestion() {
    let answer = prompt("What is your favorite color?");
    if (answer) {
        console.log("You said: " + answer);
    } else {
        console.log("You didn't enter anything.");
    }
}

function enterName() {
    let name = prompt("What is your name?")
    console.log("Name entered! Hello, Adem. To get started, click on the second button.")
}