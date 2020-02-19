####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####
def move(my_history, their_history, my_score, their_score):
  '''always betrays except for one collude in the beginning'''
  if len(my_history) == 0:
    return 'c'
  else:
    return 'b'

     