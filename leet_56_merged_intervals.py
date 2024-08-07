class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if not intervals:
            return []

        # Sort intervals based on the start time
        intervals.sort(key=lambda x: x[0])

        merged_intervals = [intervals[0]]
        
        for i in range(1, len(intervals)):
            # If the current interval overlaps with the last merged interval, merge them
            if intervals[i][0] <= merged_intervals[-1][1]:
                merged_intervals[-1][1] = max(merged_intervals[-1][1], intervals[i][1])
            else:
                # Otherwise, add the current interval as a new interval
                merged_intervals.append(intervals[i])
        
        return merged_intervals