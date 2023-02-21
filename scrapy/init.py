import os

os.system("scrapy crawl proBStats -O ../dist/dataset_proBstats.json")
os.system("scrapy crawl playersInformation -O ../dist/dataset_proBPlayers.json")
os.system("python script_clean_duplicate_players.py")