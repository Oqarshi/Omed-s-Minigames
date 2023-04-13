import math 
import random 
import sys 
from gomoku.Player import Player 

EMPTY, BLACK, WHITE = '.', 'X', 'O'
BLACK_HASH_ROW_NUM, WHITE_HASH_ROW_NUM = 0, 1
MAX, MIN = True, False 
WIN_SCORE = 1000000000 

MAX_NEIGHBOR_DIST = 2 
MAX_NUM_MOVES_TO_EVALUATE = 30
MAX_DEPTH = 5

class Strategy(Player):

	def __init__(self, color, boardDimension=13):
		"""Initializes the board attributes"""
		super().__init__(color, boardDimension)
		self.GAME_OVER = False
		self.AI_COLOR = color
		self.HUMAN_COLOR = opponentOf(color)

		self.RANDOM_HASH_TABLE = self.createHashTable(boardDimension)
		self.BOARD_STATE_DICT = {} 
		self.createThreatSequencesDictionary()
		self.createBoardPositionWeights(boardDimension)

	def createThreatSequencesDictionary(self):
		"""Creates the dictionaries that will help score board sections"""
		self.blackThreatsScores = {
			'.XXXX.' : 10000,	
			'.XXXX'  : 100,		
			'XXXX.'	 : 100, 	
			'X.XXX'	 : 90,		
			'XX.XX'	 : 85,		
			'XXX.X'	 : 90,		
			'.XXX.'	 : 30,		
			'OXXXX.' : 80,		
			'.XXXXO' : 80,		
			'.X.XX.' : 25,		
			'.XX.X.' : 25		
		}
		self.whiteThreatsScores = {
			'.OOOO.' : 10000,	
			'.OOOO'  : 100,		
			'OOOO.'	 : 100, 	
			'O.OOO'	 : 90,		
			'OO.OO'	 : 85,		
			'OOO.O'	 : 90,		
			'.OOO.'	 : 30,		
			'XOOOO.' : 80,		
			'.OOOOX' : 80,		
			'.O.OO.' : 25,		
			'.OO.O.' : 25		
		}

	def createBoardPositionWeights(self, dim):
		"""
		Create the position weights matrix for a board of dimension `dim`
		Center weighted heavier
		"""
		self.positionWeightsMatrix = []
		for i in range(dim):
			self.positionWeightsMatrix.append([0]*dim) 
		centerIndex = dim//2
		for i in range(dim//2):
			for row in range(centerIndex - i, centerIndex + i + 1):
				for col in range(centerIndex - i, centerIndex + i + 1):
					self.positionWeightsMatrix[row][col] += 3

	def createHashTable(self, dimension):
		"""Fills a 2 by dimension board with random 64 bit integers"""
		table = [] 
		for color in range(2):
			colorLocationList = []
			for boardPos in range(dimension * dimension):
				colorLocationList.append(random.getrandbits(64))
			table.append(colorLocationList)
		return table

	def createZobristValueForNewMove(self, move, color, prevZobristValue):
		"""Gives an updated Zobrist value for a board after a new move is played"""
		row, col = move
		hash_row = BLACK_HASH_ROW_NUM if color == BLACK else WHITE_HASH_ROW_NUM
		hash_val = self.RANDOM_HASH_TABLE[hash_row][row*self.BOARD_DIMENSION + col]
		return prevZobristValue ^ hash_val 

	def checkGameState(self, board):
		"""Sets the GAME_OVER var to True if there is a winner"""
		if self.isTerminal(board)[0]:
			self.GAME_OVER = True

	def isTerminal(self, board):
		"""
		Checks if the current board state is Game Over
		Returns a tuple, with [0] being the True or False value
		[1] being the winning color (None if neither color wins)
		"""
		winner = self.findWinner(board)
		if winner is not None:
			return True, winner

		for row in board:
			for spot in row:
				if spot == EMPTY:
					return False, None

		return True, None

	def findWinner(self, board):
		"""
		Checks if there is a winner
		returns the color of the winner if there is one, otherwise None
		"""

		for row in board:
			for col in range(self.BOARD_DIMENSION - 4):
				if row[col] == row[col+1] == row[col+2] == row[col+3] == row[col+4] != EMPTY:
					return row[col]

		for c in range(self.BOARD_DIMENSION):
			for r in range(self.BOARD_DIMENSION - 4):
				if board[r][c] == board[r+1][c] == board[r+2][c] == board[r+3][c] == board[r+4][c] != EMPTY:
					return board[r][c]

		for c in range(self.BOARD_DIMENSION - 4):
			for r in range(self.BOARD_DIMENSION - 4):
				if board[r][c] == board[r+1][c+1] == board[r+2][c+2] == board[r+3][c+3] == board[r+4][c+4]!= EMPTY:
					return board[r][c]

		for c in range(self.BOARD_DIMENSION - 4):
			for r in range(4, self.BOARD_DIMENSION):
				if board[r][c] == board[r-1][c+1] == board[r-2][c+2] == board[r-3][c+3] == board[r-4][c+4] != EMPTY:
					return board[r][c]

		return None

	def isCoordinateInBoardRange(self, coord):
		"""Checks if the coordinate is valid on the board"""
		rowNum = coord[0]
		colNum = coord[1]
		if rowNum % self.BOARD_DIMENSION == rowNum and colNum % self.BOARD_DIMENSION == colNum:
			return True
		else:
			return False

	def checkIfMoveCausedGameOver(self, board, move):
		"""
		Checks the spaces in outward directions to see if the move given caused a win
		returns the winner in [0] (BLACK, WHITE, or None if no winner)
		returns True or False in [1] whether or not the game is over
		"""
		emptySpotSeen = False
		color = board[move[0]][move[1]]
		directionVectorsList = [[1, -1], [1, 0], [1, 1], [0, 1]]
		for directionVector in directionVectorsList:
			numInARow = 1
			currCoordinatesForward = move.copy()
			currCoordinatesBackward = move.copy()
			forwardCheckStillValid = True
			backwardCheckStillValid = True
			outwardSpacesChecked = 0
			while outwardSpacesChecked < 4 and numInARow < 5 and (forwardCheckStillValid or backwardCheckStillValid):
				outwardSpacesChecked += 1
				if forwardCheckStillValid:

					currCoordinatesForward = [a + b for a, b in zip(currCoordinatesForward, directionVector)] 
					if self.isCoordinateInBoardRange(currCoordinatesForward):
						currForwardSpot = board[currCoordinatesForward[0]][currCoordinatesForward[1]]
						if currForwardSpot == color:
							numInARow += 1
						else:
							if currForwardSpot == EMPTY:
								emptySpotSeen = True
							forwardCheckStillValid = False
					else:
						forwardCheckStillValid = False

				if backwardCheckStillValid:
					currCoordinatesBackward = [a - b for a, b in zip(currCoordinatesBackward, directionVector)] 
					if self.isCoordinateInBoardRange(currCoordinatesBackward):
						currBackwardSpot = board[currCoordinatesBackward[0]][currCoordinatesBackward[1]]
						if currBackwardSpot == color:
							numInARow += 1
						else:
							if currBackwardSpot == EMPTY:
								emptySpotSeen = True
							backwardCheckStillValid = False
					else:
						backwardCheckStillValid = False
			if numInARow >= 5:
				return color, True

		if emptySpotSeen:
			return None, False
		for row in board:
			for spot in row:
				if spot == EMPTY:

					return None, False
		return None, True

	def getValidMoves(self, board):
		"""Returns a list of valid moves (moves in the center area or near other pieces)"""

		lists_of_valids = [] 
		for l in range(MAX_NEIGHBOR_DIST):
			lists_of_valids.append([]) 

		emptiesFoundSoFar = set() 

		filledLocations = []
		for r in range(self.BOARD_DIMENSION):
			for c in range(self.BOARD_DIMENSION):
				if board[r][c] != EMPTY:
					filledLocations.append([r,c])

  

		def locateEmptyNearSpots(filledCoord, distFromPiece):
			"""Finds all the empty spots near this coordinate and adds them to the list of valid spots"""
			row, col = filledCoord
			for i in range(-distFromPiece, distFromPiece + 1): 
				for j in range(-distFromPiece, distFromPiece + 1): 
					if i != distFromPiece and i != -distFromPiece and j != distFromPiece and j != -distFromPiece: 

						continue
					curr_row, curr_col = row + i, col + j
					if not self.isCoordinateInBoardRange((curr_row, curr_col)):

						continue
					neighborSpot = board[curr_row][curr_col]
					neighborCoordAsTuple = (curr_row, curr_col)
					if neighborSpot == EMPTY and neighborCoordAsTuple not in emptiesFoundSoFar:

						emptiesFoundSoFar.add(neighborCoordAsTuple)
						lists_of_valids[distFromPiece - 1].append([curr_row, curr_col])

		for distFromPiece in range(1, MAX_NEIGHBOR_DIST + 1):
			for filledCoord in filledLocations:
				locateEmptyNearSpots(filledCoord, distFromPiece)

		for l in lists_of_valids:
			random.shuffle(l) 

		validLocations = [item for innerlist in lists_of_valids for item in innerlist]

		if len(validLocations) == 0 and board[self.BOARD_DIMENSION//2][self.BOARD_DIMENSION//2] == EMPTY:

			return [[self.BOARD_DIMENSION//2, self.BOARD_DIMENSION//2]]

		return self.findBestValidMoves(validLocations, board)

	def findBestValidMoves(self, validMoves, board):
		"""Takes in all the spaces that were deemed valid and selects the ones that have the most potential"""
		if len(validMoves) <= MAX_NUM_MOVES_TO_EVALUATE:

			return validMoves

		def sectionContainsThreats(pieceColor, sectionString):
			"""
			Evaluates each length 5 and length 6 section of spots in the board for threats
			Returns True or False depending on whether a threat was found
			"""
			threatDictionary = self.blackThreatsScores if pieceColor == BLACK else self.whiteThreatsScores
			if len(sectionString) == 5:

				if sectionString in threatDictionary:
					return True
				return False
			for i in range(len(sectionString) - 5):
				section6 = sectionString[i:i+6]
				section5 = section6[:-1]
				if section6 in threatDictionary:
					return True
				if section5 in threatDictionary:
					return True
				if i == len(sectionString) - 6:

					section5 = section6[1:]
					if section5 in threatDictionary:
						threatMultiplier = 2
						return True
			return False

		movesWithScores = [] 

		directionVectorsList = [[1, -1], [1, 0], [1, 1], [0, 1]]
		for move in validMoves:
			moveScore = 0
			for directionVector in directionVectorsList:
				forwardScore, backwardScore = 0, 0
				if self.isCoordinateInBoardRange([move[0] + directionVector[0], move[1] + directionVector[1]]):
					forwardCheckStillValid = True
					forwardPieceColor = board[move[0] + directionVector[0]][move[1] + directionVector[1]] 
				else:
					forwardCheckStillValid = False
					forwardPieceColor = None

				if self.isCoordinateInBoardRange([move[0] - directionVector[0], move[1] - directionVector[1]]):
					backwardCheckStillValid = True
					backwardPieceColor = board[move[0] - directionVector[0]][move[1] - directionVector[1]] 
				else:
					backwardCheckStillValid = False
					backwardPieceColor = None

				numForwardPlayerPieces, numBackwardPlayerPieces = 0, 0 
				currCoordinatesForward, currCoordinatesBackward = move.copy(), move.copy()
				outwardSpacesChecked = 0
				forwardDistanceReached, backwardDistanceReached = 0, 0 
				numForwardEmptiesBeforePiece, numBackwardEmptiesBeforePiece = 0, 0 
				forwardDirectionStr, backwardDirectionStr = '', '' 

				while outwardSpacesChecked < 4 and (forwardCheckStillValid or backwardCheckStillValid):
					outwardSpacesChecked += 1
					if forwardCheckStillValid:

						currCoordinatesForward = [a + b for a, b in zip(currCoordinatesForward, directionVector)] 
						if self.isCoordinateInBoardRange(currCoordinatesForward):
							currPiece = board[currCoordinatesForward[0]][currCoordinatesForward[1]]

							if forwardPieceColor == EMPTY:

								forwardDirectionStr += currPiece
								forwardDistanceReached += 1
								if currPiece == EMPTY:
									numForwardEmptiesBeforePiece += 1
								else:

									forwardPieceColor = currPiece
									numForwardPlayerPieces += 1
									forwardScore += (5 - outwardSpacesChecked)

							elif forwardPieceColor == currPiece:

								forwardDirectionStr += currPiece
								forwardDistanceReached += 1
								numForwardPlayerPieces += 1
								forwardScore += (5 - outwardSpacesChecked) * (2 ** (2 * (numForwardPlayerPieces - 1)))

							else:

								if currPiece == EMPTY:
									forwardDirectionStr += currPiece
									forwardDistanceReached += 1
									forwardScore += (5 - outwardSpacesChecked)
								else:

									forwardCheckStillValid = False
						else:
							forwardCheckStillValid = False

					if backwardCheckStillValid:

						currCoordinatesBackward = [a - b for a, b in zip(currCoordinatesBackward, directionVector)] 
						if self.isCoordinateInBoardRange(currCoordinatesBackward):
							currPiece = board[currCoordinatesBackward[0]][currCoordinatesBackward[1]]

							if backwardPieceColor == EMPTY:

								backwardDirectionStr += currPiece
								backwardDistanceReached += 1
								if currPiece == EMPTY:
									numBackwardEmptiesBeforePiece += 1
								else:

									backwardPieceColor = currPiece
									numBackwardPlayerPieces += 1
									backwardScore += (5 - outwardSpacesChecked)

							elif backwardPieceColor == currPiece:

								backwardDirectionStr += currPiece
								backwardDistanceReached += 1
								numBackwardPlayerPieces += 1
								backwardScore += (5 - outwardSpacesChecked) * (2 ** (2 * (numBackwardPlayerPieces - 1)))

							else:

								if currPiece == EMPTY:
									backwardDirectionStr += currPiece
									backwardDistanceReached += 1
									backwardScore += (5 - outwardSpacesChecked)
								else:

									backwardCheckStillValid = False
						else:
							backwardCheckStillValid = False

				directionVectorScore = forwardScore + backwardScore
				if forwardPieceColor == backwardPieceColor:

					if forwardDistanceReached + 1 + backwardDistanceReached < 5:

						directionVectorScore = 0
					else:
						threatMultiplier = 1
						if forwardPieceColor != EMPTY and forwardPieceColor is not None:

							fullSectionString = backwardDirectionStr + forwardPieceColor + forwardDirectionStr 
							if sectionContainsThreats(forwardPieceColor, fullSectionString):
								threatMultiplier = 2

						directionVectorScore += max(forwardScore, backwardScore) * threatMultiplier
				else:

					if forwardDistanceReached + 1 + numBackwardEmptiesBeforePiece < 5 and backwardDistanceReached + 1 + numForwardEmptiesBeforePiece < 5:

						directionVectorScore = 0
					else:
						threatMultiplier = 1

						if opponentOf(forwardPieceColor) == backwardPieceColor and forwardPieceColor is not None and backwardPieceColor is not None:

							if numBackwardEmptiesBeforePiece == 0:

							 	forwardSectionStr = forwardPieceColor + forwardDirectionStr
							else:

								forwardSectionStr = "." + forwardPieceColor + forwardDirectionStr
							if numForwardEmptiesBeforePiece == 0:

							 	backwardSectionStr = backwardPieceColor + backwardDirectionStr
							else:

								backwardSectionStr = "." + backwardPieceColor + backwardDirectionStr

							if sectionContainsThreats(forwardPieceColor, forwardSectionStr) or sectionContainsThreats(backwardPieceColor, backwardSectionStr):
								threatMultiplier = 2

						else:

							if forwardPieceColor is None:

								totalSectionStr = backwardPieceColor + backwardDirectionStr
								evaluatingPieceColor = backwardPieceColor
							elif backwardPieceColor is None:

								totalSectionStr = forwardPieceColor + forwardDirectionStr
								evaluatingPieceColor = forwardPieceColor
							else:
								if forwardPieceColor == EMPTY:

									totalSectionStr = "." + backwardPieceColor + backwardDirectionStr
									evaluatingPieceColor = backwardPieceColor
								else:

									totalSectionStr = "." + forwardPieceColor + forwardDirectionStr
									evaluatingPieceColor = forwardPieceColor

							if sectionContainsThreats(evaluatingPieceColor, totalSectionStr):
								threatMultiplier = 2

						directionVectorScore += max(forwardScore, backwardScore) * threatMultiplier

				moveScore += directionVectorScore
			movesWithScores.append([move, moveScore])

		movesWithScores.sort(key = lambda x: -x[1]) 
		highestEvaluatedMoves = []
		for i in range(MAX_NUM_MOVES_TO_EVALUATE):
			highestEvaluatedMoves.append(movesWithScores[i][0])

		return highestEvaluatedMoves

	def getMove(self, board):
		"""Calculates the best move for the AI for the given board"""
		moveRow, moveCol, score = -123, -123, -123 
		for i in range(1, MAX_DEPTH + 1): 

			moveRow, moveCol, score = self.minimax(board, 0, MAX, -math.inf, math.inf, i, 0)
			self.BOARD_STATE_DICT.clear() 
			if score >= WIN_SCORE:
				break
		return moveRow, moveCol

	def minimax(self, board, depth, maxOrMin, alpha, beta, localMaxDepth, zobristValueForBoard):
		"""
		Recursively finds the best move for a given board
		Returns the row in [0], column in [1], and score of the board in [2]
		"""
		if depth == localMaxDepth:
			playerWithTurnAfterMaxDepth = self.AI_COLOR if localMaxDepth % 2 == 0 else self.HUMAN_COLOR
			boardScores = self.scoreBoard(board, self.HUMAN_COLOR, self.AI_COLOR, playerWithTurnAfterMaxDepth)
			humanScore = boardScores[0]
			aiScore = boardScores[1]
			return None, None, aiScore - humanScore
		validMoves = self.getValidMoves(board)
		if len(validMoves) == 0:
			return -1, -1, 0
		if depth == 0 and len(validMoves) == 1:
			return validMoves[0][0], validMoves[0][1], 0
		if maxOrMin == MAX:
			score = -math.inf
			bestMove = validMoves[0] 
			if depth == 0:
				percentComplete = 0 #N = (b^(d+1) - 1)/(b - 1)
				movesChecked = 0
				barCompleteMultiplier = 0
				print('\r[%s%s] %d%% (%d/%d moves checked) @ maxDepth = %d  Nodes = %d: ' % ("="*barCompleteMultiplier, "-"*(25-barCompleteMultiplier), percentComplete, movesChecked, len(validMoves), localMaxDepth, len(validMoves)**(localMaxDepth+1) - 1 // (len(validMoves) - 1)), end = "")
			for move in validMoves:
				if depth == 0:
					percentComplete = int((movesChecked/len(validMoves))*100)
					barCompleteMultiplier = percentComplete // 4
					print('\r[%s%s] %d%% (%d/%d moves checked) @ maxDepth = %d Nodes = %d: ' % ("="*barCompleteMultiplier, "-"*(25-barCompleteMultiplier), percentComplete, movesChecked, len(validMoves), localMaxDepth, len(validMoves)**(localMaxDepth+1) - 1 // (len(validMoves) - 1)), end = "")
					movesChecked += 1
				boardCopy = copyOfBoard(board)
				performMove(boardCopy, move[0], move[1], self.AI_COLOR)
				newZobristValue = self.createZobristValueForNewMove(move, self.AI_COLOR, zobristValueForBoard)
				if depth >= 2 and newZobristValue in self.BOARD_STATE_DICT:
					updatedScore = self.BOARD_STATE_DICT[newZobristValue]
				else:
					winner, gameOver = self.checkIfMoveCausedGameOver(boardCopy, move)
					if winner == self.AI_COLOR:
						updatedScore = WIN_SCORE
					elif winner == self.HUMAN_COLOR:
						updatedScore = -1 * WIN_SCORE
					else:
						if gameOver:
							updatedScore = 0
						else:
							_, __, updatedScore = self.minimax(boardCopy, depth + 1, MIN, alpha, beta, localMaxDepth, newZobristValue)
					if depth >= 2:
						self.BOARD_STATE_DICT[newZobristValue] = updatedScore
				if updatedScore > score:
					score = updatedScore
					bestMove = move
				alpha = max(alpha, score)
				if alpha >= beta:
					break 
			if depth == 0:
				sys.stdout.write('\033[2K\033[1G')
			return bestMove[0], bestMove[1], score
		else: 
			score = math.inf
			bestMoveForHuman = validMoves[0]
			for move in validMoves:
				boardCopy = copyOfBoard(board) 
				performMove(boardCopy, move[0], move[1], self.HUMAN_COLOR)
				newZobristValue = self.createZobristValueForNewMove(move, self.HUMAN_COLOR, zobristValueForBoard)
				if depth >= 2 and newZobristValue in self.BOARD_STATE_DICT:
					updatedScore = self.BOARD_STATE_DICT[newZobristValue]
				else:
					winner, gameOver = self.checkIfMoveCausedGameOver(boardCopy, move)
					if winner == self.AI_COLOR:
						updatedScore = WIN_SCORE
					elif winner == self.HUMAN_COLOR:
						updatedScore = -1 * WIN_SCORE
					else:
						if gameOver:
							updatedScore = 0
						else:
							_, __, updatedScore = self.minimax(boardCopy, depth + 1, MAX, alpha, beta, localMaxDepth, newZobristValue)
					if depth >= 2:
						self.BOARD_STATE_DICT[newZobristValue] = updatedScore
				if updatedScore < score:
					score = updatedScore
					bestMoveForHuman = move
				beta = min(beta, score)
				if beta <= alpha:
					break 
			return bestMoveForHuman[0], bestMoveForHuman[1], score

	def scoreSections(self, board, colorOfEvaluator, colorOfEnemy, playerWithTurnAfterMaxDepth):
		"""Scores all the different horizontal/vertical/diagonal sections on the board"""
		evaluatorScore = 0
		enemyScore = 0
		evaluatorTrapIndicators = [0, 0, 0, 0]
		enemyTrapIndicators = [0, 0, 0, 0]
		if colorOfEvaluator == BLACK:
			evaluatorScoresDict = self.blackThreatsScores
			enemyScoresDict = self.whiteThreatsScores
		else:
			evaluatorScoresDict = self.whiteThreatsScores
			enemyScoresDict = self.blackThreatsScores

		for c in range(self.BOARD_DIMENSION - 5):
			for r in range(self.BOARD_DIMENSION):
				section6 = "".join(board[r][c:c + 6])
				section5 = section6[:-1] 
				if section6 in evaluatorScoresDict:
					evaluatorScore += evaluatorScoresDict[section6]
					evaluatorTrapIndicators[0] = 1
				elif section6 in enemyScoresDict:
					enemyScore += enemyScoresDict[section6]
					enemyTrapIndicators[0] = 1
				if section5 in evaluatorScoresDict:
					evaluatorScore += evaluatorScoresDict[section5]
					evaluatorTrapIndicators[0] = 1
				elif section5 in enemyScoresDict:
					enemyScore += enemyScoresDict[section5]
					enemyTrapIndicators[0] = 1
				if c == self.BOARD_DIMENSION - 6:

					section5 = section6[1:] 
					if section5 in evaluatorScoresDict:
						evaluatorScore += evaluatorScoresDict[section5]
						evaluatorTrapIndicators[0] = 1
					elif section5 in enemyScoresDict:
						enemyScore += enemyScoresDict[section5]
						enemyTrapIndicators[0] = 1

		for c in range(self.BOARD_DIMENSION):
			for r in range(self.BOARD_DIMENSION - 5):
				section6 = ''
				for i in range(6):
					section6 += board[r + i][c]
				section5 = section6[:-1] 
				if section6 in evaluatorScoresDict:
					evaluatorScore += evaluatorScoresDict[section6]
					evaluatorTrapIndicators[1] = 1
				elif section6 in enemyScoresDict:
					enemyScore += enemyScoresDict[section6]
					enemyTrapIndicators[1] = 1
				if section5 in evaluatorScoresDict:
					evaluatorScore += evaluatorScoresDict[section5]
					evaluatorTrapIndicators[1] = 1
				elif section5 in enemyScoresDict:
					enemyScore += enemyScoresDict[section5]
					enemyTrapIndicators[1] = 1
				if r == self.BOARD_DIMENSION - 6:

					section5 = section6[1:] 
					if section5 in evaluatorScoresDict:
						evaluatorScore += evaluatorScoresDict[section5]
						evaluatorTrapIndicators[1] = 1
					elif section5 in enemyScoresDict:
						enemyScore += enemyScoresDict[section5]
						enemyTrapIndicators[1] = 1

		for c in range(self.BOARD_DIMENSION - 5):
			for r in range(self.BOARD_DIMENSION - 5):
				section6 = ''
				for i in range(6):
					section6 += board[r + i][c + i]
				section5 = section6[:-1]
				if section6 in evaluatorScoresDict:
					evaluatorScore += evaluatorScoresDict[section6]
					evaluatorTrapIndicators[2] = 1
				elif section6 in enemyScoresDict:
					enemyScore += enemyScoresDict[section6]
					enemyTrapIndicators[2] = 1
				if section5 in evaluatorScoresDict:
					evaluatorScore += evaluatorScoresDict[section5]
					evaluatorTrapIndicators[2] = 1
				elif section5 in enemyScoresDict:
					enemyScore += enemyScoresDict[section5]
					enemyTrapIndicators[2] = 1
				if c == self.BOARD_DIMENSION - 6 or r == self.BOARD_DIMENSION - 6:

					section5 = section6[1:] 
					if section5 in evaluatorScoresDict:
						evaluatorScore += evaluatorScoresDict[section5]
						evaluatorTrapIndicators[2] = 1
					elif section5 in enemyScoresDict:
						enemyScore += enemyScoresDict[section5]
						enemyTrapIndicators[2] = 1

		for c in range(self.BOARD_DIMENSION - 5):
			for r in range(5, self.BOARD_DIMENSION):
				section6 = ''
				for i in range(6):
					section6 += board[r - i][c + i]
				section5 = section6[:-1]
				if section6 in evaluatorScoresDict:
					evaluatorScore += evaluatorScoresDict[section6]
					evaluatorTrapIndicators[3] = 1
				elif section6 in enemyScoresDict:
					enemyScore += enemyScoresDict[section6]
					enemyTrapIndicators[3] = 1
				if section5 in evaluatorScoresDict:
					evaluatorScore += evaluatorScoresDict[section5]
					evaluatorTrapIndicators[3] = 1
				elif section5 in enemyScoresDict:
					enemyScore += enemyScoresDict[section5]
					enemyTrapIndicators[3] = 1
				if c == self.BOARD_DIMENSION - 6 or r == 0:

					section5 = section6[1:] 
					if section5 in evaluatorScoresDict:
						evaluatorScore += evaluatorScoresDict[section5]
						evaluatorTrapIndicators[3] = 1
					elif section5 in enemyScoresDict:
						enemyScore += enemyScoresDict[section5]
						enemyTrapIndicators[3] = 1

		topLeft, topRight, bottomRight, bottomLeft = '', '', '', ''
		for i in range(5):
			topLeft += board[4-i][i]
			topRight += board[i][self.BOARD_DIMENSION - (5-i)]
			bottomRight += board[self.BOARD_DIMENSION - i - 1][self.BOARD_DIMENSION - (5-i)]
			bottomLeft += board[self.BOARD_DIMENSION - (5-i)][i]
		cornerCounter = 1
		for section in [topLeft, topRight, bottomRight, bottomLeft]:
			if section in evaluatorScoresDict:
				if section.count(colorOfEvaluator) == 4:

					evaluatorScore += evaluatorScoresDict[section]
					evaluatorTrapIndicators[cornerCounter%2 + 2] = 1
				else:
					evaluatorScore += (evaluatorScoresDict[section] // 2) 
			elif section in enemyScoresDict:
				if section.count(colorOfEnemy) == 4:

					enemyScore += enemyScoresDict[section]
					enemyTrapIndicators[cornerCounter%2 + 2] = 1
				else:
					enemyScore += (enemyScoresDict[section] // 2) 
			cornerCounter += 1

		numberOfEvaluatorTraps = sum(evaluatorTrapIndicators)
		numberOfEnemyTraps = sum(enemyTrapIndicators)

		if numberOfEvaluatorTraps > 1:
			evaluatorScore *= 4
		if numberOfEnemyTraps > 1:
			enemyScore *= 4

		if playerWithTurnAfterMaxDepth == colorOfEvaluator and numberOfEvaluatorTraps >= 1:
			evaluatorScore *= 4
			if evaluatorScore > enemyScore:
				return 25 * evaluatorScore, enemyScore
		elif playerWithTurnAfterMaxDepth == colorOfEnemy and numberOfEnemyTraps >= 1:
			enemyScore *= 4
			if enemyScore > evaluatorScore:
				return evaluatorScore, 25 * enemyScore

		if numberOfEvaluatorTraps >= 1 and numberOfEnemyTraps >= 1:
			if evaluatorScore > enemyScore:
				evaluatorScore *= 5
			elif enemyScore > evaluatorScore:
				enemyScore *= 5

		return evaluatorScore, enemyScore

	def scorePositionWeights(self, board, colorOfEvaluator, colorOfEnemy):
		"""Scores the board based on the weights of the individual locations (center preferred)"""
		evaluatorScore = 0
		enemyScore = 0
		for row in range(self.BOARD_DIMENSION):
			for col in range(self.BOARD_DIMENSION):
				currSpot = board[row][col]
				if currSpot == colorOfEvaluator:
					evaluatorScore += self.positionWeightsMatrix[row][col]
				elif currSpot == colorOfEnemy:
					enemyScore += self.positionWeightsMatrix[row][col]
		return evaluatorScore, enemyScore

	def scoreBoard(self, board, colorOfEvaluator, colorOfEnemy, playerWithTurnAfterMaxDepth):
		"""
		Scores the entire board by looking at each section of spots,
		as well as the individual piece positions
		"""
		sectionsScores = self.scoreSections(board, colorOfEvaluator, colorOfEnemy, playerWithTurnAfterMaxDepth)
		positionWeightScores = self.scorePositionWeights(board, colorOfEvaluator, colorOfEnemy)
		evaluatorScore = sectionsScores[0] + positionWeightScores[0]
		enemyScore = sectionsScores[1] + positionWeightScores[1]
		return evaluatorScore, enemyScore

def opponentOf(color):
	"""Get the opposing color"""
	return WHITE if color == BLACK else BLACK

def performMove(board, row, col, color):
	"""Performs a given move on the board"""
	board[row][col] = color

def copyOfBoard(board):
	"""Returns a copy of the given board"""
	return list(map(list, board))
