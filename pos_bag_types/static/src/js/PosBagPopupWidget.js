odoo.define('pos_bag_types.PosBagPopup', function(require) {
    "use strict";

    const Popup = require('point_of_sale.ConfirmPopup');
    const Registries = require('point_of_sale.Registries');
    const PosComponent = require('point_of_sale.PosComponent');

    class PosBagPopup extends Popup {

        constructor() {
            super(...arguments);
        }

         go_back_screen() {
            this.showScreen('ProductScreen');
            this.trigger('close-popup');
        }


        //Props-stands for properties(a special keyword).
        //They are used for passing data from one component to another component.(parent->child)
        get bags() {
            let bags = [];
            $.each(this.props.products, function( i, prd ){
                prd['pos_bag_charges_img_url'] = `/web/image?model=bag.charges&field=image_1920&id=${prd.id}&write_date=${prd.write_date}&unique=1`;
                bags.push(prd)
            });
            return bags;
        }

        //currentTarget event property returns the element whose event listeners triggered the event.
        //This is particularly useful during capturing and bubbling.
        click_on_bag_product(event) {
            var self = this;
            var bag_id = parseInt(event.currentTarget.dataset['productId'])//productId: orderline.product.id
            print("=================")
            self.env.pos.get_order().add_product(self.env.pos.config.bag_charges_ids[bag_id]);
            self.trigger('close-popup');
        }



    };
    
    PosBagPopup.template = 'PosBagPopup';
    Registries.Component.add(PosBagPopup);
    return PosBagPopup;
});