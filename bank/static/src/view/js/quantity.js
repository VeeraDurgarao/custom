/**@odoo-module **/
//const { useState } = owl.hooks;
//const { xml } = owl.tags;
import { Component } from "@odoo/owl";
import {useState} from '@odoo/owl';

class MyComponent extends Component {
    setup() {
        this.state = useState({ value: 1 });
    }

    increment() {
        this.state.value++;
    }
}
MyComponent.template = point_of_sale.Customer