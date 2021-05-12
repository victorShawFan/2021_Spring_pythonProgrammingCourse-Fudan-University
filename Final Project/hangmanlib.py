'''
hangmanlib.py
   A set of library functions for use with your Hangman game
   Actually you can add all help functions here, and just 
   import you can use all functions! 
   Enjoy!
'''

LINEPERIMAGE = 9  #Every LINEPERIMAGE is a perfect picture of hangman

def print_hangman(mistakes = 6):
    '''
    print hangman : from 0 (hang) to 6 (hanged)
    '''

    lines = LINES.split('\n')
    start = mistakes * LINEPERIMAGE
    for line in lines[start: start+ LINEPERIMAGE]:
        print(line)
#end print_hangman_image

# We intentionally add LINES below: it's too long
LINES = ''' ______
|  |
|  
| 
|  
|  
|_____
|     |____
|__________|
 ______
|  |
|  O
| 
|  
| 
|_____
|     |____
|__________|
 ______
|  |
|  O
| /
|  
| 
|_____
|     |____
|__________|
 ______
|  |
|  O
| /|
|  |
|  
|_____
|     |____
|__________|
 ______
|  |
|  O
| /|\ 
|  |
|  
|_____
|     |____
|__________|
 ______
|  |
|  O
| /|\ 
|  |
| /  
|_____
|     |____
|__________|
 ______
|  |
|  O
| /|\ 
|  |
| / \ 
|_____
|     |____
|__________|

'''
