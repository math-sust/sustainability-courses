import csv




times = open("TimesHigherImpactQueries.txt","r")


cleanedWords = [] * 17
cleanedNots = [] * 17

for sdg in times:
    print(sdg)
    index = 0

    while index < len(sdg):
        print(sdg[index])
        index+=1

    break









"""
courses = open("SustainCourses.tsv","r")
reader = csv.reader(courses, delimiter='\t')


for row in reader:
        title = row[2].lower()
        desc = row[4].lower()
        sdgs = []
        for x in range(0,17):
            validWords = cleanedWords[x]
            invalidWords = cleanedNots[x]
            for word in sdg:
                if(word in title or word in desc):
                    valid = 1
                    for iw in invalidWords:
                        if(iw in title or iw in desc):
                            valid = 0
                            break
                    if valid:
                        sdgs.append(x+1)
                    break
                    
        print(sdgs)
"""





