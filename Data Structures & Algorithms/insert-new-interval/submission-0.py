class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        def overlap(s1, s2):
            if s1[0] >= s2[0] and s1[0] <= s2[1]:
                return True
            if s1[1] >= s2[0] and s1[1] <= s2[1]:
                return True
            
            return False
        def merge_interval(s1, s2):
            return [
                min(s1[0], s2[0]),
                max(s1[1], s2[1])
            ]
        
        i2 = [newInterval]
        result = []
        i = 0
        j = 0
        while i < len(intervals) and j < len(i2):
            if overlap(intervals[i], i2[j]) or overlap(i2[j], intervals[i]):
                print(1)
                result.append(merge_interval(
                    intervals[i],
                    i2[j]
                ))
                i += 1
                j += 1

            elif intervals[i][1] < i2[j][0]:
                print(2)
                if result:
                    if overlap(result[-1], intervals[i]) or overlap(intervals[i], result[-1]):
                        result.append(merge_interval(
                            result[-1],
                            intervals[i]
                        ))
                    else:
                        result.append(intervals[i])
                else:
                    result.append(intervals[i])

                i += 1
            else:
                print(3)
                result.append(i2[j])
                j += 1

        while i < len(intervals):
            print(4)
            if result:
                print(5)
                if overlap(result[-1], intervals[i]) or overlap(intervals[i], result[-1]):
                    print(6)
                    prev_interval = result.pop()
                    result.append(merge_interval(
                        prev_interval,
                        intervals[i]
                    ))
                else:
                    print(7)
                    result.append(intervals[i])
            else:
                result.append(intervals[i])

            i += 1

        while j < len(i2):
            result.append(i2[j])
            j += 1

        return result