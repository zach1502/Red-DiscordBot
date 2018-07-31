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
"""A class (that I copy pastaed)"""
"""this is the comment format right?"""
class Guess:
    

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def mycom(self):

    """welcoming the user"""
await self.bot.say("Guess the word im thinking of!")

"""thinking"""
time.sleep(3)

"""start guess"""
await self.bot.say("Start guessing...(hint: no caps/")
time.sleep(0.5)

"""make secret"""
secret = "its gonna change"

"""Probably need to create a word list and grab words from there"""
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
 
 """picks one word from list"""
secret = items[random.randrange(len(items))]

"""creates a variable with an empty value"""
guesses = ''


"""determine the number of turns"""
turns = 10

"""Create while loop"""

"""check if the turns are more than zero"""
while turns > 0:         

    """ make a counter that starts with zero"""
    failed = 0             

    """ for every character in secret_word    """
    for char in secret:      

    """ see if the character is in the players guess"""
        if char in guesses:    
    
        """ print then out the character"""
            await self.bot.say(char),    

        else:
    
        """ if not found, print a dash.."""
            await self.bot.say("_"),     
       
        """...and increase the failed counter with one"""
            failed += 1    

    """ if failed is equal to zero"""

    """ Win text"""
    if failed == 0:        
        await self.bot.say("You won! Good job! :aquaThumbsUp:")  

    """ exit the script"""
        break              

    print

    """ ask the user go guess a character"""
    guess = raw_input("guess a character:") 

    """ set the players guess to guesses"""
    guesses += guess                    

    """ incorrect letter"""
    if guess not in secret:  
 
     """ turns counter -1"""
        turns -= 1        
 
    """ print wrong"""
        await self.bot.say("Wrong")    
 
    """ number of turns left"""
        await self.bot.say("You have", + turns, 'more guesses') 
 
    """ if the turns are equal to zero"""
        if turns == 0:           
    
        """losing text"""
            await self.bot.say("You Lost" + ", " +str(secret), "was the right word")
