# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 18:23:10 2022

@filename: MindfulAppreciation.py

@author: Charlie

@version: 1.0

@date: 04/01/2022

@description: Input answers to the questions and receive outputted cards explaining them.
"""

#Instantiate a Class to Hold Data
class Appreciation:
    
    def __init__(self, item, how_works, how_helps, noticed, connect):
        self.item = item
        self.how_works = how_works
        self.how_helps = how_helps
        self.noticed = noticed
        self.connect = connect
        
    def __str__(self):
        return "What you appreciate: " + self.item + '\n' + \
            "How it works: " + self.how_works + '\n' + \
            "How it helps: " + self.how_helps + '\n' + \
            "What you've discovered about it: " + self.noticed + '\n' \
            "How it connects to your life: " + self.connect + '.'
    
output = []
            
while(True):
    word = input("What is something or someone you feel that you do not appreciate enough? ")
    how_works = input("Describe it; how does it work, what does it do? ")
    how_helps = input("What about this item/person makes you feel appreciation? ")
    noticed = input("Think about the item for a bit. What have you discovered/not before realised? ")
    connect = input("How does this item feature into your life? ")
    
    output.append(Appreciation(word, how_works, how_helps, noticed, connect))
    option = input("Once you have completed your appreciations, enter 'end' to end and receive your cards. ").lower()
    
    if option == 'end':
        break
    
print("What you have appreciated today: ")
for i in output:
    print('>', i)