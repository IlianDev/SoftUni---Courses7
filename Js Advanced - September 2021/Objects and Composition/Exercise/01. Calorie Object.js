function solve(inputArr) {
    let object = {};
    for (let i = 0; i < inputArr.length; i += 2) {
        object[inputArr[i]] = inputArr[i + 1];
    }
    console.log(object);
}
solve(['Yoghurt', '48', 'Rise', '138', 'Apple', '52'])