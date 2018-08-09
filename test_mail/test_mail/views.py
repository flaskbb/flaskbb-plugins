# -*- coding: utf-8 -*-
"""
    test_mail.views
    ~~~~~~~~~~~~~~~

    This module contains the views for the test mail Plugin.

    :copyright: (c) 2018 by Peter Justin.
    :license: BSD License, see LICENSE for more details.
"""
from flask import Blueprint, flash, redirect, url_for
from flask_babelplus import gettext as _
from flask_login import current_user

from flaskbb.extensions import allows
from flaskbb.utils.requirements import IsAdmin
from flaskbb.utils.helpers import render_template

from .forms import TestMailForm
from .tasks import send_test_mail


test_mail_bp = Blueprint("test_mail_bp", __name__, template_folder="templates")


@allows.requires(IsAdmin)
@test_mail_bp.route("/send", methods=["GET", "POST"])
def send_mail():
    form = TestMailForm()
    if form.validate_on_submit():
        send_test_mail.delay(form.email.data, current_user.username)
        flash(_("Mail sent to %(email)s", email=form.email.data), "success")
        return redirect(url_for("test_mail_bp.send_mail"))
    return render_template("test_mail.html", form=form)
