from turtle import Turtle
STARTING_POSITION = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20

class Snake:

    def __init__(self):
        self.new_segment = []
        self.create_snake()
        self.head = self.new_segment[0]

    def create_snake(self):
        for position in STARTING_POSITION  :
            segment = Turtle("square")
            segment.color("white")
            segment.penup()
            segment.goto(position)
            self.new_segment.append(segment)

    def move(self):
        for seg_num in range(len(self.new_segment) - 1, 0, -1):
            new_x = self.new_segment[seg_num - 1].xcor()
            new_y = self.new_segment[seg_num - 1].ycor()
            self.new_segment[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        self.head.setheading(90)

    def down(self):
        self.head.setheading(270)

    def right(self):
        self.head.setheading(0)

    def left(self):
        self.head.setheading(180)
