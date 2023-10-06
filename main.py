from tkinter import *
from Word import *
from Functions import *
import random

target_word = random.choice(open('words.txt').read().split()).strip().upper()
target_chars = []
for i in range(0, 5):
    target_chars.append(target_word[i])

BLOCK_WIDTH = 40
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

global current_word
global current_letter
current_word = 0
current_letter = 0
global words
words = []
chars = [[' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ']]
colors = [['b', 'b', 'b', 'b', 'b'],
          ['b', 'b', 'b', 'b', 'b'],
          ['b', 'b', 'b', 'b', 'b'],
          ['b', 'b', 'b', 'b', 'b'],
          ['b', 'b', 'b', 'b', 'b'],
          ['b', 'b', 'b', 'b', 'b']]
root = Tk()
root.title('Wordle')
root.geometry('600x600')
root.config(bg='black')

ans_label = Label(text="",font = ("Bahnschrift", 14))


def update():
    for i in range(0, 6):
        words[i].draw_word(30, 30 + i * (BLOCK_WIDTH + 10), canvas)


def reset():
    global current_word
    global current_letter
    global words
    current_word = 0
    current_letter = 0
    for i in range(0, 6):
        for j in range(0, 5):
            words[i].characters[j] = ' '
            words[i].colors[j] = 'b'
    canvas.delete("all")
    update()
    ans_label.config(text="")


reset_button = Button(text="Reset", command=reset,font = ("Bahnschrift", 14))

canvas = Canvas(
    root,
    height=350,
    width=300,
    bg="black",
)

canvas.pack()
ans_label.pack(pady=10)
reset_button.pack(pady=5)

for i in range(0, 6):
    words.append(Word(chars[i], colors[i]))
    words[i].draw_word(30, 30 + i * (BLOCK_WIDTH + 10), canvas)


def react(event):
    global current_word
    global current_letter
    if event.keysym.upper() in letters and current_letter < 5:
        words[current_word].characters[current_letter] = event.keysym.upper()
        current_letter += 1
    if event.keysym == "BackSpace" and current_letter > 0:
        current_letter -= 1
        words[current_word].characters[current_letter] = ' '
    if event.keysym == "Return" and words[current_word].is_full() and current_word <= 5:
        words[current_word].colors = analyze_colors(words[current_word].characters, target_chars)
        if words[current_word].colors == ['g', 'g', 'g', 'g', 'g']:
            print("Game Over, you won!")
            current_word = 5;
        elif current_word == 5 and words[current_word].colors != ['g', 'g', 'g', 'g', 'g']:
            ans_label.config(text="word was : " + target_word.lower())
        else:
            current_word += 1
            current_letter = 0

    update()


root.bind("<KeyRelease>", react)
root.mainloop()
