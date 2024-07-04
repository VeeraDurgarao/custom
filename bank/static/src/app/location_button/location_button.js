/* @odoo-module */

import { Component } from "@odoo/owl";
import { useService } from "@web/core/utils/hooks";
import { ProductScreen } from "@point_of_sale/app/screens/product_screen/product_screen";
import { usePos } from "@point_of_sale/app/store/pos_hook";
import { onMounted, useRef, useState } from "@odoo/owl";
import { PartnerLine } from "@point_of_sale/app/screens/partner_list/partner_line/partner_line";
import { PartnerDetailsEdit } from "@point_of_sale/app/screens/partner_list/partner_editor/partner_editor";

export class ProductCombosButton extends Component  {
static template = 'custom_pos_screen.ProductCombosButton';
    setup() {
        this.orm = useService("orm");
        this.pos = usePos();
//        this.state = useState({ selectedLocation: this.props.location});
    }
    async onClickShowTemp() {
      if(!(this.pos.get_order().partner)){
       return;
    }
       var self = this
       //connection.py python file using
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