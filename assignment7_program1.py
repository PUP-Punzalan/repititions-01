# function for counting the characters
def counter(sentenceF):
    # splitting the words
    totalWords = len(sentenceF.split())

    # arranging the COUNT VARIABLES and setting the first value to 0
    vowelCount = 0
    numberCount = 0
    consonantCount = 0
    spaceCount = 0
    otherCharCount = 0

    # arranging the VARIABLES and listing their value (in string)
    vowels = ["a", "e", "i", "o", "u"]
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
    consonants = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z", "ñ"]
    space = [" "]

    # arranging the conditions by vowels > consonants > numbers > space > other characters
    for c in sentenceF:
        if c in vowels:
                vowelCount = vowelCount + 1
        else:
            if c in consonants:
                consonantCount = consonantCount + 1
            else:
                if c in numbers:
                    numberCount = numberCount + 1
                else:
                    if c in space:
                        spaceCount = spaceCount + 1
                    else:
                        otherCharCount = otherCharCount + 1

    # printing all the data needed (words, vowels, and consonants)
    print(f"Output:\nWord(s): {totalWords}\nVowel(s): {vowelCount}\nConsonant(s): {consonantCount}")

# asking for the input as well as converting the input into lowecase
sentence = input("Input: ").lower()

# calling the funcition with the sentence variable
counter(sentence)