""" Caterpillar based on python-mini-project
    Refactor by TechGYQ
    www.MythosWorks.com
    R1:2022.06.28-2313 """


from turtle import Screen
from caterpillar import Caterpillar
from food import Food
from tally import Tally
import time

display = Screen()
display.setup(width=600, height=600)
display.bgcolor('yellow')
display.title('Caterpillar')
display.tracer(0)
display.listen()
player = Caterpillar()
food = Food()
scoreboard = Tally()
game_started = False


def outside_window():
    left_wall = -display.window_width() / 2
    right_wall = display.window_width() / 2
    top_wall = display.window_height() / 2
    bottom_wall = -display.window_height() / 2
    (x, y) = player.pos()
    outside = x < left_wall or x > right_wall or y > top_wall or y < bottom_wall
    return outside


def start_game():
    global game_started
    if game_started:
        return
    game_started = True
    player.clear()
    player.showturtle()

    while True:
        display.update()
        player.movement()
        time.sleep(0.1)
        if player.distance(food) < 20:
            food.place_leaf()
            player.pupa()
            scoreboard.ate_leaf()
        if outside_window():
            display.bgcolor('red')
            player.game_over()
            food.game_over()
            break


display.onkey(start_game, 'space')
display.onkey(player.move_up, 'Up')
display.onkey(player.move_right, 'Right')
display.onkey(player.move_down, 'Down')
display.onkey(player.move_left, 'Left')
display.mainloop()
display.exitonclick()
