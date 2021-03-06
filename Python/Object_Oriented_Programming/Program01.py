# Take the word and its meaning as input from the user.
# -> Create a class named flashcard, use the __init__() function to assign values for Word and Meaning.
# -> Now use the __str__() function to return a string that contains the word and meaning.
# -> Store the returned strings in a list named flash.
# -> Use a while loop to print all the stored flashcards.
# -> Add proper error handling

print("----------------------------------------------------------------------------------------")
print("WELCOME TO FLASHCARD APPLICATION...!!".center(80))
print("----------------------------------------------------------------------------------------")

class flashcard:           
        flash = []
        def __init__(self,word,meaning):
            self.word = word
            self.meaning = meaning
        
        def __str__(self):
            string = f'{ self.word } ({ self.meaning})'
            obj.flash.append(string)
            return string
            
while True:
        
    word_input = input("Enter the name for flashcard ")
    meaning_input = input("Enter the meaning of name ")
   
    try:
        obj = flashcard(word_input, meaning_input)
        str(obj)
        user_input = int(input("Enter 0, to add flashcard "))
    
        if user_input == 0:
            print(obj.flash)
        else:
            print('\n')
            print("Your Flashcards ")
            flash1 = list(set(obj.flash))
            n = 0
            while n < len(flash1) :
                print(flash1[n])
                n+=1
            break

    except (NameError,ValueError,TypeError):
        print("Error occurred and handled ")

# Done