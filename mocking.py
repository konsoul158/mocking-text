import argparse
import random
# import pyperclip

def mocking(string : str) -> str:
    resultString = ''
    for char in string:
        resultString = resultString + (char.upper() if bool(random.randint(0, 1)) else char.lower())

    return resultString

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-string", help = "The text to generate mocking", type = str)
    args = parser.parse_args()
    print(mocking(args.string))
    # pyperclip.copy(mocking(args.string))