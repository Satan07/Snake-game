from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    """Creates the snake and manages its functionality"""
    def __init__(self):
        self.turtles = []
        self.create_snake()
        self.head = self.turtles[0]
        ]


    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_turtle(position)


    def add_turtle(self, position):


            new_square = Turtle("square")
            new_square.color("white")
            new_square.penup()
            new_square.goto(position)
            self.turtles.append(new_square)

    def extend(self):
        """Add a new segment to snake"""
        self.add_turtle(self.turtles[-1].position())



    def move(self):

        for square_num in range(len(self.turtles) - 1, 0, -1):
            new_xcor = self.turtles[square_num - 1].xcor()
            new_ycor = self.turtles[square_num - 1].ycor()
            self.turtles[square_num].goto(new_xcor, new_ycor)
        self.turtles[0].fd(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)


    pass


