function sumTable() {
    // select first table
    // select only rows containing needed values
    // repeat for each row
    // - find last cell
    // - add cell value to sum 
    // select elements with id sum and set ints value
    const rows = document.querySelectorAll('table tr');
    sum = 0
    for (let i = 1; i < rows.length-1; i++) {
        const cell = rows[i].lastElementChild;
        sum += Number(cell.textContent);   
    }
    console.log('sum');
    document.getElementById('sum').textContent = sum;
}