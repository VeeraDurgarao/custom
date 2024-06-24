/**@odoo-module **/
import { _t } from "@web/core/l10n/translation";
import { ProductScreen } from "@point_of_sale/app/screens/product_screen/product_screen";
import { useService } from "@web/core/utils/hooks";
import { Component } from "@odoo/owl";
import { usePos } from "@point_of_sale/app/store/pos_hook";


export class CreateButton1 extends Component {
    static template = "point_of_sale.CustomerButtons";

    setup() {
    this.pos = usePos();
//        this.numberBuffer = useService("number_buffer")

    }


    async onClick() {
        //console.log("Hi Durgarao")
        console.log(this.pos.get_order())
        console.log(this.pos.get_order().get_orderlines())
        console.log(this.pos.get_order().get_orderlines().length)
        const selectedOrderline = this.pos.get_order().get_selected_orderline();
        console.log(selectedOrderline)
        const orderLine = this.pos.get_order();
//        if (!orderLine) {
//        //    console.error('No order found.');
//            return;
//          }
//        const currentOrder = orderLine.get_orderlines().slice();
//        for(let i=0;i<currentOrder.length;i++){
//             orderLine.removeOrderline(currentOrder[i]);
//    //         console.log(currentOrder[i])
//        }
//        console.log(selectedOrderline)
    }
}

ProductScreen.addControlButton({
component: CreateButton1,
});

