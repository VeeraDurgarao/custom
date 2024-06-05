/** @odoo-module **/
import { ListController } from "@web/views/list/list_controller";
import { listView } from "@web/views/list/list_view";
import { registry } from "@web/core/registry";


class jsClassModelInfos extends ListController {
    actionSaleList() {
                alert("HI")
    }
}
jsClassModelInfos.template = "bank.modelSaleBtn";

export const modelInfoViews = {
    ...listView,
    Controller: jsClassModelInfos,
};
registry.category("views").add("model_sale", modelInfoViews);

//
///** @odoo-module */
//
//import { ListController } from "@web/views/list/list_controller";
//import { useService } from "@web/core/utils/hooks";
//import { registry } from '@web/core/registry';
//import { listView } from "@web/views/list/list_view";  // Ensure listView is imported correctly
//
//export class CustomListController extends ListController {
//    setup() {
//        super.setup();
//        this.orm = useService('orm');
//        this.actionService = useService('action');
//    }
//
//    showAlert() {
//        alert('This is a custom alert message!');
//    }
//}
//
//// Register the custom list controller in the Odoo registry
//registry.category('views').add('custom_list', {
//    ...listView,
//    Controller: CustomListController,
//});
