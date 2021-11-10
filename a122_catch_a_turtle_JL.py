# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
import random as rand
import leaderboard as lb

wn = trtl.Screen()
wn.bgcolor("yellow3")


#-----initialize turtle-----

# leaderboard variables
leaderboard_file_name = "a122_leaderboard.txt"
leader_names_list = []
leader_scores_list = []
player_name = input ("Please enter your name: ")

isosceles_triangle = trtl.Turtle()
isosceles_triangle.speed(0)
isosceles_triangle_color = "blue"
isosceles_triangle_shape = "triangle"
isosceles_triangle.penup()


# Game start
game_start = False
start = trtl.Turtle()
start.shape("square")
start.shapesize(3, 7, 0)
start.color("red")

def start_game(x, y):
  global game_start
  game_start = True
  start.hideturtle()
start.onclick(start_game)

while not(game_start):
  isosceles_triangle.hideturtle()

isosceles_triangle.showturtle()
counter = trtl.Turtle()
painter = trtl.Turtle()
score_writer = trtl.Turtle()

# Score box
painter.speed(0)
painter.penup()
painter.setposition(-180, 180)
painter.pendown()
painter.write("Score")
painter.penup()
painter.setposition(-200, 200)
painter.pendown()
for i in range(2):
  painter.forward(70)
  painter.left(90)
  painter.forward(40)
  painter.left(90)
painter.hideturtle()

# Countdown timer
painter.penup()
painter.setposition(165, 180)
painter.pendown()
painter.write("Timer")
painter.penup()
painter.setposition(240, 200)
painter.pendown()
for i in range(2):
  painter.backward(130)
  painter.right(90)
  painter.backward(40)
  painter.right(90)
painter.hideturtle()

# Score
score = 0
font_setup = ("Arial", 20, "normal")
score_writer.speed(0)
score_writer.hideturtle()
score_writer.penup()
score_writer.setposition(-175, 200)
score_writer.write(score, font = font_setup)

# Countdown
counter.hideturtle()
counter.speed(0)
counter.penup()
counter.setposition(120, 200)

font_setup = ("Arial", 20, "normal")
timer = 30
counter_interval = 1000   #1000 represents 1 second
timer_up = False

# Colors & Size
colors = ["yellow", "red", "green", "olive", "aquamarine", "orange", "purple", "pink", "medium purple", "seashell", "navy"]
sizes1 = [0.5, 0.7, 1, 1.5, 2, 2.5, 3, 3.5, 4]
sizes2 = [1.5, 2.8, 3, 4.5, 6, 7.5, 9, 10.5, 12]

#-----game configuration----
isosceles_triangle.shape(isosceles_triangle_shape)
isosceles_triangle.shapesize(1, 3, 0)
isosceles_triangle.fillcolor(isosceles_triangle_color)


#-----game functions--------

# manages the leaderboard for top 5 scorers
def manage_leaderboard():
  
  global leader_scores_list
  global leader_names_list
  global score
  global isosceles_triangle

  # load all the leaderboard records into the lists
  lb.load_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list)

  # TODO
  if (len(leader_scores_list) < 5 or score > leader_scores_list[4]):
    lb.update_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list, player_name, score)
    lb.draw_leaderboard(leader_names_list, leader_scores_list, True, isosceles_triangle, score)

  else:
    lb.draw_leaderboard(leader_names_list, leader_scores_list, False, isosceles_triangle, score)


def isosceles_triangle_clicked(x, y):
  global timer
  if timer_up == False:
    update_score()
    change_color()
    change_size()
    change_position()

def change_position():
  new_xpos = rand.randint(-200, 200)
  new_ypos = rand.randint(-150, 150)
  isosceles_triangle.hideturtle()
  isosceles_triangle.setposition(new_xpos, new_ypos)
  isosceles_triangle.showturtle()

def update_score():
  global score
  score += 1
  score_writer.clear()
  score_writer.write(score, font = font_setup)

def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    isosceles_triangle.hideturtle()
    counter.write("Time's Up", font=font_setup)
    timer_up = True
    manage_leaderboard()
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval) 

def change_color():
  isosceles_triangle.color(rand.choice(colors))
  isosceles_triangle.stamp()
  isosceles_triangle.color("blue")

def change_size():
  rand_index = rand.randint(0, 8)
  isosceles_triangle.shapesize(sizes1[rand_index], sizes2[rand_index], 0)

#-----events----------------
isosceles_triangle.onclick(isosceles_triangle_clicked)

wn.ontimer(countdown, counter_interval) 
wn.mainloop()