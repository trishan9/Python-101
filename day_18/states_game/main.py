import pandas as pd
import turtle as tu

t = tu.Turtle()
s = tu.Screen()

t.hideturtle()
t.penup()

s.title("U.S. States Game")
s.setup(width=725, height=491)
s.bgpic("blank_states_img.gif")

states_data = pd.read_csv("50_states.csv")
states_name = states_data["state"].to_list()

def get_x_coordinate(state):
    df = states_data[states_data.state == state]
    series = df.x
    x_coor = series.iloc[0]
    return x_coor

def get_y_coordinate(state):
    df = states_data[states_data.state == state]
    series = df.y
    y_coor = series.iloc[0]
    return y_coor

guesses = 0
score = 0
guessed_states = []

while guesses != len(states_data):
    user_input = (s.textinput(f"{guesses}/{len(states_name)} States Correct", "What's another state name?")).title()
    if user_input in states_name and user_input not in guessed_states:
        guesses += 1
        guessed_states.append(user_input)
        
        t.setposition(get_x_coordinate(user_input), get_y_coordinate(user_input))
        t.write(user_input, align="left", font=("Arial", 8, "normal"))
    elif user_input == "Exit":
        break
else:
    print("You guessed all the states of U.S.")


missed_states = [state for state in states_name if state not in guessed_states]
x_coor = [get_x_coordinate(state) for state in missed_states]
y_coor = [get_y_coordinate(state) for state in missed_states]

states_to_learn = {
    "state": missed_states,
    "x": x_coor,
    "y": y_coor,
}

new_data = pd.DataFrame(states_to_learn)
new_data.to_csv("states_to_learn.csv")