#!/usr/bin/env python3
from brain_games.games import gcd
from brain_games.games.game_engine import engine


def main():
    print("Welcome to the Brain Games!")
    engine(gcd)


if __name__ == '__main__':
    main()
