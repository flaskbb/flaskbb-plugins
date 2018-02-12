# -*- coding: utf-8 -*-
"""
    conversations
    ~~~~~~~~~~~~~

    A conversations Plugin for FlaskBB.

    :copyright: (c) 2018 by Peter Justin.
    :license: BSD License, see LICENSE for more details.
"""
import os
from flaskbb.forum.models import Forum
from flaskbb.utils.helpers import render_template
from flaskbb.utils.forms import SettingValueType

from .views import conversations_bp


__version__ = "0.1.0"


# connect the hooks
def flaskbb_load_migrations():
    return os.path.join(os.path.dirname(__file__), "migrations")


def flaskbb_load_translations():
    return os.path.join(os.path.dirname(__file__), "translations")


def flaskbb_load_blueprints(app):
    app.register_blueprint(conversations_bp, url_prefix="/conversations")


def flaskbb_tpl_before_navigation():
    return render_template("conversations_navlink.html")


# plugin settings
SETTINGS = {
    "foobar": {
        "value": 10,
        "value_type": SettingValueType.integer,
        "name": "Foobar Number",
        "description": "The number of foo in bars.",
        "extra": {"min": 1},
    },
}
