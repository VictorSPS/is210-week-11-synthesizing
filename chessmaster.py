#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Chess piece"""

import time


class ChessPiece(object):
    """A chesspiece class.
       Stores legal chess moves.
    Attributes:
        prefix(str): by default, set as an empty string.
        position(str): stores the tile notation of its current position.
        moves(list): a list that stores tuples about each move.
    """

    prefix = ''

    def __init__(self, position, moves=None):
        self.position = position
        self.moves = moves
        self.moves = []
        myposition = self.algebraic_to_numeric(position)
        if myposition is None:
            excep = "'{}' is not a legal start position"
            raise ValueError(excep.format(position))

    def algebraic_to_numeric(self, tile):
        """Convert string into a tuple with two values.
        Args:
            tile(str): input string value.
        Returns:
            a tuple with 0 based x and 0 based y coordinate.
        Examples:
            >>> piece = ChessPiece('a1')
            >>> piece.algebraic_to_numeric('e7')
            (4, 6)
        """
        self.tile = tile
        letter_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        number_list = ['1', '2', '3', '4', '5', '6', '7', '8']
        letter_number_dict = {'a': 0,
                              'b': 1,
                              'c': 2,
                              'd': 3,
                              'e': 4,
                              'f': 5,
                              'g': 6,
                              'h': 7}
        if self.tile[1] in number_list:
            if self.tile[0] in letter_list:
                letter_num = letter_number_dict[self.tile[0]]
                return (letter_num, int(self.tile[1]) - 1)
        else:
            return None

    def is_legal_move(self, position):
        """Check if the moves are legal
        Args:
            position(str): input value for move of chess piece.
        Returns:
            True or False depends if the move is legal or not.
        """
        self.position = position
        move = self.algebraic_to_numeric(position)
        if move is not None:
            return True
        else:
            return False

    def move(self, position):
        """Algebraic notation of the new position.
        Args:
            position(str): input for new position.
        Returns:
            a tuple with olposition, newposition, timestam.
        Examples:
            >>> piece = ChessPiece('a1')
            >>> piece.move('e7')
            ('a1', 'e7', 1478524581.372149)
        """
        oldposition = self.position
        newposition = position
        piece_move = self.is_legal_move(newposition)
        if piece_move is True:
            timestamp = time.time()
            new_position = self.prefix + newposition
            old_position = self.prefix + oldposition
            self.moves.append((old_position, new_position, timestamp))
            self.position = new_position
            return (old_position, new_position, timestamp)
        else:
            return False


class Rook(ChessPiece):
    """Subclass of ChessPiece.
       Stores lefal moves for Rook.
    Attributes:
        prefix(str): a string, default to 'R'.
        position(str): a string.
        moves(list): a list.
    """
    prefix = 'R'

    def __init__(self, position, moves=None):
        self.position = position
        ChessPiece.__init__(self, position, moves=None)

    def is_legal_move(self, position):
        """Check if move is legal.
        Args:
            position(str): input for the position of Rook.
        Returns:
            True or False depends if the moveis legal or not.
        Examples:
            >>> rook = Rook('a1')
            >>> rook.move('b2')
            False
        """
        move2 = self.algebraic_to_numeric(position)
        move1 = self.algebraic_to_numeric(self.position)
        move2 = list(move2)
        move1 = list(move1)
        m1_x = move1[0]
        m1_y = move1[1]
        m2_x = move2[0]
        m2_y = move2[1]
        if m1_x != m2_x and m1_y != m2_y:
            return False
        else:
            self.position = position
            return True


class Bishop(ChessPiece):
    """Subclass of ChessPiece.
       Stores legal moves of Bishop.
    Attributes:
        prefix(str): a string, default to 'B'.
        position(str): a string.
        moves(list): a list.
    """
    prefix = 'B'

    def __init__(self, position, moves=None):
        self.position = position
        ChessPiece.__init__(self, position, moves=None)

    def is_legal_move(self, position):
        """Return True or False to check whether Bishop move is legal or not.
        Args:
            position(str): a string for the position of Bishop.
        Returns:
            True if the move is legal and False if it is not.
        Examples:
            >>> bishop = Bishop('a1')
            >>> bishop.move('a2')
            False
        """
        move2 = self.algebraic_to_numeric(position)
        move1 = self.algebraic_to_numeric(self.position)
        move2 = list(move2)
        move1 = list(move1)
        m1_x = move1[0]
        m1_y = move1[1]
        m2_x = move2[0]
        m2_y = move2[1]
        if abs(m1_x - m2_x) == abs(m1_y - m2_y):
            self.position = position
            return True
        else:
            return False


class King(ChessPiece):
    """Subclass of ChessPiece.
       Stores legal moves of King.
    Attributes:
        prefix(str): a string, default to 'K'.
        position(str): a string.
        moves(list): a list.
    """
    prefix = 'K'

    def __init__(self, position, moves=None):
        self.position = position
        ChessPiece.__init__(self, position, moves=None)

    def is_legal_move(self, position):
        """Return True or False to check whether King move is legal or not.
        Args:
            position(str): a string for the position of King.
        Returns:
            True if the move is legal and False if it is not.
        Examples:
            >>> king = King('a1')
            >>> king.move('a3')
            False
        """
        move2 = self.algebraic_to_numeric(position)
        move1 = self.algebraic_to_numeric(self.position)
        move2 = list(move2)
        move1 = list(move1)
        m1_x = move1[0]
        m1_y = move1[1]
        m2_x = move2[0]
        m2_y = move2[1]
        if abs(m1_x - m2_x) == 1 or abs(m1_y - m2_y) == 1:
            self.position = position
            return True
        else:
            return False


class ChessMatch(ChessPiece):
    """Subclass of ChessPiece.
       Store the lega chess move time and positions.
    Attributes:
        prefix(str): a string, default to ''.
        position(str): a string.
        pieces(list): a list.
    """

    def __init__(self, log=None, pieces=None):
        if pieces is not None:
            self.reset()
        else:
            self.pieces = pieces
            self.log = []

    def reset(self):
        """Reset function"""
        self.pieces = {}

    def move(self, fullnotation, position):
        def __init__(self, fullnotation, position):
            self.fullnotation = fullnotation
            ChessPiece.__init__(self, position)
        s_position = fullnotation[1:]
        prefix = fullnotation[0]
        move2 = self.algebraic_to_numeric(position)
        move1 = self.algebraic_to_numeric(s_position)
        move2 = list(move2)
        move1 = list(move1)
        m1_x = move1[0]
        m1_y = move1[1]
        m2_x = move2[0]
        m2_y = move2[1]
        x12 = abs(m1_x - m2_x)
        y12 = abs(m1_y - m2_y)
        if (prefix is 'K' and (x12 == 1 or y12 == 1)) or\
           (prefix is 'B' and (x12 == 0 or y12 == 0)) or\
           (prefix is 'R' and (x12 == y12)):
            timestamp = time.time()
            s_position = prefix + s_position
            position = prefix + position
            self.log.append((s_position, position, timestamp))              
        else:
            return False
