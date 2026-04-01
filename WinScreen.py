from PyUI.PageElements import *
from PyUI.Screen import Screen
from PyUI.Window import Window

class WinScreen(Screen):
    def __init__(self, window, winningTrainer):  
        super().__init__(window, (252, 186, 3))
        self.state = {
            "goTo": False,
        }
        self.winningTrainer = winningTrainer

        self.elements = [
            Label((50, 90), 50, 50, "Game Over!", 20, (0,255,0)),
            Label((50, 30), 50, 50, ("Winner: "+self.winningTrainer), 20, (255,200,0)), 
        ]
        print('WhatTheScreenSaw '+self.winningTrainer) 