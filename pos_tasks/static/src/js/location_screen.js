/** @odoo-module **/
import { registry } from "@web/core/registry";
import { patch } from "@web/core/utils/patch";
import { Order } from "@point_of_sale/app/store/models";
import { TicketScreen } from "@point_of_sale/app/screens/ticket_screen/ticket_screen";
import { usePos } from "@point_of_sale/app/store/pos_hook";
import { useService } from "@web/core/utils/hooks";
import { _t } from "@web/core/l10n/translation";
import { ProductCombosButton } from "../location_button/location_button";

class ProductCombosScreen extends TicketScreen {
    static template = "custom_pos_screen.ProductCombosScreen";

    setup() {
        super.setup();
        this.pos = usePos();
        this.orm = useService("orm");
        this.productCombosButton = new ProductCombosButton();
    }

//    back() {
//        this.pos.showScreen('ProductScreen');
//    }

    async _Confirm(loc) {
        const order = this.pos.get_order();
        order.set_screen_new(loc.name);

        console.log(loc);
        const result = await this.orm.call("pos.config", "get_locations", ['true'], {});
        console.log(loc.name);
    }
}

registry.category("pos_screens").add("ProductCombosScreen", ProductCombosScreen);


patch(Order.prototype,{

     export_as_JSON(){
       const res = super.export_as_JSON(...arguments);
       res.screen_new = this.get_screen_new();

       return res;
     },

     get_screen_new(){
       return this.i
     },

     set_screen_new(i){
       this.i = i
     },


     export_for_printing(){
       const rec = super.export_for_printing(...arguments);
       rec.screen_receipt = this.i
       return rec;
     }

})