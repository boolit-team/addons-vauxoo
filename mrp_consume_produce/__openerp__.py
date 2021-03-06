# coding: utf-8
###########################################################################
#    Module Writen to OpenERP, Open Source Management Solution
#
#    Copyright (c) 2012 Vauxoo - http://www.vauxoo.com
#    All Rights Reserved.
#    info@vauxoo.com
############################################################################
#    Coded by: julio (julio@vauxoo.com)
############################################################################
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
# use this command
{
    "name": "MRP Consume Produce",
    "version": "1.6",
    "author": "Vauxoo",
    "category": "Generic Modules/Production",
    "website": "http://www.vauxoo.com/",
    "license": "",
    "depends": [
        "mrp",
        "mrp_button_box"
    ],
    "demo": [],
    "data": [
        "wizard/wizard_view.xml",
        "mrp_consume_produce_view.xml",
        "security/mrp_security.xml",
        "security/ir.model.access.csv",
        "res_config_view.xml"
    ],
    "test": [],
    "js": [],
    "css": [],
    "qweb": [],
    "installable": True,
    "auto_install": False,
}
