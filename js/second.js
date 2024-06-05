/* @odoo-module */
import { First } from './first';

class Second extends First {
    constructor(name, age, city) {
        super(name, age);
        this.city = city;
    }

    result() {
        console.log(`Hello from class A, ${this.name}!, ${this.age}, This is from class B ${this.city}`);
    }
}

const instanceB = new Second("Durgarao", 24, "MyCity");
instanceB.greet();
instanceB.result();
