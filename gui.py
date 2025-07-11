import tkinter as tk
from pong import Pong
from tkinter import messagebox

CELL_SIZE = 20
GRID_WIDTH = 16
GRID_HEIGHT = 27

class Gui:

    def __init__(self):
        self.game = Pong(GRID_WIDTH, GRID_HEIGHT)
        self.root = tk.Tk()
        self.root.title("Pong")
        self.root.geometry(f"{CELL_SIZE*GRID_WIDTH}x{CELL_SIZE*GRID_HEIGHT+70}")
        self.time = 70
        self.is_running = False

        self.space_bar_label = tk.Label(self.root, text="Toggle Space bar to Start/Pause the game!")
        self.space_bar_label.pack()

        self.canvas = tk.Canvas(self.root, width=GRID_WIDTH*CELL_SIZE, height=GRID_HEIGHT*CELL_SIZE, bg="white")
        self.canvas.pack()

        self.score = tk.StringVar()
        self.lives = tk.StringVar()

        self.score.set(f"Score: {self.game.scores}")
        self.lives.set(f"Lives: {self.game.lives}")

        self.score_label = tk.Label(self.root, textvariable = self.score)
        self.score_label.pack()
        self.lives_label = tk.Label(self.root, textvariable = self.lives)
        self.lives_label.pack()

        self.root.bind("<Left>", self.moving_paddle_L)
        self.root.bind("<Right>", self.moving_paddle_R)
        self.root.bind("<space>", self.toggle_running)

        self.game.update_field()
        self.draw_grid()
        self.root.mainloop()

    def draw_grid(self):
        self.canvas.delete("all")
        for y in range(self.game.rows):
            for x in range(self.game.cols):
                cell = self.game.field[y][x]
                color = "white"
                if cell == "=":
                    color = "black"
                if cell == "*":
                    color = "red"

                self.canvas.create_rectangle(
                            x * CELL_SIZE,
                            y * CELL_SIZE,
                            (x+1) * CELL_SIZE,
                            (y+1) * CELL_SIZE,
                            fill=color,
                            outline="white"
                )


    def moving_paddle_L(self, event):
        if self.is_running == True:    
            self.game.move_paddle_left()
            self.game.update_field()
            self.draw_grid()

    def moving_paddle_R(self, event):
        if self.is_running == True:
            self.game.move_paddle_right()
            self.game.update_field()
            self.draw_grid()

    def toggle_running(self, event):
        self.is_running = not self.is_running
        if self.is_running:
            self.run()

    def run(self):  
        if self.game.game_over == False:
            if self.is_running:
                self.step()
                self.root.after(self.time, self.run)

        else:
            if messagebox.askyesno("Game Over", f"You've lost all your lives. Do you wanna play a new game?"):
                self.reset_game()
            else:
                self.root.destroy()

    def step(self):
        self.game.step()
        self.draw_grid()
        self.score.set(f"Score: {self.game.scores}")
        self.lives.set(f"Lives: {self.game.lives}")

    def reset_game(self):
        self.game.game_over = False
        self.is_running = False
        self.game.paddle.x = (self.game.cols // 2) - (self.game.paddle.length // 2)
        self.game.ball.x = self.game.starter_ball_x
        self.game.ball.y = self.game.starter_ball_y
        self.game.lives = 3
        self.game.scores = 0
        self.score.set(f"Score: {self.game.scores}")
        self.lives.set(f"Lives: {self.game.lives}")
        self.game.update_field()
        self.draw_grid()

if __name__ == "__main__":
    Gui()
