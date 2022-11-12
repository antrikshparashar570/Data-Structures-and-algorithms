def mergeCalendars(calendar1, calendar2):
    if len(calendar1) == 0:
	    return calendar2
    if len(calendar2) == 0:
	    return calendar1
	mergedC = calendar1  + calendar2
	mergedC = sorted(mergedC, key: lambda x: x[0])
	C  = []
	start = mergedC[0][0]
	end = mergedC[0][1]
	
	for i in range(1, len(mergedC)):
		if end < mergedC[i][0]:
			C.append(start, end)
			start = mergedC[i][0]
            end = mergedC[i][1]
		elif end < mergedC[i][1]:
			End = mergedC[i][1]
	C.append(start, end)
	return C

def overlappingDailyBounds(dailyB1, dailyB2):
	if dailyB1[1] < dailyB2[0] or dailyB2[0] < dailyB1[1]:
		Return []
	elif dailyB1[0] < dailyB2[0] and dailyB1[1] < dailyB2[1]:
        return [(dailyB1[0], dailyB2[1])]
  elif dailyB2[0] < dailyB1[0] and dailyB2[1] < dailyB1[1]:
    return [(dailyB2[0], dailyB1[1])]


def freeTimeBlocks(calendar1, dailyB1, calendar2, dailyB2, dur):
	mergedCalendar = mergeCalendars(calendar1, calendar2)
	availabilityTime = overlappingDailyBounds(dailyB1, dailyB2)
	freeTime = []

	if availabilityTime[0] - mergedCalendar[0] >= dur:
		freetime.append((availabilityTime[0], mergedCalendar[0]))

	for i in range(1, len(mergedCalendar)):
		if mergedCalendar[i][0] - mergedCalendar[i-1][1] >= dur:
			freetime.append((mergedCalendar[i][0], mergedCalendar[i-1][1]))

	if mergedCalendar[1] - availabilityTime[1] >= dur:
		freetime.append((availabilityTime[0], mergedCalendar[0]))
	return freetime
