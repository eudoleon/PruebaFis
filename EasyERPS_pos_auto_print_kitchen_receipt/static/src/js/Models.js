odoo.define('EasyERPS_pos_auto_print_kitchen_receipt.Models', function (require) {
"use strict";

    const { PosGlobalState, Order, Orderline, Payment } = require('point_of_sale.models');
    const Registries = require('point_of_sale.Registries');
    var utils = require('web.utils');
    var core = require('web.core');
    var QWeb = core.qweb;


    const PosOrder = (Order) => class PosOrder extends Order {
        async printChanges(){
            var printers = this.pos.printers;
            var order = this.pos.get_order();
            let isPrintSuccessful = true;
            for(var i = 0; i < printers.length; i++){
                var changes = this.computeChanges(printers[i].config.product_categories_ids);
                if ( changes['new'].length > 0 || changes['cancelled'].length > 0){
                    var receipt = QWeb.render('OrderChangeReceipt',{changes:changes, widget:this, pos: this.pos, receipt: order.export_for_printing()});
                    const result = await printers[i].print_receipt(receipt);
                    if (!result.successful) {
                        isPrintSuccessful = false;
                    }
                }
            }
            return isPrintSuccessful;
        }
    }

    Registries.Model.extend(Order, PosOrder);
});