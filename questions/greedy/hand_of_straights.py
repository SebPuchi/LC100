class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hand.sort()

        prev_card = None 
        groups = [[]]
        group_count = 0

        while len(hand) != 0:
            current_card = hand.pop(0)
            if current_card == prev_card:
                group_count+=1
            groups[group_count].append(current_card)

            
            print(current_card)
