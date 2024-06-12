/** @odoo-module **/
import {PlanningGanttController} from '@planning/views/planning_gantt/planning_gantt_controller';
import { patch } from "@web/core/utils/patch";
patch(PlanningGanttController.prototype, {

        setup() {
            super.setup();
        },
       async actionPlanning() {
  try {
    let date = new Date();
    alert("Hi");
    const usTime = date.toLocaleString("en-US", { timeZone: "America/New_York" });
    console.log(date);
    console.log(usTime);
  } catch (error) {
    console.log("Error:", error);
  }
}


    });
