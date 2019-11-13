#!/usr/bin/env python3
import sys
import random
from player import Player

class RandomPlayer(Player):

    def random_next(self, boards):
        board = random.choice(boards)
        return board