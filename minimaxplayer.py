#!/usr/bin/env python3
import sys
import random
from game import Game
from player import Player

class MinimaxPlayer(Player):

    def minimax_next(self, game):
        moves = game.next('O')
        bestMove = moves[0]
        bestScore = float('-inf')
        for move in moves:
            board = Game(game.players[0], game.players[1], move.b)
            nextBoard = board.next('O')
            if len(nextBoard) != 0:
                nextState = Game(game.players[0], game.players[1], random.choice(nextBoard).b)
                score = self.max_play(nextState, bestScore)
                if score > bestScore:
                    bestMove = move
                    bestScore = score
        return bestMove

    def min_play(self, game, s):
        if game.winner() != None:
            return s
        moves = game.next('O')
        bestScore = float('inf')
        for move in moves:
            board = Game(game.players[0], game.players[1], move.b)
            score = self.max_play(board, bestScore)
            if score < bestScore:
                bestMove = move
                bestScore = score
        return bestScore

    def max_play(self, game, s):
        if game.winner() != None:
            return s
        moves = game.next('O')
        bestScore = float('-inf')
        for move in moves:
            board = Game(game.players[0], game.players[1], move.b)
            score = self.min_play(board, bestScore)
            if score > bestScore:
                bestMove = move
                bestScore = score
        return bestScore