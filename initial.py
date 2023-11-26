import copy
# define function taking in state as dictionary which returns True if state meets conditions and False if not
def isValid(state):
    if state["wolf"] != state["person"] and state["wolf"] == state["goat"]:
        return False
    elif state["goat"] != state["person"] and state["goat"] == state["cabbage"]:
        return False
    else:
        return True
        
# defines function taking in  state as dictionary, returns list of all valid states reachable from 1move of input state
# function needs to call isValid(state)
def get_next_states(state):
    
    next_states = []
    same_side = []

    for thing in state:
            if state[thing] == state["person"] and thing != "person":
                same_side.append(thing)

    for thing in same_side:
        next_state = copy.deepcopy(state)
        next_state[thing] = not state[thing]
        next_state["person"] = not state ["person"]

        if isValid(next_state) == True:
            next_states.append(next_state)
    
    person_alone = copy.deepcopy(state)
    person_alone["person"] = not state["person"]

    if isValid(person_alone) == True:
        next_states.append(person_alone)

    return next_states

# define recursive function taking in current_state/win_state and returns path to those states by using Depth First Search (DFS) algorithm
# function will need to call get_next_states(state), as well as itself
def dfs(present_state, win_state):

    if present_state == win_state:
        return True
    next_state = get_next_states(present_state)
    past_states.append(present_state)

    for state in next_state:
        if state not in past_states:
            path.append(state)
            if dfs(state, win_state) == True:
                return True
            path.pop()

# test 
initial_state = {
    "wolf": False,
    "goat": False,
    "cabbage": False,
    "person": False
}

win_state = {
    "wolf": True,
    "goat": True,
    "cabbage": True,
    "person": True
}

past_states = [initial_state]
path = []

from termcolor import colored
def print_colored(message, color_code):
    #colored_message = f'<span style="color: \x1b[{color_code}m">{message}</span>'
    colored_message = colored(message, color_code)
    print(colored_message)
print_colored("river crossing problem", 'light_blue')

if dfs(initial_state, win_state):
    for index, step in enumerate(path):
        print("After move", index+1, "the state is ", step)
else:
    print("No solution found.")