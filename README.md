# Generating negative binomial random variables

We have one final type of random variable to learn how to generate using python - the negative binomial random variable.  If you remember 
the negative binomial random variables measures the number of trials I have to perform in order to obtain exactly k successes.

To complete the exercise you will need to:

- Write a function called `bernoulli` that takes in a parameter called `p`. This parameter gives the probability that the trial is successful - and that the 
function thus returns a 1

- Use your `bernoulli` function in a second function called `geometric`. This `geometric` function should take one parameter `p` (the probability of success in each individual trial). The function should then return a geometric random variable.

Notice that you will need to use a while loop as you did in the previous exercises on generating the geometric random variable.  Furthermore, within this while loop you are going to need to generate Bernoulli random variables and keep track of two quantities; namely:

The number of trials that have been performed
The number of trials that were successful 
