//
//
//
//
//
//
//
//
//
//
//
///** @odoo-module **/
//
//import { _t } from "@web/core/l10n/translation";
//import { ProductScreen } from "@point_of_sale/app/screens/product_screen/product_screen";
//import { useService } from "@web/core/utils/hooks";
//import { Component } from "@odoo/owl";
//import { usePos } from "@point_of_sale/app/store/pos_hook";
//import { BookOrderPopup } from "./BookOrderPopup";
//import { ErrorPopup } from "@point_of_sale/app/errors/popups/error_popup";
//
//
//export class BookDurgarao extends Component {
//    static template = "pos_book_order.Durgarao";
//    setup() {
//        this.pos = usePos();
//        this.popup = useService("popup");
//    }
//    async onClick() {
//            this.pos.popup.add(ErrorPopup, {
//                    title: _t("Please Select the Customer"),
//                    body: _t(
//                        "You need to select a customer for using this option"
//                    ),
//                });
//        }
//    }
//
//
//ProductScreen.addControlButton({
//    component: BookDurgarao,
//    condition: function () {
//        return this.pos.config.enable;
//    },
//});












///* @odoo-module */
//
//import {WebsiteSale} from "@website_sale/js/website_sale";
////websitesale is the one of the publicWidget that widget we are imported in this place.
////By using include method i override the that particular widget apply some things in inside the function
////After that i perform some action.
//WebsiteSale.include({
//    events: Object.assign({}, WebsiteSale.prototype.events, {
//        "change select[name='state_id']": "_onChangeState",
////       i only apply on the in this particular field that the reason i write inside the event.
//    }),
//    start: function () {
//        this.autoStreetTwo = document.querySelector(".div_street2");
////        this it is like self and i give one variable and document.querySelector means all html content is taken
////        after that i give the class inside methods
//        return this._super.apply(this, arguments);
//    },
//
//    _onChangeState: function () {
//        console.log("Add the data")
//
////        whenever click the state button inside click any state it is automatically add the Hi durgarao in address field
//        this.autoStreetTwo.querySelectorAll("input").forEach((input) => {
//                                input.value = "Hi Durgarao";
//                            });
//    },
//});
