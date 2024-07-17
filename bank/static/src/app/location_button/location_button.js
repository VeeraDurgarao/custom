///** @odoo-module **/
//import { Component } from "@odoo/owl";
//import { useService } from "@web/core/utils/hooks";
//import { ProductScreen } from "@point_of_sale/app/screens/product_screen/product_screen";
//import { usePos } from "@point_of_sale/app/store/pos_hook";
//import { onMounted, useRef, useState } from "@odoo/owl";
//import { PartnerLine } from "@point_of_sale/app/screens/partner_list/partner_line/partner_line";
//import { PartnerDetailsEdit } from "@point_of_sale/app/screens/partner_list/partner_editor/partner_editor";
//import { _t } from "@web/core/l10n/translation";
//
//export class ProductCombosButton extends Component {
//    static template = 'custom_pos_screen.ProductCombosButton';
//
//    setup() {
//        this.orm = useService("orm");
//        this.pos = usePos();
//        this.state = useState({ locationText: _t("Location") });
//
//        this.onUpdateState(); // Call the method to set up the listener
//    }
//
//    onUpdateState() {
//        this.pos.on("change:selectedPartnerId", this.updateLocationText.bind(this));
//    }
//
//    async onClickShowTemp() {
//        if (!this.pos.get_order().partner) {
//            return;
//        }
//
//        try {
//            const result = await this.orm.call("pos.config", "get_locations", ['true'], {});
//            console.log(result);
//
//            // Assuming you want to update the locationText state here
//            this.state.locationText = result; // Update your state or use it as needed
//
//            this.pos.showScreen('ProductCombosScreen', {
//                data: result,
//            });
//        } catch (error) {
//            console.error("Error fetching locations:", error);
//        }
//    }
//
//    updateLocationText() {
//        // Handle updating location text based on selectedPartnerId change
//        const selectedPartnerId = this.pos.get("selectedPartnerId");
//        // Perform logic to update locationText based on selectedPartnerId
//        // For example:
//        this.state.locationText = `Location for Partner ${selectedPartnerId}`;
//    }
//}
//
//ProductScreen.addControlButton({
//    component: ProductCombosButton,
//    condition: () => true
//});


/* @odoo-module */

import { Component } from "@odoo/owl";
import { useService } from "@web/core/utils/hooks";
import { ProductScreen } from "@point_of_sale/app/screens/product_screen/product_screen";
import { usePos } from "@point_of_sale/app/store/pos_hook";
import { onMounted, useRef, useState } from "@odoo/owl";
import { PartnerLine } from "@point_of_sale/app/screens/partner_list/partner_line/partner_line";
import { PartnerDetailsEdit } from "@point_of_sale/app/screens/partner_list/partner_editor/partner_editor";
import { _t } from "@web/core/l10n/translation";

export class ProductCombosButton extends Component  {
static template = 'custom_pos_screen.ProductCombosButton';
    setup() {
        this.orm = useService("orm");
        this.pos = usePos();
//           this.state = useState({ locationText: _t("Location") });
    }
    async onClickShowTemp() {
      if(!(this.pos.get_order().partner)){
       return;
    }
       var self = this
       await this.orm.call("pos.config","get_locations",['true'],{}
       ).then(function(result) {
       console.log(result);
            self.pos.showScreen('ProductCombosScreen',{
                data: result,
            });
        });
    }
//    confirm() {
//        this.props.resolve({ confirmed: true, payload: this.state.selectedLocation });
//        this.pos.closeTempScreen();
//    }
}
ProductScreen.addControlButton({
    component: ProductCombosButton,
    condition: () => true
})



















///** @odoo-module */
//import { Component } from "@odoo/owl";
//import { ProductScreen } from "@point_of_sale/app/screens/product_screen/product_screen";
//import { usePos } from "@point_of_sale/app/store/pos_hook";
//export class ProductCombosButton extends Component {
//    static template = "custom_pos_screen.ProductCombosButton";
//    setup() {
//        this.pos = usePos();
//    }
//    async click() {
//
//        this.pos.showScreen("ProductCombosScreen");
//    }
//}
//ProductScreen.addControlButton({
//    component: ProductCombosButton,
//    condition: function () {
//        return true;
//    },
//});