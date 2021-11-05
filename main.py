#!/usr/bin/env python3

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Bonjour, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def print_compter(num):
    print(f'Je sais compter jusqu\'a {num}:', end=' ')
    for i in range(num):
        print(i + 1, end=' ')
    print()


def main():
    print_hi('Tristan L. alias TL')
    print_compter(5)
    print_compter(10)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
