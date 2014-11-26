asplusquiz
==========

Python solutions for https://github.com/mark/asplus_ruby_quiz

### Problem 1

Write a program that takes an input string, and returns which characters are consecutively repeated the most times.  If there are multiple characters, return them in `sort` order.

* "aaddddffffaa" will return `[d, f]`
* "cat dog \_\_\_" will return `[_]`


### Problem 2

Write a class with a method `search` that accepts an IP address, and returns the country it's associated with (use the included specific list of mappings in `IpToCountry.csv`).

The CSV file stores IP addresses as integer values, but the comments at the top
tell how to convert to and from them. Let me know if you have any questions.

For example:

* `"67.99.163.76"` will output `'United States'`


### Problem 3

The digital root of a number is the (single digit) value obtained by an iterative process of summing digits, on each iteration using the result from the previous iteration to compute a digit sum. The process continues until a single-digit number is reached.

For example, the digital root of `65,536` is `7`, because `6 + 5 + 5 + 3 + 6 = 25` and `2 + 5 = 7`.

The digital root of of an array of numbers can be calculated similarly.  Using a similar example to the above, the digital root of `[ 6, 55, 3, 6 ]` is also `7`.

Please determine which subsets of [ 1, 2, 3, 4, 5, 6, 7, 8 ] meet ALL of the following properties:

1. Contain between 3 and 5 elements.
2. Contain the number 5.
3. Have a digital root of 9.
