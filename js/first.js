export class First {
    constructor(name = "Durgarao", age = 24) {
        this.name = name;
        this.age = age;
    }

    greet() {
        console.log(`Hello from class A, ${this.name}!`);
    }
}
