function solve(fr, kg, pr){
    let fruit = fr;
    let kilos = (Number(kg))/1000;
    let pricePerKilo = Number(pr);
    
    let totalMoney = kilos * pricePerKilo;
    console.log(`I need $${totalMoney.toFixed(2)} to buy ${kilos.toFixed(2)} kilograms ${fruit}.`)
}
solve('orange', 2500, 1.80)

