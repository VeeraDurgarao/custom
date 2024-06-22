/** @odoo-module **/
import { ListController } from "@web/views/list/list_controller";
import { listView } from "@web/views/list/list_view";
import { registry } from "@web/core/registry";
import { useService } from "@web/core/utils/hooks";

class JsClassModeButt extends ListController {
    setup() {
        super.setup();
        this.orm = useService('orm');
        this.notificationService = useService("notification");
        this.actionService = useService('action');
    }

    actionBankList() {
        this.notificationService.add("You closed a deal!", {
            title: "OOPS!",
            type: "danger",
            buttons: [
                {
                    name: "Something went wrong",
                    onClick: () => {
                        this.actionService.doAction("commission_action");
                    },
                },
            ],
        });
    }
}
JsClassModeButt.template = "bank.modelBankBtn";

export const modelInfo = {
    ...listView,
    Controller: JsClassModeButt,
};

registry.category("views").add("add_new", modelInfo);
