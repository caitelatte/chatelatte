#!/usr/bin/python3
"""Create random events that can be called by a twitch command.

Class ChatEvents:
  * event_name: what it'll be called internally or in recall commands
  * call_func: function to override for the event to happen
  * tags: tags to help categorise events (eg cooking, conversation, fight)

user: !event
bot: oh no! {user} ran into a door! respond with 1 to try open the door, or 2 to smash the door


"""

import typing

from twitchio.ext import commands


class ChatEvent:
    """An event that will be called by a twitch bot.
    """
    def __init__(self, event_name: str, reply_message: str, tags=[]) -> None:
        # in the future: there will be more complex events
        # eg: callback_handlers
        self._event_name = event_name
        self._reply_message = reply_message
        self._tags = tags

def example_events():
    """Create a list of example ChatEvents."""
    created_events = []

    # Stub toe
    created_events.append(ChatEvent(
        "stubToe",
        "oops, {ctx.author.name} stubbed their toe!",
        tags=["accident"]
    ))
    # 
    created_events.append(ChatEvent(
        "foundCordial",
        "ahhh, {ctx.author.name} found a lovely cordial, flavoured like fruit tinglers!",
        tags=["food"]
    ))
    return created_events

