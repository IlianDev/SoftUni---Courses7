function print(){
    console.log(`${this.name} is printing.`)
}
function scan(){
    console.log(`${this.name} is scanning.`)
}
const printer = {name: "Sony", print};
const scanner = {nama: "LG", scan, print};

printer.print();








    