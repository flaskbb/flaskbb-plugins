# -*- coding: utf-8 -*-
"""
    test_mail.tasks
    ~~~~~~~~~~~~~~~

    This module contains the tasks for the test mail Plugin.

    :copyright: (c) 2018 by Peter Justin.
    :license: BSD License, see LICENSE for more details.
"""
from flask import render_template_string
from flask_babelplus import gettext as _

from flaskbb.email import send_email
from flaskbb.extensions import celery


@celery.task
def send_test_mail(email, user):
    """Sends the activation token to the user's email address.

    :param user: The user object to whom the email should be sent.
    """
    body = render_template_string("Test mail sent by {{ user }}.", user=user)
    send_email(
        subject=_("Test Send Mail"),
        recipients=[email],
        text_body=body,
        html_body=body,
    )
