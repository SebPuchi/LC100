class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        output_intervals = []

        n_start = newInterval[0]
        n_end = newInterval[1]

        start = None
        end = None
        add = False
        for interval in intervals:
            if add:
                output_intervals.append(interval)
                continue

            current_start = interval[0] 
            current_end = interval[1]

            if start == None and current_end > n_start:
                start = current_start
            
            if end == None and current_start < n_end and n_end < current_end:
                end = current_end
                end = current_end


            print("START", start)
            print("END", end)

            if start != None and end != None:
                output_intervals.append([start, end])
                add = True
            elif start != None or end != None:
                continue
            else:
                output_intervals.append(interval)

            
            print(output_intervals)
            
        if not add:
            output_intervals.append(newInterval)
            output_intervals.sort()

