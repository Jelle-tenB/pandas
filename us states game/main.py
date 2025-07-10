import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States game")

image = r"us states game\blank_states_img.gif"
screen.addshape(image)
turtle.Shape(image)

data = pandas.read_csv(r"us states game\all_states.csv")
all_states = data.state.to_list()

score = 0
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{score}/50 States Correct", prompt="What's another state's name?")
    user_guess = answer_state.title()
    if user_guess == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv(r"us states game\states_to_learn.csv")
        break

    if user_guess in all_states and user_guess not in guessed_states:
        score += 1
        guessed_states.append(user_guess)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.color("black")
        state_data = data[data.state == user_guess]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(f"{user_guess}")
