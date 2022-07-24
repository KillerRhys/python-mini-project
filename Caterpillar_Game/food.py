import turtle
from random import randint


class Food(turtle.Turtle):
    """ Creates leaves and handles logic """
    def __init__(self):
        super().__init__()
        self.leaf_shape = ((0, 0), (14, 2), (18, 6), (20, 20), (6, 18), (2, 14))
        turtle.register_shape('leaf', self.leaf_shape)
        self.shape('leaf')
        self.color('green')
        self.pu()
        self.hideturtle()
        self.speed()
        self.place_leaf()

    def game_over(self):
        self.color('yellow')

    def place_leaf(self):
        self.hideturtle()
        self.setx(randint(-300, 300))
        self.sety(randint(-300, 300))
        self.showturtle()
