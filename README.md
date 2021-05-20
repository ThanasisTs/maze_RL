# Maze 3D Collaborative Learning on shared task

### Description
A human-agent collaborative maze game, solvable only through collaboration. The agent is an Reinforcement Learning (RL). The Soft-Actor Critic (SAC) algorithm is used based on [SLM Lab work](https://github.com/kengz/SLM-Lab) and modifications based on [this work](https://arxiv.org/abs/1910.07207) for discrete action space.The virtual environment of the game is based on [this work](https://github.com/amengede/Marble-Maze). The idea of the game is based on [this work](https://arxiv.org/abs/2003.01156). 


### Installation
* Run `source install_dependencies/install.sh`. A python virtual environment will be created and the necessary libraries will be installed. Furthermore, the directory of the repo will be added to the `PYTHONPATH` environmental variable.

### Run
* Run `python game/maze3d_human_only_test.py game/config/config_human_test.yaml` for human-only game.
* Run `python game/sac_maze3d_train.py game/config/<config_sac> <participant_name>` for human-agent game.
  * Notes before training: 
     * Set the <participant_name> to your name.
     * The program will create a `/tmp` and a `/plot` folder (if they do not exist). The `/tmp` folder contains CSV files with information of the game. The `/plot` folder contains figures for tha game.
     * The program will automatically create an identification number after your name on each folder name created

### Configuration
* In the game/config folder exist several YAML files for the configuration of the game. The main parameters (which are usually modified) and their descriptions are listed here. The description of each parameter lies in the YAML files
    * `game/discrete`: True in the keyboard input is discrete (False for continuous).
    * `SAC/reward_function`: Type of reward function.
    * `Experiment/loop`: Choose how the game will be terminated. Currently the game can be terminated either when a number of episodes or a number of interactions is completed.
    * `SAC/discrete`: Discrete or normal SAC (Currently only the discrete SAC is compatible with the game)
  
### Play
* `Human only`: Use keyboard keys to control the tilt of the tray around the vertical and horizontal axis
* `Human-Agent`: Use left and right arrows to control the tilt of the tray around its vertical(y) axis
* Press once the spacekey to pause and a second time to resume
* Press q to exit the experiment.

