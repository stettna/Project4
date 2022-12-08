-- Project 4 | Tic-Tac-Toe: Sockets --
@ Austin Black                   |
@ Nathan Stettler                |
==================================
-- Premise --
Our Final Project's main focus is on building a simple multiplayer game.
The two players will be playing on two seperate computers over the network
Both players (clients) will be connecting to a server and sending relevant information 
back and forth to each other through the host server

-- Libraries \ Modules Used --
sockets <- Primary
time
os

-- Gameplay --
  - tic tac toe
  - Both players connect and the game begins
  - Players take turns making moves
  - Game ends on a win/loss or restarts on a cat (tie)

-- To Run --

Run python3 server.py on a computer you want to be the host
Then run python3 client.py arg on each client window where arg is the name of the host machine.

-- To Run Tests --
   -pytest to run unit tests on win detection function

The rest can be tested my playing the game:
   -Try entering different invalid inputs to see that the are rejected
   -Try going out of turn to see that nothing malicious happens
   -Try tieing to see the that round resets
   -Try winning and losing to see that the game ends properly
   -Try losing
   -Try connecting a third client and see the connection refused
   -Try quitting in the middle of the game to see that each client is notifed and the server and clients shutdown
