#!/usr/bin/env python3
from brain_games.games import is_prime
from brain_games.engine import run

def main():
    print("Welcome to the Brain Games!")
    run(is_prime)


if __name__ == '__main__':
    main()
