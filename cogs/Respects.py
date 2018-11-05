'''Press "F" to pay respects.'''
import asyncio
import random


class Respects:
    '''Press "F" to pay respects.'''
    def __init__(self, bot):
        self.bot = bot
    @commands.command(name="f", pass_context=True) # pylint-disable=too-few-public-methods
    async def mycom(self, ctx):
        '''Press "F" to pay respects.'''
        who_F = []
        who_F.append(ctx + ", ")
        hearts = ["💚", "💙", "💜", "💘", "🧡", "♥️", "💓", "💖", "💕", "💛", "💗", "💞", "💝", "❤️", "🖤"]
        await bot.say(who_F + "has paid their respects " + random.choice(hearts))

        await asyncio.sleep(10)
        who_F.clear()

# Set Down
def setup(bot):
    '''Setup.'''
    bot.add_cog(Respects(bot))
