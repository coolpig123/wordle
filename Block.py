BLOCK_WIDTH = 40


class Block:
    def __init__(self, character, color):
        self.character = character
        self.color = color

    def draw_block(self, x, y, canvas):
        if self.color == 'b':
            canvas.create_rectangle(x, y, x + BLOCK_WIDTH, y + BLOCK_WIDTH, fill="#3A3A3C")
        elif self.color == 'y':
            canvas.create_rectangle(x, y, x + BLOCK_WIDTH, y + BLOCK_WIDTH, fill="#B59F3B")
        elif self.color == 'g':
            canvas.create_rectangle(x, y, x + BLOCK_WIDTH, y + BLOCK_WIDTH, fill="#538D4E")
        canvas.create_text(x + 20, y + 20, fill="WHITE", font="Ariel 20 bold", text=str(self.character))
