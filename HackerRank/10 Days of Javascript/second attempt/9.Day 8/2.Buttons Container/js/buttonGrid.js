const buttonContainer = document.createElement('div');
buttonContainer.id = 'btns';
for (let i = 1; i < 10; i++) {
    let button = document.createElement('button');
    button.id = `btn${i}`;
    button.innerText = i;
    buttonContainer.appendChild(button);
}
document.body.appendChild(buttonContainer);
document.getElementById('btn5').addEventListener('click', () => {
    let temp = document.getElementById('btn1').innerText;
    document.getElementById('btn1').innerText = document.getElementById('btn4').innerText;
    document.getElementById('btn4').innerText = document.getElementById('btn7').innerText;
    document.getElementById('btn7').innerText = document.getElementById('btn8').innerText;
    document.getElementById('btn8').innerText = document.getElementById('btn9').innerText;
    document.getElementById('btn9').innerText = document.getElementById('btn6').innerText;
    document.getElementById('btn6').innerText = document.getElementById('btn3').innerText;
    document.getElementById('btn3').innerText = document.getElementById('btn2').innerText;
    document.getElementById('btn2').innerText = temp;
});