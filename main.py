import time
from turtle  import Screen

from food import Food
from snake import Snake
from scoreboard import Scoreboard

# Background
screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

def repeat():
    screen.bgcolor("red")
    time.sleep(0.2)
    screen.bgcolor("black")
    scoreboard.game_over()
    snake.reset()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move_forward()

    # Detect when the snake collides with the food
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.update_scoreboard()
        snake.extend()

    if abs(snake.head.xcor()) > 285 or abs(snake.head.ycor()) > 285:
        repeat()

    # Detect collision with the tail
    for segment in snake.body_blocks[1:]:
        if snake.head.distance(segment) < 10:
            repeat()

screen.exitonclick()