#!/usr/bin/env python3
import time


def bonjour(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Bonjour, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def print_compter(num, secs=0.25):
    print(f'Je sais compter jusqu\'a {num}:', end=' ')
    for i in range(num):
        time.sleep(secs)
        print(i + 1, end=' ',flush=True)
    print()


def main():
    bonjour('Tristan L. alias TL')
    print_compter(5)
    print_compter(10)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
