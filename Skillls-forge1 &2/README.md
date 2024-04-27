String Compression and Largest Number Concatenation

This repository contains two Python programs:

1. String Compression: This program compresses a given string by replacing consecutive characters with their count. If the compressed string is shorter than the original string, it returns the compressed string; otherwise, it returns the original string.

2. Largest Number Concatenation: This program arranges a given array of non-negative integers in a manner such that, after concatenating them in order, it results in the largest possible number.

How to Run

String Compression
1. Make sure you have Python installed on your system.
2. Clone this repository to your local machine.
3. Navigate to the directory containing the `stringcompression.py` file.
4. Open a terminal or command prompt in that directory.
5. Run the following command:

    ```
    python stringcompression.py
    ```

6. Follow the on-screen instructions to enter the string you want to compress.
7. The compressed string or the original string will be printed as output.

Largest Number Concatenation
1. Make sure you have Python installed on your system.
2. Clone this repository to your local machine.
3. Navigate to the directory containing the `largestpossiblenumber.py` file.
4. Open a terminal or command prompt in that directory.
5. Run the following command:

    ```
    python largestpossiblenumber.py
    ```

6. The largest concatenated number will be printed as output.

Program Logic

String Compression
- The program iterates through the input string, counting the consecutive occurrences of each character.
- It then constructs the compressed string by appending the character and its count.
- If the length of the compressed string is shorter than the original string, it returns the compressed string; otherwise, it returns the original string.

Largest Number Concatenation
- The program defines a custom comparison function that compares two strings by concatenating them in different orders.
- It sorts the array of strings using this custom comparison function.
- Finally, it concatenates the sorted strings and returns the result, which represents the largest possible number.

---
