import time
import random
DISTANCE = 150
HEIGHT = 390
class AI :
    def __init__ (self) :
        self.__init_q_value()

    def __init_q_value (self) :
        global DISTANCE 
        # TODO : add if we already have data
        self.q_value = [[0, 0]] * (DISTANCE * HEIGHT)


    def __learning (self, bird, tube_list, score) :
        # initial q table
        while score < 10 :
            now_state = self.__make_state(bird, tube_list)
        pass


    def __make_state(self, bird, tube_list):
        pass

    def get_action (self, bird, tube_list, score) :
        #action = self.__learning(bird, tube_list, score)
        random.seed(time.time())
        t = random.randrange(0, 10)
        if t < 1 :
            action = True
        else :
            action = False
        return False

    def store_date (self) :
        pass



