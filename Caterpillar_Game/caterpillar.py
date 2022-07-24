from turtle import Turtle


class Caterpillar(Turtle):
    """ Creates the player & handles movement etc """
    def __init__(self):
        super().__init__('square')
        self.move_speed = 2
        self.length = 3
        self.color('green')
        self.shapesize(1, self.length, 1)
        self.pu()
        self.hideturtle()
        self.write('Press SPACE to start', align='center', font=('Arial', 18, 'bold'))
        self.movement()

    def movement(self):
        self.forward(self.move_speed)

    def game_over(self):
        self.color('yellow')

    def pupa(self):
        self.length += 1
        self.shapesize(1, self.length, 1)
        self.move_speed += 1

    def move_up(self):
        if self.heading() == 0 or self.heading() == 180:
            self.setheading(90)

    def move_down(self):
        if self.heading() == 0 or self.heading() == 180:
            self.setheading(270)

    def move_left(self):
        if self.heading() == 90 or self.heading() == 270:
            self.setheading(180)

    def move_right(self):
        if self.heading() == 90 or self.heading() == 270:
            self.setheading(0)
