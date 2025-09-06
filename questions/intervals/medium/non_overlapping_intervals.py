class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        output = []
        output.append(intervals[0])

        for i in range(1, len(intervals)):
            print(output)
            interval = intervals[i]
            start = interval[0]
            end = interval[1]
            if start < output[-1][1]:
                if output[-1][1] > end:
                    output[-1] = interval
            else:
                output.append(interval)
        return(len(intervals) - len(output))
