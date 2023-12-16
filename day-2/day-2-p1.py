import re, os

class Game:
    def __init__(self, game_id):
        self.game_id = game_id
        self.rounds = []

    def add_round(self, round_data):
        self.rounds.append(round_data)

    def get_rounds(self):
        return self.rounds
    
    def get_game_id(self):
        return self.game_id
        print(f"game_id: {game_id}")

#open the file
file = open("input.txt", "r")
#read the file
data = file.read()
#split the data into a list of words on new lines
words = data.split("\n")
#split the game data into a list of words on ,
games = []
for i,word in  enumerate(words):
    game_id = int(word.split(':')[0].split(' ')[1])
    rounds = []
    #print break line
    #print(f"+"*os.get_terminal_size().columns)
    #print(f"game_id: {game_id}")
    games.append(Game(game_id))
    for round  in word.split(':')[1].split(';'):
        #print(f"round: {round.split(',')}")
        rounds_data = {}
        for round_data in round.split(','):
            rounds_data[round_data.split(' ')[2]] = int(round_data.split(' ')[1])
            #print(f"round_data: {rounds_data}")
        games[i].add_round(rounds_data)

t = []
games_max_rounds = {}

for game in games:
    invalid = False
    print(f"="*os.get_terminal_size().columns)
    print(f"game_id: {game.get_game_id()}")
    for round in game.get_rounds():
        # if red is not None and its value is less than or equal to 12
        if (
            (round.get("red")  is not None and round.get("red") > 12) or
            (round.get("blue") is not None and round.get("blue") > 14) or
            (round.get("green") is not None and round.get("green") > 13)
        ):
            invalid = True
            #print(f"game_id: {game.get_game_id()} is valid")
            #print(f"round: {round}")

        #intialize an array of max rounds for each color
        if games_max_rounds.get(game.get_game_id()) is None:
            games_max_rounds[game.get_game_id()] = {}
            for color in ["red", "blue", "green"]:
                games_max_rounds[game.get_game_id()][color] = 0

        for color in ["red", "blue", "green"]:
            if round.get(color) is not None:
                if round.get(color) > games_max_rounds.get(game.get_game_id(), {}).get(color, 0):
                    print(f"color: {color}: {round.get(color)} is greater than {games_max_rounds.get(game.get_game_id(), {}).get(color, 0)}")
                    games_max_rounds[game.get_game_id()].update({color: round.get(color)})
                    print (f"games_max_rounds: {games_max_rounds[game.get_game_id()]}")
                    continue
                
        
    if not invalid:
        print(f"game_id: {game.get_game_id()} is valid")
        t.append(game.get_game_id())
total_for_max_rounds = 0
#interate over the games max rounds and multiply the values of each color and sum the answers
for game_id, game_max_rounds in games_max_rounds.items():
    print(f"game_id: {game_id}")
    print(f"game_max_rounds: {game_max_rounds}")
    print(f"game_max_rounds.values(): {game_max_rounds.values()}")
    print(f"game_max_rounds.values(): {list(game_max_rounds.values())}")
    total_for_max_rounds += game_max_rounds.get("red", 0) * game_max_rounds.get("blue", 0) * game_max_rounds.get("green", 0)

print(f"total_for_max_rounds: {total_for_max_rounds}")