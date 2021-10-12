function calc() {
    // read value of input fields
    const num1 = Number (document.getElementById('num1').value);
    const num2 =Number (document.getElementById('num2').value);
    // TODO: sum = num1 + num2
    const sum = num1 + num2;

    document.getElementById('sum').value = sum;
}
