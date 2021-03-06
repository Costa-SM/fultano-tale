import os
import pygame as pg
from resources import import_folder
from utils import BASE_PATH

class Tile(pg.sprite.Sprite):
    '''
    Class that represents a tile.
    
    '''
    def __init__(self, size, x, y):
        '''
        Tile class' constructor.
        :param size: tile size
        :type size: int
        :param x: tile x coordinate
        :type x: int
        :param y: tile y coordinate
        :type y: int
        
        '''
        super().__init__()
        self.image = pg.Surface((size, size))
        self.rect = self.image.get_rect(topleft = (x, y))

    def update(self, shift):
        '''
        Function that updates the tile's position.
        :param shift: shift lenght
        :type size: int

        '''
        self.rect.x += shift

class StaticTile(Tile):
    '''
    Class that represents a static tile.
    
    '''
    def __init__(self, size, x, y, surface):
        '''
        StaticTile class' constructor.
        :param size: tile size
        :type size: int
        :param x: tile x coordinate
        :type x: int
        :param y: tile y coordinate
        :type y: int
        :param surface: tile surface
        :type surface: pygame surface
        
        '''
        super().__init__(size, x, y)
        self.image = surface

class AnimatedTile(Tile):
    '''
    Class that represents a animated tile.
    
    '''
    def __init__(self, size, x, y, path):
        '''
        AnimatedTile class' constructor.
        :param size: tile size
        :type size: int
        :param x: tile x coordinate
        :type x: int
        :param y: tile y coordinate
        :type y: int
        :param path: sprite's path
        :type path: string
        
        '''
        super().__init__(size, x, y)
        # Animation vatiables
        self.frames = import_folder(path)
        self.frame_index = 0
        self.flip = False
        self.size = (100, 96)
        self.image = self.frames[self.frame_index]
        self.image = pg.transform.scale(self.image, self.size)

    def change_state(self, path, flip, size):
        '''
        Function that changes the animated tile sprite.
        :param path: sprite's path
        :type path: string
        :param flip: wheter the tile fliped
        :type flip: bool
        :param size: tile size
        :type size: int
        
        '''
        self.size = size
        self.flip = flip
        self.frames = import_folder(path)
        self.frame_index = 0
        self.image = self.frames[self.frame_index]
        self.image = pg.transform.scale(self.image, self.size)

    def animate(self):
        '''
        Function that animates the tile.
        
        '''
        self.frame_index += 0.15
        if self.frame_index >= len(self.frames):
            self.frame_index = 0 
        self.image = self.frames[int(self.frame_index)]
        self.image = pg.transform.scale(self.image, self.size)
        # Flip image
        if self.flip == True:
            self.image = pg.transform.flip(self.image, True, False)

    def update(self, shift):
        '''
        Function that updates the tile's position.
        :param shift: shift lenght
        :type size: int

        '''
        self.animate()
        self.rect.x += shift

class Crate(StaticTile):
    '''
    Class that represents a crate tile.
    
    '''
    def __init__(self, size, x, y):
        '''
        Crate tile class' constructor.
        :param size: tile size
        :type size: int
        :param x: tile x coordinate
        :type x: int
        :param y: tile y coordinate
        :type y: int
        
        '''
        super().__init__(size, x, y, pg.image.load(os.path.join(BASE_PATH, 'assets/world/terrain/Crate.png')).convert_alpha())

class Potion(StaticTile):
    '''
    Class that represents a potion tile.
    
    '''
    def __init__(self, size, x, y):
        '''
        Potion tile class' constructor.
        :param size: tile size
        :type size: int
        :param x: tile x coordinate
        :type x: int
        :param y: tile y coordinate
        :type y: int
        
        '''
        super().__init__(size, x, y, pg.image.load(os.path.join(BASE_PATH, 'assets/power_up/potion.png')).convert_alpha())

class Decoration(StaticTile):
    '''
    Class that loads the image for a given tile.
    
    '''
    def __init__(self, size, x, y, type):
        '''
        Decoration class' constructor.
        :param size: tile size
        :type size: int
        :param x: tile x coordinate
        :type x: int
        :param y: tile y coordinate
        :type y: int
        :param type: tile type
        :type type: int
        
        '''
        if type == '0':
            super().__init__(size, x, y, pg.image.load(os.path.join(BASE_PATH, 'assets/world/decoration/Bone (1).png')).convert_alpha())
        elif type == '1':
            super().__init__(size, x, y, pg.image.load(os.path.join(BASE_PATH, 'assets/world/decoration/Bone (2).png')).convert_alpha())
        elif type == '2':
            super().__init__(size, x, y, pg.image.load(os.path.join(BASE_PATH, 'assets/world/decoration/Bone (3).png')).convert_alpha())
        elif type == '3':
            super().__init__(size, x, y, pg.image.load(os.path.join(BASE_PATH, 'assets/world/decoration/Bone (4).png')).convert_alpha())
        elif type == '4':
            super().__init__(size, x, y, pg.image.load(os.path.join(BASE_PATH, 'assets/world/decoration/Bush (1).png')).convert_alpha())
        elif type == '5':
            super().__init__(size, x, y, pg.image.load(os.path.join(BASE_PATH, 'assets/world/decoration/Bush (2).png')).convert_alpha())
        elif type == '6':
            super().__init__(size, x, y, pg.image.load(os.path.join(BASE_PATH, 'assets/world/decoration/DeadBush.png')).convert_alpha())
        elif type == '7':
            super().__init__(size, x, y, pg.image.load(os.path.join(BASE_PATH, 'assets/world/decoration/Sign.png')).convert_alpha())
        elif type == '8':
            super().__init__(size, x, y, pg.image.load(os.path.join(BASE_PATH, 'assets/world/decoration/Skeleton.png')).convert_alpha())
        elif type == '9':
            super().__init__(size, x, y, pg.image.load(os.path.join(BASE_PATH, 'assets/world/decoration/TombStone (1).png')).convert_alpha())
        elif type == '10':
            super().__init__(size, x, y, pg.image.load(os.path.join(BASE_PATH, 'assets/world/decoration/TombStone (2).png')).convert_alpha())
        elif type == '11':
            super().__init__(size, x, y, pg.image.load(os.path.join(BASE_PATH, 'assets/world/decoration/Tree.png')).convert_alpha())
        elif type == '12':
            super().__init__(size, x, y, pg.image.load(os.path.join(BASE_PATH, 'assets/world/decoration/ArrowSign.png')).convert_alpha())
        # Tile offset
        offsetY = y + size
        self.rect = self.image.get_rect(bottomleft = (x, offsetY))
        