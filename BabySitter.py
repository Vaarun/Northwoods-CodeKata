def timeInput():
    startTime = input("Enter the start hour(ex: 7PM):")
    endTime = input("Enter an end hour (ex: 3AM):")
    bedTime = input("Enter the bedtime hour(ex: 10PM):")

    return[startTime, endTime, bedTime]

def timeValid(time):
    #Grab the times from the Array
    start = time[0]
    end = time[1]
    bed = time[2]
    #Grab the Suffixes from each time
    startSuffix = start[-2:].lower()
    endSuffix = end[-2:].lower()
    bedSuffix = bed[-2:].lower()

    startHour = 0
    endHour = 0
    bedHour = 0

    oneDigitStart = False

    #If last two chars are not AM/PM then time is in invalid format.
    if (startSuffix != "am" and startSuffix !=  "pm") or (endSuffix != "am" and endSuffix != "pm") or (bedSuffix != "am" and bedSuffix != "pm"):
        print("Incorrect Format on AM/PM")
        return []
    #With the above check, confirms that the format of the input is correct
    if(len(start) == 3):
        if (not start[:1].isnumeric()):
            print("Incorrect Format on Start Hour Number")
            return []
    elif(len(start) == 4):
        if (not start[:2].isnumeric()):
            print("Incorrect Format on Start Hour Number")
            return []
    
    if(len(end) == 3):
        if (not end[:1].isnumeric()):
            print("Incorrect Format on End Hour Number")
            return []
    elif(len(end) == 4):
        if (not end[:2].isnumeric()):
            print("Incorrect Format on End Hour Number")
            return []
    
    if(len(bed) == 3):
        if (not bed[:1].isnumeric()):
            print("Incorrect Format on Bed Hour Number")
            return []
    elif(len(bed) == 4):
        if (not bed[:2].isnumeric()):
            print("Incorrect Format on Bed Hour Number")
            return []


    #Note: I am under the assumption that it is unreasonable to have the start time be after 11pm, and that bedtime must be held before 12 am.

    #Validate and grab the start hour
    #Check if it is a 2 digit number or one digit number. if not fail. 
    #If it is a number confirm the number is accurate for the requirements.
    if(not start[:2].isnumeric()):
        if(not start[:1].isnumeric()):
            print("Enter a valid number for start hour")
            return([])
        else:
            if((int(start[:1]) > 4) and (startSuffix == "pm")):
                startHour = int(start[:1])
                oneDigitStart = True
            else:
                print("Start hour entered is invalid")
                return([])

    else:
        if((int(start[:2]) < 12) and (startSuffix == "pm")):
            startHour = int(start[:2])
        else:
            print("Start hour entered is invalid")
            return([])
    
    #Validate and grab the end hour
    #Check if it is a 2 digit number or one digit number. if not fail. 
    #If it is a number confirm the number is accurate for the requirements.

    # This checks if the first two numbers are the same for the start and end, or if its a one digit number, the first letter of  the suffix and the number are the same because if they are then the times inputed are the same, 
    # There is no overlapping numbers that are valid so we can use this as a quick way to fail
    if(end[:2] == start[:2]):
        return []

    if(not end[:2].isnumeric()):
        if(not end[:1].isnumeric()):
            print("Enter a valid number for end hour")
            return([])
        else:
            if( ((int(end[:1]) < 5) and (endSuffix == "am"))  or ( (oneDigitStart) and ((int(end[:1]) > startHour) and (endSuffix == "pm")))):
                endHour = int(end[:1])
            else:
                print("End hour entered is invalid")
                return([])
    else:
        if(((not oneDigitStart) and (12 > int(end[:2]) > startHour) and (endSuffix == "pm")) or ((oneDigitStart) and  (12 > int(end[:2]) > startHour) and (endSuffix == "pm")) or (int(end[:2]) == 12  and (endSuffix == "am")) ):
            endHour = int(end[:2])
        else:
            print("End hour entered is invalid")
            return([])
    


    #Validate and grab the bed hour
    #Check if it is a 2 digit number or one digit number. if not fail. 
    #If it is a number confirm the number is accurate for the requirements.

    if(not bed[:2].isnumeric()):
        if(not bed[:1].isnumeric()):
            print("Enter a valid number for bed hour")
            return([])
        else:
            if(bedSuffix == "am"):
                print("Bed hour entered is not correct")
                return([])

            elif(bedSuffix == "pm"):
                if(int(bed[:1]) >= startHour):
                    bedHour = int(bed[:1])
                else:
                    print("Bed hour entered is not during the babysitting hours")
                    return([])
    else:
        if(bedSuffix == "am"):
            print("Bed hour entered is not correct")
            return([])

        elif(bedSuffix == "pm"):
            if(int(bed[:2]) >= startHour):
                if(endSuffix =="pm"):
                    if(int(bed[:2]) <= endHour):
                        bedHour = int(bed[:2])
                    else:
                        print("Bed hour entered is not during the babysitting hours")
                        return([])
                else:
                    bedHour = int(bed[:2])
            else:
                print("Bed hour entered is not during the babysitting hours")
                return([])

    timeReturn = [startHour, endHour, bedHour]

    return(timeReturn)

def calulatePay(times):
    startHour = times[0]
    endHour = times[1]
    bedHour = times[2]
    sum = 0

    startToBedTime = bedHour - startHour
    bedTimeToMidnight = 12 - bedHour 
    midnightToEndTime = endHour - 12


    #Convert all the values to the actual values by adding 12 in case its negative. 
    if(startToBedTime < 0):
        startToBedTime += 12

    if(midnightToEndTime < 0):
        midnightToEndTime += 12
    
    #Skips calulations with midnight, if babysitter leaves before midnight
    if (endHour == (11 or 10 or 9 or 8 or 7) ):
        sum = 12 * startToBedTime
    else:
        #Multiples the money/hour * hours spent to get each section's money and then they are added.  
        sum = (12 * startToBedTime) + (8 * bedTimeToMidnight) + (16 *midnightToEndTime)
    print("You made $" ,sum, ".00")
    return(sum)



times = []
while(len(times) == 0):
    userValues = timeInput()
    times = timeValid(userValues)
calulatePay(times)
