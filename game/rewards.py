from maze3D.utils import get_distance_from_goal


def main(config):
	global reward_type
	reward_type = config['SAC']['reward_function'] if 'SAC' in config.keys() else None

def reward_function_maze(done, timedout, goal=None):
	if reward_type in ["Timeout", "timeout"]:
		return reward_function_timeout_pentalty(done, timedout)
	elif reward_type in ["Distance", "distance"]:
		return reward_function_distance(done, timedout, goal=goal)
	elif reward_type in ["Shafti", "shafti"]:
		return reward_function_shafti(done, timedout)

def reward_function_timeout_pentalty(done, timedout):
	# for every timestep -1
	# timed out -50
	# reach goal +100
	if done and not timedout:
		return 100
	if timedout:
		return -50
	return -1

def reward_function_shafti(done, timedout):
	# For every timestep -1
	# Reach goal +100
	if done:
		return 100
	if timedout:
		return -1
	return -1

def reward_function_distance(done, timedout, ball, goal=None):
	# for every timestep -target_distance
	# timedout -50
	# reach goal +100
	if done:
		return 100
	if timedout:
		return -50
	target_distance = get_distance_from_goal(ball, goal)

def reward_function(timedout, goal=None):
	if done:
		return 100
	# Construct here the mathematical reward function
	# The reward function can depend on time, the distance of 
	# the ball to the goal, it can be static or anything else
	# Default is static
	return -1		

if __name__ == "__main__":
	main(config)
