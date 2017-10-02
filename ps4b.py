from ps4a import *
import time

#
#
# Problem #6: Computer chooses a word
#
#
def compChooseWord(hand, wordList, n):
    """
    Given a hand and a wordList, find the word that gives
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)

    returns: string or None
    """
    # Create a new variable to store the maximum score seen so far (initially 0)
    max_score = 0
    # Create a new variable to store the best word seen so far (initially None)
    best_word = None

    # For each word in the wordList
    for test_word in wordList:
        # If you can construct the word from your hand
        # (hint: you can use isValidWord, or - since you don't really need to test if the word is in the wordList - you can make a similar function that omits that test)
        if isValidWord(test_word, hand, wordList) :
            # Find out how much making that word is worth
            test_word_score = getWordScore(test_word, n)
            # If the score for that word is higher than your best score
            # Update your best score, and best word accordingly
            if max_score < test_word_score:
                max_score = test_word_score
                best_word = test_word

    # return the best word you found.
    return best_word


#
# Problem #7: Computer plays a hand
#
def compPlayHand(hand, wordList, n):
    """
    Allows the computer to play the given hand, following the same procedure
    as playHand, except instead of the user choosing a word, the computer 
    chooses it.

    1) The hand is displayed.
    2) The computer chooses a word.
    3) After every valid word: the word and the score for that word is 
    displayed, the remaining letters in the hand are displayed, and the 
    computer chooses another word.
    4)  The sum of the word scores is displayed when the hand finishes.
    5)  The hand finishes when the computer has exhausted its possible
    choices (i.e. compChooseWord returns None).
 
    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    """
    #create a new variable to store the sum_score
    sum_score = 0
    #while computer return None, no suitable word
    while calculateHandlen(hand) > 0:
        # display a hand
        print "Current Hand: ",
        displayHand(hand)
        # computer choose the best word
        comp_word = compChooseWord(hand, wordList, n)
        #if computer return a word, calculate the score
        #else break
        if comp_word:
            comp_word_score = getWordScore(comp_word, n)
            sum_score += comp_word_score
            print "'%s' earned %d points. Total: %d points" % (comp_word, comp_word_score, sum_score)
            print
            hand = updateHand(hand, comp_word)
        else:
            break

    #print the sum_score
    print "Total score: %s points." % sum_score
    print

#
# Problem #8: Playing a game
#
#
def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.
      
        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the 
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)
    """
    # TO DO... <-- Remove this comment when you code this function
    print "playGame not yet implemented." # <-- Remove this when you code this function

        
#
# Build data structures used for entire session and play game
#
'''
if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)
'''
wordList = loadWords()
n=12
for i in range(5):
    hand = dealHand(n)
    compPlayHand(hand, wordList, n)

