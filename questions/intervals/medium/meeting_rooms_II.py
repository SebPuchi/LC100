class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
            start = []
            end = []
            for interval in intervals:
                start.append(interval[0])
                end.append(interval[1])
            start.sort()
            end.sort()

            s = 0
            e = 0
            max_meetings = 0
            current_meetings = 0
            while s < len(start) and e < len(end):
                if start[s] < end[e]:
                    current_meetings+=1
                    s+=1
                elif start[s] >= end[e]:
                    current_meetings-=1
                    e+=1
                    
                max_meetings = max(current_meetings, max_meetings)
            return max_meetings
