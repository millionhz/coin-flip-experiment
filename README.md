# Lucky Coin

A simulation of a coin flip thought experiment.

Check this out: <https://www.youtube.com/watch?v=uTChrirK-hw&t=373s>

## The Experiment

The experiment involves 100 people standing and flipping a coin and if the coin lands on heads they keep standing and if there coin lands on tails they sit.

Theoretically, considering that the chance of landing a heads is around 50%, 50 of the 100 people will sit down in the first round. Then 50% of those 50 people will site down in the next round and so on.

At the end there will be a person standing who would have flipped heads 6 times or more.

The purpose of the experiment is to prove that anything, no matter how unlikely it is, will happen when performed enough times.

The experiment also proves that there will always be someone who landed heads six times in a row, from a group of 100 people, which means that there is nothing like luck, its just all probabilities.

Also check out the [link](https://www.youtube.com/watch?v=uTChrirK-hw&t=373s) provided above.

## How the code works

The python scripts simulate the coin flip experiment by making a set of a specific number of people, and recording there coin flips in an array, until only one person stands. The coin flips are calculated using the python random library.

`sim_low_memory.py` simulates **10000** people. I choose that number as it is a quick script you can run and it does not uses a lot of memory.

`sim_high_memory.py` simulates **9000000** people. It is just to show that **22** consecutive coin flips to heads is possible. However, this script can use up to **2000MB** of memory and it is also a little slow. The memory usage can be decreased by using a better data structure _(which i didn't)_.

## The Anomalies

Sometimes the script will not return a result, and its mainly because the last 2 or 3 people standing flipped tails. This is very unlikely but I have seen it happen during testing.
