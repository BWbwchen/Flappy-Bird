import time
import random
import sys
import json

# 0 ~ 149
#DISTANCE = 150
DISTANCE = 288
# -402 ~ 500
HEIGHT = 902


# 0 for not jump 1 for jump
class AI :
    def __init__ (self) :
        self.__init_q_value()
        self.GAMMA = 0.7
        self.ALPHA = 0.7
        # bird's y 
        self.pre_state = 206

    def __init_q_value (self) :
        global DISTANCE 
        # TODO : add if we already have data
        fil = open("data.json", "r")

        self.q_value = json.load(fil)['1']
        #self.q_value = [[0, 0]] * (DISTANCE * HEIGHT)


    def __learning (self, bird, tube_list, score) :
        # initial q table
        while score < 10 :
            now_state = self.__make_state(bird, tube_list)
        pass


    def __make_state(self, bird, tube_list):
        # state = delta_y * 150 + delta_x

        target_tube = None
        # find the target tube
        for i, val in enumerate(tube_list):
            if val.tube_x > (bird.x + bird.size//2) :
                target_tube = val
                break

        if target_tube is None:
            return int(288 - bird.x)
        # range 0 ~ 149
        delta_x = target_tube.tube_x - (bird.x + bird.size//2)

        # range -402 ~ 500
        # -500 is offset
        delta_y = bird.y - target_tube.tube_height + target_tube.tube_gap + 402

        state = delta_y * 211 + delta_x
        return int(state)

    def get_action (self, bird, tube_list, score) :
        state = self.__make_state(bird, tube_list)
        self.pre_state = state
        if self.q_value[state][0] < self.q_value[state][1] :
            return True
        elif self.q_value[state][0] > self.q_value[state][1] :
            return False
        else :
            return False


    def request_reward (self, action, dead, bird, tube_list):
        if dead :
            reward = -1000
        else :
            reward = 100

        now_state = self.__make_state(bird, tube_list)

        if self.q_value[now_state][0] < self.q_value[now_state][1] :
            MAX = self.q_value[now_state][1]
        elif self.q_value[now_state][0] >= self.q_value[now_state][1] :
            MAX = self.q_value[now_state][0]

        self.q_value[self.pre_state][int(action)] = \
                (1 - self.ALPHA) * self.q_value[self.pre_state][int(action)] + \
                self.ALPHA * (reward + self.GAMMA * MAX)
        
    def store_date (self) :
        data = {}
        data['1'] = self.q_value
        with open('data.json', 'w') as outfile:
            json.dump(data, outfile)



