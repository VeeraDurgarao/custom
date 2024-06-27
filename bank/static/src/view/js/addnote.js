/** @odoo-module **/

import { _t } from "@web/core/l10n/translation";
import { ProductScreen } from "@point_of_sale/app/screens/product_screen/product_screen";
import { useService } from "@web/core/utils/hooks";
import { TextAreaPopup } from "@point_of_sale/app/utils/input_popups/textarea_popup";
import { Component } from "@odoo/owl";
import { usePos } from "@point_of_sale/app/store/pos_hook";

export class CustomerNoteButton extends Component {
    static template = "point_of_sale.addNotes";

    setup() {
        this.pos = usePos();
        this.popup = useService("popup");
    }
    async onClick() {
        const Orderline = this.pos.get_order().get_selected_orderline();
        if (!Orderline) {
            return;
        }
        const { confirmed, payload: inputNote } = await this.popup.add(TextAreaPopup, {
            startingValue: Orderline.get_customer_note(),
            title: _t("Add Customer Note"),
        });

        if (confirmed) {
           Orderline.setNote(inputNote);
        }
    }
}

ProductScreen.addControlButton({
    component: CustomerNoteButton,
});
