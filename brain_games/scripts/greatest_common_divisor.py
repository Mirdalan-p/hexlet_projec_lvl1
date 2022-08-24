#!/usr/bin/env python3
from brain_games.games import gcd
from brain_games.engine import run


def main():
    print("Welcome to the Brain Games!")
    run(gcd)


if __name__ == '__main__':
    main()
