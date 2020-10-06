'''
Veda wants to work on a project. The main aim of the project is to detect the prime
number within the specified range. So, help him to develop the project.
Input format:
1. First line contains two integer “start” and “stop”, which resembles a range I.e, start ≤
range ≤ stop.
Output format:
1. The output should contain all the prime numbers within the specified range.
2. If the value of start is greater than stop, it should print “Invalid Range” in the output.
Constraints:
1. Start ≤range ≤stop.
2. 1≤start≤1000 and 1≤start≤1000.
3. 1 is neither prime nor composite.
Sample input 0:
1 20
Sample output 0:
2 3 5 7 11 13 17 19
Sample input 1:
100 500
Sample output 1:
101 103 107 109 113 127 131 137 139 149 151 157 163 167 173 179 181 191 193 197 199
211 223 227 229 233 239 241 251 257 263 269 271 277 281 283 293 307 311 313 317 331
337 347 349 353 359 367 373 379 383 389 397 401 409 419 421 431 433 439 443 449 457
461 463 467 479 487 491 499
'''

start, stop = map(int,input().split())

for i in range(start, stop+1):
    if i % 2 != 0:
        print(i, end = ' ')

#Time Complexcity : O(n)
