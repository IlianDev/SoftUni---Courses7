function toggle() {
    const button = document.getElementsByClassName('button')[0];
    const textDiv = document.getElementById('extra');
    
    if (button.textContent == 'More') {
        textDiv.style.display = 'block';
        button.textContent = 'Less';
    } else {
        textDiv.style.display = 'none';
        button.textContent = 'More';
    }
}
