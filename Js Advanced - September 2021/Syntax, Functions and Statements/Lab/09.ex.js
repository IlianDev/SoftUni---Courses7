function solve(arr) {
    let sumResult = arr.reduce((a, x) => a + x);
    let sumInverse = arr.reduce((a, x) => a + (1 / x));
    let concat = arr.reduce((a, x) => a + x, '');
    console.log(sumResult);
    console.log(sumInverse);
    console.log(concat);
}
solve([1, 2, 3])