import cards, simpleMod

class BJ_Card(cards.Card):
    """ A Blackjack Card """
    ACE_VALUE = 1
    @property
    def value(self):
        if self.is_face_up:
            v = BJ_Card.RANKS.index(self.rank) + 1 
            if v > 10:
                v = 10
        else:
            v = None
        return v 
        
        
class BJ_Deck(cards.Deck):
    """ A Blackjack Deck """
    def populate(self):
        for suit in BJ_Card.SUITS:
            for rank in BJ_Card.RANKS:
                self.cards.append(BJ_Card(rank, suit))
                
