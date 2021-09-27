function population(townAsStrings) {
    const towns = {};
    for (let data of townAsStrings) {
        const givenData = data.split('<->');

        const name = givenData[0];
        const pop = Number(givenData[1]);

        if (towns[name] == undefined) {
            towns[name] = pop;
        }else{
            towns[name] += pop
        }
    }
    for (const name in towns) {
        console.log(`${name}: ${towns[name]}`);
    }
}
population([
    'Sofia <-> 1200000',
    'Montana <-> 20000',
    'New York <-> 10000000',
    'Washington <-> 2345000',
    'Las Vegas <-> 1000000'
])
console.log('------------------');

population([
    'Istanbul <-> 100000',
    'Honk Kong <-> 2100004',
    'Jerusalem <-> 2352344',
    'Mexico City <-> 23401925',
    'Istanbul <-> 1000'
])