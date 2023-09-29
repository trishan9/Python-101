import pandas as pd
import turtle as tu

t = tu.Turtle()
s = tu.Screen()

states_data = pd.read_csv("50_states.csv")
print(states_data)