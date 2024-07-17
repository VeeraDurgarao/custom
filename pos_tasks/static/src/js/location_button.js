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
}
ProductScreen.addControlButton({
    component: ProductCombosButton,
    condition: () => true
})
