from turtle import Screen
import time
from snake import Snake
from food import Food
from Scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Snake game")
screen.bgcolor("black")
screen.tracer(0)
snake = Snake()
food = Food()
score = ScoreBoard()
# gsuvs

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()
    if snake.head.distance(food) < 15:
        food.food_move()
        snake.extend()
        score.score_change()

    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() < -290 or snake.head.ycor() > 290:
        game_is_on = False
        score.game_over()

    for turtle in snake.turtles[1::]:

        if snake.head.distance(turtle) < 10:
            game_is_on = False
            score.game_over()

screen.exitonclick()
