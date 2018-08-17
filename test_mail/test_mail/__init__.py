# -*- coding: utf-8 -*-
"""
    test_mail
    ~~~~~~~~~

    A test mail Plugin for FlaskBB.

    :copyright: (c) 2018 by Peter Justin.
    :license: BSD License, see LICENSE for more details.
"""
import os

from flask_babelplus import gettext as _
from pluggy import HookimplMarker

from flaskbb.display.navigation import NavigationLink

from .views import test_mail_bp

__version__ = "0.2.0"

hookimpl = HookimplMarker("flaskbb")


# connect the hooks
@hookimpl
def flaskbb_load_translations():
    return os.path.join(os.path.dirname(__file__), "translations")


@hookimpl
def flaskbb_load_blueprints(app):
    app.register_blueprint(test_mail_bp, url_prefix="/test-mail")


@hookimpl
def flaskbb_tpl_admin_settings_sidebar():
    return [
        NavigationLink(
            endpoint="test_mail_bp.send_mail", name=_("Test Send Mail")
        )
    ]
