/////** @odoo-module **/
//import publicWidget from "@web/legacy/js/public/public_widget";
//import PortalSidebar from "@portal/js/portal_sidebar";
//
//PortalSidebar.include({
//    selector: ".o_portal_purchase_sidebar",
//
//    init: function (parent, options) {
//        try {
//            this._super.apply(this, arguments);
//            console.log("Custom functionality: PurchasePortalSidebar initialized");
//        } catch (error) {
//            console.error("An error occurred during initialization:", error);
//        }
//    },
//
//    start: function () {
//        try {
//            this.$el.css('background-color', '#a7abb0');
//            this.$el.css('border-radius', '15px');
//
//            let element = document.querySelector(".col-lg-3.col-xl-4.d-print-none");
//            let e1 = document.querySelector(".col-12.col-lg-9.col-xl-8.mt-5.mt-lg-0")
//            if (e1){
//            console.log("e1..........")
//              let button1 = document.createElement("button");
//                  button1.textContent = "Click Me";
//                  button1.style.backgroundColor = "#ffffff";
//                    button1.addEventListener('click', function(){
//                    alert("hi")
//                    })
//                e1.appendChild(button);
//                }
//            if (element) {
//                element.style.backgroundColor = '#186fdb';
//                element.style.borderTopLeftRadius = '15px';
//                element.style.borderBottomLeftRadius = '15px';
//                element.addEventListener('click', function(){
//                    alert("It's a Sidebar of Purchase Orders")
//                })
//                 let button = document.createElement("button");
//                  button.textContent = "Click Me";
//                  button.style.backgroundColor = "#ffffff";
//                    button.addEventListener('click', function(){
//                    alert("hi")
//                })
//                  element.appendChild(button);
//            } else {
//                console.warn("Element with class 'col-lg-3 col-xl-4 d-print-none' not found");
//            }
//        } catch (error) {
//            console.error("An error occurred during start:", error);
//        }
//    },
//});
//
////import publicWidget from "@web/legacy/js/public/public_widget";
////import PortalSidebar from "@portal/js/portal_sidebar";
////
////PortalSidebar.include({
////    selector: ".o_portal_purchase_sidebar",
////
////    init: function (parent, options) {
////        this._super.apply(this, arguments);
////        console.log("Custom functionality: PurchasePortalSidebar initialized");
////    },
////
////    start: function () {
////        this.$el.css('background-color', '#34ebcf');
////        this.$el.css('border-radius', '15px');
////
////        let element = document.querySelector(".col-lg-3.col-xl-4.d-print-none");
////        if (element) {
////            element.style.backgroundColor = '#d141bb';
////            element.style.borderTopLeftRadius = '15px';
////            element.style.borderBottomLeftRadius = '15px';
////            element.addEventListener('click', function(){
////                alert("It's a Sidebar of Purchase Orders")
////            })
//             let button = document.createElement("button");
//              button.textContent = "Click Me";
//              button.style.backgroundColor = "#ffffff";
//              element.appendChild(button);
////        } else {
////            console.warn("Element with class 'col-lg-3 col-xl-4 d-print-none' not found");
////        }
////    },
////});
/ @odoo-module /
import publicWidget from "@web/legacy/js/public/public_widget";
import PortalSidebar from "@portal/js/portal_sidebar";

PortalSidebar.include({
    selector: ".o_portal_purchase_sidebar",

    init: function (parent, options) {
        this._super.apply(this, arguments);
        console.log("Custom functionality: PurchasePortalSidebar initialized");
    },

    start: function () {
        this.$el.css('background-color', '#d7d2d7');
        this.$el.css('border-radius', '15px');

        let element = document.querySelector(".col-lg-3.col-xl-4.d-print-none");
        let element2 = document.querySelector(".col-12.col-lg-9.col-xl-8.mt-5.mt-lg-0");
        if (element) {
            element.style.backgroundColor = '#cdd0dc';
            element.style.borderTopLeftRadius = '15px';
            element.style.borderBottomLeftRadius = '15px';
            element.addEventListener('click', function(){
                alert("It's a Sidebar of Purchase Orders")
            })
        } else {
            console.warn("Element with class 'col-lg-3 col-xl-4 d-print-none' not found");
        }
        if (element2) {
            element2.style.backgroundColor = '#d141bb';
            let button = document.createElement("button");
              button.textContent = "Click Me";
              button.style.backgroundColor = "#ffffff";
              element2.appendChild(button);

        } else {
            console.warn("Element with class 'col-lg-3 col-xl-4 d-print-none' not found");
        }

//        let customer_support = document.getElementById('contact_us');
//        if(customer_support) {
//            customer_support.addEventListener('click',function(e){
//                alert("Customer Support Clicked");
//                e.stopPropagation();
//            })
//        }

//        this.$el.on('click', '#contact_us', function() {
//            window.location.href = '/contactus';
//        });
    },
});


