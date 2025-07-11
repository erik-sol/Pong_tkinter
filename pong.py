
class Pong:
    
    def __init__(self, cols, rows):
        self.cols = cols
        self.rows = rows
        self.field = [["-" for _ in range(cols)] for _ in range(rows)]
        self.paddle_lenght = 4
        self.paddle_x = (self.cols//2) - (self.paddle_lenght//2)
        self.paddle = Paddle(self.paddle_x, self.paddle_lenght)
        self.starter_ball_x = 7
        self.starter_ball_y = 1
        self.ball = Ball(self.starter_ball_x, self.starter_ball_y)

        self.lives = 3
        self.scores = 0
        self.game_over = False

    def draw_ball(self):
        self.field[self.ball.y][self.ball.x] = "*"

    def draw_paddle(self):
        row = self.rows - 1
        self.paddle.y = row  # Vertical position of the paddle
        for i in range(self.paddle.length):
            col = self.paddle.x + i
            self.field[row][col] = "="

    def clear_field(self):
        self.field = [["-" for _ in range(self.cols)] for _ in range(self.rows)]

    def update_field(self):
        self.clear_field()
        self.draw_ball()
        self.draw_paddle()

    def update_ball_direction(self):
        # Bouncing off the walls
        if self.ball.x == 0 or self.ball.x == self.cols - 1:
            self.ball.dx *= -1

        if self.ball.y == 0:
            self.ball.dy *= -1

            self.scores += 10
            #print(self.scores)

        # Bouncing off the paddle
        if self.ball.y == self.paddle.y - 1:
            if self.paddle.x <= self.ball.x < self.paddle.x + self.paddle.length:
                self.ball.dy *= -1

        #Bouncing at the LEFT edge of the paddle
        if self.ball.y == self.paddle.y - 1:
            if self.ball.x == self.paddle.x - 1:
                if self.ball.dx == 1 and self.ball.dy == 1:    
                    self.ball.dx *= -1
                    self.ball.dy *= -1

                    self.scores += 50
                    #print(self.scores)
        
        #Bouncing at the RIGHT edge of the paddle
        if self.ball.y == self.paddle.y - 1:
            if self.ball.x == self.paddle.x + self.paddle.length:
                if self.ball.dx == -1 and self.ball.dy == 1:    
                    self.ball.dx *= -1
                    self.ball.dy *= -1

                    self.scores += 50
                    #print(self.scores)

        # Lost at the bottom
        if self.ball.y == self.rows - 1:
            self.ball.x = self.starter_ball_x
            self.ball.y = self.starter_ball_y
            self.lives -= 1

        if self.lives == 0:
            self.game_over = True

    def step(self):
        self.update_ball_direction()
        self.ball.move()
        self.update_field()

        #print(f"Ball at ({self.ball.x}, {self.ball.y})")
        #print(f"Paddle from {self.paddle.x} to {self.paddle.x + self.paddle.length - 1}")

    def move_paddle_right(self):
        self.paddle.move_right(self.cols)

    def move_paddle_left(self):
        self.paddle.move_left()

    def __str__(self):
        outstring = ""
        for rows in self.field:
            for col in rows:
                outstring += str(col) + " "
            outstring += "\n"
        return outstring
    

class Paddle:
    def __init__(self, x, length):
        self.x = x              # x coord. on the left side
        self.y = None           # Later, given by Pong
        self.length = length

    def move_left(self):
        if self.x > 0:
            self.x -= 1

    def move_right(self, max_x):
        if self.x + self.length < max_x:
            self.x += 1

class Ball:
    def __init__(self, x, y):
        self.x = x  # Horizontal
        self.y = y  # Vertical
        self.dx = 1
        self.dy = 1

    def move(self):
        self.x += self.dx
        self.y += self.dy

if __name__ == "__main__":
    pong = Pong(10, 10)
    print("### Start állapot ###")
    pong.draw_ball()
    pong.draw_paddle()
    print(pong)

    pong.move_paddle_right()
    pong.ball.move()
    pong.update_field()
    print("### 1. lépés ###")
    print(pong)

    pong.move_paddle_right()
    pong.ball.move()
    pong.update_field()
    print("### 2. lépés ###")
    print(pong)
    pong.move_paddle_right()
    pong.ball.move()
    pong.update_field()
    print(pong)
    pong.move_paddle_right()
    pong.ball.move()
    pong.update_field()
    print(pong)
    