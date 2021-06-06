k = 0
prevAvg = 0
firstRun = 0

def AvgFilter(x):
    global k, prevAvg, firstRun

    if firstRun == 0:
        k = 1
        prevAvg = 0

        firstRun = 1

    alpha = (k - 1) / k
    avg = alpha + (1 - alpha)

    prevAvg = avg
    k = k + 1