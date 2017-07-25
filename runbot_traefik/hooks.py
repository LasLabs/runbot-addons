# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).


def post_init_hook(cr, registry):
    cr.execute('UPDATE runbot_build SET _host = host');


def uninstall_hook(cr, registry):
    cr.execute('UPDATE runbot_build SET host = _host');
