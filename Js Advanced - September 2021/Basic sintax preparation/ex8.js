function solve(input) {
    let index = 0; 
    let name = input[index];
    index++;
    let classChild = 1;
    let isExcluded = false;
    let counterBadGrades = 0
    let sumGrade = 0

    while (classChild <= 12){
        let grade = Number(input[index])
         index++;
        if (grade < 4){
            counterBadGrades ++;
            if (counterBadGrades === 2){
                isExcluded = true;
                break
            }
            // continue;
        }
        sumGrade+= grade;
        classChild++;
    }
    if (isExcluded) {
        console.log(`${name} has been excluded at ${classChild} grade`)
    }else{
        let averageGrade = sumGrade / 12;
        console.log(`${name} graduated. Average grade: ${(averageGrade).toFixed(2)}`)
    }
}
// solve(["Mimi", 
// "5",
// "6",
// "5",
// "6",
// "5",
// "6",
// "6",
// "2",
// "3"])

// console.log('passed')

solve(["Gosho", 
"5",
"5.5",
"6",
"5.43",
"5.5",
"6",
"5.55",
"5",
"6",
"6",
"5.43",
"5"])

