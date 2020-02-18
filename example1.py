####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'E1'
strategy_name = 'Betray based on last 3 rounds'
strategy_description = 'Betray 75% unless colluded within last 3 rounds.'
''
import random
    
def move(my_history, their_history, my_score, their_score):
  if 'c' in their_history[-3:]: # If the other player has colluded within last 3 rounds 
    return 'c'    # collude.
  else:
    if random.random()<0.25: # 25% of the other rounds
      return 'c'         # collude
    else:
      return 'b'         # but 75% of the time betray
