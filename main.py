import BabySitter

times = []
while(len(times) == 0):
    userValues = BabySitter.timeInput()
    times = BabySitter.timeValid(userValues)
BabySitter.calulatePay(times)