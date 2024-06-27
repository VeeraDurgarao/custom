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
        this.pos = usePos();
        this.popup = useService("popup");
    }
    async onClick() {
    try {
        const orderLines = this.pos.get_order().get_orderlines();
        let validInput = false;

        while (!validInput) {
            const { confirmed, payload: inputNote } = await this.popup.add(TextInputPopup, {
                title: _t("Add Discount %"),
//                startingValue: _t("%"),
            });

            if (confirmed) {
                const discount = parseFloat(inputNote);

                if (isNaN(discount) || discount < 0 || discount > 100) {
                    await this.popup.add(ErrorPopup, {
                        title: _t("Invalid Discount"),
                        body: _t(`You cannot give discount value ${inputNote} as it is not between 0 and 100. Please enter a valid value.`),
                    });
                } else {
                    validInput = true;
                    for (let orderLine of orderLines) {
                        orderLine.set_discount(discount);
                    }
                }
            } else {
                validInput = true; // Exit loop if user cancels the input
            }
        }
    } catch (error) {
        this.popup.add(ErrorPopup, {
            title: _t("Error"),
            body: _t(error.message),
        });
    }
}

//    async onClick() {
//      const Orderlines = this.pos.get_order().get_orderlines();
//        const { confirmed, payload: inputNote } = await this.popup.add(TextInputPopup, {
//            startingValue: Orderlines.get_customer_note(),
//            title: _t("Add Discount %"),
//        });
//
//          if (confirmed) {
//          if ((inputNote > 100) || (inputNote < 0) || (!Number())){
//            this.popup.add(ErrorPopup, {
//                title: _t("You cannot give discount value " + inputNote + " as it is not between 0 and 100"),
////                body: _t("Please Enter valid value!"),
//            });
//          }
//          else{
//          for (let orderLine of Orderlines){
//                orderLine.set_discount(inputNote);
//               }
//               }
//        }
//    }
//}

ProductScreen.addControlButton({
    component: CustomerDiscountButton,
});

