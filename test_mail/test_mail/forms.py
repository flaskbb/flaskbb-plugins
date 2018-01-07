# -*- coding: utf-8 -*-
"""
    flaskbb.management.forms
    ~~~~~~~~~~~~~~~~~~~~~~~~

    It provides the forms that are needed for the management views.

    :copyright: (c) 2014 by the FlaskBB Team.
    :license: BSD, see LICENSE for more details.
"""
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

from flask_babelplus import lazy_gettext as _


class TestMailForm(FlaskForm):
    email = StringField(_("Email"), validators=[
        DataRequired(message=_("Please enter a email address."))])

    submit = SubmitField(_("Send"))
