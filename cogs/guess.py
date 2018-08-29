"""importsss (that i don't know if it belongs here)

    you can get rid of excess comments"""
import time
import random
from discord.ext import commands
from random import choice
from collections import Counter, defaultdict, namedtuple
import discord
import os
import asyncio
import re
"""Guessing game """
class Guess:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="guess", pass_context = True)
    async def mycom(self):
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
        items = ["here", "are", "some", "strings", "of", "which", "we", "will", 
         "select", "one", "two", "three", "four", "five", "six", 
         "seven", "eight", "nine", "ten", "python", "ruby", "java", "javascript", "traceback", "print", 
         "random", "input", "raw", "print", "sleep", "time", "secret", "while", "then", "if", 
         "loop", "in", "else", "break", "empty", "mocha", "matcha", "money", "spam","jazz","jam","spaz", 
         "binder", "jokes", "chemistry", "person", "matcha", "night", "everyone", "pasta", "craving", 
         "jolly", "ranch", "lit", "still", "first", "second", "third", "skull", "ketchup", 
         "ice", "red", "life", "death", "magic", "comments", "class", "secret", "value", 
         "variable", "guess", "incorrect", "russian", "roulette", "bot", "turn", 
         "failed", "wood", "stone", "cobblestone", "blanket", "ore", "chest", "poster", "hash", "secure", "magical", "never", "public",
         "private", "key", "encryption", "cypher", "cryptogram", "theory", "open", "thread", "ripper", "core", "graphical", "graphics",
         "asymmetrical", "symmetrical"]
        # picks one word from list
        secret = random.choice(items)

        # creates a variable with an empty value
        guesses = ''
        turns = 5
        while turns > 0:
            failed = 0
            for char in secret:
                if char in guesses:
                    await self.bot.say(char),
                else:
                    await self.bot.say("_"),
                    failed += 1
                #if failed is equal to zero
                # Win text
            if failed == 0:
                await self.bot.say("You won! Good job! :aquaThumbsUp:")  
                # exit the script"""
            
                break
            # ask the user go guess a character"""
            await self.bot.say("lower case letters please~~!")
            guess = self.bot.discord.wait_for_message(channel = context.message.channel)
            
            
            while guess == None:
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
                    
                    
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# # # Set-up # # #     # # # Set-up # # #    # # # Set-up # # #    # # # Set-up # # #    # # # Set-up # # #    # # # Set-up # # #    # # # Set-up # # #    # # # Set-up # # #                           å∫ç∂´ƒ©˙ˆ∆˚¬µ˜øπœ¨®ß†¨√∑≈¥Ω å∫ç∂´ƒ©˙ˆ∆˚¬µ˜øπœ¨®ß†¨√∑≈¥Ω å∫ç∂´ƒ©˙ˆ∆˚¬µ˜øπœ¨®ß†¨√∑≈¥Ω å∫ç∂´ƒ©˙ˆ
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def setup(bot):
    check_folders()
    check_files()
    bot.add_cog(Guess(bot))

    
# dab xd oof indents 
