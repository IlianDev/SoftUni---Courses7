function solve(inputArr) {
    let object = {};
    for (let i = 0; i < inputArr.length; i += 2) {

        object[inputArr[i]] = Number(inputArr[i + 1]);
    }
    return object;
}
console.log(solve(['Yoghurt', '48', 'Rise', '138', 'Apple', '52']))
