'''
Created on Aug 29, 2017

@author: Joyce
'''

import tkinter


# construct a root window
root = tkinter.Tk()
root.title("Rubik's Cube Application")
root.protocol('WM_DELETE_WINDOW', quit)


# place a canvas on the window
canvas = tkinter.Canvas(master = root, width = 700, height = 750, background = 'white')
canvas.grid(row = 1, column = 0, sticky = tkinter.N + tkinter.S + tkinter.W + tkinter.E)


# decorate the canvas
canvas.create_text(350, 280, text = "Welcome to the Rubik's Cube Application!", font = ('Helvetica', 18))
canvas.create_text(350, 330, text = '(Click to get started)', font = ('Helvetica', 16))



    
    
    
    