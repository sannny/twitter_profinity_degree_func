# twitter_profinity_degree_func

## ABOUT 

This script helps in identifying racial slurs and rates them on their profinity. 

## How it works?

This sections explains the idea of how the algorithm works

### Assumptions

We have identified the racial slurs and given them a score. 

### Overview

The overall idea is that we take important words from the slurs in a sequence that we think it should occur in and then look for the sequence in the tweet.

For example, racial slur is "M people should go back to T fields!". Here we can say that if "M", "back", "T" and "fields" occur in these sequence it can be identified as a racial slur.

The reason we look for sequence is that these sentences might not occur as a substring in the tweet. Like, "Ms, you know what? you guys dont belong here. Go back to T fields!".

Also, since tweets are bounded by 140 characters, it would not be too long for sure.

Lastly, we run each sequence through each tweet to make sure if there is use of multiple slurs.

### Steps

  1. Initialize the Profinity_calculator class with racial slurs.
  2. Read the tweets csv.
  3. Get the profinity score for each tweet using profin_calculator function
  4. Get the profinity rank for each tweet using profin_ranker function
  5. Lastly print your results using print_results function

***OR***

You can just call profinity_checker(racial_slurs, path) from the main.py. 

Here racial slurs is a dictionary.

Key = Tuple(Sequence)
Value = profinity score

Here's how the output from the smaple tweet would look like
![image](https://user-images.githubusercontent.com/43197031/176900097-36607e67-844e-4c59-abb4-c9c2caa5abd9.png)

##NOTE : I AM NOT A RACIST. JUST WROTE THE GENERAL SLURS TO EXPLAIN THE CONCEPT. 


