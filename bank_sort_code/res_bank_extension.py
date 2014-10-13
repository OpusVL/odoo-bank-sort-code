# -*- coding: utf-8 -*-
##############################################################################
#
# Add Bank Sort Code to banks in Odoo.
# Copyright (C) 2014 OpusVL
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# If you require assistance, support, or further development of this
# software, please contact OpusVL using the details below:
#
# Telephone: +44 (0)1788 298 410
# Email: community@opusvl.com
# Web: http://opusvl.com
#
##############################################################################

from openerp.osv import osv, fields

class res_bank_extension(osv.osv):
    _inherit = 'res.bank'

    _columns = {
        'sort_code': fields.char('Sort Code', help='e.g. 99-99-99'),
    }


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
