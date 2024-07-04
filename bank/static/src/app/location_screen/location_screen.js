/** @odoo-module **/
/*
 * This file is used to register a new screen for Booked orders.
 */
// connection.py python file using
import { registry } from "@web/core/registry";
import { patch } from "@web/core/utils/patch";
import { Order } from "@point_of_sale/app/store/models";
import { TicketScreen } from "@point_of_sale/app/screens/ticket_screen/ticket_screen";
import { usePos } from "@point_of_sale/app/store/pos_hook";
import { useService } from "@web/core/utils/hooks";

class ProductCombosScreen extends TicketScreen {
    static template = "custom_pos_screen.ProductCombosScreen";
    setup() {
        super.setup();
        this.pos = usePos();
        this.orm = useService("orm");
    }
    back() {
        this.pos.showScreen('ProductScreen');
    }
    async _Confirm(loc) {
    const order=this.pos.get_order()
    order.set_screen_new(loc.name)

        console.log(loc)
     const result = await this.orm.call("pos.config","get_locations",['true'],{})
     console.log(result)
    this.pos.showScreen('ProductScreen');
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



///** @odoo-module */
//import { registry } from "@web/core/registry";
//import { useService } from "@web/core/utils/hooks";
//import { usePos } from "@point_of_sale/app/store/pos_hook";
//import { Component } from "@odoo/owl";
//export class ProductCombosScreen extends Component {
//    static template = "custom_pos_screen.ProductCombosScreen";
//    setup() {
//        this.orm = useService("orm");
//        this.pos = usePos();
//    }
////    async getPosConfigs() {
////    // fetch all booked order in draft stage to screen
////       var self = this
////       await this.orm.call(
////            "pos.config", "get_locations", ['True'], {}
////        ).then(function(result) {
////            self.pos.showScreen('ProductCombosScreen', {
////                data: result,
////                new_order:false
////            });
////        })
////    }
//async getPosConfigs() {
//       var self = this
//       await this.orm.call("pos.config","get_locations",['true'],{}
//       ).then(function(result) {
//            console.log(result);
//            self.pos.showScreen('ProductCombosScreen',{
//                data: result,
//            });
//        });
//    }
//}
//
////ProductScreen.addControlButton({
////    component: ProductCombosScreen,
////    condition: () => true
////})
//registry.category("pos_screens").add("ProductCombosScreen", ProductCombosScreen);