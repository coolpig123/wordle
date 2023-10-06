from Block import *

BLOCK_WIDTH = 40

class Word:
    def __init__(self, characters, colors):
        self.characters = characters
        self.colors = colors

    def draw_word(self, x, y,canvas):
        blocks = []
        for i in range(0, 5):
            blocks.append(Block(self.characters[i], self.colors[i]))
        for i in range(0, 5):
            blocks[i].draw_block(x + (BLOCK_WIDTH + 10) * i, y,canvas)

    def is_full(self):
        for i in range(0, 5):
            if self.characters[i] == ' ':
                return False
        return True