####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'Rush Hour'
strategy_name = 'Random'
strategy_description = 'everything is completly random'
import random
listss = [0, 1]
def move(my_history, their_history, my_score, their_score):
  '''randomly chooses either c or b
    '''
  guess = random.choice(listss)
  if guess == 0:
    return 'c'
  if guess == 1:
    return 'b'
    