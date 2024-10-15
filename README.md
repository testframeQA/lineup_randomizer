This is a basic randomizer I use for my sons' little league baseball lineups.
The program runs via command line, and requires three arguments to find roster data and correctly route the generated lineup file:

* year
* season
* week

The folder structure year, season (fall or spring), and game week (1-10)
The roster included here, roster_test_fall.json, is a dummy roster. 
Run Command: 
  python lineup_randomizer.py y test s fall w 1
The program will then:
  * load roster_test_fall.json into a variable called "players"
  * shuffle index order of "players"
  * create generated lineup file with fieldnames "Batting", "Player", "Jersey"
  * assign batting order position to "Batting" field
  * assign player name to "Player" field
  * assign jersey number to "Jersey" field
  * write each player in the roster line-by-by in the shuffled order

lineup_randomizer.py load
