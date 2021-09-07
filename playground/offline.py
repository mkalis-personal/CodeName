from codenames.game.base import TeamColor
from codenames.game.builder import words_to_random_board
from codenames.game.manager import GameManager
from codenames.solvers.cli_players import CliHinter, CliGuesser

words = [
    "cloak",
    "kiss",
    "flood",
    "mail",
    "skates",
    "paper",
    "frog",
    "skyscraper",
    "moon",
    "egypt",
    "teacher",
    "avalanche",
    "newton",
    "violet",
    "drill",
    "fever",
    "ninja",
    "jupiter",
    "ski",
    "attic",
    "beach",
    "lock",
    "earth",
    "park",
    "gymnast",
    "king",
    "queen",
    "teenage",
    "tomato",
    "parrot",
    "london",
    "spiderman",
]

board = words_to_random_board(words=words)
blue_hinter = CliHinter("Leonardo", team_color=TeamColor.BLUE)
blue_guesser = CliGuesser("Bard", team_color=TeamColor.BLUE)
red_hinter = CliHinter("Adam", team_color=TeamColor.RED)
red_guesser = CliGuesser("Eve", team_color=TeamColor.RED)
game_manager = GameManager(blue_hinter, red_hinter, blue_guesser, red_guesser)
game_manager.run_game(language="english", board=board)
