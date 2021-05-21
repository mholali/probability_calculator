import copy
import random

class Hat:
    def __init__(self, **variable_arguments):
        self.coloured_balls_created_in_hat = variable_arguments
        contents_list = [(key, value) for key, value in self.coloured_balls_created_in_hat.items()]
        contents = []
        for x_contents_list_items in contents_list:
            for _ in range(x_contents_list_items[1]):
                contents.append(x_contents_list_items[0])
        self.contents = contents
        
    def draw(self, number_of_balls_to_draw_from_the_hat):
        self.number_of_balls_to_draw_from_the_hat = number_of_balls_to_draw_from_the_hat
        container_list_from_which_balls_will_be_drawn_from = self.contents
        container_list_of_randomly_selected_balls = []
        
        if number_of_balls_to_draw_from_the_hat < len(container_list_from_which_balls_will_be_drawn_from):       
            for _ in range(self.number_of_balls_to_draw_from_the_hat):
                select_a_ball_randomly = random.choice(container_list_from_which_balls_will_be_drawn_from)
                container_list_from_which_balls_will_be_drawn_from.remove(select_a_ball_randomly)
                container_list_of_randomly_selected_balls.append(select_a_ball_randomly)
            
            return container_list_of_randomly_selected_balls
              
        else:
            return container_list_from_which_balls_will_be_drawn_from 

            
    # def __str__(self):
    #     return str(self.contents)

        # return (f"Random Balls drawn = {self.container_of_randomly_drawn_balls}" + 
        #         " and " + 
        #         f"Balls left = {self.contents}") 


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    count = 0
    expected_ball_colours = []
    expected_ball_colours_reversed = []
    
    # create a list with the colors of the balls we want to draw
    for _ in expected_balls:
        expected_ball_colours.append(_)
    
    # same list but reversed
    for _ in range(len(expected_ball_colours) - 1, -1, -1):
        expected_ball_colours_reversed.append(expected_ball_colours[_])

    # Each experiment consists of starting with a hat containing the specified balls, drawing a number of balls
    for _ in range(0, num_experiments, 1):
        # copy of the hat object so we don't modify the hat object directly
        copy_of_hat = copy.deepcopy(hat)

        # balls drawn from the hat object copy
        random_balls_drawn = copy_of_hat.draw(num_balls_drawn)

        # create a list to know th balls we checked from the balls drawn
        colour_of_random_ball_drawn = []

        # for every balls drawn check the color of it
        for colour in random_balls_drawn:
            # if the color is expected and not checked yet
            if (colour in expected_balls) and (colour not in colour_of_random_ball_drawn):
                # add it to the colors checked list if the the ball concerned appears at least the number of times expected
                if (random_balls_drawn.count(colour) >= expected_balls[colour]):
                    colour_of_random_ball_drawn.append(colour)
                # checking if we got the balls we were attempting to draw
                if (colour_of_random_ball_drawn == expected_ball_colours) or (colour_of_random_ball_drawn == expected_ball_colours_reversed):
                    count += 1
                    break
    # The experiment function should return a probability calculated and returned
    return count / num_experiments

hat1 = Hat(black=6, red=4, green=3)
hat1.draw(5)
hat1.draw(4)

hat1 = Hat(black=6, red=4, green=3)
experiment(hat=hat1,
            expected_balls={"red":2, "green":1},
            num_balls_drawn=5,
            num_experiments=2000)

hat2 = Hat(blue=3, red=2, green=6)
experiment(hat=hat2,
            expected_balls={"blue":2,"green":1},
            num_balls_drawn=4,
            num_experiments=1000) #ans = 0.26---0.272---0.28

hat3 = Hat(yellow=5,red=1,green=3,blue=9,test=1)
experiment(hat=hat3,
            expected_balls={"yellow":2,"blue":3,"test":1},
            num_balls_drawn=20,
            num_experiments=100) #ans = 1.0

hat4 = Hat(blue=3, red=2, green=6)
experiment(hat=hat4,
            expected_balls={"blue":2,"green":1},
            num_balls_drawn=4,
            num_experiments=3000)

hat5 = Hat(blue=4, red=2, green=6)
experiment(hat=hat5,
            expected_balls={"blue":2,"red":1},
            num_balls_drawn=4,
            num_experiments=3000)