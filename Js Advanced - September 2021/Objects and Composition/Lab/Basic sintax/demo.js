const myPerson = {
    name: 'Peter',
    'Last name': 'Jackson',
    age: 23
};
// I 
console.log(myPerson); // {name: 'Peter', age: 23}
console.log(myPerson.age); // 23
myPerson.age = 24 
console.log(myPerson); // {name: 'Peter', age: 24}
console.log(myPerson.name); // 'Peter'

// II 
const propName = 'name'
console.log(myPerson[propName]) // Peter
console.log(myPerson['name']) // Peter
console.log(myPerson['na' + 'me']) // Peter 
console.log(myPerson['Last name']) // Jackson * it can be reached only with index operator []

// Adding 
myPerson["Second name"] = 'Simon'; // push 
myPerson.nationality = 'UK'; //UK
console.log(myPerson);

// Delite
delete myPerson.age;
console.log(myPerson);