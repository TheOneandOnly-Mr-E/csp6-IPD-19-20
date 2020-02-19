####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'Rush Hour'
strategy_name = 'History Manipulation'
strategy_description = 'Convert all of their bs to cs'
    
def move(my_history, their_history, my_score, their_score):
  'changes their history to all collude while ours is all betray with one collude at the start'
  if len(my_history) == 0:
    return 'c'
  else:
    return 'b'

  for i in their_history:
    if i == 'b':
      i = 'c'
