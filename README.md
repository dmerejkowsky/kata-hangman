# Goal

Implement the hangman game on the command line

# Instructions

* Read the entire contents of the `mots.txt`
* Select a word at random
* Start an interactive loop

At each step, represent the word to guess, using `_` where the letter is
missing, or the letter itself if it's in the correct position.

The game should look like this, assuming the word to guess is "verre":

```
_____
entrer une lettre
> v
v____
entrer une lettre
> e
ve__e
entrer une lettre
> t
ve__e
entrer une lettre
> r
verre
gagné !
```

# To go further

Compute a score score and display it at the end. For instance,
you can use the number of tentatives it took the player to guess
the word.

Then, ask the player for its name and save the score in a database.

Then, display a message when the player breaks the record.
