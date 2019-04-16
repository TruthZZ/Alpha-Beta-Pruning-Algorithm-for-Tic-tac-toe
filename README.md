# Alpha-Beta-Pruning-Algorithm-for-Tic-tac-toe
A Python implementation of Tic-tac-toe based on PyQt5 and two heuristic solution to game with each other or with human.

This program can simulate a Tic-tac-toe game:
1. You can set the length of the word chess, that is, the board of n*n, and the winning condition is that the n pieces are connected in a line.
2. Two artificial intelligence search algorithms are designed, one is heuristic mountain climbing method, and the other is third-order α-β clipping algorithm based on the heuristic function.
3. Two players (one-handed) can choose three players (human player, mountain climbing method, α-β pruning algorithm), and perform everyone's game, man-machine game and artificial intelligence.

Some experimental results:
1. After repeated measures, when the man-machine is playing, neither type of AI can be lost to human players, and at most can only draw.
2. Because the chess game is simple, the heuristic algorithm is enough to ensure that the AI ​​will not lose. When using the α-β pruning algorithm, the AI ​​will change and will not lose to humans, but the algorithm operation Time will increase greatly

Some areas that have not been improved:
1. In the AI interlocking, some lengths of α-β pruning algorithm vs. mountain climbing, α-β pruning algorithm will win (theoretically should be a draw, due to time, the problem is not clear), but Other situations such as different lengths, as well as the hill-climbing-climbing method, the α-β pruning algorithm-α-β pruning algorithm are a draw for the tactic experiment.
