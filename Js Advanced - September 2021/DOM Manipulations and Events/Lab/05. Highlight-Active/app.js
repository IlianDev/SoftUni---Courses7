function focused() {
    const fields = Array.from(document.getElementsByTagName("input"));

    for (let fileld of fields) {
        fileld.addEventListener('focus', onFocus);
        fileld.addEventListener('blur', onBlur);

    }
    function onFocus(event) {
        event.target.parentNode.className = 'focused';
    }
    function onBlur(event) {
        event.target.parentNode.className = '';
    }
}