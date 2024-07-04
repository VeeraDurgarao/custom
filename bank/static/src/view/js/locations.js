/** @odoo-module **/
/*
 * This file is used to register the a new button to see booked orders data.
 */
import { Component } from "@odoo/owl";
import { useService } from "@web/core/utils/hooks";
import { ProductScreen } from "@point_of_sale/app/screens/product_screen/product_screen";
import { usePos } from "@point_of_sale/app/store/pos_hook";

class locations extends Component {
static template = 'point_of_sale.location';
    setup() {
        this.orm = useService("orm");
        this.pos = usePos();
    }
    async onClick() {
       var self = this
       await this.orm.call(
            "book.order", "all_orders", [], {}
        ).then(function(result) {
            self.pos.showScreen('BookedOrdersScreen', {
                data: result,
                new_order:false
            });
        })
    }
}
ProductScreen.addControlButton({
    component: locations,
    condition: () => true
})
