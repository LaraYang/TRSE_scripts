import fileinput
import csv
import sys

subject = sys.stdin.read().strip('\n')

#result arrays for each block
both_s = []
both_f = []
cat_s = []
cat_f = []
relevant_s = []
relevant_f = []
irrelevant_s = []
irrelevant_f = []
errors = []

#final result arrays for various conditions
both_s_file = []
both_f_file = []
cat_s_file = []
cat_f_file = []
relevant_s_file = []
relevant_f_file = []
irrelevant_s_file = []
irrelevant_f_file = []
errors_file = []

#column numbers of relevant information
# original (REACH subjects, 14**)
GoOnsetCol = 49
StimOnsetCol = 63
StimACCCol = 58
CategoryCol = 29
ConditionCol = 33
RelevanceCol = 56

#TRSE_TMS6
# GoOnsetCol = 45
# StimOnsetCol = 59
# StimACCCol = 54
# CategoryCol = 25
# ConditionCol = 29
# RelevanceCol = 52

#Enhance 76** and RVR 9**; same format
# GoOnsetCol = 50
# StimOnsetCol = 64
# StimACCCol = 59
# CategoryCol = 30
# ConditionCol = 34
# RelevanceCol = 57

#Estrogen
# GoOnsetCol = 11
# StimOnsetCol = 16
# StimACCCol = 14
# CategoryCol = 4
# ConditionCol = 5
# RelevanceCol = 13

# #TMS1
# GoOnsetCol = 42
# StimOnsetCol = 56
# StimACCCol = 51
# CategoryCol = 22
# ConditionCol = 26
# RelevanceCol = 49

GoOnsetTime = 0
StimOnsetTime = 0
cond = ""

#for every run
for i in range(1,6):
	linenum = 1
	# if (subject == "7614" and i == 5):
		# break
	for line in fileinput.input(subject+"-"+str(i)+".txt"):
	# for line in fileinput.input(subject+"-"+str(1)+"_fixed.txt"):
		if (linenum > 2):
			fields = line.strip('\r\n').split('\t')
			if (((linenum - 3) % 22) == 0):
				if (len(fields) > 1):
					GoOnsetTime = fields[GoOnsetCol].replace('\x00', '')
				if (linenum != 3):
					if (len(both_s) > 0):
						both_s_file.append(' '.join(both_s))
					else:
						both_s_file.append("*")
					if (len(both_f) > 0):
						both_f_file.append(' '.join(both_f))
					else:
						both_f_file.append("*")
					if (len(cat_s) > 0):
						cat_s_file.append(' '.join(cat_s))
					else:
						cat_s_file.append("*")
							
					if (len(cat_f) > 0):
						cat_f_file.append(' '.join(cat_f))
					else:
						cat_f_file.append("*")

					if (len(relevant_s) > 0):
						relevant_s_file.append(' '.join(relevant_s))
					else:
						relevant_s_file.append("*")

					if (len(relevant_f) > 0):
						relevant_f_file.append(' '.join(relevant_f))
					else:
						relevant_f_file.append("*")

					if (len(irrelevant_s) > 0):
						irrelevant_s_file.append(' '.join(irrelevant_s))
					else:
						irrelevant_s_file.append("*")
					
					if (len(irrelevant_f) > 0):
						irrelevant_f_file.append(' '.join(irrelevant_f))
					else:
						irrelevant_f_file.append("*")

					if (len(errors) > 0):
						errors_file.append(' '.join(errors))
					else:
						errors_file.append("*")
					
					del both_s[:]
					del both_f[:]
					del cat_s[:]
					del cat_f[:]
					del relevant_s[:]
					del relevant_f[:]
					del irrelevant_s[:]
					del irrelevant_f[:]
					del errors[:]

			else:
				StimOnsetTime = fields[StimOnsetCol].replace('\x00', '')				
				if ('1' in fields[StimACCCol]):
					result = str(float(int(StimOnsetTime) - int(GoOnsetTime)) / 1000)					

					if ((fields[ConditionCol].replace('\x00', '') == 'Faces') or (fields[ConditionCol].replace('\x00', '') == 'Scenes')):
						cond = fields[CategoryCol].replace('\x00', '') + fields[RelevanceCol].replace('\x00', '')
					else:
						cond = fields[CategoryCol].replace('\x00', '') + fields[ConditionCol].replace('\x00', '')
					if (cond == 'ScenesIrrelevant'):
						irrelevant_s.append(result)
					elif (cond == 'ScenesRelevant'):
						relevant_s.append(result)
					elif (cond == 'FacesIrrelevant'):
						irrelevant_f.append(result)
					elif (cond == 'FacesRelevant'):
						relevant_f.append(result)	
					elif (cond == 'ScenesBoth'):
						both_s.append(result)
					elif (cond == 'ScenesCategorize'):
						cat_s.append(result)
					elif (cond == 'FacesBoth'):
						both_f.append(result)
					elif (cond == 'FacesCategorize'):
						cat_f.append(result)
				elif ('0' in fields[StimACCCol]):
					result = str(float(int(StimOnsetTime) - int(GoOnsetTime)) / 1000)
					errors.append(result)

		linenum += 1

# Print final block for Estrogen files and TRSETMS1
# if (len(both_s) > 0):
# 	both_s_file.append(' '.join(both_s))
# else:
# 	both_s_file.append("*")
# if (len(both_f) > 0):
# 	both_f_file.append(' '.join(both_f))
# else:
# 	both_f_file.append("*")
# if (len(cat_s) > 0):
# 	cat_s_file.append(' '.join(cat_s))
# else:
# 	cat_s_file.append("*")
		
# if (len(cat_f) > 0):
# 	cat_f_file.append(' '.join(cat_f))
# else:
# 	cat_f_file.append("*")

# if (len(relevant_s) > 0):
# 	relevant_s_file.append(' '.join(relevant_s))
# else:
# 	relevant_s_file.append("*")

# if (len(relevant_f) > 0):
# 	relevant_f_file.append(' '.join(relevant_f))
# else:
# 	relevant_f_file.append("*")

# if (len(irrelevant_s) > 0):
# 	irrelevant_s_file.append(' '.join(irrelevant_s))
# else:
# 	irrelevant_s_file.append("*")

# if (len(irrelevant_f) > 0):
# 	irrelevant_f_file.append(' '.join(irrelevant_f))
# else:
# 	irrelevant_f_file.append("*")

# if (len(errors) > 0):
# 	errors_file.append(' '.join(errors))
# else:
# 	errors_file.append("*")

#write all files
f = open(subject+'_both_scene.txt', 'w')
for val in both_s_file:
	f.write(val + '\n')
f.close()
f = open(subject+'_both_face.txt', 'w')
for val in both_f_file:
	f.write(val + '\n')
f.close()
f = open(subject+'_categorize_scene.txt', 'w')
for val in cat_s_file:
	f.write(val + '\n')
f.close()
f = open(subject+'_categorize_face.txt', 'w')
for val in cat_f_file:
	f.write(val + '\n')
f.close()
f = open(subject+'_relevant_scene.txt', 'w')
for val in relevant_s_file:
	f.write(val + '\n')
f.close()
f = open(subject+'_relevant_face.txt', 'w')
for val in relevant_f_file:
	f.write(val + '\n')
f.close()
f = open(subject+'_irrelevant_scene.txt', 'w')
for val in irrelevant_s_file:
	f.write(val + '\n')
f.close()
f = open(subject+'_irrelevant_face.txt', 'w')
for val in irrelevant_f_file:
	f.write(val + '\n')
f.close()
f = open(subject+'_errors.txt', 'w')
for val in errors_file:
	f.write(val + '\n')
f.close()
