'''pylint told me to put something here'''
from random import randint, sample
from discord.ext import commands

ZALGO_DEFAULT_AMT = 3
ZALGO_MAX_AMT = 7

ZALGO_PARAMS = {
    'above': (5, 10),
    'below': (5, 10),
    'overlay': (0, 2)
}

ZALGO_CHARS = {
    'above': ['\u0300', '\u0301', '\u0302', '\u0303', '\u0304', '\u0305', '\u0306', '\u0307', '\u0308', # pylint: disable=line-too-long
              '\u0309', '\u030A', '\u030B', '\u030C', '\u030D', '\u030E', '\u030F', '\u0310', '\u0311', # pylint: disable=line-too-long
              '\u0312', '\u0313', '\u0314', '\u0315', '\u031A', '\u031B', '\u033D', '\u033E', '\u033F', # pylint: disable=line-too-long
              '\u0340', '\u0341', '\u0342', '\u0343', '\u0344', '\u0346', '\u034A', '\u034B', '\u034C', # pylint: disable=line-too-long
              '\u0350', '\u0351', '\u0352', '\u0357', '\u0358', '\u035B', '\u035D', '\u035E', '\u0360', # pylint: disable=line-too-long
              '\u0361'],
    'below': ['\u0316', '\u0317', '\u0318', '\u0319', '\u031C', '\u031D', '\u031E', '\u031F', '\u0320', # pylint: disable=line-too-long
              '\u0321', '\u0322', '\u0323', '\u0324', '\u0325', '\u0326', '\u0327', '\u0328', '\u0329', # pylint: disable=line-too-long
              '\u032A', '\u032B', '\u032C', '\u032D', '\u032E', '\u032F', '\u0330', '\u0331', '\u0332', # pylint: disable=line-too-long
              '\u0333', '\u0339', '\u033A', '\u033B', '\u033C', '\u0345', '\u0347', '\u0348', '\u0349', # pylint: disable=line-too-long
              '\u034D', '\u034E', '\u0353', '\u0354', '\u0355', '\u0356', '\u0359', '\u035A', '\u035C', # pylint: disable=line-too-long
              '\u035F', '\u0362'],
    'overlay': ['\u0334', '\u0335', '\u0336', '\u0337', '\u0338']
}

class Zalgo:
    '''pylint told me to do this'''
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def zalgo(self, *, text: str):
        '''pylint told me to do this, This will "zalgofy" your text :aquaThumbsUp:'''
        if len(text) >= 1000:
            await self.bot.say("You know, Discord has a limit of 2k characters, you just exceeded half of that, keep it shorter please") # pylint: disable=line-too-long
        else:
            fw = text.split()[0] # pylint: disable=invalid-name
            try:
                amount = min(int(fw), ZALGO_MAX_AMT) # pylint: disable=invalid-name
                text = text[len(fw):].strip() # pylint: disable=invalid-name
            except ValueError:
                amount = ZALGO_DEFAULT_AMT
            text = self.zalgoify(text.upper(), amount)
            await self.bot.say(text)

    def zalgoify(self, text, amount=3):
        '''do i really need a docstring here pylint?'''
        zalgo_text = '' # pylint: disable=invalid-name
        for c in text: # pylint: disable=invalid-name
            zalgo_text += c # pylint: disable=invalid-name
            if c != ' ': # pylint: disable=invalid-name
                for t, range in ZALGO_PARAMS.items(): # pylint: disable=invalid-name
                    range = (round(x*amount/5) for x in range)
                    n = min(randint(*range), len(ZALGO_CHARS[t])) # pylint: disable=invalid-name
                    zalgo_text += ''.join(sample(ZALGO_CHARS[t], n)) # pylint: disable=invalid-name
        return zalgo_text

def setup(bot):
    '''do I really need a Docstring here?'''
    n = Zalgo(bot) # pylint: disable=invalid-name
    bot.add_cog(n)
    #fekkin pylint btw what is CamelCase :thonk:
