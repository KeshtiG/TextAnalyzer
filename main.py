#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
TEXT ANALYZER
"""

import os
import analyzer

def main():
    """
    Analyzer main function
    """

    stop = False
    filepath = analyzer.change_file("cats.txt")

    while not stop:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\nWelcome Human.")
        print("Enter a command from the list to execute a task.\n")
        print(f"Current file: {os.path.basename(filepath)}\n")
        print("1:   Count lines")
        print("2:   Count words")
        print("3:   Count letters")
        print("4:   Count word frequency")
        print("5:   Count letter frequency")
        print("6:   Print all results")
        print("7:   Change text file")
        print("Q:   Quit\n")

        choice = input("--> ")
        choice = choice.lower()

        if choice == "q":
            print("Good bye, Human... *shutting down*")
            stop = True

        elif choice == "1":
            print(f"Number of lines:\n{analyzer.count_lines(filepath)}")

        elif choice == "2":
            print(f"Number of words:\n{analyzer.count_words(filepath)}")

        elif choice == "3":
            print(f"Number of letters:\n{analyzer.count_letters(filepath)}")

        elif choice == "4":
            print(f"Word frequency (top 8):\n{analyzer.count_frequency(filepath, 'words')}")

        elif choice == "5":
            print(f"Letter frequency (top 8):\n{analyzer.count_frequency(filepath, 'letters')}")

        elif choice == "6":
            print(analyzer.get_all_results(filepath))

        elif choice == "7":
            print("Available files:\nphil.txt\ncats.txt\npackers.txt\n")
            user_input = input("Enter a file name: ")
            filepath = analyzer.change_file(user_input)
            print(f"File changed to {os.path.basename(filepath)}")

        else:
            print("That is not a valid command.")

        if not stop:
            input("\nPress enter to continue...")
            os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    main()
