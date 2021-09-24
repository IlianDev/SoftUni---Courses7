function solve(arr) {
    arr.sort(sortingEl)
    console.log(arr)

    function sortingEl(a, b) {
        return a - b
    }
}
solve([7, -2, 8, 9])