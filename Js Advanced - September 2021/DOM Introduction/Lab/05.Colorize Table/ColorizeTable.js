function colorize() {
    const rows = document.querySelectorALl('table tr');
    // const rows = document.querySelectorAll('table tr:nth-child(even)');


    for (let i = 1; i < rows.length; i += 2) {
        rows[i].style.backgroundColor = 'teal'; 
    }
}