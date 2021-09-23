let array2 = [1, 30, 4, 21, 100000];
array2.sort(compareNumbers);
console.log(array2); // [ 1, 4, 21, 30, 100000 ]
function compareNumbers(a, b) { return a - b; }
