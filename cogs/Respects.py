'''Press "F" to pay respects'''
import asyncio
import discord
import random
import logging


class Respects:
    '''Press "F" to pay respects'''
    def __init__(self, bot, argument):
        self.bot = bot
    @commands.command(name="f", pass_context=True) # pylint-disable=too-few-public-methods
    async def mycom(self, ctx, member : discord.Member):
        '''Press "F" to pay respects'''
        hearts = ["💚", "💙", "💜", "💘", "🧡", "♥️", "💓", "💖", "💕", "💛", "💗", "💞", "💝", "❤️", "🖤"]
        await bot.say({0} + "has paid their respects " + random.choice(hearts).format(ctx))
