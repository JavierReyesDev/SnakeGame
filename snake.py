from turtle  import Turtle
from typing import List

# Constants
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE = 15
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.body_blocks: List[Turtle] = []
        self.create_snake()
        self.start_position()
        self.head = self.body_blocks[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_block(position)


    def start_position(self):
        accumulator_x = 0
        for turtle in self.body_blocks:
            turtle.goto(accumulator_x, 0)
            accumulator_x -= MOVE
            turtle.showturtle()

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

    def move_forward(self):
        for seg_num in range(len(self.body_blocks) - 1, 0, -1):
            new_x = self.body_blocks[seg_num - 1].xcor()
            new_y = self.body_blocks[seg_num - 1].ycor()
            self.body_blocks[seg_num].goto(new_x, new_y)

        self.body_blocks[0].forward(MOVE)

    def add_block(self, position):
        segment = Turtle("square")
        segment.color("green")
        segment.penup()
        segment.goto(position)
        self.body_blocks.append(segment)

    def extend(self):
        self.add_block(self.body_blocks[-1].position())

    def reset(self):
        for block in self.body_blocks:
            block.hideturtle()
        self.body_blocks.clear()
        self.create_snake()
        self.head = self.body_blocks[0]


