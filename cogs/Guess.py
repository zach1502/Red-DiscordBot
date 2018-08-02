"""importsss (that i don't know if it belongs here)"""

"""you can get rid of excess comments"""
import time
import random
from discord.ext import commands
from random import choice
from .utils.dataIO import dataIO
from .utils import checks
from .utils.chat_formatting import box
from collections import Counter, defaultdict, namedtuple
import discord
import os
import asyncio
import chardet
"""Guessing game """
class Guess:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="guess")
    async def mycom(self):
        """welcoming the user"""
        await self.bot.reply("guess what word I'm thinking of!")

        """thinking"""
        await asyncio.sleep(3)

        """start guess"""
        await self.bot.say("Start guessing...(hint: no caps/")
        await asyncio.sleep(0.5)

        #make secret
        secret = "its gonna change"

        #Probably need to create a word list and grab words from there
        items = ["here", "are", "some", "strings", "of","which", "we", "will", 
         "select", "one", "two", "three", "four", "five", "six", 
         "seven", "eight", "nine", "ten", "python", "ruby", "java", "javascript", "traceback", "print", 
         "random", "input", "raw", "print", "sleep", "time", "secret", "while", "then", "if", 
         "loop", "in", "else", "break", "empty", "mocha", "matcha", "money", "spam","jazz","jam","spaz", 
         "binder", "jokes", "chemistry", "person", "matcha", "night", "everyone", "pasta", "craving", 
         "jolly", "ranch", "lit", "still", "first", "second", "third", "skull", "ketchup", 
         "ice", "red", "life", "death", "magic", "comments", "class", "secret", "value", 
         "variable", "guess", "incorrect", "russian", "roulette", "bot", "turn", 
         "failed", "wood", "stone", "cobblestone", "blanket", "ore", "chest", "poster"]
        #picks one word from list
        secret = items[random.randrange(len(items))]

        #creates a variable with an empty value
        guesses = ''
        turns = 10
        while turns > 0:
            failed = 0
            for char in secret:
                if char in guesses:
                    await self.bot.say(char),
                else:
                    await self.bot.say("_"),
                    failed += 1
            """ if failed is equal to zero"""
            """ Win text"""
            if failed == 0:        
                await self.bot.reply("You won! Good job! :aquaThumbsUp:")  
            """ exit the script"""
            break              

            print

            """ ask the user go guess a character"""
            guess = self.bot.discord.wait_for_message(content='a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z') 
            """ set the players guess to guesses"""
            guesses += guess
            """ incorrect letter"""
            if guess not in secret:
                turns -= 1        
                await self.bot.say("Wrong")    
            """ number of turns left"""
                await self.bot.say("You have", + turns, "more guesses") 
            """ if the turns are equal to zero"""
                if turns == 0:           
            
                    await self.bot.say("You Lost" + ", " +str(secret), "was the right word")
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Set-up
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#def setup(bot):
#   if not import random:
#       raise RuntimeError("Random failed to import")
#       return
#   bot.add_cog(Guess(bot))
