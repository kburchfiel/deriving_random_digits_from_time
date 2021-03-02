# Deriving 'Random' Digits From Time.Time()
Python's time.time() function returns a number representing the number of seconds since 1970-1-1 (Allen B. Downey, Think Python, 2nd ed.). This number contains a decimal component with many digits. Therefore, I figured that the digits 8+ places to the right should be quite random (as it would be hard for a human to time the program to output a desired number). 

This program contains a function that converts the current time.time() output into a (somewhat) random digit between 0 and 10. It also contains a while loop that allows a user to manually request a new 'random' number. Finally, it contains a method to test how random the numbers created by this program are.

Please note that the numbers created by this program are likely not truly random! I do not recommend using it for any tasks that require high-quality random number generation.
