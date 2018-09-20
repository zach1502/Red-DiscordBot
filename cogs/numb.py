'''This is a guess the number game'''
import random
import asyncio
from discord.ext import commands


GuessesTaken = 0

class Guess:
	'''this is a number guessing game'''
	def __init__(self, bot):
		self.bot = bot
	@commands.command(name="numguess", pass_context=True)
	async def mycom(self, context):
		'''this will start a number guessing game'''

		await self.bot.reply("how hard would you like the number game to be? easy/med/hard")
		mode = self.bot.wait_for_message(channel=context.message.channel, timeout=30)
		if mode = 'easy':
			number = random.randint(1, 10)

		elif mode = 'med':
			number = random.randint(1,50)

		elif mode = 'hard':
			number = random.randint(1,100)

		#easter egg
		elif mode = 'no u:
			number = randome.randint(1,420)
			await self.bot.say('no u')

		else:
			await self.bot.say('type again')
			return

		await self.bot.say('I am thinking of a number between 1 and 100.')
		while guessesTaken != 5:

  			await self.bot.say('Take a guess.')
  			guess = self.bot.wait_for_message(channel=context.message.channel, timeout 30)
  			if not guess:
  				await self.bot.say('you think too slowly, imma just leave now')
  				return
  			
  			guess = int(guess)
  			guessesTaken = guessesTaken + 1

  			if guess < number:
    			print('Your guess is too low.')

  			if guess > number:
    			print('Your guess is too high.')
    		
  			if guess == number:
    			break
    		
		if guess == number:
			guessesTaken = str(guessesTaken)
			print('Good job! You guessed my number in ' + guessesTaken + ' guesses!')
		if guess != number:
  			number = str(number)
  			print('Nope. The number I was thinking of was ' + number)
