function validate() {
    const input = document.getElementById('email');
    input.addEventListener('change', onChange);

    function onChange(ev) {
        const pattern = /^[a-z]+@[a-z]+\.[a-z]+$/;

        // metod test ще върне тру ако патерна отговаря и фолс ако не
        if(pattern.test(ev.target.value)) {
            ev.target.classList.remove('error');
        } else {
            ev.target.classList.add('error');
        }
    }
}