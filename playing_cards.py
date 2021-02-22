import random

class Card:
    
    def __init__(self, rank, suit):
        ValidRank = [ 'A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K' , 'a']
        assert rank in ValidRank, 'rank not valid'
        #if the rank is not in the valid rank list then an assertion error will pop up
        ValidSuit = [ 'S', 'H', 'D', 'C']
        #if the suit is not in the valid suit then an assertion error will pop up
        assert suit in ValidSuit, 'suit not valid'
        
        '''
        Initializes a card object. Cards have a suit and rank. Asserts that the
        provided suit and rank are valid.

        Parameters:
          - rank (string): represents number 2-10, Jack, Queen, King, or Ace
          - suit (string): represents spade, heart, diamond, or club


        Returns: None
        ''' 
        # asserts go here
        
        self.__suit = suit.upper()
        self.__rank = rank.upper()        
    
        
    def isFaceCard(self):
        FaceCardList = ['J', 'Q', 'K' ]
        if self.__rank in FaceCardList:
            return True
        else:
            return False
        #if the card is a face card then the function will return true
        
    def isAce(self):
        if self.__rank == 'A' or self.__rank == 'a':
            return True
        else:
            return False
        #if the rank is an a then the function will return a true
    def isNumeric(self):
        NumericRankList = ['2', '3', '4', '5', '6', '7', '8', '9','10']
        if self.__rank in NumericRankList:
            return True
        else:
            return False
        
        #if the function is in the numeric list then it will return true
    def getRank(self):
        RankList = ['2', '3', '4', '5', '6', '7', '8', '9']
        FaceList = ['J', 'Q', 'K', '10','T']
        
        if self. __rank in RankList:
            self.__rank = str(self.__rank)
        elif self.__rank in FaceList:
            self.__rank = '0'
        elif self.__rank == 'a' or self.__rank == 'A':
            self.__rank = '1'

        return self.__rank

        #if the rank is in the list then it will return the same digit but as a string
        #if the rank is in the facelist then it will return a 0
        #if the rank is an an ace then it will reutn a 1
    def getSuit(self):
        return str(self.__suit)
        
    def __str__(self):
        '''
        Informal string representation of the Card object.
        
        Parameters: None
        
        Returns: string
        '''
        return self.__rank + self.__suit
        
        #this function returns the string form of rank and suit
class Deck:
    
    def __init__(self, capacity):
        if type(capacity) != int or capacity<=0:
            raise Exception ('Capacity Error') 
        #raise an error if the capacity entered was not an int or less then 0
        self.__items = []
        self.__capacity = capacity
        self.__count=0
        self.__head=0
        self.__tail=0

    #used a circular queue for the deck
    def addCard(self, card):
        if self.__count == self.__capacity:
            raise Exception('Error: Queue is full')
        if len(self.__items) < self.__capacity:
            self.__items.append(card)
        else:
            self.__items[self.__tail]= card

        self.__count +=1
        self.__tail=(self.__tail +1) % self.__capacity        
        
    def dealCard(self):
        if self.__count == 0:
            raise Exception('Error: Queue is empty')

        item = self.__items[self.__head]
        self.__items[self.__head] = None
        self.__count -=1
        self.__head = (self.__head+1) % self.__capacity

        return item         

    def deckSize(self):
        return self.__count
        #returns the length of the deck
    def shuffle(self):
        return random.shuffle(self.__items)
        #use the random module to shuffle the deck in a random order
        
    def __str__(self):
        str_exp = ""
        i = self.__head
        for j in range(self.__count):
            str_exp += str(self.__items[i]) + ' ' # + "-" #+ str(self.__items[i[1]])
            i=(i+1) % self.__capacity
        return str_exp 
        # returns the string expression
if __name__ == '__main__':
    # test your Card class here
    

    C = Card('5','H')
    
    #print(C.isFaceCard())
    #print(C.isAce())
    #print(C.isNumeric())
    #print(C.getRank())
    #print(C.getSuit())
    #print(type(C.getRank()))
    #print(type(C.getSuit()))
    #print(C.__str__())


    # test your Deck class here
    #D = Deck(54)

    #D.addCard('4H')
    #D.addCard('AK')
    #D.addCard('JS')
    #print(D.deckSize())
    #print(D.__str__())
    #D.shuffle()
    #print(D.__str__())
    #print(D.dealCard())
    #print(D.__str__())



