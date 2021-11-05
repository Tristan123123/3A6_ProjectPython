#!/usr/bin/env python3

"""
Autre script pour appeler les fonctions du
script principal, version 1

Par: Tristan Lanouette
"""

import main as bonjour


def main():
    """
    Autre méthode main pour appeler les fonctions
    du script principal
    """
    bonjour.bonjour('Tristan L.')
    bonjour.print_compter(8, 0.5)


if __name__ == '__main__':
    main()
