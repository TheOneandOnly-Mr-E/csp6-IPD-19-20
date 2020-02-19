####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

import random

team_name = 'E1'
strategy_name = 'Betray'
strategy_description = 'Always betray.'
    
def move(my_history, their_history, my_score, their_score):
  random_value = random.randint(100,200)

  
  if random_value == random_value:
    for i in my_history:
      if len(my_history) % random_value == 0:
        return 'c'
      else:
        return 'b'