'''Press "F" to pay respects'''
import asyncio
import discord

class Respects:
'''Press "F" to pay respects'''
    def __init__(self, bot):
        self.bot = bot
    @commands.command(name="f", pass_context=True) # pylint-disable=too-few-public-methods
    async def mycom(self, context):
        '''Press "F" to pay respects'''
        await bot.say(context.message.author + "hAs pAiD rEsPeCtS")

