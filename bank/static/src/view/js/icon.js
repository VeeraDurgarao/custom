/** @odoo-module **/
import { patch } from "@web/core/utils/patch";
import { jsClassStock } from '@bank/view/js/control';
patch(jsClassStock.prototype, {
        setup() {
            super.setup();
        },
        async actionIcons() {
           alert("Hi")
            },
    });
