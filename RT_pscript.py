import fileinput
import csv
import sys

#result array
current_results = []

#column numbers of relevant information
StimRTCol = 65
StimACCCol = 58
CategoryCol = 29
ConditionCol = 33
RelevanceCol = 56

cond = ""
#for every subject
for subj_num in range(1401, 1432):
	if ((subj_num != 1410) and (subj_num != 1420) and (subj_num != 1424) and (subj_num != 1425) and (subj_num != 1428)):
 	#for every run
		for i in range(1,6):
			linenum = 1
			for line in fileinput.input(str(subj_num) + "-" + str(i) + ".txt"):
				if (linenum > 2):
					fields = line.strip('\r\n').split('\t')
					if (len(fields) >= (StimRTCol + 1)):
						StimRT = fields[StimRTCol].replace('\x00', '')
						StimACC = fields[StimACCCol].replace('\x00', '')
						if (len(StimRT) > 0):
							if ((fields[ConditionCol].replace('\x00', '') == 'Faces') or (fields[ConditionCol].replace('\x00', '') == 'Scenes')):
								cond = fields[RelevanceCol].replace('\x00', '') + ' ' + fields[CategoryCol].replace('\x00', '')
							else:
								cond = fields[ConditionCol].replace('\x00', '') + ' ' + fields[CategoryCol].replace('\x00', '')
							result_line = ','.join([str(subj_num), cond, StimACC, StimRT])
							current_results.append(result_line)
				linenum += 1

#write single big file
f = open('StimRTResults.txt', 'w')
f.write('Subject,Condition,StimACC,StimRT' + '\n')
for val in current_results:
	f.write(val + '\n')
f.close()
