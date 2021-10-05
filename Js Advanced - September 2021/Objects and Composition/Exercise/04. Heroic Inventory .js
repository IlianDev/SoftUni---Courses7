function solve(input) {
    let result = [];
    for (let index = 0; index < input.length; index++) {
        let [name, level, items] = input[index].split(' / ');
        level = Number(level);
        items = items !== undefined ? items.split(', ') : [];
        result.push({
            name: name,
            level: level,
            items: items,
        });
    }
    return JSON.stringify(result);
}
console.log(solve(['Isacc / 25 / Apple, GravityGun',
    'Derek / 12 / BarrelVest, DestructionSword',
    'Hes / 1 / Desolator, Sentinel, Antara'
]));

console.log('----------------------------------------------------------------')

console.log(solve(['Jake / 1000 / Gauss, HolidayGrenade']));