class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        card_hash = {} 

        for i in range(len(hand)):
            if hand[i] in card_hash:
                card_hash[hand[i]] +=1
            else:
                card_hash[hand[i]] = 1
        
        while len(card_hash) != 0:
            smallest_card = min(card_hash.keys())
            card_hash[smallest_card] -=1
            if card_hash[smallest_card] == 0:
                del card_hash[smallest_card]
            
            for i in range(1, groupSize):
                if (smallest_card + i) in card_hash:
                    card_hash[smallest_card + i] -=1
                    if card_hash[smallest_card + i] == 0:
                        del card_hash[smallest_card + i]
                else: 
                    return False
        return True
