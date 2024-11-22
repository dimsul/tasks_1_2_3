def appearance(intervals: dict[str, list[int]]) -> int:

    def search_overlap(range1, range2):
        return max(range1[0], range2[0]), min(range1[1], range2[1])

    lesson = intervals['lesson']

    pupil = []
    for i in range(1, len(intervals['pupil']), 2):
        res = search_overlap([intervals['pupil'][i-1], intervals['pupil'][i]], lesson)
        if range(res[0], res[1]):
            pupil.append((res[0], res[1]))

    tutor = []
    for i in range(1, len(intervals['tutor']), 2):
        res = search_overlap([intervals['tutor'][i - 1], intervals['tutor'][i]], lesson)
        if range(res[0], res[1]):
            tutor.append((res[0], res[1]))

    sum_ = []
    for i in pupil:
        for j in tutor:
            res = search_overlap(i, j)
            if range(res[0], res[1]):
                sum_ += list(range(res[0], res[1]))

    return len(set(sum_))
