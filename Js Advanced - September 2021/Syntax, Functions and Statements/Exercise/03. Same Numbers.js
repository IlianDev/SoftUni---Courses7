function solve(intNum){
    const strNum = intNum.toString();
    let result = parseInt(intNum[0]);
    let isSame = true;

    for(let i=1; i<strNum.length; i ++){
        result += parseInt(strNum[i]);

        if (strNum[i] != strNum[i]){
            isSame = false;
        }
    }
    console.log(isSame);
    console.log(result);
}
solve("2222222")

