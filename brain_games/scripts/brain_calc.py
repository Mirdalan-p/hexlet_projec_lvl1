#!/usr/bin/env python3
from brain_games.games import brain_calc
from brain_games.games.game_engine import engine


def main():
    print("Brain-calc\n\n\nWelcome to the Brain Games!")
    engine(brain_calc)


if __name__ == '__main__':
    main()
