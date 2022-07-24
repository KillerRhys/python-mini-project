from turtle import Turtle


class Tally(Turtle):
    """ Keeps track of player score """
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.pu()
        self.color('teal')
        self.goto(150, 200)
        self.score = 0
        self.high_score = 0
        self.write(f"Score: {self.score}", align='center', font=('Arial', 40, 'bold'))

    def display_score(self):
        self.clear()
        self.write(f"Score: {self.score}", align='center', font=('Arial', 40, 'bold'))

    def ate_leaf(self):
        self.score += 1
        self.display_score()
