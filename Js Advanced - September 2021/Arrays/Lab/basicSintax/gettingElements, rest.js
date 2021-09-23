names = ['Pesho', 'Gosho', 'Stamat', 'Mariyka']
getNames(names)

function getNames(names){
    // let firstName = names[0];
    // let secondName = names[1];
    // == second 
    let [firstName, secondName] = names;
    console.log(firstName); // Pesho
    console.log(secondName); // Gosho

    //  rest operator
    let [firstName, ...others] = names;
    console.log(others); 
}