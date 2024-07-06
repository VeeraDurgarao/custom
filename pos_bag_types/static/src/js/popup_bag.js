odoo.define('pos_bag_types.CarryBagButton', function(require) {
    'use strict';

    const PosComponent = require('point_of_sale.PosComponent');
    const ProductScreen = require('point_of_sale.ProductScreen');
    const { useListener } = require('web.custom_hooks');
    const Registries = require('point_of_sale.Registries');

    var models = require('point_of_sale.models');
    models.load_models({
            model:  'bag.charges',
            fields: [],
            domain: function (self) {
            return [['id', '=', self.config.bag_charges_ids]];
        },
            loaded: function(self,prod_cat){
                self.prod_cat = prod_cat;
        },
    });


    class CarryBagButton extends PosComponent {
        constructor() {
            super(...arguments);
            useListener('click', this.onClick);
        }
        async onClick() {
            let category = this.env.pos.prod_cat;
            if(category){
                let products = this.env.pos.prod_cat;
                console.log("productssssssssss",products)
                console.log("category",category)
                products.forEach(function(prd) {
                        prd['pos_bag_charges_img_url'] = window.location.origin + '/web/binary/image?model=bag.charges&field=image_medium&id=' + prd.id;
                    });
                    console.log("xxxxxxxxxxxxxxxxxxxxxxx",category)
                    this.showPopup('PosBagPopup', {'products': products});
                    console.log("xxxxxxxxxxxxxxxxxxxxxxx",category)
//                }
            }
        }
    }
    CarryBagButton.template = 'CarryBagButton';
    ProductScreen.addControlButton({
        component: CarryBagButton,
        condition: function() {
           return this.env.pos.config.bag_charges_ids;
        }
    });

    Registries.Component.add(CarryBagButton);

    return CarryBagButton;
});
