# -*- coding: utf-8 -*-
"""
    test_mail
    ~~~~~~~~~

    A test mail Plugin for FlaskBB.

    :copyright: (c) 2018 by Peter Justin.
    :license: BSD License, see LICENSE for more details.
"""
import os

from .views import test_mail_bp


__version__ = "0.1.0"


# connect the hooks
def flaskbb_load_translations():
    return os.path.join(os.path.dirname(__file__), "translations")


def flaskbb_load_blueprints(app):
    app.register_blueprint(test_mail_bp, url_prefix="/test-mail")
