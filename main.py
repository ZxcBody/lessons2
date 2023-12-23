class Snake:
    def __init__(self, direction='left',lenght = 1, x = 3, y = 3):
        self.direction = direction
        self.lenght = lenght
        self.x = x
        self.y = y

    def change(self, new_direction):
        if self.direction == 'left' and (new_direction == 'top' or new_direction == 'bottom'):
            self.direction = new_direction
        if self.direction == 'right' and (new_direction == 'top' or new_direction == 'bottom'):
            self.direction = new_direction
        if self.direction == 'top' and (new_direction == 'left' or new_direction == 'right'):
            self.direction = new_direction
        if self.direction == 'buttom' and (new_direction == 'left' or new_direction == 'right'):
            self.direction = new_direction

    def move(self):
        if self.direction == 'left':
            self.x -= 1
        if self.direction == 'right':
            self.x += 1
        if self.direction == 'bottom':
            self.y += 1
        if self.direction == 'top':
            self.y -= 1


