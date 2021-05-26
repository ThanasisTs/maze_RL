from maze3D.utils import get_distance_from_goal


def main(config):
	global reward_type
	reward_type = config['SAC']['reward_function'] if 'SAC' in config.keys() else None

def reward_function_maze(done, timedout, goal=None):
	if reward_type in ["Timeout", "timeout"]:
		return reward_function_timeout_penalty(goal_reached, timedout)
	elif reward_type in ["Distance", "distance"]:
		return reward_function_distance(goal_reached, timedout, goal=goal)
	elif reward_type in ["Shafti", "shafti"]:
		return reward_function_shafti(goal_reached)

def reward_function_timeout_penalty(goal_reached, timedout):
	# for every timestep -1
	# timed out -50
	# reach goal +100
	if goal_reached:
		return 100
	if timedout:
		return -50
	return -1

def reward_function_shafti(goal_reached):
	# For every timestep -1
	# Reach goal +100
	if goal_reached:
		return 100
	return -1

def reward_function_distance(goal_reached, timedout, ball, goal=None):
	# for every timestep -target_distance
	# timedout -50
	# reach goal +100
	if goal_reached:
		return 100
	if timedout:
		return -50
	return get_distance_from_goal(ball, goal)
	

def reward_function(goal_reached, timedout, goal=None):
	if goal_reached:
		return 100
	# Construct here the mathematical reward function
	# The reward function can depend on time, the distance of 
	# the ball to the goal, it can be static or anything else
	# Default is static
	return -1		

if __name__ == "__main__":
	main(config)
