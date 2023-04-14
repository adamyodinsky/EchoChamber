"""Main module for the Echo Chamber Discord bot."""

import os
import random
import time

from discord import Intents
from discord.ext import commands
from echochamber.llm import (exceeding_token_limit, get_user_answer,
                 num_tokens_from_messages, reduce_tokens)
from echochamber.personalities import personalities_map

messages = [
    {"role": "system", "content": personalities_map[os.environ.get("PERSONALITY")]}
]

intents = Intents.default()
intents.typing = True
intents.presences = True
intents.messages = True
intents.guilds = True

# Create a new bot instance with intents
bot = commands.Bot(command_prefix="/bee", intents=intents, help_command=None)


# Event that echoes messages
@bot.event
async def on_message(message):
    """Event that echoes messages."""

    global messages
    # Ignore messages sent by the bot itself
    if message.author == bot.user:
        return

    if message.content == "":
        message = await message.channel.fetch_message(message.id)
    if message.content == "":
        return
    # Process commands before sending the message content back to the user
    await bot.process_commands(message)

    sleep_time = float(os.environ.get("SLEEP_TIME", random.uniform(10, 20)))
    time.sleep(sleep_time)

    async with message.channel.typing():
        # Get the messages from the channel
        messages.append({"role": "user", "content": message.content})
        total_usage = num_tokens_from_messages(messages)

        # Prevent reaching tokens limit
        if exceeding_token_limit(total_usage, 3072):
            messages, total_usage = reduce_tokens(
                messages=messages,
                total_usage=total_usage,
                token_limit=3072,
            )

        try:
            # Get the answer from OpenAI API and append it to the messages list
            answer = get_user_answer(messages)
            message.content = answer["choices"][0]["message"]["content"]

            # Send the message content back to the user
            await message.channel.send(message.content)
            messages.append({"role": "assistant", "content": message.content})
        except Exception as error:
            print(str(error))
            await message.channel.send("I'm sorry, I can't say that.")

# Event that prints the bot is ready when it starts up
@bot.event
async def on_ready():
    """Event that prints the bot is ready when it starts up."""        
    print(f"{bot.user} has connected to Discord!")


# Run the bot with your token
bot.run(os.environ.get("DISCORD_BOT_TOKEN"))
