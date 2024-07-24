/* @odoo-module */
import publicWidget from "@web/legacy/js/public/public_widget";

publicWidget.registry.popupWidget = publicWidget.Widget.extend({
    selector: '.card-body',
    start: function () {
        console.log('Custom Web page render using controller');
        this._super.apply(this, arguments);
        this._bindEvents();
    },

    _bindEvents: function () {
        this.$('.o_popup').on('click', this.open_popup.bind(this));
    },

      open_popup: function(){

       }

});
