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
from algorithms import RubixCube, InvalidCubeError


DEFAULT_FONT = ('Helvetica', 14)


# main dictionaries storing the rubix cube and the algorithms needed to solve it
cube = {'front': {1: '', 2: '', 3: '', 4: '', 5: 'white', 6: '', 7: '', 8: '', 9: ''},
        'top': {1: '', 2: '', 3: '', 4: '', 5: 'blue', 6: '', 7: '', 8: '', 9: ''},
        'right': {1: '', 2: '', 3: '', 4: '', 5: 'red', 6: '', 7: '', 8: '', 9: ''}, 
        'left': {1: '', 2: '', 3: '', 4: '', 5: 'orange', 6: '', 7: '', 8: '', 9: ''}, 
        'back': {1: '', 2: '', 3: '', 4: '', 5: 'yellow', 6: '', 7: '', 8: '', 9: ''}, 
        'bottom': {1: '', 2: '', 3: '', 4: '', 5: 'green', 6: '', 7: '', 8: '', 9: ''}}

algorithms = {'top': [], 'middle': [], 'finish': []}


# checks whether the user inputed a valid rubix cube
pass_check = True


# used to map rectangle ID's to their corresponding colors
id_dict = {}


# nested list containing lists of ID's
id_list = []


## id_dict and id_list are continually updated as each of the sides are configured by the user
## once configuration is finished, information from id_dict and id_list are used to fill out the cube dictionary


# translate the colors of the rubik's cube into the basic names of the colors
color_chart = {'white': 'white', 'red3': 'red', 'DarkOrange1': 'orange', 'yellow': 'yellow', 'forest green': 'green', 
               'RoyalBlue4': 'blue'}


# number of counters mapped to the color of the face of the cube
counter_chart = {0: 'white', 1: 'red', 2: 'blue', 3: 'orange', 4: 'yellow', 5: 'green'}


# coordinates to place cube solution models depending on the step number of the solution
solution_placement = {1: (20, 20), 2: (253, 20), 3: (486, 20), 4: (20, 270), 5: (253, 270), 6: (486, 270),
                      7: (20, 520), 8: (253, 520), 9: (486, 520)}


# to keep count of how many times the Next button has been clicked and get the appropriate index for id_list
# start at -2 because the first click increments it to -1, and the second click starts the configuration and increments it to 0, 
# which we can use to get the first item of id_list
counter = -2


# when showing cube solutions, keep track of the page count
page_count = 0


# current step in the list of algorithms
algorithm_step = 'top'


# convert algorithms to user-friendly terms
convert_alg = {'Moves(self.cube_config).R_AWAY()': ('right', 'Right away'), 
               'Moves(self.cube_config).R_TOWARDS()': ('right', 'Right towards'),
               'Moves(self.cube_config).L_TOWARDS()': ('left', 'Left towards'),
               'Moves(self.cube_config).L_AWAY()': ('left', 'Left away'),
               'Moves(self.cube_config).T_COUNTER_CLOCK()': ('top', 'Top counter-clockwise'),
               'Moves(self.cube_config).T_CLOCK()': ('top', 'Top clockwise'),
               'Moves(self.cube_config).BM_RIGHT()': ('bottom', 'Bottom right'),
               'Moves(self.cube_config).BM_LEFT()': ('bottom', 'Bottom left'),
               'Moves(self.cube_config).F_RIGHT()': ('front', 'Front right'),
               'Moves(self.cube_config).F_LEFT()': ('front', 'Front left'),
               'Moves(self.cube_config).BA_LEFT()': ('back', 'Back left'),
               'Moves(self.cube_config).BA_RIGHT()': ('back', 'Back right'),
               'Moves(self.cube_config).ROTATE_CLOCK()': ('rotate', 'Rotate clockwise'),
               'Moves(self.cube_config).ROTATE_COUNTER()': ('rotate', 'Rotate counter-clockwise')}



def organize_algorithms(alg: list) -> list:
    '''Generator that splits the list of algorithms into lists of 9 algorithms'''
    for i in range(0, len(alg), 9):
        yield alg[i: i + 9]
        
        
        
def color_generator(color: str) -> str:
    '''Given a color, returns the next color in a sequence of colors'''
    if color == 'white':
        return 'red3'
    if color == 'red3':
        return 'DarkOrange1'
    if color == 'DarkOrange1':
        return 'yellow'
    if color == 'yellow':
        return 'forest green'
    if color == 'forest green':
        return 'RoyalBlue4'
    if color == 'RoyalBlue4':
        return 'white'



def update_cube(list_id: list, dict_id: dict) -> None:
    '''Update the cube dictionary with the information given from the ID list and ID dictionary'''
    # create a map list to skip the index 5 when adding to dict_id
    map_list = list(zip([i for i in range(1,10) if i != 5], [i for i in range(8)]))
    for i in range(6):
        for index in map_list:
            if counter_chart[i] == 'red':
                cube['right'][index[0]] = dict_id[list_id[i][index[1]]]
            if counter_chart[i] == 'orange':
                cube['left'][index[0]] = dict_id[list_id[i][index[1]]]
            if counter_chart[i] == 'yellow':
                cube['back'][index[0]] = dict_id[list_id[i][index[1]]]
            if counter_chart[i] == 'green':
                cube['bottom'][index[0]] = dict_id[list_id[i][index[1]]]
            if counter_chart[i] == 'blue':
                cube['top'][index[0]] = dict_id[list_id[i][index[1]]]
            if counter_chart[i] == 'white':
                cube['front'][index[0]] = dict_id[list_id[i][index[1]]]
                
        
    
def change_position_color(event: tkinter.Event) -> None:
    '''Change the color of each position after it's been clicked on'''
    item = root_window.canvas.find_closest(event.x, event.y)
    new_color = color_generator(root_window.canvas.itemcget(item, 'fill'))
    root_window.canvas.itemconfig(item, fill = new_color, tag = (item, color_chart[new_color]))
    change = root_window.canvas.gettags(item)
    id_dict[int(change[0])] = change[1]
    for x in id_list[counter]:
        if x not in id_dict.keys():
            id_dict[x] = 'white'     # if a piece was never clicked on, its color is white



def main_reference(color: str) -> list:
    '''Draw a reference of the side of the cube the user is currently configuring and bind each position on the
       reference to a mouse click'''
    one1 = root_window.canvas.create_rectangle(250, 350, 350, 450, fill = 'white', outline = 'black', tag = 'white')   
    two2 = root_window.canvas.create_rectangle(350, 350, 450, 450, fill = 'white', outline = 'black', tag = 'white')  
    three3 = root_window.canvas.create_rectangle(450, 350, 550, 450, fill = 'white', outline = 'black', tag = 'white')  
    four4 = root_window.canvas.create_rectangle(250, 450, 350, 550, fill = 'white', outline = 'black', tag = 'white')  
    six6 = root_window.canvas.create_rectangle(450, 450, 550, 550, fill = 'white', outline = 'black', tag = 'white')  
    seven7 = root_window.canvas.create_rectangle(250, 550, 350, 650, fill = 'white', outline = 'black', tag = 'white')  
    eight8 = root_window.canvas.create_rectangle(350, 550, 450, 650, fill = 'white', outline = 'black', tag = 'white')  
    nine9 = root_window.canvas.create_rectangle(450, 550, 550, 650, fill = 'white', outline = 'black', tag = 'white')  
    root_window.canvas.create_rectangle(350, 450, 450, 550, fill = color, outline = 'black')
    
    positions = [one1, two2, three3, four4, six6, seven7, eight8, nine9]
    
    root_window.canvas.create_text(100, 400, text = 'Top row:', font = DEFAULT_FONT)
    root_window.canvas.create_text(100, 500, text = 'Middle row:', font = DEFAULT_FONT)
    root_window.canvas.create_text(100, 600, text = 'Bottom row:', font = DEFAULT_FONT)
    root_window.canvas.create_text(402, 675, text = '(Click on a box to change its color)', font = ('Helvetica', 13))
    
    for each in positions:
        root_window.canvas.tag_bind(each, '<Button-1>', change_position_color)
    
    return positions   # this is a list of all the ID's of the different positions of the face of the cube
    
       

def top_reference(side: str, include_text = True, flipped = False) -> tkinter.Text:
    '''Draws the reference diagram at the top of the canvas with specified side shaded.  Includes text instructions as a default.'''
    # create the outline of the cube
    back = root_window.canvas.create_polygon(350, 50, 350, 150, 450, 150, 450, 50, 350, 50,fill = '',outline = 'black')
    left = root_window.canvas.create_polygon(300, 100, 350, 50, 350, 150, 300, 200, 300, 100,fill = '',outline = 'black')
    bottom = root_window.canvas.create_polygon(350, 150, 300, 200, 400, 200, 450, 150, 350, 150,fill = '',outline = 'black')  
    top = root_window.canvas.create_polygon(300, 100, 350, 50, 450, 50, 400, 100, 300, 100,fill = '',outline = 'black')  
    right = root_window.canvas.create_polygon(400, 100, 450, 50, 450, 150, 400, 200, 400, 100,fill = '',outline = 'black')  
    front = root_window.canvas.create_polygon(300, 100, 300, 200, 400, 200, 400, 100, 300, 100,fill = '',outline = 'black')
    
    # fill in the specified side of the cube with the given parameter
    if side == 'front':
        root_window.canvas.itemconfig(front, fill = 'white')
    if side == 'back':
        root_window.canvas.itemconfig(back, fill = 'yellow')
    if side == 'top':
        if flipped == True:
            root_window.canvas.itemconfig(top, fill = 'forest green')
        else:
            root_window.canvas.itemconfig(top, fill = 'RoyalBlue4')
    if side == 'bottom':
        root_window.canvas.itemconfig(bottom, fill = 'forest green')
    if side == 'right':
        if flipped == True:
            root_window.canvas.itemconfig(right, fill = 'DarkOrange1')
        else:
            root_window.canvas.itemconfig(right, fill = 'red3')
    if side == 'left':
        root_window.canvas.itemconfig(left, fill = 'DarkOrange1')
    
    # create text to provide instructions for the user
    if include_text:
        current_side = root_window.canvas.create_text(
            350, 260, text = 'Please enter cube configuration for the {} side of the cube.'.format(side),font = DEFAULT_FONT)
        # return current_side to be able to configure it later when sides are changed
        return current_side      



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


def create_cube(position: int, page: int, algorithm: tuple) -> None:
    '''Draws a cube for the solution template for the user to follow'''
    x = solution_placement[position][0] + 25
    y = solution_placement[position][1] + 70
    
    def draw_arrow(x: int, y: int, alg: str) -> None:
        '''Draw arrow indicating direction of algorithm'''
        if alg == 'Right away':
            pass
            #root_window.canvas.create_line(x + 70, y + 90, x + 50, y - 10, x + 120, y - 40, arrow = tkinter.LAST)
            
    root_window.canvas.create_text(solution_placement[position], text = str(position + (page * 9)) + '.', font = DEFAULT_FONT)
    back = root_window.canvas.create_polygon(x + 50, y - 50, x + 150, y - 50, x + 150, y + 50, x + 50, y + 50, x + 50, y - 50,
                                             fill = '', outline = 'black')
    left = root_window.canvas.create_polygon(x, y + 100, x, y, x + 50, y - 50, x + 50, y + 50, x, y + 100, fill = '',
                                             outline = 'black')
    bottom = root_window.canvas.create_polygon(x, y + 100, x + 50, y + 50, x + 150, y + 50, x + 100, y + 100, x, y + 100,
                                               fill = '', outline = 'black')
    top = root_window.canvas.create_polygon(x, y, x + 50, y - 50, x + 150, y - 50, x + 100, y, x, y, fill = '',
                                            outline = 'black')
    right = root_window.canvas.create_polygon(x + 100, y, x + 150, y - 50, x + 150, y + 50, x + 100, y + 100, x + 100, y,
                                              fill = '', outline = 'black')
    front = root_window.canvas.create_polygon(x, y, x + 100, y, x + 100, y + 100, x, y + 100, x, y, fill = '', outline = 'black')
    draw_arrow(x, y, algorithm[1]) 
    alg = root_window.canvas.create_text(x + 70, y + 130, text = algorithm[1], font = DEFAULT_FONT)
    
    if algorithm[0] == 'front':
        root_window.canvas.itemconfig(front, fill = 'midnight blue')
    if algorithm[0] == 'back':
        root_window.canvas.itemconfig(back, fill = 'midnight blue')
    if algorithm[0] == 'top':
        root_window.canvas.itemconfig(top, fill = 'midnight blue')
    if algorithm[0] == 'bottom':
        root_window.canvas.itemconfig(bottom, fill = 'midnight blue')
    if algorithm[0] == 'left':
        root_window.canvas.itemconfig(left, fill = 'midnight blue')
    if algorithm[0] == 'right':
        root_window.canvas.itemconfig(right, fill = 'midnight blue')



def finish_instructions() -> None:
    '''Sets the user up to finish solving the cube'''
    global algorithm_step
    algorithm_step = 'finish'
    root_window.canvas.delete(tkinter.ALL)
    root_window.canvas.create_text(350, 100, text = 'press space')
    root_window.canvas.bind('<space>', show_template)


def solve_middle_instructions() -> None:
    '''Sets the user up to get started on solving the middle portion of the cube'''
    global algorithm_step
    algorithm_step = 'middle'
    root_window.canvas.delete(tkinter.ALL)
    top_reference('top', False, True)
    top_reference('right', False, True)
    top_reference('front', False, True)
    root_window.canvas.create_text(350, 300, text = '* * * * * *', font = ('Helvetica', 21))
    root_window.canvas.create_text(350, 320, text = 'Next set of instructions: FLIP THE CUBE', font = DEFAULT_FONT)
    root_window.canvas.create_text(350, 342, text = 'Hold the cube so that Blue is now at the bottom, Green is on top,',
                                   font = DEFAULT_FONT)
    root_window.canvas.create_text(350, 364, text = 'White is facing you, and Orange is on the right (shown above)', 
                                   font = DEFAULT_FONT)
    root_window.canvas.create_text(350, 397, text = '* * * * * *', font = ('Helvetica', 21))
    root_window.canvas.create_text(350, 500, text = 'We will now solve for the Middle Row of the cube.  For this, you',
                                   font = DEFAULT_FONT)
    root_window.canvas.create_text(350, 522, text = 'will occasionally be asked to rotate the cube. If so, rotate the',
                                   font = DEFAULT_FONT)
    root_window.canvas.create_text(350, 544, text = 'cube clockwise or counter-clock only ONCE in that direction. ',
                                   font = DEFAULT_FONT)
    root_window.canvas.create_text(350, 570, text = '(Press Space to get started)', font = DEFAULT_FONT)
    root_window.canvas.bind('<space>', show_template)
    
    


def show_template(event: tkinter.Event) -> None:
    '''Creates the template for displaying the solution algorithms to the user'''
    root_window.canvas.delete(tkinter.ALL)
    global page_count
    print(algorithm_step)
    print(algorithms)
    print('$$$$$$$', algorithms[algorithm_step])
    print('BEGIN LENGTH: ', len(algorithms[algorithm_step]))
    if algorithms[algorithm_step] != []:
        current = algorithms[algorithm_step][0]
        print('current: ', current)
        for i in range(1, len(current) + 1):
            create_cube(i, page_count, convert_alg[current[i - 1]])
        del algorithms[algorithm_step][0]
        page_count += 1
        print('NEXT LENGTH: ', len(algorithms[algorithm_step]))
    print('-------------------------------')
    if algorithms[algorithm_step] == []:
        root_window.canvas.unbind('<space>')
        page_count = 0
        if algorithm_step == 'top':
            next_button().configure(command = solve_middle_instructions)
        if algorithm_step == 'middle':
            next_button().configure(command = finish_instructions)
                     


def solve_cube(cube: dict) -> None:
    '''Given the configuration of the cube, solve the cube and update the algorithm dictionary'''
    print('ORIGINAL CUBE: ', cube)
    top = list(organize_algorithms(RubixCube(cube).SolveTop()))
    no_flip = RubixCube(cube).SolveMiddle()[1:]
    middle = list(organize_algorithms(no_flip))
    last = RubixCube(cube).SolveTopCross() + RubixCube(cube).SolveRest()
    finish = list(organize_algorithms(last))
    algorithms['top'] = top
    algorithms['middle'] = middle
    algorithms['finish'] = finish
    print(algorithms)
    print('RESULT CUBE: ', cube)


def solve_top_instructions() -> None:
    '''Set the user up to get started on solving the top part of the cube'''
    root_window.canvas.delete(tkinter.ALL)
    root_window.canvas.create_text(350, 170, text = 'We will start by solving the top row of the cube.', font = ('Helvetica', 18))
    root_window.canvas.create_text(350, 320, text = 'For this first set of instructions, remember to keep the cube in',
                                   font = DEFAULT_FONT)
    root_window.canvas.create_text(350, 342, text = 'STARTING POSITION. (Blue on top, White in front, Red on the right)',
                                   font = DEFAULT_FONT)
    root_window.canvas.create_text(350, 395, text = 'Just as with the Next button, you cannot go back after pressing SPACE',
                                   font = ('Helvetica', 12))
    root_window.canvas.create_text(350, 417, text = 'Press SPACE to get started!', font = DEFAULT_FONT)
    root_window.canvas.bind('<space>', show_template)



def solve_cube_instructions() -> None:
    '''If the cube was configured correctly, provide the next set of instructions for the user'''
    root_window.canvas.create_text(350, 170, text = "Alright! I've solved your cube! ", font = ('Helvetica', 18))
    root_window.canvas.create_text(350, 320, text = 'The following pages will provide a step by step walk-through. Press',
                                   font = DEFAULT_FONT)
    root_window.canvas.create_text(350, 342, text = 'the SPACE BAR after each page to view the next set of instructions.',
                                   font = DEFAULT_FONT)
    root_window.canvas.create_text(350, 395, text = 'Each step will feature a cube with a highlighted face in blue. An',
                                   font = DEFAULT_FONT)
    root_window.canvas.create_text(350, 417, text = 'arrow, along with a caption, will indicate how to move the face.',
                                   font = DEFAULT_FONT)
    root_window.canvas.create_text(350, 470, text = '**Remember to keep the cube in starting position **', font = DEFAULT_FONT)
    root_window.canvas.create_text(350, 492, text = '(White in front, Blue on top, and Red on the right)', font = DEFAULT_FONT)
    next_button().configure(command = solve_top_instructions)



def cube_check(check: bool) -> None:
    '''If cube was not configured properly, terminate the program. Otherwise proceed with solving cube'''
    if check:
        # cube was configured properly; proceed to next step
        update_cube(id_list, id_dict)
        try:
            solve_cube(cube)
            solve_cube_instructions() 
        except InvalidCubeError:
            root_window.canvas.create_text(
                350, 350, text = 'Sorry!  An error occurred.  I cannot solve this cube.', font = DEFAULT_FONT)
    else:
        # cube was not configured properly; terminate the program
        solve_middle_instructions()
        #=======================================================================
        # print(cube)
        # root_window.canvas.create_text(
        #     350, 350, text = 'Sorry!  I cannot solve this cube.  It was not configured properly.', font = DEFAULT_FONT)
        #=======================================================================



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
        assert set(check.values()) == {8}
    except AssertionError:
        # if not, then the cube does not pass the configuration check
        global pass_check
        pass_check = False
    # call cube_check to take the appropriate actions for the result of the check
    cube_check(pass_check)



def setup_format(side: str, direction: str, color: str, check_length: int or None) -> None:
    '''Prompt user for configuration of the specified side of the Rubik's cube'''
    root_window.canvas.delete(tkinter.ALL)
    top_reference(side)
    
    if side == 'front':
        root_window.canvas.create_text(350, 280, text = 'Translate what you see onto the figure below.', font = DEFAULT_FONT)
    else:
        root_window.canvas.create_text(350, 280, text = 'To do so, rotate the cube {} and translate what'.format(direction),
                                        font = DEFAULT_FONT)
        root_window.canvas.create_text(350, 300, text = 'you see.  Rotate back to starting position once finished.',
                                        font = DEFAULT_FONT)
    
    ids = main_reference(color)
    id_list.append(ids)
    
    if len(id_dict) == check_length:
        for x in id_list[counter]:
            id_dict[x] = 'white'



def bottom_setup() -> None:
    '''Prompt user for configuration of the bottom side of the Rubik's cube'''
    setup_format('bottom', 'upwards once', 'forest green', 36)
    next_button().configure(command = complete_setup)



def back_setup() -> None:
    '''Prompt user for configuration of the back side of the Rubik's cube'''        
    setup_format('back', 'to the left twice', 'yellow', 27)
    next_button().configure(command = bottom_setup)



def left_setup() -> None:
    '''Prompt user for configuration of the left side of the Rubik's cube'''
    setup_format('left', 'once to the right', 'DarkOrange1', 18)
    next_button().configure(command = back_setup)



def top_setup() -> None:
    '''Prompt user for configuration of the top side of the Rubik's cube'''
    setup_format('top', 'downwards once', 'RoyalBlue4', 9)
    next_button().configure(command = left_setup)
    
    

def right_setup() -> None:
    '''Prompt user for configuration of the right side of the Rubik's cube'''
    setup_format('right', 'once to the left', 'red3', 0)
    next_button().configure(command = top_setup)
    
    

def front_setup() -> None:
    '''Prompt user for configuration of the front side of the Rubik's cube'''
    setup_format('front', '', 'white', None)
    next_button().configure(command = right_setup)
            
            
            
def on_first_click(event: tkinter.Event) -> None:
    '''Brief the user on how to hold the Rubik's cube with the correct orientation'''
    root_window.canvas.delete(tkinter.ALL)
    root_window.canvas.unbind('<Button-1>')
    top_reference('top', False)
    top_reference('right', False)
    top_reference('front', False)
    root_window.canvas.create_text(350, 260, text = "SOME RUBIK'S CUBE BASICS:", font = DEFAULT_FONT)
    root_window.canvas.create_text(350, 290, text = "The center piece on each side determines that side's color.", 
                                   font = DEFAULT_FONT)
    root_window.canvas.create_text(350, 310, text = "Blue is across from Green, Red is across from Orange, and", 
                                   font = DEFAULT_FONT)
    root_window.canvas.create_text(350, 330, text = 'White is across from Yellow.', font = DEFAULT_FONT)
    root_window.canvas.create_text(350, 410, text = 'INSTRUCTIONS:', font = DEFAULT_FONT)
    root_window.canvas.create_text(350, 440, text = '1.  Hold your cube so that the Blue center piece is on top, with White',
                                    font = DEFAULT_FONT)
    root_window.canvas.create_text(350, 460, text = '    facing you and Red on the right (as shown in the model).', 
                                   font = DEFAULT_FONT)
    root_window.canvas.create_text(350, 490, text = '2.  (The Orange center piece should now be on your left, Green on the',
                                    font = DEFAULT_FONT)
    root_window.canvas.create_text(350, 510, text = '    bottom, and Yellow should be at the back.)', font = DEFAULT_FONT)
    root_window.canvas.create_text(350, 540, text = '3.  How the cube sits in your hand right now will be called the', 
                                   font = DEFAULT_FONT)
    root_window.canvas.create_text(350, 560, text = '    "starting position" of the cube.  Keep the cube in starting',
                                    font = DEFAULT_FONT)
    root_window.canvas.create_text(350, 580, text = '    position unless instructed otherwise.', font = DEFAULT_FONT)
    root_window.canvas.create_text(450, 730, text = 'WARNING:  You cannot go back after clicking Next', font =
                                    ('Helvetica', 10), fill = 'red')
    root_window.canvas.create_polygon(137, 280, 137, 301, 245, 301, 245, 280, 137, 280,fill = '',outline = 'red')
    next_button().configure(command = front_setup)

    
    
    
    
# bind the root_window canvas to an event (mouse click) to start the application
root_window.canvas.bind('<Button-1>', on_first_click)
# then focus the application on the keyboard, since later the space bar will be used
root_window.canvas.focus_set()
 
 
if __name__ == '__main__':
    root_window.canvas.mainloop() 
        
        
        