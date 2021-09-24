function solve(arr){
    let smallest = []
    arr.sort((a, b) => (a-b));
    smallest.push(arr[0], arr[1]);
    console.log(smallest);
}
solve([30, 15, 50, 5])