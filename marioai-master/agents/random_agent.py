import random
import marioai
import pandas as pd
from sklearn import tree
import numpy as np
from sklearn.model_selection import train_test_split

__all__ = ['RandomAgent']
__all__ = ['TestAgent']
testar = True

class RandomAgent(marioai.Agent):
    def act(self):
        esq = 0
        dire = 1
        baixo = 0
        pulo = 0
        fogo = 0
        
        self.vision += esq.__str__() + dire.__str__() + baixo.__str__() + pulo.__str__() + fogo.__str__() + "\n"

        return [0, 1, random.randint(0,1), random.randint(0, 1), random.randint(0, 1)]
        #return [esq, dire, baixo, pulo, fogo]


class TestAgent(marioai.Agent):
    if testar == True:
        df = pd.read_csv('database_old2.csv', header=None, sep=",")

        X = df.iloc[:, 1:].values
        y = df.iloc[ :, -1:].values
        


        X_train, X_test, y_train, y_test = \
            train_test_split(X, y, test_size=0.9, random_state=0)

        clf = tree.DecisionTreeClassifier()
        clf = clf.fit(X, y)

    vision = ""
    rew = 0

    def sense(self, obs):
        super(TestAgent, self).sense(obs)
       
        
        #self.vision += self.level_scene.__str__()
        

    def act(self):
        

        pulo = random.randint(0, 1)
        dire = 1
        fogo = 0
        baixo = 0
        
        if (len(self.enemies_floats) > 0):
            fogo = random.randint(0,1)
            baixo = random.randint(0,1)

        esq = 0
        
        """
            e d b p f
            0 1 0 0 0 = 8
            0 1 0 0 1 = 9
            0 1 0 1 0 = 10
            0 1 0 1 1 = 11
            
        """
        if testar == True:
            self.vision = []
        
        for x in range(9, 13):
            for y in range(9, 13):  
                if x == 9 and y == 9: 
                    self.vision += ""
                else:
                    self.vision += ","
                self.vision += str(self.level_scene[x][y])
        
        #if testar == False:
            #self.vision = self.level_scene        

        if testar == True:
            #print self.vision
            acao = self.clf.predict(self.vision)
            print acao


        jog = esq.__str__() + dire.__str__() + baixo.__str__() + pulo.__str__() + fogo.__str__();
        valor = 0
        if jog == "01000": 
            valor = 8

        if jog == "01001":
            valor = 9
        
        if jog == "01010":
            valor = 10

        if jog == "01011":
            valor = 11

        if jog == "00100":
            valor = 4
        
        if jog == "00000":
            valor = 0

        #esq.__str__() + dire.__str__() + baixo.__str__() + pulo.__str__() + fogo.__str__() 

        if testar == False:
            self.vision += valor.__str__() + "\n"

        return [esq, dire, baixo, pulo, fogo]


    def give_rewards(self, reward, cum_reward):
            self.rew = reward

    #def bin_to_act(str) 