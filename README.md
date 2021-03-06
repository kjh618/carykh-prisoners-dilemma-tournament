# Entry for Carykh's Prisoner's Dilemma Tournament

This is my entry for [carykh](https://www.youtube.com/user/carykh)'s [prisoner's dilemma tournament](https://www.youtube.com/watch?v=r2Fw_rms-mA).
The submitted strategy is `code/strats/kjhDetectRandom2.py`.

You can see the original README below.

---

# PrisonersDilemmaTournament

This is my CS 269i class project. Check out my webpage for context! https://htwins.net/prisoners-dilemma/

Watch This Place's awesome videos about iterated Prisoner's Dilemma for more context!

https://www.youtube.com/watch?v=t9Lo2fgxWHw

https://www.youtube.com/watch?v=BOvAbjfJ0x0

Nicky Case's "The Evolution of Trust" is also super fascinating, but it's not necessary to understand this project: https://ncase.me/trust/

How this works:
When you run code/prisonersDilemma.py, it will search through all the Python strategy files in code/exampleStrats. Then, it will simulate "Iterated Prisoner's Dilemma" with every possible pairing. (There are (n choose 2) pairings.) After all simulations are done, it will average each strategies' overall score. It will then produce a leaderboard of strategies based on their average performance, and save it to results.txt.

If you'd like to add your own strategy, all you have to do is create a new .py file in the code/exampleStrats folder that follows the same format as the others. Then, when you run code/prisonersDilemma.py, it should automatically include your strategy into the tournament!

# Details
| Payout Chart  | Player A stays silent | Player A tells the truth |
| ------------- | ------------- | ------------- |
| Player B stays silent  | A: +3, B: +3  | A: +5, B: +0  |
| Player B tells the truth  | A: +0, B: +5  | A: +1, B: +1  |

In this code, 0 = 'T' = telling the truth, and 1 = 'S' = staying silent.

---

Strategy functions take in two parameters, 'history' and 'memory', and output two values: 'moveChoice' and 'memory'. 'history' is a 2\*n numpy array, where n is the number of turns so far. Axis one corresponds to "this player" vs "opponent player", and axis two corresponds to what turn number we're on.
For example, it might have the values
```
 [[0 0 1]       a.k.a.    T T S
  [1 1 1]]      a.k.a.    S S S
```
In this case, there have been 3 turns, we have told the truth twice and then stayed silent once, and our opponent has stayed silent all three times.

'memory' is a very open-ended parameter that can takes on any information that should be retained, turn-to-turn. Strategies that don't need memory, like Tit-for-tat, can simply return None for this variable. If you want to keep track of some state, like whether the other person has ever told the truth (such as in grimTrigger.py), you can set memory to True or False. If you have an extremely complicated strategy, you have make 'memory' store a list of arbitrarily many varibles!

For the outputs: the first value is just the move your strategy chooses to make, with 0 being telling the truth and 1 being staying silent. The second value is any memory you'd like to retain into the next iteration. This can be 'None'.

---

Each pairing simulation runs for this many turns:
```
200-40*np.log(random.random())
```
This means each game is guaranteed to be at least 200 turns long. But then, for every turn after the 200th, there is an equal probability that the game ends. The probability is very low, so there should be no strategizing on the very last turn consequence-free.

---

Please submit your strategies to this Google Form: https://forms.gle/wWwZY9mmSHF2X34P7 by May 26th, 2021 at 10 PM UTC. Your file can be named whatever you want your strategy to be called, like "superCleverDetective.py", but you must keep it a .py file. Also, do not rename the function header within the file - you must keep it as "def strategy(history, memory):". When I???ve got all your strategies collected in one place, I will combine them with that list of 9 example strategies already provided in the GitHub repo. With these (9 + n) strategies all appearing once in this giant "mosh pit", I will run the program "prisonersDilemma.py". Whoever???s single strategy takes the top spot will win $1,000!  Second place will win $300, and third place will win $100. (Note: There is a small chance one of the 9 default strategies win, but I hope that doesn't happen!)
