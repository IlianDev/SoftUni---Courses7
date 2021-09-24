function solve(nums) {
    nums.sort((a, b) => (a - b));
    let middle = nums.length / 2;
    let result = nums.slice(middle)
    console.log(result);
}
// solve([3, 19, 14, 7, 2, 19, 6])
solve([4, 7, 2, 5])
