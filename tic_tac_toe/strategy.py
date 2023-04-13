from tic_tac_toe.Player import Player
import math 
import random 

EMPTY, X_PIECE, O_PIECE = ' ', 'X', 'O'
MAX, MIN = True, False 
WIN_SCORE = 1000000000 

class Strategy(Player):

	def __init__(self, aiColor):
		"""Initializes the board attributes"""
		super().__init__(aiColor)
		self.AI_COLOR = aiColor
		self.HUMAN_COLOR = opponentOf(aiColor)

	def getMove(self, board):
		"""Calculates the best move for the AI for the given board"""
		moveRow, moveCol = -1, -1
		for depth_to_search in range(1, 10): 

			moveRow, moveCol, score = self.minimax(board, 0, MAX, -math.inf, math.inf, depth_to_search)
			if score == WIN_SCORE:
				break
		return moveRow, moveCol

	def minimax(self, board, depth, maxOrMin, alpha, beta, localMaxDepth):
		"""
		Recursively finds the best move for a given board
		Returns the row in [0], column in [1], and score of the board in [2]
		"""
		gameOver, winner = isTerminal(board)
		if gameOver or depth == localMaxDepth:
			if winner == self.AI_COLOR:
				return None, None, WIN_SCORE
			elif winner == self.HUMAN_COLOR:
				return None, None, -1 * WIN_SCORE
			else:
				return None, None, 0

		validMoves = getValidMoves(board)
		if len(validMoves) == 0:
			return -1, -1, 0
		elif len(validMoves) == 9:

			return 1, 1, 0 
		random.shuffle(validMoves)
		if maxOrMin == MAX:

			score = -math.inf
			bestMove = validMoves[0] 
			for move in validMoves:
				boardCopy = copyOfBoard(board)
				performMove(boardCopy, move[0], move[1], self.AI_COLOR)
				gameOver, winner = isTerminal(boardCopy)
				if winner == self.AI_COLOR:
					updatedScore = WIN_SCORE
				elif winner == self.HUMAN_COLOR:
					updatedScore = -1 * WIN_SCORE
				else:

					if gameOver:

						updatedScore = 0
					else:
						_, __, updatedScore = self.minimax(boardCopy, depth + 1, MIN, alpha, beta, localMaxDepth)
				if updatedScore > score:
					score = updatedScore
					bestMove = move
				alpha = max(alpha, score)
				if alpha >= beta:
					break 
			return bestMove[0], bestMove[1], score

		else: 

			score = math.inf
			bestMoveForHuman = validMoves[0]
			for move in validMoves:
				boardCopy = copyOfBoard(board)
				performMove(boardCopy, move[0], move[1], self.HUMAN_COLOR)
				gameOver, winner = isTerminal(boardCopy)
				if winner == self.AI_COLOR:
					updatedScore = WIN_SCORE
				elif winner == self.HUMAN_COLOR:
					updatedScore = -1 * WIN_SCORE
				else:

					if gameOver:

						updatedScore = 0
					else:
						_, __, updatedScore = self.minimax(boardCopy, depth + 1, MAX, alpha, beta, localMaxDepth)
				if updatedScore < score:
					score = updatedScore
					bestMoveForHuman = move
				beta = min(beta, score)
				if beta <= alpha:
					break 
			return bestMoveForHuman[0], bestMoveForHuman[1], score

def opponentOf(piece):
	"""Get the opposing piece"""
	return X_PIECE if piece == O_PIECE else O_PIECE

def performMove(board, row, col, piece):
	"""Performs a given move on the board"""
	board[row][col] = piece

def findWinner(board):
	"""
    Checks if there is a winner
    returns the color of the winner if there is one, otherwise None
    """

	for row in board:
		if row[0] == row[1] == row[2] != EMPTY:
			return row[0]

	for col in range(3):
		if board[0][col] == board[1][col] == board[2][col] != EMPTY:
			return board[0][col]

	if board[0][0] == board[1][1] == board[2][2] != EMPTY:
		return board[0][0]

	if board[0][2] == board[1][1] == board[2][0] != EMPTY:
		return board[0][2]

	return None

def isTerminal(board):
	"""
    Checks if the current board state is Game Over
    Returns a tuple, with [0] being the True or False value
    [1] being the winning color (None if neither color wins)
    """
	winner = findWinner(board)
	if winner is not None:
		return True, winner

	for row in board:
		for spot in row:
			if spot == EMPTY:
				return False, None

	return True, None

def getValidMoves(board):
	"""Returns a list of valid moves (moves in the center area or near other pieces)"""
	validLocations = []
	for rowNum in range(3):
		for colNum in range(3):
			if board[rowNum][colNum] == EMPTY:
				validLocations.append([rowNum, colNum])
	return validLocations

def copyOfBoard(board):
	"""Returns a copy of the given board"""
	return list(map(list, board))