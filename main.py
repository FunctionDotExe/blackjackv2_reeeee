
#are u happy i comment the thing?
#ima inport  libraries
import string, math, random
# COLOURS cuz y not
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
#the class "card"

class Card (object):
  # card types
    RANKS = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)
    SUITS = ('S', 'D', 'H', 'C')
# it is going to read a number for itself
    def __init__ (self, rank, suit):
        self.rank = rank
        self.suit = suit
# what suits number should be
    def __str__ (self):
        if self.rank == 1:
            rank = 'A'
        elif self.rank == 13:
            rank = 'K'
        elif self.rank == 12:
            rank = 'Q'
        elif self.rank == 11:
            rank = 'J'
        else:
            rank = self.rank
        return str(rank) + self.suit

    def __eq__ (self, other):
        return (self.rank == other.rank)

    def __ne__ (self, other):
        return (self.rank != other.rank)

    def __lt__ (self, other):
        return (self.rank < other.rank)

    def __le__ (self, other):
        return (self.rank <= other.rank)

    def __gt__ (self, other):
        return (self.rank > other.rank)

    def __ge__ (self, other):
        return (self.rank >= other.rank)
#class deck
class Deck (object):
    def __init__ (self):
        self.deck = []
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                card = Card (rank, suit)
                self.deck.append(card)

    def shuffle (self):
        random.shuffle (self.deck)

    def __len__ (self):
        return len (self.deck)

    def deal (self):
        if len(self) == 0:
            return None
        else:
            return self.deck.pop(0)
# the class  player
class Player (object):
    def __init__ (self, cards):
        self.cards = cards
 #definition of hitting a card
    def hit (self, card):            
        self.cards.append(card)

    def getPoints (self):
        count = 0
        for card in self.cards:
            if card.rank > 9:
                count += 10
            elif card.rank == 1:
                count += 11
            else:
                count += card.rank
        # sub 10 if Ace is there and needed as 1
        for card in self.cards:
            if count <= 21:
                break
            elif card.rank == 1:
                count = count - 10
        return count

  # does the player have 21 points or not
    def hasBlackjack (self):
        return len (self.cards) == 2 and self.getPoints() == 21

  # complete the code so that the cards and points are printed
    def __str__ (self):
        hand=''
        for i in range(len(self.cards)):
            hand=hand+str(self.cards[i])+' '
        return (hand+ ' - '+ str(self.getPoints())+' points')
          

# Dealer class inherits from the Player class
class Dealer (Player):
    def __init__ (self, cards):
        Player.__init__ (self, cards)
        self.show_one_card = True   #meaning of show_one_card???

  # over-load the hit function() in the parent class
  # add cards while points < 17, then allow all to be shown
    def hit (self, deck):
        self.show_one_card = False
        while self.getPoints() < 17:
            self.cards.append (deck.deal())

  # return just one card if not hit yet
    def __str__ (self):
        if self.show_one_card:
            return str(self.cards[0])
        else:
            return Player.__str__(self)

class Blackjack (object):
    def __init__ (self, numPlayers):
        self.deck = Deck()
        self.deck.shuffle()
        self.numPlayers = numPlayers
        self.Players = []
#REEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE im bored it is 11:00 Pm in the night time wut am i doing 
        for i in range (self.numPlayers):
            self.Players.append (Player([self.deck.deal(), self.deck.deal()]))
        self.dealer = Dealer ([self.deck.deal(), self.deck.deal()])

    def play (self):
# Print the cards that each player has
        for i in range (self.numPlayers):
            print (bcolors.OKGREEN + 'Player ' + str(i + 1) + ': ' + str(self.Players[i]) + bcolors.ENDC)

    # Print the cards that the dealer has
        print (bcolors.FAIL + 'Dealer: ' + str(self.dealer)+ bcolors.ENDC)

    # Each player hits until he says no
        playerPoints = []
        for i in range (self.numPlayers):
          #while to check if true
            while True:
                print ('Player'+str(i+1),end='')
                choice = input (', do you want to hit? [y / n]: ')
                if choice in ('y', 'Y'):
                    (self.Players[i]).hit (self.deck.deal())
                    points = (self.Players[i]).getPoints()
                    print ('Player ' + str(i + 1) + ': ' + str(self.Players[i]))
                    if points >= 21:
                        break
                else:
                    break
            playerPoints.append ((self.Players[i]).getPoints())

    # Dealer's turn to hit
        self.dealer.hit (self.deck)
        dealerPoints = self.dealer.getPoints()
        print ( 'Dealer: ' + str(self.dealer) + ' - ' + str(dealerPoints))

         #loop through all the players
        for i in range(len(playerPoints)):   
            if playerPoints[i] > 21:                                
              #if the player got over 21, he/she loses                      
                print (bcolors.FAIL + 'Player '+str(i+1)+' loses'+ bcolors.ENDC)
            elif dealerPoints > 21:                            
                   #if dealer got over 21,he loses
                print (bcolors.OKGREEN +'Player '+str(i+1)+' wins' + bcolors.ENDC)
            elif Player.hasBlackjack(self.Players[i]):          
                  #as long as player got blackjack, he/she wins
                print ('Player '+str(i+1)+' wins')
            elif Player.hasBlackjack(self.dealer) or dealerPoints==21:
                #if player doesn't get Blackjack but got 21points, she/he reaches a tie
                if playerPoints == 21:                           
                    print ( 'Player '+str(i+1)+'reaches a tie' )
                else:
                    print ( 'Player '+str(i+1)+' loses')
                     #if both player and dealer got less than 21 points
            elif dealerPoints <21:                      
                # if player got higher score than dealer, he wins           
                if playerPoints[i] > dealerPoints:                
                    print ( 'Player '+ str(i+1)+' wins yay! \(0_0)/' )
                     # If they got same points, it ties
                elif playerPoints[i] == dealerPoints:              
                    print ('Player '+str(i+1)+'ties')  
                     # if player got lower score than dealer, he loses
                else:                                              
                    print ('Player '+str(i+1)+' loses')
# the function "main"
def main ():
    numPlayers = eval (input (bcolors.OKBLUE + 'Enter number of players: '+ bcolors.ENDC))
    while (numPlayers < 1 or numPlayers > 6):
        numPlayers = eval (input ('Enter number of players: '))
    game = Blackjack (numPlayers)
    game.play()

main()
# i spent 5 hours on this  y, just just y