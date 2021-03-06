# -*- encoding: utf-8 -*-
##############################################################################
#    
#    Odoo, Open Source Management Solution
#
#    Author: Andrius LaukaviÄius. Copyright: JSC NOD Baltic
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.     
#
##############################################################################
from odoo import models, fields, api
from odoo.exceptions import Warning
from odoo.tools.translate import _

class sale_order(models.Model):
    _inherit = 'sale.order'

    calendar_service_id = fields.Many2one('calendar.service', 'Calendar Service')

    @api.one
    def action_button_confirm(self):
        """
        Prevents completing sale order, if related
        calendar service is not finished yet.
        """
        if self.calendar_service_id and self.calendar_service_id.state != 'done':
            raise Warning(_("Related Calendar Service with No. %s is not in Done State!" % \
                (self.calendar_service_id.name)))
        return super(sale_order, self).action_button_confirm()
