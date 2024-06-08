/** @odoo-module **/
import { patch } from "@web/core/utils/patch";
import { ExpenseListController } from '@hr_expense/views/list';
patch(ExpenseListController.prototype, {

        setup() {
            super.setup();
        },
        async actionHrList() {
            const records = this.model.root.selection;
            const recordIds = records.map((a) => a.resId);
            console.log(typeof records)
            for (let key in records){
            console.log("keys and val" + key+ ":" +records[key].data.name)

            }
            console.log(records)
            console.log(recordIds)
            },
    });
