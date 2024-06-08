/* @odoo-module */

import {WebsiteSale} from "@website_sale/js/website_sale";
//websitesale is the one of the publicWidget that widget w are imported in this pplace.
//By using include method i override the that particular widget apply some thigs in inside the function
//After that i perform some action.
WebsiteSale.include({
    events: Object.assign({}, WebsiteSale.prototype.events, {
        "change select[name='state_id']": "_onChangeState",
//       i only apply on the in this particular field that the reason i write inside the event.
    }),
    start: function () {
        this.autoStreetTwo = document.querySelector(".div_street2");
//        this it is like self and i give one variable and document.querySelector means all are taken leke class,heading,para
//        after that i give the class
        return this._super.apply(this, arguments);
    },
    _onChangeState: function () {
        console.log("Add the data")
//        whenever click the state button inside click any state it is automatically add the Hi durgarao in address field
        this.autoStreetTwo.querySelectorAll("input").forEach((input) => {
                                input.value = "Hi Durgarao";
                            });
    },
});
