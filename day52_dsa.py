#MERGE INTERVALS
def merge_intervals(intervals):
    intervals.sort(key=lambda x: x[0])

    merged = []

    for interval in intervals:
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])

    return merged


print(merge_intervals([[1,3],[2,6],[8,10],[15,18]]))



#MEETING ROOMS
def can_attend_meetings(intervals):
    intervals.sort(key=lambda x: x[0])

    for i in range(1, len(intervals)):
        if intervals[i][0] < intervals[i-1][1]:
            return False

    return True


print(can_attend_meetings([[0,5],[6,10],[11,15]]))   # True
print(can_attend_meetings([[0,10],[5,15]]))          # False