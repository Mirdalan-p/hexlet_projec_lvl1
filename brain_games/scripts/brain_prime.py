#!/usr/bin/env python3
from brain_games.games import is_prime
from brain_games.games.game_engine import engine


def main():
    print("Welcome to the Brain Games!")
    engine(is_prime)


if __name__ == '__main__':
    main()
