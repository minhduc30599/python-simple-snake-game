import time
from turtle import Screen, Turtle

from snake import Snake
from food import Food
from score_board import ScoreBoard

# set up screen for snake game
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Welcome to snake game')
screen.tracer(0)

# create snake body and control snake with key in keyboard
snake = Snake()
food = Food()
score_board = ScoreBoard()

screen.listen()
screen.onkey(snake.move_up, 'Up')
screen.onkey(snake.move_down, 'Down')
screen.onkey(snake.move_right, 'Right')
screen.onkey(snake.move_left, 'Left')

# start the game
is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)

    # move snake
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh_location()
        snake.extend_snake_tail()
        score_board.get_point()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        # is_game_on = False
        # score_board.end_game()
        score_board.get_high_score()
        snake.reset_snake()

    for segment in snake.segments:
        if snake.head == segment:
            pass
        elif snake.head.distance(segment) < 10:
            # is_game_on = False
            # score_board.end_game()
            score_board.get_high_score()
            snake.reset_snake()

screen.exitonclick()
