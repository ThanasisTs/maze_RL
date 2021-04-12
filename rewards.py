from maze3D.utils import get_distance_from_goal


reward_type, goal_reward, state_reward = None, None, None
def main(config):
	global reward_type, goal_reward, state_reward
	reward_type = config['SAC']['reward_function'] if 'SAC' in config.keys() else None
	goal_reward = config['SAC']['goal_reward'] if 'SAC' in config.keys() else None
	state_reward = config['SAC']['state_reward'] if 'SAC' in config.keys() else None

def reward_function_maze(done, timedout, goal=None):
	if reward_type == "Sparse" or reward_type == "sparse":
		return reward_function_sparse(done, timedout)
	elif reward_type == "Dense" or reward_type == "dense":
		return reward_function_dense(done, timedout, goal=goal)
	elif reward_type == "Sparse_2" or reward_type == "sparse_2":
		return reward_function_sparse2(done, timedout)

def reward_function_sparse(done, timedout):
	# for every timestep state_reward
	# timed out -50
	# reach goal goal_reward
	if done and not timedout:
		return goal_reward
	if timedout:
		return -50
	return state_reward

def reward_function_sparse2(done, timedout):
	# For every timestep -1
	# Reach goal +100
	if done and not timedout:
		return goal_reward
	return state_reward

def reward_function_dense(done, timedout, ball, goal=None):
	# for every timestep -target_distance
	# timedout -50
	# reach goal +goal_reward
	if done:
		return goal_reward
	if timedout:
		return -50
	target_distance = get_distance_from_goal(ball, goal)

def reward_function(timedout, goal=None):
	if done:
		return goal_reward
	# Construct here the mathematical reward function
	# The reward function can depend on time, the distance of 
	# the ball to the goal, it can be static or anything else
	# Default is static
	return -1		

if __name__ == "__main__":
	main(config)