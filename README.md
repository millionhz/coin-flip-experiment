# The Coin Flip Experiment

A simulation of the coin flip thought experiment.

Concept: <https://www.youtube.com/watch?v=uTChrirK-hw&t=373s>

## The Experiment

The experiment involves 100 people standing and flipping a coin and if the coin lands on heads they keep standing and if there coin lands on tails they sit.

Theoretically, considering that the chance of landing a heads is around 50%, 50 of the 100 people will sit down in the first round. Then 50% of those 50 people will site down in the next round and so on.

At the end there will be a person standing who would have flipped heads 6 times or more.

The purpose of the experiment is to prove that anything, no matter how unlikely it is, will happen when performed enough times.

The experiment also proves that there will always be at least one person who landed heads six times in a row, from a group of 100 people, which means that there is nothing like luck, its all just probabilities (provided that the probability of getting heads is perfectly 50%).

Check this [link](https://www.youtube.com/watch?v=uTChrirK-hw&t=373s) for more information.

NOTE: If you run `sim_no_log.py` with 100 subjects, mostly the last two or three subjects standing will flip tails, leaving no winner. This happens because of probability. This issue is also mentioned in [The Anomaly](#the-anomaly) section.

_I would recommend you to run the simulation with at least to 50000 subjects, for more prominent results (you can use this command: `python sim_no_log.py 50000`)._

## How the scripts works

The python scripts simulate the coin flip experiment by making a set of a specific number of subjects, and calculating the state of the flipped coin by using the python random library.

## Main Script

**Use `sim_no_log.py` for the simulation.**

It uses only a **few MBs** of memory and there is **no limit** to the number of subjects it can simulate.

### Using `sim_no_log.py`

By default `sim_no_log.py` will simulate 10000 subjects if no argument is provided:

```code
python sim_no_log.py

Running simulation with 10000 subjects
```

You can specify the number of subject by using the positional argument:

```code
python sim_no_log.py 10000000

Running simulation with 10000000 subjects
```

## Other Scripts

`sim_low_memory.py` and `sim_high_memory.py` are **slower** and **more memory intensive** as they log all the details (i.e. the ids of the subjects and there coin flips) into an array. Logging info is good if we want to analyze the data later or plot it but in our case it is irrelevant. They also **do not support argument parsing.**

`sim_low_memory.py` simulates up to **20000** subjects. This script stores all the subjects in one array and manipulate that array by removing the subjects who lost (i.e. flipped tails). The removing mechanism causes memory errors when a large data set is used.

`sim_high_memory.py` simulates **10000000** subjects. This script stores the subjects in an array, it then makes another array where it stores the subjects who got a heads and then it replaces the old array with the new one. That is the reason why this script can use up to **2000MB** of memory. The memory usage can be decreased by using a better data structure _(which i didn't)_. It is just to show that up to **22** consecutive coin flips to heads is possible.

## The Anomaly

Sometimes the script will not return a result (i.e. %age Lost : 100%); its mainly because the last 2 or 3 subjects standing flipped tails. This is very unlikely but these sort of things happen because of probability. This issue is also mentioned at the end of the [The Experiment](#the-experiment) section.

## Example Run

```code
python sim_no_log.py 50

Running simulation with 50 subjects

Round: 1
Out of 50; 28 people flipped heads 1 time/s
%age Lost: 44.0


Round: 2
Out of 28; 16 people flipped heads 2 time/s
%age Lost: 42.857142857142854


Round: 3
Out of 16; 10 people flipped heads 3 time/s
%age Lost: 37.5


Round: 4
Out of 10; 3 people flipped heads 4 time/s
%age Lost: 70.0


Round: 5
Out of 3; 1 people flipped heads 5 time/s
%age Lost: 66.66666666666666

In this simulation 1 person flipped heads 6 times
```
