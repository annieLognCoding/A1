import random

words = [
    'apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape', 'honeydew', 'kiwi', 'lemon',
    'mango', 'nectarine', 'orange', 'papaya', 'quince', 'raspberry', 'strawberry', 'tangerine', 'ugli', 'vanilla',
    'watermelon', 'xigua', 'yam', 'zucchini', 'almond', 'broccoli', 'carrot', 'dill', 'eggplant', 'fennel',
    'garlic', 'horseradish', 'iceberg', 'jalapeno', 'kale', 'leek', 'mushroom', 'nutmeg', 'onion', 'parsley',
    'quince', 'radish', 'spinach', 'tomato', 'ugli', 'vanilla', 'watercress', 'xigua', 'yam', 'zucchini',
    'aardvark', 'buffalo', 'cheetah', 'dingo', 'elephant', 'flamingo', 'gorilla', 'hyena', 'iguana', 'jaguar',
    'kangaroo', 'lion', 'mongoose', 'narwhal', 'octopus', 'penguin', 'quokka', 'rhino', 'sloth', 'tiger',
    'urial', 'vulture', 'walrus', 'xenops', 'yak', 'zebra', 'airplane', 'bicycle', 'car', 'drone',
    'elevator', 'ferry', 'glider', 'helicopter', 'icebreaker', 'jet', 'kayak', 'limousine', 'motorcycle', 'narwhal',
    'oceanliner', 'paddleboard', 'quadcopter', 'rocket', 'submarine', 'tractor', 'unicycle', 'van', 'wagon', 'yacht'
]



def display_hangman(tries):
    stages = ["""
                --------
                |      |
                |      O
                |     \\|/
                |      |
                |     / \\
                -
             """,
             """
                --------
                |      |
                |      O
                |     \\|/
                |      |
                |     / 
                -
             """,
             """
                --------
                |      |
                |      O
                |     \\|/
                |      |
                |      
                -
             """,
             """
                --------
                |      |
                |      O
                |     \\|/
                |      
                |     
                -
             """,
             """
                --------
                |      |
                |      O
                |     \\|
                |      
                |     
                -
             """,
             """
                --------
                |      |
                |      O
                |      |
                |      
                |     
                -
             """,
             """
                --------
                |      |
                |      O
                |      
                |      
                |     
                -
             """,
             """
                --------
                |      |
                |      
                |      
                |      
                |     
                -
             """
    ]
    return stages[tries]

guess_word = words[int(random.random()*100)]
result = '_' * len(guess_word)
tries = 8

while(result != guess_word and tries > 0):
    print(result)
    print(display_hangman(8-tries))
    letter = input('guess a letter: ')
    if letter in guess_word:
        index = 0
        for c in guess_word:
            if c == letter:
                result = result[:index] + letter + result[index + 1:]
            index += 1
    else:
        tries -= 1

if result == guess_word:
    print('good job! the word was ' + guess_word)
    print('you win!')
else:
    print('the word was ' + guess_word)
    print('you lose')