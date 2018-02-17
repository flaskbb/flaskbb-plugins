# -*- coding: utf-8 -*-
"""
    conversations
    ~~~~~~~~~~~~~

    A conversations Plugin for FlaskBB.

    :copyright: (c) 2018 by Peter Justin.
    :license: BSD License, see LICENSE for more details.
"""
import os

from pluggy import HookimplMarker

from flaskbb.utils.helpers import render_template

from .views import conversations_bp
from .utils import get_unread_count, get_unread_messages


__version__ = "0.1.0"


hookimpl = HookimplMarker("flaskbb")


# connect the hooks
def flaskbb_load_migrations():
    return os.path.join(os.path.dirname(__file__), "migrations")


def flaskbb_load_translations():
    return os.path.join(os.path.dirname(__file__), "translations")


def flaskbb_load_blueprints(app):
    app.register_blueprint(conversations_bp, url_prefix="/conversations")


def flaskbb_tpl_before_user_nav_loggedin():
    return render_template("_inject_navlink.html")


@hookimpl(trylast=True)
def flaskbb_tpl_profile_sidebar_stats(user):
    return render_template("_inject_new_message_button.html", user=user)


@hookimpl(trylast=True)
def flaskbb_tpl_after_post_author_info(user):
    return render_template("_inject_new_message_link.html", user=user)


def flaskbb_current_user_loader(user):
    user.unread_count = get_unread_count(user)
    user.unread_messages = get_unread_messages(user)
