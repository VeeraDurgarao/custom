/** @odoo-module **/

import { _t } from "@web/core/l10n/translation";
import { ProductScreen } from "@point_of_sale/app/screens/product_screen/product_screen";
import { useService } from "@web/core/utils/hooks";
import { TextInputPopup } from "@point_of_sale/app/utils/input_popups/text_input_popup";
import { Component } from "@odoo/owl";
import { usePos } from "@point_of_sale/app/store/pos_hook";
import { ErrorPopup } from "@point_of_sale/app/errors/popups/error_popup";

export class CustomerDiscountButton extends Component {
    static template = "point_of_sale.discount";
    setup() {
        super.setup();
        this.pos = usePos();
        this.popup = useService("popup");
        this.orm = useService("orm")
    }
    async onClick() {
      const Orderlines = this.pos.get_order().get_orderlines();
         const result = await this.orm.call('pos.order', 'get_discount', ['true']);
         for (let orderLine of Orderlines){
            orderLine.set_discount(result);
           }
    }
}

ProductScreen.addControlButton({
    component: CustomerDiscountButton,
});

