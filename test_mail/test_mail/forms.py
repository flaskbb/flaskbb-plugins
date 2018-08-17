# -*- coding: utf-8 -*-
"""
    test_mail.forms
    ~~~~~~~~~~~~~~~

    This module contains the forms for the test mail Plugin.

    :copyright: (c) 2018 by Peter Justin.
    :license: BSD License, see LICENSE for more details.
"""
from flask_babelplus import lazy_gettext as _
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class TestMailForm(FlaskForm):
    email = StringField(
        _("Email"),
        validators=[DataRequired(message=_("Please enter a email address."))],
    )

    submit = SubmitField(_("Send"))
