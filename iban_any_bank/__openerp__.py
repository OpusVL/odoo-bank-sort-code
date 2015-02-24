# -*- coding: utf-8 -*-

##############################################################################
#
# IBAN Field for any bank
# Copyright (C) 2015 OpusVL (<http://opusvl.com/>)
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################


{
    'name': 'IBAN Field for any bank',
    'version': '0.1',
    'author': 'OpusVL',
    'website': 'http://opusvl.com/',
    'summary': 'Add explicit IBAN field on banks, so account number and IBAN number need not be mutually exclusive',
    
    'category': 'Accounting & Finance',
    
    'description': """Add explicit IBAN field on banks, so account number and IBAN number need not be mutually exclusive,
""",
    'images': [
    ],
    'depends': [
        'base',
    ],
    'data': [
        'bank.xml',
    ],
    'demo': [
    ],
    'test': [
    ],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,

}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
