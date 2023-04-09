#!/usr/bin/python3
"""Run

"""

import asyncio
import random

from twitchio.ext import commands

import chat_events
from secrets_file import twitch_client_id, twitch_client_secret, twitch_chat_oauth_token

VEGETABLES = "🫒 🥑 🍆 🥕 🌽 🌶️ 🫑 🥒 🥬 🍄 🥚 🧂 🧀 🍅 🍳".split(" ")

class Bot(commands.Bot):

    def __init__(self):
        # Initialise our Bot with our access token, prefix and a list of channels to join on boot...
        # prefix can be a callable, which returns a list of strings or a string...
        # initial_channels can also be a callable which returns a list of strings...
        super().__init__(token=twitch_chat_oauth_token, prefix='!', initial_channels=['caitelatte'])

    async def event_ready(self):
        # Notify us when everything is ready!
        # We are logged in and ready to chat and use commands...
        print(f'Logged in as | {self.nick}')
        print(f'User id is | {self.user_id}')

    async def event_message(self, message):

        # Print the contents of our message to console...
        print(message.content)
        # Messages with echo set to True are messages sent by the bot...
        # For now we just want to ignore them...
        if message.echo:
            return

        # Since we have commands and are overriding the default `event_message`
        # We must let the bot know we want to handle and invoke our commands...
        await self.handle_commands(message)

    @commands.command()
    async def hello(self, ctx: commands.Context):
        # Here we have a command hello, we can invoke our command with our prefix and command name
        # e.g ?hello
        # We can also give our commands aliases (different names) to invoke with.

        # Send a hello back!
        # Sending a reply back to the channel is easy... Below is an example.
        print(dir(ctx))
        print(ctx.message)
        await ctx.send(f'Hello {ctx.author.name}!')

    @commands.command()
    async def sandwich(self, ctx: commands.Context, *requested_ingreds):
        """Given an optional list of ingredients, make a sandwich!"""
        sender = ctx.author.name
        ingredients = ["🍞"]
        if len(requested_ingreds) > 0:
            ingredients += list(requested_ingreds)
        else:
            ingredients += random.choices(VEGETABLES, k=random.randint(0,10))
        if len(ingredients) == 1:
            ingredients += "🧈"
        ingredients += "🍞"

        await ctx.reply(f'i made a sandwich for {sender}! {" ".join(ingredients)}')

    @commands.command()
    async def adventure(self, ctx: commands.Context, *adventure_input):
        """Run a random event for the user"""
        sender = ctx.author.name
        adventure_input = adventure_input

        randventure = random.choice(chat_adventures)
        print(f"event: {sender} gets random event {randventure._event_name} - {randventure._tags}")

        await ctx.reply(randventure._reply_message.format(ctx=ctx))

chat_adventures = chat_events.example_events()

bot = Bot()
bot.run()
# bot.run() is blocking and will stop execution of any below code here until stopped or closed.
