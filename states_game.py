import pandas
import turtle

# Setting up the screen
screen = turtle.Screen()
screen.title("Indian States Game")
screen.setup(height=610, width=560)
image = "map.gif"
screen.addshape(image)
turtle.shape(image)

# Code to get coordinates of any point on screen
# def get_mouse_click_coordinates(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coordinates)

# Turtle for writing states name and you won statement
cursor = turtle.Turtle()
cursor.hideturtle()
cursor.penup()

# Reading data from csv file and creating list of state names - original and states
data = pandas.read_csv("states_game.csv")
states_list = data["state"].values

# Required variables for the game
correct_guesses = 0
last_answer_status = 1  # 1-last answer correct, 2-last answer wrong, 3-last answer correct but already answered before
answered_states = []

# Game main logic
while correct_guesses < 30:
    if last_answer_status == 1:
        user_answer = screen.textinput(title=f"Correct guesses:{correct_guesses}/30",
                                       prompt="Guess a state: ")
    elif last_answer_status == 2:
        user_answer = screen.textinput(title=f"Correct guesses:{correct_guesses}/30",
                                       prompt="Wrong answer! Guess again:")
    elif last_answer_status == 3:
        user_answer = screen.textinput(title=f"Correct guesses:{correct_guesses}/30",
                                       prompt="Already answered! Guess another state:")
    if user_answer is None:
        exit()  # or handle the cancellation in another way
    else:
        user_answer = user_answer.title().strip()
    if user_answer == "Exit":
        missing_states = [state for state in states_list if state not in answered_states]
        df = pandas.DataFrame(missing_states)
        df.to_csv("states_to_learn.csv")
        exit()
    elif user_answer in states_list and user_answer not in answered_states:
        correct_guesses += 1
        answered_states.append(user_answer)
        coordinates_data = data[data.state == user_answer]
        cursor.goto(coordinates_data.x.values[0], coordinates_data.y.values[0])
        cursor.write(user_answer, align="center",
                     font=("Verdana", 8, "bold"))
        last_answer_status = 1
    elif user_answer in states_list and user_answer in answered_states:
        last_answer_status = 3
    else:
        last_answer_status = 2

cursor.goto(0, 0)
cursor.write("CONGRATS! YOU WON :)", align="center", font=("Verdana", 30, "bold"))

turtle.mainloop()  # to keep screen open
