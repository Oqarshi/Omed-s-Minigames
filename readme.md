# Omed's Minigames

## Overview
## 🎮 Gomoku
The objective of Gomoku is to get 5 of your pieces to line up in 
succession. You can think of it like a much more advanced version 
of Tic Tac Toe. The board is much bigger (13x13), and you need 5 
pieces in a row instead of just 3. You may be surprised how much 
strategy is involved a game of Gomoku!
### 🧠 AI Features
- Advanced Minimax algorithm using Alpha-Beta Pruning, transposition 
tables, Zobrist Hashing, Iterative Deepening, and smart 
search-space-selection
- Very powerful AI engine. Calculates about ***729 MILLION*** Different positions before picking its move. Average time to calculate only ***30 sec - 2 min***!
- Dueling AI functionality allows you to challenge this AI with 
your own Gomoku AI
- Color-coded output on the game board to easily distinguish friendly 
pieces from enemy pieces, including highlighting the most recently 
played move.
- Save state functionality for if you want to exit the program and 
come back later 
- Ability to see all the previous moves that have been played, one by
  one, displayed on the game board
- Progress bar will be displayed as the AI is evaluating moves as well as the amount of nodes being processed
- Output to the terminal will be updated in place instead of printing 
lines and lines of output across turns. This can be disabled if you 
would like to have all output to the terminal preserved
- Modifiable AI parameters, including max AI search depth (# moves 
to look ahead), max number of moves to evaluate from each board 
state, and max neighbor distance (for determining valid moves)
- Ability to ****premove****

---

## 🎮 Othello
The objective of Othello is to end the game with more pieces than 
your opponent. You can capture enemy pieces by trapping them between 
two friendly pieces.
### 🧠 AI Features
- Minimax algorithm using Alpha-Beta Pruning
- Dueling AI functionality allows you to challenge this AI with
your own Othello AI
- Color-coded output on the game board to easily distinguish friendly 
pieces from enemy pieces.
- Valid moves will be highlighted for you before each turn
- Optional colorblind mode will use a blue/orange color scheme instead 
of green/red
- Save state functionality for if you want to exit the program and 
come back later 
- Ability to see all the previous moves that have been played, one by 
one, displayed on the game board.
- Output to the terminal will be updated in place instead of 
printing lines and lines of output across turns. This can be 
disabled if you would like to have all output to the terminal 
preserved
- Modifiable AI parameters, including max AI search depth (# moves 
to look ahead), max number of moves to evaluate from each board 
state, and board size
- Ability to ****premove****

--- 

## 🎮 Sea Battle
If you've ever played Battleship, Sea Battle is the same thing. You 
take turns guessing where the opponent has their ships laid out on 
a grid. Whoever sinks all the opposing ships first wins! This AI 
assists you by showing you which locations are mathematically most 
likely to contain ships.
### 🧠 AI Features
- Color-coded output on the game board to easily distinguish misses, 
hits, and sinks. Also used to show which locations are ideal for 
your next guess.
- A super beautiful colorful output of scores for each coordinate 
on the board, making use of a color gradient to distinguish the 
levels of certainty that a coordinate contains a ship
- Save state functionality for if you want to exit the program and
  come back later
- Board sizes of 8x8, 9x9, or 10x10
- Output to the terminal will be updated in place instead of 
printing lines and lines of output across turns. This can be 
disabled if you would like to have all output to the terminal 
preserved  


---

## 🎮 Connect 4
The objective of the game is to get 4 of your pieces to line up in 
succession. There are 7 columns for you to play, and the piece will 
be dropped to the lowest free space in the column you choose.
### 🧠 AI Features
- Minimax algorithm using Alpha-Beta Pruning
- Dueling AI functionality allows you to challenge this AI with
your own Connect 4 AI
- Save state functionality for if you want to exit the program and
  come back later
- Ability to see all the previous moves that have been played, one by
  one, displayed on the game board.
- Color-coded output on the game board to easily distinguish 
friendly pieces from enemy pieces. Includes a green coloring of 
the most recently played column, grey coloring of unavailable 
columns, and a blue border to match the classic look of the 
physical game rig.
- Output to the terminal will be updated in place instead of 
printing lines and lines of output across turns. This can be 
disabled if you would like to have all output to the terminal 
preserved
- Ability to ****premove****

---

## 🎮 Word Hunt
You're given a 4x4 grid of letters. To earn points, you connect 
adjacent letters together. This can be in any direction (horizontal, 
vertical, diagonal, and combinations of all three). You can't use 
the same tile on the grid more than once per word though!
### 🧠 AI Features
- Near-instant identification of all valid words present on the 
board up to 10 letters long
- Two output modes: Diagram Mode, and List Mode, both displaying 
words with higher values first
- Diagram mode will display the output as a grid with numbers to 
show the order and locations on the board for which you should drag 
your finger to create the word
- Output to the terminal will be updated in place instead of 
printing lines and lines of output across turns. This can be 
disabled if you would like to have all output to the terminal 
preserved  

---

## 🎮 Word Bites
Think of Scrabble, except you can play the pieces anywhere, and 
they can come in pairs (both vertical and horizontal). You earn 
points by combining letter pieces together to form words. Some 
pieces can only be played in certain orientations.
### 🧠 AI Features
- Near-instant identification of all valid words that can fit on 
the 9x8 board
- Two output modes: Diagram Mode, and List Mode, both displaying 
words with higher values first
- Diagram mode will display the output as it appears on the game 
board, whether thats in vertical or horizontal orientation
- Output to the terminal will be updated in place instead of 
printing lines and lines of output across turns. This can be 
disabled if you would like to have all output to the terminal 
preserved  

---

## 🎮 Mancala Avalanche
In this version of the classic Mancala game, a player's turn doesn't 
end until they run out of pebbles in an empty pocket. Players earn 
points by moving pebbles around the board and dropping them in 
their bank.
### 🧠 AI Features
- Two different versions that accomplish the same thing: One 
written in Python (recommended), and one written in Java
- Determines the optimal move order for the current board. (Note: 
It will be practically impossible for you to lose)
- Visualization of the board after each turn that replicates what 
the actual game board looks like
- (Python version only) Output to the terminal will be updated in 
place instead of printing lines and lines of output across turns. 
This can be disabled if you would like to have all output to the 
terminal preserved  

---

## 🎮 Anagrams
You're given 6 or 7 letters that you can arrange in any order you 
want to form words. Longer words earn you more points.
### 🧠 AI Features
- Option for either 6 or 7 letter games
- List mode displays 10 words at a time, displaying words with 
higher values first
- Output to the terminal will be updated in place instead of 
printing lines and lines of output across turns. This can be 
disabled if you would like to have all output to the terminal 
preserved  

--- 

## 🎮 Tic Tac Toe
On a 3x3 board, the objective is to get 3 of your pieces to line up 
in succession.
### 🧠 AI Features
- Minimax algorithm using Alpha-Beta Pruning
- Dueling AI functionality allows you to challenge this AI with
your own Tic Tac Toe AI
- Save state functionality for if you want to exit the program and
  come back later
- Ability to see all the previous moves that have been played, one by
  one, displayed on the game board.
- Color-coded output on the game board to easily distinguish 
friendly pieces from enemy pieces.
- Output to the terminal will be updated in place instead of 
printing lines and lines of output across turns. This can be 
disabled if you would like to have all output to the terminal 
preserved
- Ability to ****premove****

--- 

## 🎮 Wordle
You're given three options: Test Solver [T], Game Assist [A], and Play Game [P]. The client works by probability, not by picking a word, but by choosing the closest word that is probable and using it.
### 🧠 AI Features
#### Test Solver [T]
- Ability to choose how many games the tester should incorporate
- Capable of showing **games/second**, **Total time**, **Estimated completion time**, **Win percentage**, **Average Moves/game**, **Percentage of completion**, and **Progress bar**
#### Game Assist [A]
- Shows Best Starting word.
- ***Hands free***, no need to pick a word. Auto picker.
- Average guesses to solve based on ****10,000**** games is **3.8** Guesses
- Average Success rate based on ****10,000**** games is ****99.13%**** (5 guesses)
#### Play Game [P]
- Simple UI
- Color Coded UI
- Play wordle as much as you like
- No inappropriate words
- Uses Wordle's **official** word list
- Ability to ****premove****