import random

def prs(user_action, my_action):
    rules = {
        'paper': {'scissors': True, 'rock': False},
        'rock': {'paper': True, 'scissors': False},
        'scissors': {'paper': True, 'rock': False}
    }
    return rules[user_action][my_action]

actions = ['paper', 'rock', 'scissors']
my_action = random.choice(actions)

user_action = str(input('(paper), (rock), (scissors)\nChose your action: '))

outcomes = {
    True: 'You win!',
    False: 'You lose!',
    'Draw': 'Draw'
}

print(outcomes[prs(user_action, my_action)])