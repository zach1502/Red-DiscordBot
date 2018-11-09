'''Press "F" to pay respects.'''
import asyncio
import random


class Respects: # pylint-disable=too-few-public-methods
    '''Press "F" to pay respects.'''
    def __init__(self, bot):
        self.bot = bot
    @commands.command(name="f", pass_context=True) # pylint-disable=too-few-public-methods
    async def mycom(self, ctx):
        '''Press "F" to pay respects.'''
        who_F = [] # pylint-disable=invalid-name
        who_F.append(ctx.message.author + ", ")
        hearts = ["💚", "💙", "💜", "💘", "🧡", "♥️", "💓", "💖", "💕", "💛", "💗", "💞", "💝", "❤️", "🖤"]
        await bot.say(who_F + "has paid their respects " + random.choice(hearts)) # pylint-disable=undefined-variable
    
    async def Helper(self, ctx):
        '''Apu Apustaja checks when latest invocation was'''
        
        
        #we`ll probably want a helper function to do some kind of a lookup to see when the latest invocation was
        #and if it exceeds, then we want a new "has paid respects", 
       #else append to the old one, delete the pre-existing "respects", 
        #and put a new one.
    
    
    
    
    
        who_F.clear()

# Set Down
def setup(bot):
    '''Setup.'''
    bot.add_cog(Respects(bot))
