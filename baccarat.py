from playing_cards import Card, Deck

class Player:
    def __init__(self):
        self.__hand = []
        self.__handValue = 0
    
    def updateHand(self, card):

        hand = Card(card[0],card[1])
    
        self.__hand.append(card)
        self.__handValue = hand.getRank()
        #adds the card to the hand and gets the value of the hand
    def clearHand(self):
        self.__hand = []
        self.__handValue = 0
        #clears the cards in the hand and the hands value
    def getHand(self):
        return self.__hand
        #returns the hand
    def getHandValue(self):
        return self.__handValue
        #returns the value of the hand
              
    
    
class Table:
    def __init__(self):
        self.__player = Player()
        self.__dealer = []
        self.__deck = Deck(52)
        self.__DIscardPile = []



    def populateDeck(self):
        FileName = input('Enter the input filename:')
        getFile = open (FileName,'r')
        #asks for the filename and opens the file
        for card in getFile:
            
            self.__deck.addCard(card)
        
        assert (self.__deck.deckSize()) == 52, 'deck not valid'
        
        #assert len(set(Deck) == len(Deck), 'deck not valid'
        
        #adds the cards to the deck  if the deck is unique and has 52 cards
        
        return self.__deck

    def CardDeck(self):

        return self.__deck

    
    def cardsRemaining(self):
        return self.__deck.deckSize()
        #returns the number of cards remaining in the deck
    def deal(self, toWho):
        
        Newcard = self.__deck.dealCard()
        if toWho % 2 == 0:
            TopCard = self.__player.updateHand(Newcard)
        elif toWho % 2 != 0:
            TopCard = self.__dealer.append(Newcard)
        #if towho is even add a card to the player, if its odd add it to the dealer

        return Newcard
    def playerTotal(self):
        playersCards = []
        rank = 0
        playerUpdate = self.__player
        
        playerUpdate = [item.strip() for item in playerUpdate.getHand()]
        
        #strips the newline and adds the cards to the players totoal
        
        for x in range(len(playerUpdate)):
            y = playerUpdate[x]
            playersCards += y

        return playersCards
            


    def dealerTotal(self):
        #dealersCards = Card(self.__dealer[0][0],self.__dealer[0][1])
        dealersCards = []
        rank = 0
        self.__dealer = [item.strip() for item in self.__dealer]
        
        
        for x in range(len(self.__dealer)):
            y = self.__dealer[x]
            dealersCards += y
            
        #strips the newline from the list and adds the cards to dealerscards
        
    
        return dealersCards
             
    
    def displayTable(self):
        
        #prints the player/dealers cards and values
    
        print('player:',self.playerTotal(),' --> score = ')
        print('dealers:', self.__dealer,' --> score = ')
    def checkTableValues(self):
        
        #returns the tuple of card and rank
        hand = Deck.dealCard(T.populateDeck())
        return tuple(self.__player.getHandValue()), tuple(hand.getRank())
    
    def clearTable(self):
       #adds the cards already dealed out to the dealer and player to the discard pile
        for x in self.__player.getHand():
            self.__DIscardPile.append(x)
        
        
        for x in self.__dealer:
            self.__DIscardPile.append(x)
   
        self.__dealer = []
        self.__player.clearHand()

       #if the deck has 6 or less cards, reset the deck
        cardSize = int(self.__deck.deckSize())
        if cardSize <= 6:
            print('not enough cards for another round')
            print('creating a new deck')
            self.newDeck()

        #clear the dealer and players hand to start a new turn
    def newDeck(self):

        ReturnCards = self.__DIscardPile
        #returns all the cards from the discard pile, shuffles the deck and starts a new game
        
        for x in ReturnCards:
            #print('the card being returned is', x)
            self.__deck.addCard(x)

        print('deck after all cards put back in is',(self.__deck.deckSize()))
        self.__deck.shuffle()
    
      
    
if __name__=='__main__':

    #test for player class
    # main baccarat game should be run from here
    P = Player()
    #P.updateHand('aH')
    #print(P.getHand())
    #print(P.getHandValue())

    #shuffledDeck.txt
    T = Table()
    #test for table class
    #T.populateDeck()
    #print(T.deal(1))
    #print(T.cardsRemaining())
    #print(T.displayTable())
    #T.clearTable()
    #T.newDeck()
    roundOfGame = 1
    
    stars = '*' * 19
    dashes = '-' * 10
    print(stars)
    print('Welcome to BACCARAT')
    print(stars)
    T.populateDeck()
    
    
    
    #prints the welcome sign and asks for the user to enter the filename
   
    gamePlay = True
    while gamePlay:
        print('round',roundOfGame)
        print(dashes)
        for x in range(2):
            #NextCard = Deck.dealCard(T.CardDeck())
            #print('the next card is',NextCard)
        
            T.deal(0)
            T.deal(1)
        
        #table = T.displayTable()

        #deals two cards to the player and two cards to the dealer 
        
        DealerHand = T.dealerTotal()
        playerTotal = T.playerTotal()
        rank = 0
        P_rank = 0
        rankPos = 0
        suitPos = 1

        
        #for x in range(2):
            #print(x)
            #print('rankpos is',rankPos)
            #print('suitpos is',suitPos)
            #print(DealerHand[rankPos])
            #print(DealerHand[suitPos])
            #rankPos += 2
            #suitPos += 2
        #print('players cards are', T.playerTotal())
        
        for x in range(2):
        
            dealersCards = Card(DealerHand[rankPos],DealerHand[suitPos])
            dealersRank = dealersCards.getRank()
            playersCards = Card(playerTotal[rankPos],playerTotal[suitPos])
            playersRank = playersCards.getRank()
            rank += int(dealersRank)
            P_rank += int(playersRank)
        
        #checks the ranks of the dealers/players cards and adds them up
            rankPos += 2
            suitPos += 2
        print('players: ',playerTotal,' --> score =',P_rank)
        print('Dealers: ', DealerHand,' --> score =',rank)
       
        #prints out the dealer/players cards and values(was suppose to be done in display table
        # but i did rank in main, so had to do it here)

        if P_rank >= 10:
                P_rank = P_rank - 10
        if rank >= 10:
                rank = P_rank - 10
    
        #if the rank is above 10 we take the right most figure, which we can achieve by 
        #deducting 10

        natural = [8,9]
        if rank in natural or P_rank in natural:
            if rank > P_rank:
                print('Natural! dealer wins')
                
            elif P_rank > rank:
                print('Natural, player wins')
                
            else:
                print('draw')
            gamePlay = False
        #if the card is a natural the game is over and the player with the higher card wins
        #or its a draw if they have the same cards

        dealtThirdCard = [0,1,2,3,4,5]
        if P_rank in dealtThirdCard:
            T.deal(0)
            
            #print('player draws', T.deal(0))
            playerTotal = T.playerTotal()
            print('player draws',playerTotal[4],playerTotal[5])
            playersCards = Card(playerTotal[4],playerTotal[5])
            playersRank = playersCards.getRank()
            P_rank += int(playersRank)
            if P_rank >= 10:
                P_rank = P_rank - 10
        
        #if the card is between 0-5 the player gets a third card
        #the rank is the right most figure if above 10
            if rank <= 2:
                T.deal(1)
                DealerHand = T.dealerTotal()
                print('dealer draws',DealerHand[4],DealerHand[5])
                dealersCards = Card(DealerHand[rankPos],DealerHand[suitPos])
                dealersRank = dealersCards.getRank()
                rank += int(dealersRank)
                
        #if the dealers rank is under 2 we give the dealer a third card
            elif rank == 3 and P_rank == 8:
                T.deal(1)
                DealerHand = T.dealerTotal()
                print('dealer draws',DealerHand[4],DealerHand[5])
                dealersCards = Card(DealerHand[rankPos],DealerHand[suitPos])
                dealersRank = dealersCards.getRank()
                rank += int(dealersRank)
                if rank >= 10:
                    rank = rank - 10
        #if the dealers rank total is 3 and player 8 the dealer gets a third card
            elif rank == 4 and P_rank in [2,3,4,5,6,7]:
                T.deal(1)
                DealerHand = T.dealerTotal()
                print('dealer draws',DealerHand[4],DealerHand[5])
                
                dealersCards = Card(DealerHand[rankPos],DealerHand[suitPos])
                dealersRank = dealersCards.getRank()
                rank += int(dealersRank)
                if rank >= 10:
                    rank = rank - 10
            #if the dealers rank total is 4 and player between 2-7 the dealer gets a third card
            elif rank == 5 and p_rank in [4,5,6,7]:
                T.deal(1)
                DealerHand = T.dealerTotal()
                print('dealer draws',DealerHand[4],DealerHand[5])
                
                dealersCards = Card(DealerHand[rankPos],DealerHand[suitPos])
                dealersRank = dealersCards.getRank()
                rank += int(dealersRank)
                print('rankkk', rank)
                if rank >= 10:
                    rank = rank - 10
            elif rank == 6 and P_rank in [6,7]:
                T.deal(1)
                DealerHand = T.dealerTotal()
                print('dealer draws',DealerHand[4],DealerHand[5])
                
                dealersCards = Card(DealerHand[rankPos],DealerHand[suitPos])
                dealersRank = dealersCards.getRank()
                rank += int(dealersRank)
                if rank >= 10:
                    rank = rank - 10
        ##if the dealers rank total is 6 and player 6,7 the dealer gets a third card
            elif rank >= 10:
                print('dealer stands')
                if rank >= 10:
                    rank = rank - 10
        elif P_rank in [6,7]:
            print('no third card given')
            if rank in dealtThirdCard:
                T.deal(1)
                DealerHand = T.dealerTotal()
                
                dealersCards = Card(DealerHand[rankPos],DealerHand[suitPos])
                dealersRank = dealersCards.getRank()
                rank += int(dealersRank)
        #if the players rank total is 6,7 no third card is given
                if rank >= 10:
                    rank = rank - 10
            elif rank in [6,7]:
                print('no card given')
        #if the dealers rank total is 6,7 no third card is given
        gamePlay = False

        
        
        print('players: ',playerTotal,' --> score =',P_rank)
        print('Dealers: ', DealerHand,' --> score =',rank)
        
        #prints the player/deaalers final cards and rank totals

        if P_rank > rank:
            print('player wins round', roundOfGame,'!')
        elif rank > P_rank:
            print('dealer wins round', roundOfGame,'!')
        elif P_rank == rank:
            print('round', roundOfGame,'is a tie!')
        #determines who won the round by who has the higher rank total
        print('**********')
        playAgain = input('play another round? (Y/N)')

        if playAgain == 'Y':
            T.clearTable()
            gamePlay = True
            roundOfGame += 1
        elif playAgain == 'N':
            print('game over')

        #asks the player if he wants to play again
        #if yes the cards are put back in the deck, shuffled and the game starts again
        