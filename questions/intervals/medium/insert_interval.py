class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        output_intervals = []
        overlapped = newInterval[:] 

        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                output_intervals.append(newInterval)
                return output_intervals + intervals[i:]
            elif intervals[i][1] < newInterval[0]:
                output_intervals.append(intervals[i])
            else:
                overlapped[0] = min(intervals[i][0], overlapped[0])
                overlapped[1] = max(intervals[i][1], overlapped[1])
                
        output_intervals.append(overlapped)
        return(output_intervals
