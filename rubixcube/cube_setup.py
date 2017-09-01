'''
Created on Aug 29, 2017

@author: Joyce
'''


#
#               CUBE DICTIONARY REFERENCE
#          _____________________________________
#         |           |            |           |
#         |           |            |           |
#         |     1     |      2     |     3     |
#         |           |            |           |
#         |___________|____________|___________|
#         |           |            |           |
#         |           |            |           |
#         |     4     |      5     |     6     |
#         |           |            |           |
#         |___________|____________|___________|
#         |           |            |           |
#         |           |            |           |
#         |     7     |      8     |     9     |
#         |           |            |           |
#         |___________|____________|___________|
#



import root_window, tkinter
from collections import Counter


DEFAULT_FONT = ('Helvetica', 14)


# main dictionary storing the rubix cube
cube = {'red': {1: '', 2: '', 3: '', 4: '', 5: 'red', 6: '', 7: '', 8: '', 9: ''}, 
        'orange': {1: '', 2: '', 3: '', 4: '', 5: 'orange', 6: '', 7: '', 8: '', 9: ''}, 
        'yellow': {1: '', 2: '', 3: '', 4: '', 5: 'yellow', 6: '', 7: '', 8: '', 9: ''}, 
        'green': {1: '', 2: '', 3: '', 4: '', 5: 'green', 6: '', 7: '', 8: '', 9: ''}, 
        'blue': {1: '', 2: '', 3: '', 4: '', 5: 'blue', 6: '', 7: '', 8: '', 9: ''}, 
        'white': {1: '', 2: '', 3: '', 4: '', 5: 'white', 6: '', 7: '', 8: '', 9: ''}}


# checks whether the user inputed a valid rubix cube
pass_check = True


# used to map rectangle ID's to their corresponding colors
id_dict = {}


# nested list containing lists of ID's
id_list = []


# translate the colors of the rubik's cube into the basic names of the colors
color_chart = {'white': 'white', 'red3': 'red', 'DarkOrange1': 'orange', 'yellow': 'yellow', 'green3': 'green', 'RoyalBlue4': 'blue'}


# to keep count of how many times the Next button has been clicked and get the appropriate index for id_list
# start at -1 because the initial configuration of the button will increment it to 0, which can get us the first item of id_list
counter = -1



def color_generator(color: str) -> str:
    '''Given a color, returns the next color in a sequence of colors'''
    if color == 'white':
        return 'red3'
    if color == 'red3':
        return 'DarkOrange1'
    if color == 'DarkOrange1':
        return 'yellow'
    if color == 'yellow':
        return 'green3'
    if color == 'green3':
        return 'RoyalBlue4'
    if color == 'RoyalBlue4':
        return 'white'



def update_cube(list_id: list, dict_id: dict) -> None:
    '''Update the cube dictionary with the information given from the ID list and dictionary'''
    print(list_id)
    print(dict_id)
    for each_list in list_id:
        for i in [i for i in range(9) if i != 4]:
            cube[dict_id[each_list[4]]][i + 1] = dict_id[each_list[i]]
    print(cube)
    
        
    
def change_position_color(event: tkinter.Event) -> None:
    '''Change the color of each position after it's been clicked on'''
    item = root_window.canvas.find_closest(event.x, event.y)
    new_color = color_generator(root_window.canvas.itemcget(item, 'fill'))
    root_window.canvas.itemconfig(item, fill = new_color, tag = (item, color_chart[new_color]))
    change = root_window.canvas.gettags(item)
    id_dict[int(change[0])] = change[1]
    for x in id_list[counter]:
        if x not in id_dict.keys():
            id_dict[x] = 'white'



def main_reference() -> None:
    '''Draw a reference of the side of the cube the user is currently configuring and bind each position on the
       reference to a mouse click'''
    one1 = root_window.canvas.create_rectangle(250, 350, 350, 450, fill = 'white', outline = 'black', tag = 'white')   
    two2 = root_window.canvas.create_rectangle(350, 350, 450, 450, fill = 'white', outline = 'black', tag = 'white')  
    three3 = root_window.canvas.create_rectangle(450, 350, 550, 450, fill = 'white', outline = 'black', tag = 'white')  
    four4 = root_window.canvas.create_rectangle(250, 450, 350, 550, fill = 'white', outline = 'black', tag = 'white')  
    color5 = root_window.canvas.create_rectangle(350, 450, 450, 550, fill = 'white', outline = 'black', tag = 'white')  
    six6 = root_window.canvas.create_rectangle(450, 450, 550, 550, fill = 'white', outline = 'black', tag = 'white')  
    seven7 = root_window.canvas.create_rectangle(250, 550, 350, 650, fill = 'white', outline = 'black', tag = 'white')  
    eight8 = root_window.canvas.create_rectangle(350, 550, 450, 650, fill = 'white', outline = 'black', tag = 'white')  
    nine9 = root_window.canvas.create_rectangle(450, 550, 550, 650, fill = 'white', outline = 'black', tag = 'white')  
    
    positions = [one1, two2, three3, four4, color5, six6, seven7, eight8, nine9]
    
    root_window.canvas.create_text(100, 400, text = 'Top row:', font = DEFAULT_FONT)
    root_window.canvas.create_text(100, 500, text = 'Middle row:', font = DEFAULT_FONT)
    root_window.canvas.create_text(100, 600, text = 'Bottom row:', font = DEFAULT_FONT)
    root_window.canvas.create_text(402, 675, text = '(Click on a box to change its color)', font = ('Helvetica', 13))
    
    for each in positions:
        root_window.canvas.tag_bind(each, '<Button-1>', change_position_color)
    
    return positions   # this is a list of all the ID's of the different positions of the face of the cube
    
       

def top_reference(side: str) -> tkinter.Text:
    '''Draws the reference diagram at the top of the canvas with specified side shaded'''
    # create the outline of the cube
    left = root_window.canvas.create_polygon(300, 100, 350, 50, 350, 150, 300, 200, 300, 100, fill = '', outline = 'black')
    bottom = root_window.canvas.create_polygon(350, 150, 300, 200, 400, 200, 450, 150, 350, 150, fill = '', outline = 'black')
    back = root_window.canvas.create_polygon(350, 50, 350, 150, 450, 150, 450, 50, 350, 50, fill = '', outline = 'black') 
    front = root_window.canvas.create_polygon(300, 100, 300, 200, 400, 200, 400, 100, 300, 100, fill = '', outline = 'black')  
    top = root_window.canvas.create_polygon(300, 100, 350, 50, 450, 50, 400, 100, 300, 100, fill = '', outline = 'black')      
    right = root_window.canvas.create_polygon(400, 100, 450, 50, 450, 150, 400, 200, 400, 100, fill = '', outline = 'black')   
    
    # fill in the specified side of the cube with the given parameter
    if side == 'front':
        root_window.canvas.itemconfig(front, fill = 'red')
    if side == 'back':
        root_window.canvas.itemconfig(back, fill = 'red')
    if side == 'top':
        root_window.canvas.itemconfig(top, fill = 'red')
    if side == 'bottom':
        root_window.canvas.itemconfig(bottom, fill = 'red')
    if side == 'right':
        root_window.canvas.itemconfig(right, fill = 'red')
    if side == 'left':
        root_window.canvas.itemconfig(left, fill = 'red')
    
    # create text to provide instructions for the user
    current_side = root_window.canvas.create_text(350, 260, text = 'Please enter cube configuration for the {} side of the cube.'.format(side), font = DEFAULT_FONT)
    return current_side      # to configure it later when sides are changed



def next_button() -> tkinter.Button:
    '''Creates the Next button on the bottom right corner of the Rubik's cube application'''
    next_button = tkinter.Button(root_window.canvas, text = 'Next', font = DEFAULT_FONT, anchor = tkinter.E, command = None)
    next_button.configure()
    root_window.canvas.create_window(680, 740, anchor = tkinter.SE, window = next_button)
   
    # increment the counter each time Next is clicked
    global counter
    counter += 1
   
    # return button to be able to configure it
    return next_button


def cube_check(check: bool) -> None:
    '''If cube was not configured properly, terminate the program. Otherwise proceed with solving cube'''
    if check:
        update_cube(id_list, id_dict)
    else:
        root_window.canvas.create_text(350, 350, text = 'Sorry! I cannot solve this cube.  It was not configured properly.', font = DEFAULT_FONT)


def complete_setup() -> None:
    '''Cube check after configuration is finished.  Move onto cube solution if check is passed, display error otherwise'''
    root_window.canvas.delete(tkinter.ALL)
    if len(id_dict) == 45:
        for x in id_list[counter]:
            id_dict[x] = 'white'
    try:
        # after configuring the cube, there should be 6 colors and 9 occurrences of each of the colors
        check = Counter(id_dict.values())
        assert len(check) == 6
        assert set(check.values()) == {9}
    except AssertionError:
        # if not, then the cube does not pass the configuration check
        global pass_check
        pass_check = False
        if check == {'white': 54} or check == {'red': 1, 'orange': 1, 'yellow': 1, 'green': 1, 'blue': 1, 'white': 49}:
            pass_check = True
    # call cube_check to take the appropriate actions for the result of the check
    cube_check(pass_check)
    
     

def back_setup() -> None:
    '''Prompt user for configuration of the back side of the Rubik's cube'''
    root_window.canvas.delete(tkinter.ALL)
    top_reference('back')
    root_window.canvas.create_text(350, 280, text = 'To do so, rotate the cube to the left twice and translate what', font = DEFAULT_FONT)
    root_window.canvas.create_text(350, 300, text = 'you see.  Rotate back to starting position once finished.', font = DEFAULT_FONT)
    
    back_ids = main_reference()
    id_list.append(back_ids)
    
    if len(id_dict) == 36:
        for x in id_list[counter]:
            id_dict[x] = 'white'
            
    next_button().configure(command = complete_setup)



def bottom_setup() -> None:
    '''Prompt user for configuration of the bottom side of the Rubik's cube'''
    root_window.canvas.delete(tkinter.ALL)
    top_reference('bottom')
    root_window.canvas.create_text(350, 280, text = 'To do so, rotate the cube upwards once and translate what', font = DEFAULT_FONT)
    root_window.canvas.create_text(350, 300, text = 'you see.  Rotate back to starting position once finished.', font = DEFAULT_FONT)
   
    bottom_ids = main_reference()
    id_list.append(bottom_ids)
    
    if len(id_dict) == 27:
        for x in id_list[counter]:
            id_dict[x] = 'white'
            
    next_button().configure(command = back_setup)



def top_setup() -> None:
    '''Prompt user for configuration of the top side of the Rubik's cube'''
    root_window.canvas.delete(tkinter.ALL)
    top_reference('top')
    root_window.canvas.create_text(350, 280, text = 'To do so, rotate the cube downwards once and translate what', font = DEFAULT_FONT)
    root_window.canvas.create_text(350, 300, text = 'you see.  Rotate back to starting position once finished.', font = DEFAULT_FONT)
   
    top_ids = main_reference()
    id_list.append(top_ids)
    
    if len(id_dict) == 18:
        for x in id_list[counter]:
            id_dict[x] = 'white'
            
    next_button().configure(command = bottom_setup)



def left_setup() -> None:
    '''Prompt user for configuration of the left side of the Rubik's cube'''
    root_window.canvas.delete(tkinter.ALL)
    top_reference('left')
    root_window.canvas.create_text(350, 280, text = 'To do so, rotate the cube once to the right and translate what', font = DEFAULT_FONT)
    root_window.canvas.create_text(350, 300, text = 'you see.  Rotate back to starting position once finished.', font = DEFAULT_FONT)
    
    left_ids = main_reference()
    id_list.append(left_ids)
  
    if len(id_dict) == 9:
        for x in id_list[counter]:
            id_dict[x] = 'white'
            
    next_button().configure(command = top_setup)
    
    

def right_setup() -> None:
    '''Prompt user for configuration of the right side of the Rubik's cube'''
    root_window.canvas.delete(tkinter.ALL)
    top_reference('right')
    root_window.canvas.create_text(350, 280, text = 'To do so, rotate the cube once to the left and translate what', font = DEFAULT_FONT)
    root_window.canvas.create_text(350, 300, text = 'you see.  Rotate back to starting position once finished.', font = DEFAULT_FONT)
    
    right_ids = main_reference()
    id_list.append(right_ids)
    
    if len(id_dict) == 0:
        for x in id_list[counter]:
            id_dict[x] = 'white'
  
    next_button().configure(command = left_setup)
    
    

def front_setup() -> None:
    '''Prompt user for configuration of the front side of the Rubik's cube'''
    front_ids = main_reference()
    id_list.append(front_ids)
   
    root_window.canvas.create_text(350, 280, text = 'Translate what you see onto the figure below.  How the cube sits in your ', font = DEFAULT_FONT)
    root_window.canvas.create_text(350, 300, text = 'hand right now will be called the "starting position" of the cube.', font = DEFAULT_FONT)
    top_reference('front')
    next_button().configure(command = right_setup)
    
    
            
            
            
def on_first_click(event: tkinter.Event) -> None:
    '''Clear and unbind the canvas, and start the cube configuration setup'''
    root_window.canvas.delete(tkinter.ALL)
    root_window.canvas.unbind('<Button-1>')
    front_setup()
    

    
    
    
    
# bind the root_window canvas to an event (mouse click) to start the application
root_window.canvas.bind('<Button-1>', on_first_click)


if __name__ == '__main__':
    root_window.canvas.mainloop() 
        
        
        