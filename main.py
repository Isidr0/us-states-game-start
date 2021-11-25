import turtle
import pandas

# set up map background and rest of screen
screen = turtle.Screen()
write_state = turtle.Turtle()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
turtle.addshape(image)
turtle.shape(image)
screen.tracer(0)

# import states CSV
states = pandas.read_csv("50_states.csv")
state_name = states.state


# write correct guess onto map in correct position
def write_state_name():
    state_x = int(states[states.state == s].x)
    state_y = int(states[states.state == s].y)
    write_state.penup()
    write_state.hideturtle()
    write_state.setpos(state_x, state_y)
    write_state.write(s, align='center', font=('Arial', 12, 'normal'))


# Loop through while user is guessing.
correct_answers = []
game_is_on = True
while game_is_on:
    answer_state = screen.textinput(title=f"{len(correct_answers)}/50 States Correct",
                                    prompt="What's another state's name?").title()
    if answer_state == "Exit":
        # states_to_learn.csv
        state_list = state_name.to_list()
        leftover = []
        for s in state_list:
            if s not in correct_answers:
                leftover.append(s)
        data = pandas.DataFrame(leftover)
        data.to_csv("states_to_learn.csv")
        break
    for s in state_name:
        if answer_state == s:
            write_state_name()
            correct_answers.append(s)
    if len(correct_answers) == 50:
        game_is_on = False

