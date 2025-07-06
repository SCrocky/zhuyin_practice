import os
import click
import json
import random
from enlarge_chars import print_large_char

dir_path = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(dir_path, "bpmf.json")) as reader:
    bpmf: dict[str, dict] = json.load(reader)


def which_sound(char: str, values: dict) -> bool:
    print_large_char(char)
    attempt = input("Which sound corresponds to this Zhuyin character ?\n\n> ")
    answer = values["pinyin"]

    is_correct = False
    if len(attempt) == 1 and attempt == answer[0]:
        is_correct = True
    elif len(answer) == 1 and len(attempt) == 2 and attempt[0] == answer:
        is_correct = True
    elif attempt in answer:
        is_correct = True
    else:
        print(f"\nWrong! The correct answer was: {answer}")
    return is_correct


def which_char(char: str, values: dict) -> bool:
    raise NotImplementedError("")
    is_correct = False
    return is_correct


@click.command()
@click.option(
    "--guess", default="sound", help="whether to guess the sound or the character"
)
@click.option("--nb", default=20, help="Number of questions to ask")
def main(guess, nb):
    chars = list(bpmf.keys())
    questions = random.sample(chars, k=nb)
    total = 0
    guesser = which_sound if guess == "sound" else which_char
    for char in questions:
        if guesser(char, bpmf[char]):
            total += 1
            print(f"\nThat is Correct!")
        print(f"\nHere is an example of usage: {bpmf[char]['example']}")

    print("Final Score:" + str(total) + "/" + str(nb))


if __name__ == "__main__":
    main()
