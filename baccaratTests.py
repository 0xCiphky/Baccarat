C = Card('5','H')
    
    print(C.isFaceCard())
    print(C.isAce())
    print(C.isNumeric())
    print(C.getRank())
    print(C.getSuit())
    print(type(C.getRank()))
    print(type(C.getSuit()))
    print(C.__str__())


    # test your Deck class here
D = Deck(54)

    D.addCard('4H')
    D.addCard('AK')
    D.addCard('JS')
    print(D.deckSize())
    print(D.__str__())
    D.shuffle()
    print(D.__str__())
    print(D.dealCard())
    print(D.__str__())