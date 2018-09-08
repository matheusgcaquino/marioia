import random
import marioai

__all__ = ['RandomAgent']
__all__ = ['TestAgent']

class RandomAgent(marioai.Agent):
    def act(self):
        return [0, 1, 0, random.randint(0, 1), random.randint(0, 1)]


class TestAgent(marioai.Agent):
    vision = []
    rew = 0

    def sense(self, obs):
        super(TestAgent, self).sense(obs)
        self.vision.append(self.level_scene)


    def act(self):

        pulo = random.randint(0, 1)
        dire = 1
        fogo = 0
        
        if (len(self.enemies_floats) > 0):
            fogo = random.randint(0,1)

        esq = 0
        baixo = 0
        # esq, dire, baixo, pulo, fogo
        return [esq, dire, baixo, pulo, fogo]


    def give_rewards(self, reward, cum_reward):
            self.rew = reward
