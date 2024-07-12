/** @odoo-module **/
import { FormController } from "@web/views/form/form_controller";
import { formView } from "@web/views/form/form_view";
import { registry } from "@web/core/registry";

// In this code we are try to do add one button inside form view it is only showing on particular form view

export class jsClassStock extends FormController {
    actionInfoStockForm() {
                alert("HI")

    }
}
jsClassStock.template = "bank.modelStockBtn";

export const modelInfoStock = {
    ...formView,
    Controller: jsClassStock,
};
registry.category("views").add("stock_info", modelInfoStock);
