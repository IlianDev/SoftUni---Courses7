function addItem() {
    // select input field and read value
    const input = document.getElementById('newItemText');

    // create new <li> and set its content ot input value
    const liElement = document.createElement('li');
    liElement.textContent = input.value;
    // selct <ul> and append new <li> element 
    document.getElementById('items').appendChild(liElement);
    // nice-to-have clear field
    input.value = '';
}