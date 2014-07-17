# -*- coding: utf-8 -*-
##############################################################################
#
#    Add Bank Sort Code to banks in Odoo.
#    Copyright (C) 2014 Opus Vision Limited (<http://opusvl.com>).
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


{
    'name': 'Sort Code for Bank Account',
    'version': '0.1',
    'category': 'Accounting & Finance',
    'summary': 'Add sort code field to banks',
    'description': """Adds a Sort Code field to the res.partner.bank model""",
    'author': 'OpusVL',
    'website': 'http://opusvl.com',
    'depends': ['base'],
    'data': [
        'res_partner_bank_extension_view.xml',
    ],
    'demo': [],
    'test': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
