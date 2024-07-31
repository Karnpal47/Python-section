#14)Find the number of vowels from the string

str="KarmaSaidUs"
count_vowel=0
for i in str:
    if (i in('a','e','i','o','u','A','E','I','O','U')):
        count_vowel+=1
print(f"The vowels in string {str}=",count_vowel)