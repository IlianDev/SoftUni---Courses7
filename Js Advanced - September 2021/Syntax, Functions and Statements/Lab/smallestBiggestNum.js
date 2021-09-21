function smallest(input){
    let numbers = input[0];
    let largestNumber = Number.MIN_VALUE;
    let smallestNumber = Number.MAX_VALUE;
    let inputL= input.length;

    for(i=1; i<inputL; i++){
        let currentNumber = Number(input[i]);
        if(currentNumber > largestNumber){
            largestNumber=currentNumber;
        }
        if (currentNumber < smallestNumber){
            smallestNumber = currentNumber;
        }
}
console.log(largestNumber)
console.log(smallestNumber)

}
smallest(['3', '18', '-255', '666'])