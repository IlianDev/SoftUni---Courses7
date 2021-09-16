function solve(input1, input2){
    let num1 = Number(input1);
    let num2 = Number(input2);
    let sum = 0;

    for (i=num1; i<=num2; i++) {
        sum = sum + i;

    }
    console.log(sum);
}
// solve('1','5')
solve('-8', '20')

