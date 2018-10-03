'''This is a guess the number game.'''
import random
from discord.ext import commands


class NumbGuess:  # pylint: disable=too-few-public-methods
    '''This is a number guessing game.'''
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="numguess", pass_context=True)
    async def mycom(self, context):  # pylint: disable=too-many-statements,too-many-branches
        '''This will start a number guessing game.'''
        guessesTaken = 0
        await self.bot.say('How hard would you like the number game to be? (easy/mid/hard)')
        mode = self.bot.wait_for_message(channel=context.message.channel, timeout=30)

        if mode == 'easy':
            number = random.randint(1, 10)

        elif mode == 'mid':
            number = random.randint(1, 50)

        elif mode == 'hard':
            number = random.randint(1, 100)

        #easter egg in honor of rennou, 172 uses before removal, number 1 most used rencc
        elif mode == 'no u':
            number = random.randint(1, 420)
            await self.bot.say('no u')

        elif mode is None:
            await self.bot.say('you think too despacito, I am going to leave now...')

        else:
            await self.bot.say('type again')
            mode = self.bot.wait_for_message(channel=context.message.channel, timeout=30)

        while True:
            try:
                if mode != 'easy' or 'mid' or 'hard' or 'no u':
                    raise ValueError
            except ValueError:
                await self.bot.say('type again')
                mode = self.bot.wait_for_message(channel=context.message.channel, timeout=30)
                continue
            else:
                break

        await self.bot.say('I am thinking of a number between 1 and 100. You have 30 seconds.')
        while guessesTaken != 5:
            await self.bot.say('Take a guess.')
            guess = self.bot.wait_for_message(channel=context.message.channel, timeout=30)

            if not guess:
                await self.bot.say('you think too despacito, I am going to leave now...')
                return

            while True:
                try:
                    guess = int(guess)
                except ValueError:
                    await self.bot.say("That's not a number, type in a number please")
                    guess = self.bot.wait_for_message(channel=context.message.channel, timeout=30)
                    continue
                else:
                    break

            guessesTaken += guessesTaken

            if guess < number:
                await self.bot.say('Your guess is too low.')

            if guess > number:
                await self.bot.say('Your guess is too high.')

            if guess == number:
                return

        if guess == number:
            await self.bot.say('Good job! You guessed my number in ' + str(guessesTaken) + ' guesses!')     

        if guess != number:
            await self.bot.say('Nope. The number I was thinking of was ' + str(number))


#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
#-  _________       __   ____ ___           #
#- /   _____/ _____/  |_|    |   \______    # Ascii Art Haiku:
#- \_____  \_/ __ \   __\    |   /\____ \   #
#- /        \  ___/|  | |    |  / |  |_> |  # "Ascii art is fun
#-/_______  /\___  >__| |______/  |   __/   # I spend too much time on this
#-        \/     \/               |__|      # but it's very fun"
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#        -zach1502

def setup(bot):
    '''Setup.'''
    bot.add_cog(NumbGuess(bot))
