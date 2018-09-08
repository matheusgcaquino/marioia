
import marioai
import agents
import random

def main():
    f = open('database.txt', 'w')
    #agent = agents.RandomAgent()
    agent = agents.TestAgent()
    task = marioai.Task()
    exp = marioai.Experiment(task, agent)
    exp.max_fps = 50

    for i in range(0, 10):
        task.env.level_type = random.randint(0, 2)
        task.env.level_difficulty = random.randint(0, 15)
        task.env.init_mario_mode = random.randint(0, 2)
        exp.doEpisodes()

        f.write(agent.vision.__str__() + " - " + agent.rew.__str__() + '\n')
        agent.vision = []

    f.close()



if __name__ == '__main__':
    main()
