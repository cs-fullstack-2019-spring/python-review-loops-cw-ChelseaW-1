

def main():
   # Exercise1()
    # Exercise2()
   # Exercise3


   # Exercise1
   # Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.
   # Hint: Use 'continue' statement.
   # Expected Output : 0 1 2 4 5
# Loop check
   # for i=0: i=6: i++:
   # for eachEl in range(0,6):
   #     if (eachEl ==3 or eachEl ==6):
   #         continue
   #
   #     print (eachEl)


   # while(true);
   #     if(3 or 6)
   #      print(continue);
   #     else

#    Exercise 2
#    Write a Python program to count the number of even and odd numbers from a series of numbers.
#
# Sample numbers: numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
#     List of number
    numbers = (1,21,3,19,5,6,73,81,9)

    numOfOdds = 0
    numOfEvens = 0

    for num in numbers:
        if num % 2== 0:
            numOfEvens+=1
        else:
            numOfOdds+=1


    # Print of the count for even and odd numbers
    print("Even numbers:" +str(numOfEvens))
    print("Odd Numbers:" + str(numOfOdds))



   #Exercise3
# Write a Python program that accepts a sequence of lines (blank line to terminate)
# as input and prints the lines as output after User enters a blank line to end.
#
# Do not use an array to hold the lines of text
#
# Hints: You can use "\n" if you want to add a line break between sentences
#










if __name__ == '__main__':
        main()