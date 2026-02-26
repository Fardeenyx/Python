#Program to check the how many vowels are ther in a word 

s = input('Enter a word:') # hello world

vowels = 'aeiouAEIOU'

count = 0

for ch in s:
    if ch in vowels:
        count = count + 1;

print("Number of Vowels: ", count);