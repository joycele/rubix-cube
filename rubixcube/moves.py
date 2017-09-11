'''
Created on Sep 10, 2017

@author: Joyce
'''

##  each method in class Moves corresponds to a certain side of the Rubik's cube 
##  each method returns an updated Rubik's cube after making its move


# tuples indicating a row or column on the cube
right = (3,6,9)
left = (1,4,7)
top = (1,2,3)
bottom = (7,8,9)
middle_row = (4,5,6)
middle_col = (2,5,8)


class Moves:
    
    def __init__(self, rubixcube: dict):
        '''initialize the Rubik's cube to contain the current configuration of the cube'''
        self.rubixcube = rubixcube
    
    
    def R_AWAY(self) -> dict:
        '''Right --right side should be rotated away from user'''
        original_top = {3: self.rubixcube['top'][3], 6: self.rubixcube['top'][6], 9: self.rubixcube['top'][9]}
        for i in right:
            self.rubixcube['top'][i] = self.rubixcube['front'][i]
            self.rubixcube['front'][i] = self.rubixcube['bottom'][i]
        for pair in zip(right, reversed(left)):
            self.rubixcube['bottom'][pair[0]] = self.rubixcube['back'][pair[1]]
            self.rubixcube['back'][pair[1]] = original_top[pair[0]]
        self.rubixcube['right'] = rotate_face('right', self.rubixcube['right'])
        return self.rubixcube
    
    
    def R_TOWARDS(self) -> dict:
        '''Right inverted --right side should be rotated towards user'''
        original_top = {3: self.rubixcube['top'][3], 6: self.rubixcube['top'][6], 9: self.rubixcube['top'][9]}
        for pair in zip(right, reversed(left)):
            self.rubixcube['top'][pair[0]] = self.rubixcube['back'][pair[1]]
            self.rubixcube['back'][pair[1]] = self.rubixcube['bottom'][pair[0]]
        for i in right:
            self.rubixcube['bottom'][i] = self.rubixcube['front'][i]
            self.rubixcube['front'][i] = original_top[i]
        self.rubixcube['right'] = rotate_face('left', self.rubixcube['right'])
        return self.rubixcube
    
    
    def L_TOWARDS(self) -> dict:
        '''Left --left side should be rotated towards user'''
        original_top = {1: self.rubixcube['top'][1], 4: self.rubixcube['top'][4], 7: self.rubixcube['top'][7]}
        for pair in zip(reversed(right), left):
            self.rubixcube['top'][pair[1]] = self.rubixcube['back'][pair[0]]
            self.rubixcube['back'][pair[0]] = self.rubixcube['bottom'][pair[1]]
        for i in left:
            self.rubixcube['bottom'][i] = self.rubixcube['front'][i]
            self.rubixcube['front'][i] = original_top[i]
        self.rubixcube['left'] = rotate_face('right', self.rubixcube['left'])
        return self.rubixcube
    
    
    def L_AWAY(self) -> dict:
        '''Left inverted --left side should be rotated away from user'''
        original_top = {1: self.rubixcube['top'][1], 4: self.rubixcube['top'][4], 7: self.rubixcube['top'][7]}
        for i in left:
            self.rubixcube['top'][i] = self.rubixcube['front'][i]
            self.rubixcube['front'][i] = self.rubixcube['bottom'][i]
        for pair in zip(reversed(right), left):
            self.rubixcube['bottom'][pair[1]] = self.rubixcube['back'][pair[0]]
            self.rubixcube['back'][pair[0]] = original_top[pair[1]]
        self.rubixcube['left'] = rotate_face('left', self.rubixcube['left'])
        return self.rubixcube
    
    
    def T_COUNTER_CLOCK(self) -> dict:
        '''Top inverted --top side should be rotated counter-clockwise'''
        original_front = {1: self.rubixcube['front'][1], 2: self.rubixcube['front'][2], 3: self.rubixcube['front'][3]}
        for i in top:
            self.rubixcube['front'][i] = self.rubixcube['left'][i]
            self.rubixcube['left'][i] = self.rubixcube['back'][i]
            self.rubixcube['back'][i] = self.rubixcube['right'][i]
            self.rubixcube['right'][i] = original_front[i]
        self.rubixcube['top'] = rotate_face('left', self.rubixcube['top'])
        return self.rubixcube
        
    
    def T_CLOCK(self) -> dict:
        '''Top --top side should be rotated clockwise'''
        original_front = {1: self.rubixcube['front'][1], 2: self.rubixcube['front'][2], 3: self.rubixcube['front'][3]}
        for i in top:
            self.rubixcube['front'][i] = self.rubixcube['right'][i]
            self.rubixcube['right'][i] = self.rubixcube['back'][i]
            self.rubixcube['back'][i] = self.rubixcube['left'][i]
            self.rubixcube['left'][i] = original_front[i]
        self.rubixcube['top'] = rotate_face('right', self.rubixcube['top'])
        return self.rubixcube
    
    
    def BM_RIGHT(self) -> dict:
        '''Bottom --bottom side should be rotated clockwise'''
        original_bottom = {7: self.rubixcube['front'][7], 8: self.rubixcube['front'][8], 9: self.rubixcube['front'][9]}
        for i in bottom:
            self.rubixcube['front'][i] = self.rubixcube['left'][i]
            self.rubixcube['left'][i] = self.rubixcube['back'][i]
            self.rubixcube['back'][i] = self.rubixcube['right'][i]
            self.rubixcube['right'][i] = original_bottom[i]
        self.rubixcube['bottom'] = rotate_face('right', self.rubixcube['bottom'])
        return self.rubixcube
    
    
    def BM_LEFT(self) -> dict:
        '''Bottom inverted --bottom side should be rotated counter-clockwise'''
        original_bottom = {7: self.rubixcube['front'][7], 8: self.rubixcube['front'][8], 9: self.rubixcube['front'][9]}
        for i in bottom:
            self.rubixcube['front'][i] = self.rubixcube['right'][i]
            self.rubixcube['right'][i] = self.rubixcube['back'][i]
            self.rubixcube['back'][i] = self.rubixcube['left'][i]
            self.rubixcube['left'][i] = original_bottom[i]
        self.rubixcube['bottom'] = rotate_face('left', self.rubixcube['bottom'])
        return self.rubixcube
    
    
    def F_RIGHT(self) -> dict:
        '''Front --front side should be rotated clockwise'''
        original_top = {7: self.rubixcube['top'][7], 8: self.rubixcube['top'][8], 9: self.rubixcube['top'][9]}
        for pair in zip(bottom, reversed(right)):
            self.rubixcube['top'][pair[0]] = self.rubixcube['left'][pair[1]]
        for pair in zip(right, top):
            self.rubixcube['left'][pair[0]] = self.rubixcube['bottom'][pair[1]]
        for pair in zip(top, reversed(left)):
            self.rubixcube['bottom'][pair[0]] = self.rubixcube['right'][pair[1]]
        for pair in zip(bottom, left):
            self.rubixcube['right'][pair[1]] = original_top[pair[0]]
        self.rubixcube['front'] = rotate_face('right', self.rubixcube['front'])
        return self.rubixcube
        
    
    def F_LEFT(self) -> dict:
        '''Front inverted --front side should be rotated counter-clockwise'''
        original_top = {7: self.rubixcube['top'][7], 8: self.rubixcube['top'][8], 9: self.rubixcube['top'][9]}
        for pair in zip(bottom, left):
            self.rubixcube['top'][pair[0]] = self.rubixcube['right'][pair[1]]
        for pair in zip(left, reversed(top)):
            self.rubixcube['right'][pair[0]] = self.rubixcube['bottom'][pair[1]]
        for pair in zip(top, right):
            self.rubixcube['bottom'][pair[0]] = self.rubixcube['left'][pair[1]]
        for pair in zip(right, reversed(bottom)):
            self.rubixcube['left'][pair[0]] = original_top[pair[1]]
        self.rubixcube['front'] = rotate_face('left', self.rubixcube['front'])
        return self.rubixcube
        
    
    def BA_LEFT(self):
        '''Back --rotate back piece to the left'''
        original_top = {1: self.rubixcube['top'][1], 2: self.rubixcube['top'][2], 3: self.rubixcube['top'][3]}
        for pair in zip(top, right):
            self.rubixcube['top'][pair[0]] = self.rubixcube['right'][pair[1]]
        for pair in zip(right, reversed(bottom)):
            self.rubixcube['right'][pair[0]] = self.rubixcube['bottom'][pair[1]]
        for pair in zip(bottom, left):
            self.rubixcube['bottom'][pair[0]] = self.rubixcube['left'][pair[1]]
        for pair in zip(left, reversed(top)):
            self.rubixcube['left'][pair[0]] = original_top[pair[1]]
        self.rubixcube['back'] = rotate_face('right', self.rubixcube['back'])
        return self.rubixcube
        
        
    def BA_RIGHT(self):
        '''Back inverted --rotate back piece to the right'''
        original_top = {1: self.rubixcube['top'][1], 2: self.rubixcube['top'][2], 3: self.rubixcube['top'][3]}
        for pair in zip(top, reversed(left)):
            self.rubixcube['top'][pair[0]] = self.rubixcube['left'][pair[1]]
        for pair in zip(left, bottom):
            self.rubixcube['left'][pair[0]] = self.rubixcube['bottom'][pair[1]]
        for pair in zip(bottom, reversed(right)):
            self.rubixcube['bottom'][pair[0]] = self.rubixcube['right'][pair[1]]
        for pair in zip(right, top):
            self.rubixcube['right'][pair[0]] = original_top[pair[1]]
        self.rubixcube['back'] = rotate_face('left', self.rubixcube['back'])
        return self.rubixcube
        


def rotate_face(direction: str, face: dict) -> dict:
    '''Rotates a face of the Rubik's cube to the left or to the right and returns it'''
    new_face = face.copy()
    if direction == 'right':
        full_tuple = tuple(zip(top, reversed(left))) + tuple(zip(middle_row, reversed(middle_col))) + tuple(zip(bottom, reversed(right)))
    if direction == 'left':
        full_tuple = tuple(zip(top, right)) + tuple(zip(middle_row, middle_col)) + tuple(zip(bottom, left))
    for pair in full_tuple:
        new_face[pair[0]] = face[pair[1]]
    return new_face
            
  
        
        
        