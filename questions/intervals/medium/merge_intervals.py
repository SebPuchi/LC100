class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        output = []
        output.append(intervals[0])
        for i in range(1, len(intervals)):
            interval = intervals[i]
            start = interval[0]
            end = interval[1]
            if output[-1][1] < start:
                output.append(interval)
            else:
                output[-1] = [min(output[-1][0], start), max(output[-1][1], end)]
        return (output)
