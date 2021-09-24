function solve(input) {
    let evens = []
    for (let i = 0; i < input.length; i++) {
        if (i % 2 == 0) {
            evens.push(input[i])
        }
    }
    console.log(evens)
}

solve(['20', '30', '40', '50', '60'])