const myPerson = {
    firstName: 'Peter',
    lastName: 'Jackson',
    age: 23,
    sayHi(){
        return `${this.firstName} ${this.lastName} says hi.`
    }
};
console.log(myPerson.sayHi());

