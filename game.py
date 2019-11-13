#!/usr/bin/env python3
import sys
from player import Player

CONNECT = 3
COLS = 4
ROWS = 3
EMPTY = ' '
TIE = 'TIE'

class Game:
    players = []
    boards = []

    def __init__(self, player1, player2, board="    |    |    "):
        self.initBoard = board
        if isinstance(board, str):
            self.b = [list(line) for line in board.split('|')]
        else:
            self.b = board
        self.players.append(player1)
        self.players.append(player2)

    def compact_string(self):
        return '|'.join([''.join(row) for row in self.b])

    def clone(self):
        return Game(self.players[0], self.players[1], self.compact_string())

    def get(self, i, j):
        return self.b[i][j] if i >= 0 and i < COLS and j >= 0 and j < ROWS else None

    def row(self, j):
        return [self.get(i, j) for i in range(COLS)]

    def put(self, i, j, val):
        self.b[i][j] = val
        return self

    def empties(self):
        return self.compact_string().count(EMPTY)

    def first_empty(self, i):
        j = ROWS - 1
        if self.get(i, j) != EMPTY:
            return None
        while j >= 0 and self.get(i, j) == EMPTY:
            j -= 1
        return j + 1

    def place(self, i, label):
        j = self.first_empty(i)
        if j is not None:
            self.put(i, j, label)
        return self

    def equals(self, board):
        return self.compact_string() == board.compact_string()

    def next(self, label):
        boards = []
        for i in range(COLS):
            j = self.first_empty(i)
            if j is not None:
                board = self.clone()
                board.put(i, j, label)
                boards.append(board)
        return boards

    def _winner_test(self, label, i, j, di, dj):
        for _ in range(CONNECT - 1):
            i += di
            j += dj
            if self.get(i, j) != label:
                return False
        return True

    def winner(self):
        for i in range(COLS):
            for j in range(ROWS):
                label = self.get(i, j)
                if label != EMPTY:
                    if self._winner_test(label, i, j, +1, 0) \
                            or self._winner_test(label, i, j, 0, +1) \
                            or self._winner_test(label, i, j, +1, +1) \
                            or self._winner_test(label, i, j, -1, +1):
                        return label
        return TIE if self.empties() == 0 else None

    def random_game(self):
        firstPlayerMove = True
        self.boards.append(self.clone())
        while self.winner() == None:
            if (firstPlayerMove):
                player = self.players[0]
                boards = self.next(player.label)
                if len(boards) != 0:
                    board = player.random_next(boards)
                    self.boards.append(board)
                    self.b = board.b
                firstPlayerMove = False
            else:
                player = self.players[1]
                boards = self.next(player.label)
                if len(boards) != 0:
                    board = player.random_next(boards)
                    self.boards.append(board)
                    self.b = board.b
                firstPlayerMove = True
        return self.boards

    def minimax(self):
        firstPlayerMove = True
        self.boards.append(self.clone())
        while self.winner() == None:
            if (firstPlayerMove):
                player = self.players[0]
                boards = self.next(player.label)
                if len(boards) != 0:
                    board = player.random_next(boards)
                    self.boards.append(board)
                    self.b = board.b
                firstPlayerMove = False
            else:
                player = self.players[1]
                boards = self.next(player.label)
                if len(boards) != 0:
                    board = player.minimax_next(self)
                    self.boards.append(board)
                    self.b = board.b
                firstPlayerMove = True
        return self.boards