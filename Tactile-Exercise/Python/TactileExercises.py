# -*- coding: utf-8 -*-
"""
Created on Wed Jan  5 20:51:29 2022

@author: Charlie

@description: Program will deliver some hurtful truths until prompted to stop.

@version history:
    
    version      |      date      |      author      |      comment      |
    1.0          |   05/01/2022   |      CMF         |   Initial Version |
"""
import random


class HurtfulTruth():
    def __init__(self):
        self.truths = ["People out there make millions playing video games.",
            "Newton invented calculus at 24. What have you done?",
            "Stop looking at your phone, they're not as into you as you are them.",
            "At a universal scale: you don't matter. Like, at all.",
            "You were born too late to explore the world, and too early to explore space.",
            "Isn't there better things you can be doing with your time?",
            "Enjoy thinking of that really embarrassing thing you did when you were younger as you go to bed.",
            "Harambe isn't coming back.",
            "Time is running out.",
            "Everyone you know is going to die someday.",
            "Dogs have no concept of accidents; they all think you kicked/stepped on them on purpose.",
            "Revan isn't canon.",
            "You're the oldest you've ever been, and you'll never be younger than you are now.",
            "More people die worldwide from obesity than starvation.",
            "Blue Waffle is a real thing.",
            "G.R.R. Martin will never finish A Song of Ice and Fire.",
            "It's too late to make millions overnight investing in Amazon, Google or Apple.",
            "Breaking Bad is Over."
            ]
    
    def __str__(self):
        return random.choice(self.truths)
    
print("Prepared for Painful Truths?")
    
while True:
    print(HurtfulTruth())
    option = input("Continue? Y/N").upper()
    
    if option != 'Y':
        break
print("Use what you've experienced. \nTake Care.")