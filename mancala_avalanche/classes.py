class Player(object):
    def __init__(self):
        self.score = 0
    def incrementScore(self):
        self.score += 1
    def copyPlayer(self):
        p = Player()
        p.score = self.score
        return p

BANK = 0
EMPTY_PIT = 1
PIT_WITH_PIECES = 2

class AvalancheBoard(object):

    def __init__(self, pebblesInEach, player1, player2, playerOneTurn):
        self.pebblesList = pebblesInEach.copy()
        self.p1 = player1
        self.p2 = player2
        self.p1Turn = playerOneTurn

    def performMoveSet(self, moveList):
        continueMoves = True
        moveNumber = 1
        for boardSpot in moveList:
            if not continueMoves:
                print("Move #%d in the given move set was invalid (previous move did not end in player bank)" % moveNumber)
                print("The move set was:  " + str(moveList))
                break
            continueMoves = self.performMove(boardSpot)
            moveNumber += 1
        self.switchTurn()
        return self.p1.score, self.p2.score

    def performMove(self, position):
        currBankIndex, enemyBankIndex = self.getBankIndexes()
        currPlayer = self.p1 if self.p1Turn else self.p2
        numPebbles = self.pebblesList[position]
        self.pebblesList[position] = 0
        turnEndedInPlayerBank = False
        while True:
            if numPebbles == 0:
                endOfMove = self.endOfCurrentMove(position, currBankIndex)

                if(endOfMove != PIT_WITH_PIECES):

                    turnEndedInPlayerBank = True if endOfMove == BANK else False
                    break
                else:
                    numPebbles = self.pebblesList[position]
                    self.pebblesList[position] = 0
            position = (position + 1) % 14 if (position + 1) != enemyBankIndex else (position + 2) % 14
            self.addPebbleToLocation(position, currBankIndex, currPlayer)
            numPebbles -= 1
        return turnEndedInPlayerBank

    def endOfCurrentMove(self, pos, currBankIndex):

        if pos == currBankIndex:
            return BANK
        elif self.pebblesList[pos] == 1:
            return EMPTY_PIT
        else:
            return PIT_WITH_PIECES

    def addPebbleToLocation(self, index, currBankIndex, currPlayer):
        self.pebblesList[index] += 1
        if index == currBankIndex:
            currPlayer.incrementScore()

    def getBankIndexes(self):
        if self.p1Turn:
            return 6,13
        else:
            return 13,6

    def printBoardHorizontal(self):

        if self.p2.score == self.p1.score:
            scoreStr = "\t  The score is tied at %d\n" % self.p2.score
        else:
            if self.p2.score > self.p1.score:
                scoreStr = "\t  Enemy winning %d to %d\n" % (self.p2.score, self.p1.score)
            else:
                scoreStr = "\t  You're winning %d to %d\n" % (self.p1.score, self.p2.score)
        print(str(self) + scoreStr)

    def __str__(self):
        enemyRow = "E\t|" + self.scoreRowToStrHoriz(12, 6, -1) + "\n"
        bankRow = "%d\t-------------------------\t%d\n" % (self.p2.score, self.p1.score)
        playerRow = "\t|" + self.scoreRowToStrHoriz(0, 6, 1) + "\tP\n"
        return enemyRow + bankRow + playerRow

    def scoreRowToStrHoriz(self, start, end, direction):
        scoresStr = ""
        for i in range(start, end, direction): 
            thisSpotStr = "%d |" % self.pebblesList[i]
            if self.pebblesList[i] < 10:
                thisSpotStr = " " + thisSpotStr
            scoresStr += thisSpotStr
        return scoresStr

    def switchTurn(self):
        self.p1Turn = not self.p1Turn

class AvalancheSolver(object):

    def __init__(self, board):
        self.board = board

    def copyBoard(self, boardToCopy):
        return AvalancheBoard(boardToCopy.pebblesList, boardToCopy.p1.copyPlayer(), boardToCopy.p2.copyPlayer(), boardToCopy.p1Turn)

    def makeMovesOnMoveset(self, moveList, board):
        prevScore = board.p1.score
        board.performMoveSet(moveList)
        return board.p1.score - prevScore

    def makeMove(self, index, board):
        prevScore = board.p1.score
        endedInBank = board.performMove(index)
        return board.p1.score - prevScore, endedInBank

    def findBestMove(self, board, currVal):
        indexOptions = self.getListOfNonZeroIndexes(board)
        if len(indexOptions) == 0:

            return currVal, []
        bestIncrease = -1
        bestIndex = indexOptions[0]
        bestMoveList = [0]

        for index in indexOptions:
            thisRunIncrease = 0
            thisMoveList = []
            boardCopy = self.copyBoard(board)
            makeMoveResults = self.makeMove(index, boardCopy)
            pointsGained, endedInBank = makeMoveResults[0], makeMoveResults[1]
            if endedInBank:
                thisRunIncrease, thisMoveList = self.findBestMove(boardCopy, pointsGained)
            else:
                thisRunIncrease = pointsGained
            if thisRunIncrease > bestIncrease:
                bestIncrease = thisRunIncrease
                bestIndex = index
                bestMoveList = thisMoveList.copy()
                bestMoveList.insert(0, bestIndex)
        return bestIncrease + currVal, bestMoveList

    def getListOfNonZeroIndexes(self, board):
        nonZeros = []
        for i in range(0, 6, 1):
            if board.pebblesList[i] != 0:
                nonZeros.append(i)
        return nonZeros