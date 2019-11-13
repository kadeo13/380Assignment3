#!/usr/bin/env python3
import sys

class Player:
    label = ""

    def __init__(self, label):
        if (label == "O" or label == "X"):
            self.label = label