# The 6.00 Word Game

import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordList: list of strings
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print("  ", len(wordList), "words loaded.")
    return wordList

def getFrequencyDict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq
	

# (end of helper code)
# -----------------------------------

#
# Problem #1: Scoring a word
#
def getWordScore(word, n):
	score=0
	for i in range(len(word)):
		score=score+SCRABBLE_LETTER_VALUES[word[i]]
	score=score*len(word)
	if len(word)==n:
		score=score+50
	return score
    # TO DO ... <-- Remove this comment when you code this function



#
# Problem #2: Make sure you understand how this function works and what it does!
#
def displayHand(hand):
    """
    Displays the letters currently in the hand.

    For example:
    >>> displayHand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    for letter in hand.keys():
        for j in range(hand[letter]):
             print(letter,end=" ")       # print all on the same line
    print()                             # print an empty line

#
# Problem #2: Make sure you understand how this function works and what it does!
#
def dealHand(n):
    """
    Returns a random hand containing n lowercase letters.
    At least n/3 the letters in the hand should be VOWELS.

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    hand={}
    numVowels = n // 3
    
    for i in range(numVowels):
        x = VOWELS[random.randrange(0,len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1
        
    for i in range(numVowels, n):    
        x = CONSONANTS[random.randrange(0,len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1
        
    return hand

#
# Problem #2: Update a hand by removing letters
#
def updateHand(hand, word):
	new_hand=hand.copy()
	for letter in word:
		new_hand[letter]-=1
	return new_hand
#
# Problem #3: Test word validity
#
def isValidWord(word, hand, wordList):
	if word in wordList:
		if len(word)<=calculateHandlen(hand):
			for letter in word:
				if letter not in hand.keys():
					return False
			new_hand=updateHand(hand,word)
			for i in new_hand.values():
				if i<0:
					return False
			return True
	return False

def isInWord(word, hand, wordList):
	if len(word)<=calculateHandlen(hand):
		for letter in word:
			if letter not in hand.keys():
				return False
		new_hand=updateHand(hand,word)
		for i in new_hand.values():
			if i<0:
				return False
		return True
	return False

#
# Problem #4: Playing a hand
#

def calculateHandlen(hand):
	length=0
	for i in hand.values():
		length+=i	
	return length
    # TO DO... <-- Remove this comment when you code this function



def playHand(hand, wordList, n, player):
	Total_points=0
	temp_hand=hand.copy()
	while True:
		print("Current hand : ",end=' ')
		displayHand(temp_hand)
		if player=='u':
			word=input("Enter word or a '.' to finish : ")
		else:
			maxScore=0
			maxWord='.'
			for word in wordList:
				if isInWord(word, temp_hand,wordList):
					if maxScore<getWordScore(word,n):
						maxScore=getWordScore(word,n)
						maxWord=word
			word=maxWord
		if word=='.':
			break
		elif isValidWord(word,temp_hand,wordList):
			Total_points+=getWordScore(word,n)
			print(word," earned ",getWordScore(word,n)," points. Total score: ",Total_points," points")
			temp_hand=updateHand(temp_hand,word)
		else:
			print("Invalid word. Please try again")
	print("Total score : ",Total_points," points\n\n")

    # Game is over (user entered a '.' or ran out of letters), so tell user the total score


#
# Problem #5: Playing a game
# 

def playGame(wordList):
	hand={}
	while True:
		user_input=input("Game \n n : new hand \n r : replay hand \n e : End game \n Enter input : ")
		if user_input=='e':
			break
		else:
			while True:
				player=input("enter u to play yourself or c to have computer play : ")
				if player == 'u' or player== 'c':
					break
				print("Invalid command.\n")
			if user_input=='n':
				hand=dealHand(HAND_SIZE)
				playHand(hand,wordList,HAND_SIZE,player)
			elif user_input=='r':
				playHand(hand,wordList,HAND_SIZE,player)
			else:
				print("Enter valid input")
	print("Game Over!")

#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)
