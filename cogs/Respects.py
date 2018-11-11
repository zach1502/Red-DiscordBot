'''Press "F" to pay respects.'''
import time
import asyncio
import random


class Respects: # pylint-disable=too-few-public-methods
    '''Press "F" to pay respects.'''
    def __init__(self, bot):
        self.bot = bot
    @commands.command(name="f", pass_context=True) # pylint-disable=too-few-public-methods
    async def mycom(self, ctx):
        '''Press "F" to pay respects.'''
        Initial_Time = time.time()
        Delta_Time = time.time() - Initial_Time
        who_F = [] # pylint-disable=invalid-name

        who_F.append(ctx.message.author + ", ")
        hearts = ["💚", "💙", "💜", "💘", "🧡", "♥️", "💓", "💖", "💕", "💛", "💗", "💞", "💝", "❤️", "🖤"]
        await bot.say(who_F + "has paid their respects " + random.choice(hearts)) # pylint-disable=undefined-variable
    
    async def Helper(self, ctx):
        '''Apu Apustaja checks when latest invocation was.'''
        while Delta_Time < 10:
            Delta_Time = time.time() - Initial_Time
        while Delta_Time > 10:
            who_F = []

        #we`ll probably want a helper function to do some kind of a lookup to see when the latest invocation was
        #and if it exceeds, then we want a new "has paid respects", 
       #else append to the old one, delete the pre-existing "respects", 
        #and put a new one.


# Set Down
def setup(bot):
    '''Setup.'''
    bot.add_cog(Respects(bot))
