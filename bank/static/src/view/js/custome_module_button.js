/** @odoo-module **/
import { ListController } from "@web/views/list/list_controller";
import { listView } from "@web/views/list/list_view";
import { registry } from "@web/core/registry";


class jsClassModeButt extends ListController {
    actionBankList() {
                alert("HI")
    }
}
jsClassModeButt.template = "bank.modelBankBtn";

export const modelInfo = {
    ...listView,
    Controller: jsClassModeButt,
};
registry.category("views").add("add_new", modelInfo);