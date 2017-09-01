'''
Created on Aug 29, 2017

@author: Joyce
'''

import tkinter


DEFAULT_FONT = ('Helvetica', 16)


# construct a root window
root = tkinter.Tk()
root.title("Rubik's Cube Application")
root.protocol('WM_DELETE_WINDOW', quit)


# place a canvas on the window
canvas = tkinter.Canvas(master = root, width = 700, height = 750, background = 'white')
canvas.grid(row = 1, column = 0, sticky = tkinter.N + tkinter.S + tkinter.W + tkinter.E)


# decorate the canvas
canvas.create_text(350, 260, text = "Welcome to the Rubik's Cube Application!", font = DEFAULT_FONT)
canvas.create_text(350, 290, text = '(Click to get started)', font = DEFAULT_FONT)
canvas.create_text(350, 380, text = 'WARNING:     You cannot go back after clicking Next, so please follow instructions carefully :)', font = ('Helvetica', 10), fill = 'red')



    
    
    
    