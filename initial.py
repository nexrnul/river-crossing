#importcopy
# Define a function that takes in a state as a dictionary and returns True if the state meets the conditions and False if it does not
def isValid(state):
    if state["wolf"] is not state["person"] and state["wolf"] == state["goat"]:
        return False
    elif state["goat"] is not state["person"] and state["goat"] == state["cabbage"]:
        return False
    else:
        return True

# Define a function that takes in a state as a dictionary and returns a list of all valid states that can be reached from 1 move of the input state
# This function will need to call the function isValid(state)
def get_next_states(state):
    
    next_state = []
    same_side = []

    for thing in state:
            if state[thing] == state["person"] and thing is not "person":
                same_side.appened(thing)

    for thing in same_side:
        next_state = copy.deepcopy(state)
        next_state[thing] = not state[thing]
        next_state["person"] = not state ["person"]

        if isValid(next) == True:
            next_states.append(next_state)
    
    persone_alone = copy.deepcopy(state)
    person_alone["person"] = not state["person"]

    if isValid(person_alone) == True:
        next_states.append(person_alone)

    return next_states

# Define a recursive function that takes in a current_state and win_state and returns the path to those states using the Depth First Search algorithm
# This function will need to call the function get_next_states(state), as well as itself
def dfs(present_state, win_state):
    
    if present_state == win_state:
        return True
    next_states = get_next_states(present_state)
    past_states.append(present_state)

    for state in next_state:
        if not in past_states:
            path.append(state)
            if dfs(state, win_state) == True:
                return True
    
    
# Test your code! Does it solve the river crossing riddle?
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

visited_states = [initial_state]
path = []

if dfs(initial_state, win_state):
    for index, step in enumerate(path):
        print("After move", index+1, "the state is ", step)
else:
    print("No solution found.")