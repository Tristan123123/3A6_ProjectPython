#!/usr/bin/env python3

"""
Autre script pour appeler les fonctions du
script principal, version 2

Par: Tristan Lanouette
"""


from main import bonjour
from main import print_compter


def main():
    """
    Fonction principal du script
    """
    bonjour('Tristan L.')
    print_compter(3)


if __name__ == '__main__':
    main()
