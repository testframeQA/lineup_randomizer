import json
import random
import argparse
import csv

def randomize_players_and_write_to_file(roster_file, lineup_file):
    with open(roster_file, 'r') as json_file:
        data = json.load(json_file)

    players = data["players"]
    random.shuffle(players)

    with open(lineup_file, 'w', newline='') as csv_file:
        fieldnames = ['Batting', 'Player', 'Jersey']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()
        for i, player in enumerate(players, start=1):
            row = {
                'Batting': i,
                'Player': player['name'],
                'Jersey': player['number']
            }
            writer.writerow(row)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument('-y', '--year', required=True, help='Provide Year as String')
    parser.add_argument('-s', '--season', required=True, help='Provide Season as String')
    parser.add_argument('-w', '--week', required=True, help='Provide Week Number as String')
    args = parser.parse_args()

    roster_file = f"./rosters/{args.year}/{args.season}/roster_{args.year}_{args.season}.json"
    lineup_file = f"./generated_lineups/{args.year}/{args.season}/week_{args.week}_lineup_randomized.csv"

    randomize_players_and_write_to_file(roster_file, lineup_file)
