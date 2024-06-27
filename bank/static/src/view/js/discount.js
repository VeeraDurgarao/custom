/** @odoo-module **/

import { _t } from "@web/core/l10n/translation";
import { ProductScreen } from "@point_of_sale/app/screens/product_screen/product_screen";
import { useService } from "@web/core/utils/hooks";
import { TextAreaPopup } from "@point_of_sale/app/utils/input_popups/textarea_popup";
import { Component } from "@odoo/owl";
import { usePos } from "@point_of_sale/app/store/pos_hook";

export class CustomerDiscountButton extends Component {
    static template = "point_of_sale.discount";

    setup() {
        this.pos = usePos();
        this.popup = useService("popup");
    }
    async onClick() {
      const Orderlines = this.pos.get_order().get_orderlines();
        const { confirmed, payload: inputNote } = await this.popup.add(TextAreaPopup, {
//            startingValue: Orderlines.get_customer_note(),
            title: _t("Add Discount %"),
        });
          if (confirmed) {
          if ((inputNote > 100) || (inputNote < 0)){
            alert("Discount cannot be more than 100%")
          }
          else{
          for (let orderLine of Orderlines){
                orderLine.set_discount(inputNote);
               }
               }
        }
    }
}

ProductScreen.addControlButton({
    component: CustomerDiscountButton,
});


///** @odoo-module **/
//
//import { _t } from "@web/core/l10n/translation";
//import { ProductScreen } from "@point_of_sale/app/screens/product_screen/product_screen";
//import { useService } from "@web/core/utils/hooks";
//import { TextAreaPopup } from "@point_of_sale/app/utils/input_popups/textarea_popup";
//import { Component } from "@odoo/owl";
//import { usePos } from "@point_of_sale/app/store/pos_hook";
//
//// Extend the order line model to include our custom validation method
//function set_discount_with_validation(discount) {
//    var parsed_discount =
//        typeof discount === "number"
//            ? discount
//            : isNaN(parseFloat(discount))
//            ? 0
//            : parseFloat("" + discount);
//
//    // Add validation for discount above 100
//    if (parsed_discount > 100) {
//        // Show validation error (you might want to replace this with your preferred method of displaying errors)
//        alert(_t("Discount cannot be more than 100%"));
//        parsed_discount = 100;
//    }
//
//    var disc = Math.min(Math.max(parsed_discount || 0, 0), 100);
//    this.discount = disc;
//    this.discountStr = "" + disc;
//}
//
//export class CustomerDiscountButton extends Component {
//    static template = "point_of_sale.discount";
//
//    setup() {
//        this.pos = usePos();
//        this.popup = useService("popup");
//    }
//    async onClick() {
//        const Orderlines = this.pos.get_order().get_orderlines();
//        const { confirmed, payload: inputNote } = await this.popup.add(TextAreaPopup, {
//            title: _t("Add Discount %"),
//        });
//        if (confirmed) {
//            for (let orderLine of Orderlines) {
//                // Use the extended method with validation
//                set_discount_with_validation.call(orderLine, inputNote);
//            }
//        }
//    }
//}
//
//ProductScreen.addControlButton({
//    component: CustomerDiscountButton,
//});
