
import marioai
import agents
import random
import csv

def main():
    #f = open('database.data', 'w')

    #agent = agents.RandomAgent()
    agent = agents.TestAgent()
    task = marioai.Task()
    exp = marioai.Experiment(task, agent)
    exp.max_fps = 50

    for i in range(0, 1):
        task.env.level_type = random.randint(0, 2)
        task.env.level_difficulty = random.randint(0, 4)
        task.env.init_mario_mode = random.randint(0, 2)
        exp.doEpisodes()

       # f.write(agent.vision.__str__() + '\n')

        agent.vision = ""
        print agent.rew
    f.close()



if __name__ == '__main__':
    main()
