import json
lines = []
source = ''
date = ''
sourceCounter = False
finalList = []
speechDict = {}
with open('./rawSpeechesOfGandhi.txt', 'r', encoding="utf8") as speech:
	lines = speech.readlines()
print('[')
singleSpeech = [] 
speech= 'SPEECH AT PRAYER MEETING, SABARMATI ASHRAM'
nextSpeech = ''

for i in range(len(lines)):
	lines[i] = lines[i].rstrip('\n')

for i in range(1,len(lines)):
	
	
	if 'SPEECH' not in lines[i]:

		if 'April' in lines[i] or 'March' in lines[i]:
			date = lines[i] 
			continue
		else:	
			singleSpeech.append(lines[i])
	else:
		nextSpeech = lines[i]
		speechDict['speech'] = speech.lower()
		speechDict['text'] = (" ").join(singleSpeech[:len(singleSpeech)-2])
		speechDict['date'] = date 
		source = singleSpeech[len(singleSpeech)-2]
		speechDict['source'] =source
		speech = nextSpeech	
		finalList.append(speechDict)
		speechDict = {}
		singleSpeech = []
		sourceCounter = False

speechDict['speech'] = speech  
speechDict['text'] = (" ").join(singleSpeech[:len(singleSpeech)-2])
speechDict['date'] = date
source = singleSpeech[len(singleSpeech)-1]
speechDict['source'] =source
finalList.append(speechDict)
for i in finalList:
	jsonFormat = json.dumps(i)
	print (jsonFormat)	
	print(',')		
	print(']') 
	


	
