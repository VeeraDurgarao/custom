/** @odoo-module **/
import { ListController } from "@web/views/list/list_controller";
import { listView } from "@web/views/list/list_view";
import { registry } from "@web/core/registry";


class jsClassModelManifest extends ListController {
    actionManifestList() {
    const records = this.model.root.selection;
    print(records)
                alert("HI");
                console.log("Durgarao")
    }
}
jsClassModelManifest.template = "bank.modelManifest";

export const modelInfoManifest = {
    ...listView,
    Controller: jsClassModelManifest,
};
registry.category("views").add("manifest_but", modelInfoManifest);