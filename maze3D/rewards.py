def reward_function_maze(self, timedout, goal_reward, state_reward, goal=None):
    if self.reward_type == "Sparse" or self.reward_type == "sparse":
        return self.reward_function_sparse(timedout, goal_reward, state_reward)
    elif self.reward_type == "Dense" or self.reward_type == "dense":
        return self.reward_function_dense(timedout, goal_reward, state_reward, goal=goal)
    elif self.reward_type == "Sparse_2" or self.reward_type == "sparse_2":
        return self.reward_function_sparse2(timedout, goal_reward, state_reward)

def reward_function_sparse(self, timedout, goal_reward, state_reward):
    # For every timestep -1
    # Timed out -50
    # Reach goal +100
    if self.done and not timedout:
        # solved
        return goal_reward
    # if not done and timedout
    if timedout:
        return -50
    # return -1 for each time step
    return state_reward


def reward_function_sparse2(self, timedout, goal_reward, state_reward):
    # For every timestep -1
    # Timed out -50
    # Reach goal +100
    if self.done and not timedout:
        # solved
        return goal_reward
    # return -1 for each time step
    return state_reward

def reward_function_dense(self, timedout, goal_reward, state_reward, goal=None):
    # For every timestep -target_distance
    # Timed out -50
    # Reach goal +goal_reward
    if self.done:
        # solved
        return goal_reward
    # if not done and timedout
    if timedout:
        return -50
    # return -target_distance/10 for each time step
    target_distance = get_distance_from_goal(self.board.ball, goal)
    return -target_distance / 10