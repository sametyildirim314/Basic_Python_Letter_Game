You are expected to write a program for a game played between two people (Player A and Player B).
Both players will have a string consisting of 26 letters and a list containing 10 integers (ranging from 0 to 25). These lists will be taken as input from the user. Instead of entering the values one by one, you can run the input files provided to you as described above.

Each integer in the list indicates the index of the letter to be removed from the other player's letter string.
At the end of the game, both players will have 16 letters left.

For example,
Player A's letter list is as follows:
str_A = "MZNHUVIOEPTWFJCBXKALSDQGYR"

Player B's letter list is as follows:
str_B = "YFTUCSQOMGKPXNDWHIVJRABZEL"
The index list of letters to be removed from str_B is as follows:
ind_A = [1, 3, 2, 8, 10, 12, 9, 7, 4, 22]
In order, the letters F, U, T,…, C, B will be removed from the str_B list.
The index list of letters to be removed from str_A is as follows:
ind_B = [21, 24, 25, 3, 4, 1, 8, 9, 10, 17]
In order, the letters D, Y, R,…, T, K will be removed from the str_A list.

As a result, the new lists of Player A and Player B will be as follows:
str_A = "MNVIOWFJCBXALSQG"
str_B = "YSQPNDWHIVJRAZEL"

After this process, the ASCII values of the remaining letters of both players (starting from the left) will be compared, and the difference in ASCII values between the letters in the same position will be given as points to the player whose letter has a higher ASCII value.

str_A = "MNVIOWFJCBXALSQG"
str_B = "YSQPNDWHIVJRAZEL"
Player A = 77, 78, 86, 73, 79, 87, 70, 74, 67, 66, 88, 65, 76, 83, 81, 71
Player B = 89, 83, 81, 80, 78, 68, 87, 72, 73, 86, 74, 82, 65, 90, 69, 76

Comparison of the ASCII values of the letters will start:
Player A vs. Player B:
Round 1: 77 vs. 89
Player B gains 12 points (89 - 77 = 12)

Round 2: 78 vs. 83
Player B gains 5 points (83 - 78 = 5)

Round 3: 86 vs. 81
Player A gains 5 points (86 - 81 = 5)

Round 4: 73 vs. 80
Player B gains 7 points (80 - 73 = 7)

Round 5: 79 vs. 78
Player A gains 1 point (79 - 78 = 1)

...and so on.

Your result should be in the form of a dictionary:
{'A': 64, 'B': 96}

