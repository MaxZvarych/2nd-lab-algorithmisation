# Hamsters problem

### Write on Python language

You need to buy a hamster in the store.
Each hamster has two characteristics - hunger and greed.
Hunger - how much food a hamster eats per day.
Greediness - how much food he eats for each of his neighbors.
You have a certain amount of food per day.
There are a certain amount hamsters in the store.
You need to buy as many hamsters as possible.
The task is to determine the maximum number of hamsters that can be purchased.

## Instruction :

Algorithm calculates the data from the hamstr_in file and write the answer to the hamstr_out file.
If you want to fill hamstr.in file by your own:
	Enter the first number - the amount of feed per day.
	Enter the second number - the number of hamsters in the store.
	Next, list the characteristics of each hamster through a space, where each line has two numbers.
	Then press enter and the algorithm will calculate the answer for you.

## Algorithm :

To begin, the algorithm reads the data
Where hunger is not greater than the amount of food, he writes in list
Next, if no element was recorded - 0 is displayed
Otherwise, the first n most profitable hamsters are sought, where n is iterated to the number of elements
During each iteration there is the total amount of food needed for these hamsters
If some amount is bigger than amount of food you have, the previous number of hamsters will be displayed
Also, if the algorithm reaches the end, but no amount is found that is greater than what you have - the maximum value will be displayed
