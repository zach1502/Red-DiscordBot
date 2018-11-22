'''Press "F" to pay respects.'''
import time
import asyncio
import random
import discord


class Respects: # pylint-disable=too-few-public-methods
    '''Press "F" to pay respects.'''
    def __init__(self, bot):
        self.bot = bot
    @commands.command(name="f", pass_context=True) # pylint-disable=too-few-public-methods
    async def mycom(self, ctx):
        '''Press "F" to pay respects.'''
        who_F.append(ctx.message.author + ", ")
        hearts = ["💚", "💙", "💜", "💘", "🧡", "♥️", "💓", "💖", "💕", "💛", "💗", "💞", "💝", "❤️", "🖤"]
        await bot.say(who_F + "has paid their respects " + random.choice(hearts)) # pylint-disable=undefined-variable
    
    async def Helper(ctx, channel: discord.channel):
        '''Apu Apustaja checks when latest invocation was.'''
        Initial_Time = time.time()
        Get_Context = (get_message(channel, id))
        if Get_Context == None: # in a dilima, hold on letme get my ti84
            who_F.append(ctx.message.author)
        else:
            who_F = []
            Get_Context = (get_message(channel, id))

#If there was no invocation, just send the message with who has paid respects 
#AND save the message ID, and save who has paid respects, the message ID, and the invocation time to the lookup.

#If there was, check the time, and see if it's within a threshold (you determine). 
#If the time has passed, create a new one.
#Else just delete the previous message and make a new one in the same manner as above.


# Set Down
def setup(bot):
    '''Setup.'''
    bot.add_cog(Respects(bot))
