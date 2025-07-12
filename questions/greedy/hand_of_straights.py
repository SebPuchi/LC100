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
            if card_hash[smalles_card] == 0:
                del card_hash[smalles_card]
            
            for i in range(groupSize -1):
                
        print(card_hash)

