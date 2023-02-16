import json

with open('dataset_proBPlayers.json') as proB_players_file:
    data = json.load(proB_players_file)

ids = []
for player in data:
    ids.append(player['playerId'])

ids2 = []
with open('dataset_proBstats.json', "r") as proB_stats_file_reading:
    data2 = json.load(proB_stats_file_reading)
    # sort by playerId, and by gamesPlayed descending if same playerId
    sorted_list = sorted(data2, key=lambda x: (x['playerId'], -x['gamesPlayed']))

    for player in sorted_list:
        if player['playerId'] not in ids2:
            ids2.append(player['playerId'])
        else:
            sorted_list.remove(player)

with open('dataset_proBstats.json', "w") as proB_stats_file_writing:
    json.dump(sorted_list, proB_stats_file_writing)