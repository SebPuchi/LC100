class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        output = []

        for i in range(len(intervals)):
            interval = intervals[i]
            start = interval[0]
            end = interval[1]
            if newInterval[1] < start:
                output.append(newInterval)
                output += intervals[i:]
                return output
            if newInterval[0] > end:
                output.append(interval)
            else:
                newInterval = [min(start, newInterval[0]), max(end, newInterval[1])]
        output.append(newInterval)
        return output
