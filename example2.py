####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'E2'
strategy_name = 'Alternate'
strategy_description = 'Collude, then alternate.'
    
def move(my_history, their_history, my_score, their_score):
  for i in their_history:
    if i == 'b':
      i = 'c'

  if len(my_history) == 0:
    return 'c'
  else:
    return 'b'
  
  