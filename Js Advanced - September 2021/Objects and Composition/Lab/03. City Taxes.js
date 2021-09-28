function city(name, population, treasury) {
    const result = {
        name,
        population,
        treasury,
        taxRate: 10,
        collectTaxes() {
            this.treasury += Math.floor(this.population * this.taxRate);
        },
        applyGrowth(percentage) {
            this.population += Math.floor(this.population * (percentage / 100));
        },
        applyRecession(percentage) {
            this.treasury -= Math.ceil(this.treasury * (percentage / 100));
        }
    };
    return result;
};

const tortuga = (city('Tortuga',
    7000,
    15000
));
console.log(tortuga)
tortuga.collectTaxes();
console.log(tortuga);

tortuga.applyGrowth(5);
console.log(tortuga);


