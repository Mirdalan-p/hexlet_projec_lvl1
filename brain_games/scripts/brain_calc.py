#!/usr/bin/env python3
from brain_games.games import brain_calc
from brain_games.engine import run


def main():
    print("Welcome to the Brain Games!")
    run(brain_calc)


if __name__ == '__main__':
    main()
