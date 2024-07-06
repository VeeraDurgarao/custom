/** @odoo-module */
import { ProductScreen } from "@point_of_sale/app/screens/product_screen/product_screen";
import { CustomPopup } from "@bank/emi/popup/popup";
import { useService } from "@web/core/utils/hooks";
import { usePos } from "@point_of_sale/app/store/pos_hook";
import { _t } from "@web/core/l10n/translation";
import { Component } from "@odoo/owl";

export class CustomButton extends Component {
   static template = "custom_popup.CustomButton";
   setup() {
       this.pos = usePos();
       this.popup = useService("popup");
   }

   async click() {
       const order = this.pos.get_order();
        console.log(order)
       await this.popup.add(CustomPopup, {
           title: _t("Customer Details"),
           partner: this.pos.get_order().partner
       });
   }
}
// Adds the custom button to the ProductScreen controls.
ProductScreen.addControlButton({
   component: CustomButton,
   condition: function () {
       return true;
   },
});