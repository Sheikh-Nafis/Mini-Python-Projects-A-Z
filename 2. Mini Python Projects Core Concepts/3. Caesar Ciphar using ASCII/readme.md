Encoding Example 1: Shifting 'c' by 3

# chr(ord(char) - ord('a') + shift % 26 + ord('a'))

ord('c') gives 99 and rd('a') gives 97.
Subtracting gives:
99 - 97 = 2
(This is the position of 'c' in the alphabet, where 'a' = 0, 'b' = 1, 'c' = 2.)

Adding the shift value of 3 gives:
2 + 3 = 5.
This means we want to move 3 positions after 'c'.

Modulo 26 keeps it within bounds:
5 % 26 = 5
No wraparound is needed, since 5 is within the alphabet.

Adding ord('a') gives:
5 + 97 = 102,
which corresponds to chr(102), resulting in 'f'.

Final Result for Encoding:
So, shifting 'c' by 3 results in 'f'.



	Encoding Example 2: Shifting 'y' by 3
	
	ord('y') gives 121 and ord('a') gives 97.
	Subtracting gives:
	121 - 97 = 24
	(This is the position of 'y' in the alphabet, where 'a' = 0, 'b' = 1, ..., 'y' = 24.)
	
	Adding the shift value of 3 gives:
	24 + 3 = 27.
	This means we want to move 3 positions after 'y'.
	
	Modulo 26 keeps it within bounds:
	27 % 26 = 1
	The modulo operation wraps around, as 27 is beyond 'z'. The result is 1, which corresponds to 'b'.
	
	Adding ord('a') gives:
	1 + 97 = 98,
	which corresponds to chr(98), resulting in 'b'.
	
	Final Result for Encoding:
	So, shifting 'y' by 3 results in 'b'.



Decoding Example 1: Shifting 'f' by -3
Now, let's decode 'f' by shifting it backwards by 3:

ord('f') gives 102.

ord('a') gives 97.
Subtracting gives:
102 - 97 = 5
(This is the position of 'f' in the alphabet, where 'a' = 0, 'b' = 1, 'c' = 2, ..., 'f' = 5.)

Subtracting the shift value of -3 gives:
5 - 3 = 2.
This means we want to move 3 positions back from 'f'.

Modulo 26 keeps it within bounds:
2 % 26 = 2
No wraparound is needed, since 2 is within the alphabet.

Adding ord('a') gives:
2 + 97 = 99,
which corresponds to chr(99), resulting in 'c'.

Final Result for Decoding:
So, decoding 'f' by -3 results in 'c'.



	Decoding Example 2: Shifting 'b' by -3
	Now, let's decode 'b' by shifting it backwards by 3:
	
	ord('b') gives 98 and ord('a') gives 97.
	Subtracting gives:
	98 - 97 = 1
	(This is the position of 'b' in the alphabet, where 'a' = 0, 'b' = 1.)
	
	Subtracting the shift value of -3 gives:
	1 - 3 = -2.
	Since this is a negative value, we need to use modulo 26 to "wrap around" to the end of the alphabet.
	
	Modulo 26 keeps it within bounds:
	-2 % 26 = 24
	This gives us 24, which corresponds to 'y'.
	
	Adding ord('a') gives:
	24 + 97 = 121,
	which corresponds to chr(121), resulting in 'y'.
	
	Final Result for Decoding:
	So, decoding 'b' by -3 results in 'y'.

Summary:
Encoding Example 1: Shifting 'c' by 3 results in 'f'.
Encoding Example 2: Shifting 'y' by 3 results in 'b'.
Decoding Example 1: Shifting 'f' by -3 results in 'c'.
Decoding Example 2: Shifting 'b' by -3 results in 'y'.
