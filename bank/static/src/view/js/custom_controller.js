/** @odoo-module **/
import { FormController } from "@web/views/form/form_controller";
import { formView } from "@web/views/form/form_view";
import { registry } from "@web/core/registry";


export class  stockPicking extends FormController {
}
stockPicking.template = "bank.formController";

export const FormStock = {
    ...formView,
    Controller: stockPicking,
};
registry.category("views").add("picking_form", FormStock);