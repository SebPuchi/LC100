# use the difference between the cost and the amount of gas at each station
class Solution:
    def checkComplete(self, index, gas, cost):
        total_gas = 0
        for i in range(index, index + len(gas) + 1):
            if i > len(gas)-1:
                total_gas += gas[i % len(gas)]
                total_gas -= cost[i % len(gas)]
            else: 
                total_gas += gas[i]
                total_gas -= cost[i]
            if total_gas <= 0:
                return False
        if total_gas <= 0:
            return False
        else: 
            return True

    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        rates = {}
        for i in range(len(gas)):
            rates[gas[i] / cost[i]] = i

        print(rates)
        start = max(rates.keys())
        while not (self.checkComplete(rates[start], gas, cost)):
            print("RATES", rates)
            if len(rates) == 0:
                return -1
            del rates[max(rates.keys())]
            start = max(rates.keys())
        return rates[start] 


