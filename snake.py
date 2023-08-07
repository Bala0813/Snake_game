from turtle import Turtle

POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
DISTANCE = 20
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270


class Snake:

    def __init__(self):
        self.snake_body = []
        self.create_snake_body()

    def create_snake_body(self):
        for position in POSITIONS:
            self.snake_add_segment(position)

    def snake_add_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(x=position[0], y=position[1])
        self.snake_body.append(new_segment)

    def snake_body_extend(self):
        self.snake_add_segment(self.snake_body[-1].position())


    def move(self):
        for seg_index in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[seg_index - 1].xcor()
            new_y = self.snake_body[seg_index - 1].ycor()
            self.snake_body[seg_index].goto(new_x, new_y)
        self.snake_body[0].forward(DISTANCE)

    def move_left(self):
        if self.snake_body[0].heading() != RIGHT:
            self.snake_body[0].setheading(LEFT)

    def move_right(self):
        if self.snake_body[0].heading() != LEFT:
            self.snake_body[0].setheading(RIGHT)

    def move_up(self):
        if self.snake_body[0].heading() != DOWN:
            self.snake_body[0].setheading(UP)

    def move_down(self):
        if self.snake_body[0].heading() != UP:
            self.snake_body[0].setheading(DOWN)
