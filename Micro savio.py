import tkinter as tk
import random
from tkinter import messagebox


class MemoryPuzzle:
    def __init__(self, master):
        self.master = master
        self.master.title("Memory Puzzle")
        self.cards = []
        self.flipped_cards = []
        self.card_values = []
        self.card_buttons = []
        self.moves = 0
        self.create_board()
        self.shuffle_cards()
        self.add_exit_button()

    def create_board(self):
        frame = tk.Frame(self.master)
        frame.grid(row=0, column=0, padx=10, pady=10)

        self.master.grid_rowconfigure(0, weight=1, minsize=400)
        self.master.grid_columnconfigure(0, weight=1, minsize=400)

        for i in range(4):
            row = []
            for j in range(4):
                button = tk.Button(frame, width=10, height=4, command=lambda r=i, c=j: self.flip_card(r, c))
                button.grid(row=i, column=j, padx=5, pady=5)
                row.append(button)
            self.cards.append(row)

    def shuffle_cards(self):
        self.card_values = [i // 2 for i in range(16)]
        random.shuffle(self.card_values)
        self.card_values = [str(value) for value in self.card_values]

    def flip_card(self, row, col):
        button = self.cards[row][col]
        index = row * 4 + col
        card_value = self.card_values[index]

        if button["state"] == "disabled":
            return

        button.config(text=card_value, state="disabled")
        self.flipped_cards.append((row, col, card_value))

        if len(self.flipped_cards) == 2:
            self.moves += 1
            self.master.title(f"Memory Puzzle - Moves: {self.moves}")
            self.check_match()

    def check_match(self):
        (row1, col1, value1), (row2, col2, value2) = self.flipped_cards

        if value1 == value2:
            self.flipped_cards = []
            if all(button["state"] == "disabled" for row in self.cards for button in row):
                messagebox.showinfo("You Win!", f"You've completed the game in {self.moves} moves!")
        else:
            self.master.after(500, self.flip_back, row1, col1, row2, col2)

    def flip_back(self, row1, col1, row2, col2):
        self.cards[row1][col1].config(text="", state="normal")
        self.cards[row2][col2].config(text="", state="normal")
        self.flipped_cards = []

    def add_exit_button(self):
        exit_button = tk.Button(self.master, text="Exit", command=self.master.destroy, bg="yellow", fg="black")
        exit_button.grid(row=1, column=0, pady=10)


def main():
    root = tk.Tk()
    game = MemoryPuzzle(root)
    root.mainloop()


if __name__ == "__main__":
    main()
