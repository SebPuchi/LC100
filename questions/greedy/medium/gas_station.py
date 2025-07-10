class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        total = 0
        start_index = 0
        for i in range(len(gas)):
            current_diff = gas[i] - cost[i]
            total += current_diff
            if total < 0:
                total = 0
                start_index = i + 1
        return start_index
