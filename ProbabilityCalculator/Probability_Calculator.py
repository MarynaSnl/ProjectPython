import random
import copy
class Hat:
    def __init__(self, **kvargs):
        self.contents = [key for key, value in kvargs.items() for y in range(0, value ) ]  
        if self.contents == []:
            print("Error. Mast be at least one ball. ")
            return False
        self.__initial_contents = copy.deepcopy(self.contents)

    def draw(self, number_balls):
        # Refill the hat if empty or <
        if number_balls >= len(self.__initial_contents):
            return self.__initial_contents
        if number_balls >= len(self.contents):
            self.contents = copy.deepcopy(self.__initial_contents)
        selected_balls = []
        for i in range(number_balls,0,-1):
            num = random.randrange(0, len(self.contents))
            selected_balls.append(self.contents[num])
            self.contents.pop(num)
        # Refill the hat if empty
        if len(self.contents) == 0:
            self.contents = copy.deepcopy(self.__initial_contents)
        selected_balls.sort()    

        #cc = {}
        #for x in selected_balls:
        #    cc[x] = cc.get(x,0) + 1
        #return cc 
        return selected_balls
    
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    if num_experiments == 0:
        print("Error. Number experiments can't be 0.")
        return 0
    number_successful = 0
    for i in range(0,num_experiments):
        #rez_one_exp = hat.draw(num_balls_drawn)
        rez_one_exp_list = hat.draw(num_balls_drawn)
        rez_one_exp = {}
        for x in rez_one_exp_list:
             rez_one_exp[x] = rez_one_exp.get(x,0) + 1
       
        len_expected_balls = len(expected_balls)
        for x, y in expected_balls.items():
            if rez_one_exp.get(x,0) >= y:
                len_expected_balls -= 1
        if len_expected_balls ==0:
            number_successful += 1 
    return number_successful/num_experiments
