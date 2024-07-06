/** @odoo-module */
import { AbstractAwaitablePopup } from "@point_of_sale/app/popup/abstract_awaitable_popup";
import { _t } from "@web/core/l10n/translation";
import { usePos } from "@point_of_sale/app/store/pos_hook";
import { useRef, onMounted } from "@odoo/owl";
import { useService } from "@web/core/utils/hooks";
/**
* This class represents a custom popup in the Point of Sale.
* It extends the AbstractAwaitablePopup class.
*/
export class CustomPopup extends AbstractAwaitablePopup {
   static template = "custom_popup.CustomButtonPopup";
   static defaultProps = {
       closePopup: _t("Cancel"),
       confirmText: _t("Save"),
       title: _t("Customer Details"),
   };
   setup() {
        super.setup();
        this.pos = usePos();
        this.orm = useService("orm");
        this.order = this.pos.selectedOrder
        this.pickup_date = useRef("pickUpDate")
        this.order_note= useRef("orderNote")
        this.delivery_date= useRef("deliveryDate")
        this.pickup= useRef("pickup_radio")
        this.delivery= useRef("deliver_radio")
        this.Method_pickup= useRef("Method_pickup")
        this.Method_deliver= useRef("Method_deliver")
    }
}