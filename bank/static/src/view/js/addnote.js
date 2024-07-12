/** @odoo-module **/

import { _t } from "@web/core/l10n/translation";
import { ProductScreen } from "@point_of_sale/app/screens/product_screen/product_screen";
import { useService } from "@web/core/utils/hooks";
import { TextAreaPopup } from "@point_of_sale/app/utils/input_popups/textarea_popup";
import { Component } from "@odoo/owl";
import { usePos } from "@point_of_sale/app/store/pos_hook";
import { Order } from "@point_of_sale/app/store/models";
import { patch } from "@web/core/utils/patch";

export class CustomerNoteButton extends Component {
    static template = "point_of_sale.addNotes";

    setup() {
        this.pos = usePos();

        this.popup = useService("popup");
    }


    async onClick() {
    // in this code whenever user enter any data inside note it is stored in backed and all orders after one line
       const order = this.pos.get_order();
         const orderLines = this.pos.get_order().get_orderlines();
        if (!orderLines) {
            return;
        }
        const { confirmed, payload: inputNote } = await this.popup.add(TextAreaPopup, {
//            startingValue: orderLines.getCustomNote(),
            title: _t("Add Customer Note"),
        });

        if (confirmed) {
//         for (let orderLine of orderLines){
//            orderLine.setNote(inputNote);


            let note1 = document.getElementsByClassName('customNote');
            if(note1.length > 0){
            var value = note1[0]
            value.innerText=inputNote;
//}
          }
        order.setCustomNote(inputNote);
        }
    }
}

ProductScreen.addControlButton({
    component: CustomerNoteButton,
});


//patch(Order.prototype,{
//        export_as_JSON(){
//        const result = super.export_as_JSON(...arguments);
//        result.notes = this.getCustomNote();
//        return result;
//        },
//        getCustomNote(){
//        return "Durgarao Goriparthi";
//        }
//
//})
// Assuming you are extending the Order model in POS
//patch(Order.prototype, {
//    export_as_JSON() {
//        const result = super.export_as_JSON(...arguments);
//        result.note = this.getCustomNote();  // Corrected to match the field name in Python
//        return result;
//    },
////    set_note(note) {
////        this.note = inputNote;
////    },
//    getCustomNote() {
//        return this.inputNote
//    },
//});
patch(Order.prototype, {
    export_as_JSON() {
        const result = super.export_as_JSON(...arguments);
        result.note = this.getCustomNote();
        return result;
    },
    getCustomNote() {
        return this.note || "";
    },
    setCustomNote(note) {
        this.note = note;
    },
    export_for_printing(){
        const resultnote = super.export_for_printing(...arguments);
        resultnote.note = this.note || "";
        return resultnote;
    },
});





