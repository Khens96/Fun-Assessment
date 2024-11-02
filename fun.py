def dog_years(human_years):
    
    """
    Create a program that counts a dog's age in dog's years. The program should only calculate dog years until 20 human years.
    Note: For the first two years, a dog year is equal to 10.5 human years. After that, each dog year equals 4 human years.

    Expected Output:
    ```
    Input a dog's age in human years: 15
    The dog's age in dog's years is 73
    ```
    """

    if human_years <= 2:
        dog_years = human_years * 2
    else:
        dog_age = 21 + (human_years - 2) * 4
        return dog_age
    human_years = int(input("Enter dog's age in human years:"))
    dog_age = dog_years(human_years)
    print(f"The dog's age in dog's years is {dog_age}")

     




def fizzbuzz(num):
    """
    Create a program that returns the numbers as a string from 1 to num. 
    But for multiples of three print “Fizz” instead of the number, 
    and for multiples of five print “Buzz”. For numbers which are 
    multiples of both three and five, print “FizzBuzz”.

    Expected Output:
    fizzbuzz(15) => "1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz"
    """

    if num%3 == 0 and num%5 == 0:
        return "FizzBuzz"
    elif num%5 == 0:
        return "Buzz"
    elif num%3 == 0:
        return "Fizz"
    else:
        return str(num)
    print(fizzbuzz(15))
    

    

def word_lengths(sentence):
    """
    Create a program that takes a sentence and returns a dictionary with each unique word
    as the key and the length of the word as the value.

    Expected Output:
    ```
    Input a sentence: "Aunty Yankho is amazing"
    Output: {'Aunty': 5, 'Yankho': 6, 'is': 2, 'amazing': 7}
    ```
    """
    
    word = sentences.split()
    word_lengths = {}
    for word in words:
        word_lengths[word] = len(word)
    return word_lengths

    sentences = int(input("Enter a sentence:"))
    result - word_lengths(sentence)
    print(result)

def cube_sum(number):
    """
    Create a program that calculates the sum of the cubes of each digit in a number.
    
    Expected Output:
    ```
    cube_sum(123) => 1^3 + 2^3 + 3^3 = 1 + 8 + 27 = 36
    ```
    """
      
    cube_sum = 0
    while number > 0:
        digit = number % 10
        cube_sum += digit **3
        number //= 10
    return cube_sum
    number = int(input("Enter a number:"))
    result = cube_sum(number)
    print(f"The sum of cubes of each digits in a {number} is {result}")

