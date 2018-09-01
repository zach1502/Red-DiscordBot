"""importsss (that i don't know if it belongs here)

    you can get rid of excess comments"""
import random
import asyncio
from discord.ext import commands

class Guess: # pylint: disable=too-few-public-methods
    # fekkin pylint cogs/guess.py:9:19: C0303: Trailing whitespace (trailing-whitespace)
    # E0012: Bad option value 'too-few-public-methods fekkin pylint' (bad-option-value)
    # cogs/guess.py:8:0: R0903: Too few public methods (1/2) (too-few-public-methods)
    '''this is guessing game'''
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="guess", pass_context=True)
    async def mycom(self, context):
        '''pylint told me to do this, this will start a guessing game :aquaThumbsUp:'''
        # welcoming the user
        await self.bot.reply("guess what word I'm thinking of!")

        # thinking
        await asyncio.sleep(3)

        # start guess
        await self.bot.say("Start guessing...(hint: no caps)")
        await self.bot.say("you have 30 seconds to make a guess")
        await asyncio.sleep(0.5)

        # make secret
        secret = "its gonna change"

        # Probably need to create a word list and grab words from there
        items = ["here", "are", "some", "strings", "of", "which", "we", "will", "select", "one",
                 "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "python",
                 "ruby", "java", "javascript", "traceback", "print", "random", "input", "raw",
                 "print", "sleep", "time", "secret", "while", "then", "if", "loop", "in", "else",
                 "break", "empty", "mocha", "matcha", "money", "spam", "jazz", "jam", "spaz",
                 "binder", "jokes", "chemistry", "person", "matcha", "night", "everyone", "pasta",
                 "craving", "jolly", "ranch", "lit", "still", "first", "second", "third", "skull",
                 "ketchup", "ice", "red", "life", "death", "magic", "comments", "class", "secret",
                 "value", "variable", "guess", "incorrect", "russian", "roulette", "bot", "turn",
                 "failed", "wood", "stone", "cobblestone", "blanket", "ore", "chest", "poster",
                 "hash", "secure", "magical", "never", "public", "private", "key", "encryption",
                 "cypher", "cryptogram", "theory", "open", "thread", "ripper", "core", "graphical",
                 "graphics", "asymmetrical", "symmetrical"]
        # picks one word from list
        secret = random.choice(items)

        # creates a variable with an empty value
        guesses = ''
        turns = 5
        while turns > 0:
            failed = 0
            for char in secret:
                if char in guesses:
                    await self.bot.say(char)
                else:
                    await self.bot.say("_")
                    failed += 1
                #if failed is equal to zero
                # Win text
            if failed == 0:
                await self.bot.say("You won! Good job! :aquaThumbsUp:")
                # exit the script"""
                break
            # ask the user go guess a character"""
            await self.bot.say("lower case letters please~~!")
            guess = self.bot.wait_for_message(channel=context.message.channel)
            while not guess:
                await asyncio.sleep(30)
                await self.bot.say("I'm just going to assume you're gone...You think too slowly")
                break
            # add to the player(s) guess to guesses"""
            guesses += guess
            # incorrect letter"""
            if guess not in secret:
                turns -= 1
                await self.bot.say("Wrong")
                #if the turns equal to zero
                if turns == 0:
                    # losing text
                    await self.bot.say("You Lost, {0}  was the right word".format(secret))

                else:
                    # turns remaining text
                    await self.bot.say("You have {0} more guesses".format(turns))


# --------------------------------------------------------------------------------------------------
# # # Set-up # # # No U Pylint cogs/pylint.py:90:0: C0301: Line too long (101/100) (line-too-long)
# --------------------------------------Fekkin pylint-----------------------------------------------
def setup(bot):
    '''pylint also told me to do this'''
    bot.add_cog(Guess(bot))

# dab xd oof indents
