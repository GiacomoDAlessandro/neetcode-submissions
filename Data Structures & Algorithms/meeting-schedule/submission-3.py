"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        for i, time in enumerate(intervals):
            for j in range (i + 1, len(intervals)):
                B = intervals[j]
                if min(time.end, B.end) > max(time.start, B.start):
                    return False
        return True
        