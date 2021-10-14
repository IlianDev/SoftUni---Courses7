function toggle() {
    let button = document.getElementsByClassName('button')[0];
    let buttonA = document.getElementsByClassName('button');
    let divText = document.getElementById('extra');

    // if textContent of button is 'More' set it to 'Less' and if it less set to 'More'
    button.textContent = button.textContent === 'More' ? 'Less' : 'More';
    divText.style.display = divText.style.display === 'block' ? 'none' : 'block';
}

