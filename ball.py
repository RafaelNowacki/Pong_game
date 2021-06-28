from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 2
        self.y_move = 2


    def move(self):
        new_y = self.ycor() + self.y_move
        new_x = self.xcor() + self.x_move
        self.goto(new_x, new_y)

    def bounce(self, hit):
        if hit == "wall":
            self.y_move *= -1
        elif hit == "paddle":
            self.x_move *= -1

    def reset_position(self):
        self.goto(0, 0)
        self.bounce("paddle")
