function solve(word) {
    if (typeof (word) == 'number') {
        let area = Math.PI * word ** 2;
        console.log(area.toFixed(2))
    } else {
        console.log(`We can not calculate the circle area, because we receive a ${typeof(word)}`)
    }
}
solve(5);
solve("string input")