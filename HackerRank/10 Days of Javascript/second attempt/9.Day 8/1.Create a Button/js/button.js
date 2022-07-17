const myBtn = document.createElement('button');
myBtn.id = 'btn';
var i = 0;
myBtn.innerHTML = i;
myBtn.addEventListener('click', () => {
    myBtn.innerHTML = ++i;
});
document.body.appendChild(myBtn);