from random import randint
import argparse

parser = argparse.ArgumentParser(description="The Coin Flip Experiment",
                                 epilog="If no number of subjects is provided the simulation will run with 10000 subjects")
parser.add_argument("subjects", action="store",
                    nargs="?", default=10000, type=int, help="number of subjects to run simulation with")
parsed_args = parser.parse_args()

subjects = parsed_args.subjects
round = 1
standing = 0

print(f"\nRunning simulation with {subjects} subjects")

while subjects > 1:
    print()
    print(f"Round: {round}")
    for x in range(subjects):
        if randint(0, 1) == 1:
            standing += 1
    print(f"Out of {subjects}; {standing} people flipped heads {round} time/s")
    print(f"%age Lost: {((subjects - standing)/subjects)*100}")
    print()
    round += 1
    subjects = standing
    standing = 0

if subjects == 1:
    print(
        f"In this simulation {subjects} person flipped heads {round} times\n")
