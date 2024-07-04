import numpy as np

gamma = 0.75 # discount factor
alpha = 0.9 # learning rate

# States s
location_to_state = {"A": 0,
                    "B": 1,
                    "C": 2,
                    "D": 3,
                    "E": 4,
                    "F": 5,
                    "G": 6,
                    "H": 7,
                    "I": 8,
                    "J": 9,
                    "K": 10,
                    "L": 11
                    }
# Actions a
actions = [0,1,2,3,4,5,6,7,8,9,10,11]

# Reward of action in some state R(s,a)
# rows correspond to the states, and the columns correspond to the actions
R = np.array([[0,1,0,0,0,0,0,0,0,0,0,0],
[1,0,1,0,0,1,0,0,0,0,0,0],
[0,1,0,0,0,0,1,0,0,0,0,0],
[0,0,0,0,0,0,0,1,0,0,0,0],
[0,0,0,0,0,0,0,0,1,0,0,0],
[0,1,0,0,0,0,0,0,0,1,0,0],
[0,0,1,0,0,0,0,1,0,0,0,0],
[0,0,0,1,0,0,1,0,0,0,0,1],
[0,0,0,0,1,0,0,0,0,1,0,0],
[0,0,0,0,0,1,0,0,1,0,1,0],
[0,0,0,0,0,0,0,0,0,1,0,1],
[0,0,0,0,0,0,0,1,0,0,1,0]])


#PART 2 - BUILDING THE AI SOLUTION WITH Q-LEARNING

# Making a mapping from the states to the locations
state_to_location = {state: location for location, state in location_to_state.items()}
# Making the final function that will return the route
def route(starting_location, ending_location):
    R_new = np.copy(R) # do not modify rewards matrix. create new and alter it depending on end state
    ending_state = location_to_state[ending_location] # find coresponding number of location
    R_new[ending_state, ending_state] = 1000 #set reward for end state
    Q = np.array(np.zeros([12,12])) # Initial Q values

    # Learning process
    for i in range(1000):
        current_state = np.random.randint(0,12) # select random state
        playable_actions = []
        # go through all reward matrix, for all possible actions (R>0) 
        # play random action
        for j in range(12):
                # in current state, go trough all actions j and for R>0 add to playable actions list
            if R_new[current_state, j] > 0:
                playable_actions.append(j)
        # reach the next state and get reward
        next_state = np.random.choice(playable_actions)
        # calculate temporal difference
        # R_new[current_state, next_state] => Reward of played action in current state
        # gamma => discount factor
        # Q[next_state, np.argmax(Q[next_state,])] => Q value of the best action played in future state (next_state)
        # Q[current_state, next_state] => Q value of action played in current state
        TD = R_new[current_state, next_state] + gamma * Q[next_state, np.argmax(Q[next_state,])] - Q[current_state, next_state]
        # update Q values matrix 
        # alpha => learning rate
        Q[current_state, next_state] = Q[current_state, next_state] + alpha * TD
    # print(Q.astype(int)) # uncomment to see calculated Q values

    route = [starting_location]
    next_location = starting_location
    #making moves
    while (next_location != ending_location):
        starting_state = location_to_state[starting_location] # convert location to numeric value
        next_state = np.argmax(Q[starting_state,]) # on the starting state row we search for max q value column
        next_location = state_to_location[next_state]
        route.append(next_location)
        starting_location = next_location
    return route

# adding an intermediate location to go through
def best_route(starting_location, intermediary_location, ending_location):
    return route(starting_location, intermediary_location) + route(intermediary_location, ending_location)[1:]
# Printing the final route
print("Route: ")
print(best_route("H","G","K"))