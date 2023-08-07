from turtle import Screen
from snake import Snake
from Snake_food import SnakeFood
from snake_scoreboard import FoodScore
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake game!")
screen.tracer(0)

snake = Snake()
food = SnakeFood()
score = FoodScore()

screen.listen()
# controls
screen.onkey(snake.move_up, "Up")
screen.onkey(snake.move_down, "Down")
screen.onkey(snake.move_left, "Left")
screen.onkey(snake.move_right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # locating the food
    if snake.snake_body[0].distance(food) < 15:
        food.food_relocater()
        score.increase_score()
        snake.snake_body_extend()
    # wall collison
    if snake.snake_body[0].xcor() < -280 or snake.snake_body[0].xcor() > 280 or snake.snake_body[0].ycor() < -280 or snake.snake_body[0].ycor() > 280:
        game_is_on = False
        score.game_over()

    # tail collision
    for snake_segment in snake.snake_body[1:]:
        if snake.snake_body[0].distance(snake_segment) < 10:
            game_is_on = False
            score.game_over()

screen.exitonclick()
