# -*- coding: utf-8 -*-
"""
    conversations.utils
    ~~~~~~~~~~~~~~~~~~~

    This module contains some utils which are used by the
    conversations Plugin.

    :copyright: (c) 2018 by Peter Justin.
    :license: BSD License, see LICENSE for more details.
"""
from flaskbb.extensions import cache
from flaskbb.user.models import User

from .models import Conversation, Message


@cache.memoize()
def get_unread_count(user):
    """Returns the unread message count for the given user.

    :param user: The user object.
    """
    return Conversation.query.filter(
        Conversation.unread,
        Conversation.user_id == user.id
    ).count()


@cache.memoize()
def get_message_count(user):
    """Returns the number of private messages of the given user.

    :param user: The user object.
    """
    return Conversation.query.filter(
        Conversation.user_id == user.id,
        Conversation.id == Message.conversation_id).count()


@cache.memoize()
def get_unread_messages(user):
    """Returns all unread messages for the given user.

    :param user: The user object.
    """
    return Conversation.query.filter(
        Conversation.unread,
        User.id == user.user_id
    ).all()
