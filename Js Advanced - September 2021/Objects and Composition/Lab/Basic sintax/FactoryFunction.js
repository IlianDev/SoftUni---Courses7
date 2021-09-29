function city(name, population, treasury) {
    const result = {
        name,
        population,
        treasury,
        taxRate: 10,
        collectTaxes() {
            result.treasury += Math.floor(result.population * result.taxRate);
        },
        applyGrowth(percentage) {
            result.population += Math.floor(result.population * (percentage / 100));
        },
        applyRecession(percentage) {
            result.treasury -= Math.ceil(result.treasury * (percentage / 100));
        }
    };
    return result;
};

const barselona = (city('Barselona',
    7000,
    15000
));
console.log(barselona)
barselona.collectTaxes();
console.log(barselona);

barselona.applyGrowth(5);
console.log(barselona);

// insted of this we use the name factory function.



