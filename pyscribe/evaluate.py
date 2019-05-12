from cost import hcosts, vcosts
from itertools import combinations, product

def isBlackKey(pitch):
  blackKeys = { 1, 3, 6, 8, 10 }
  return (pitch.midi % 12) in blackKeys

def isCrossover(fingerPair, distance):
  if fingerPair[0] == 0 and distance < 0:
    return True
  if fingerPair[1] == 0 and distance > 0:
    return True
  return False

def hcost(fingerPair, distance):
  fingerPairLst = [str(i) for i in fingerPair]
  fingerPairStr = ''.join(fingerPairLst)
  distanceChart =  hcosts[fingerPairStr]
  return distanceChart[distance] if distance in distanceChart else 5

def horizontalCost(individual, chords):
  totalcost = 0
  for i in range(len(individual) - 1):
    assignedFingeringsCurr = [(finger, note) for finger, note in zip(individual[i], chords[i].pitches)]
    assignedFingeringsNext = [(finger, note) for finger, note in zip(individual[i+1], chords[i+1].pitches)]

    allPairs = list(product(assignedFingeringsCurr, assignedFingeringsNext))
    for pair in allPairs:
      fingerPair = (pair[0][0], pair[1][0])
      distance = pair[1][1].midi - pair[0][1].midi
      totalcost += hcost(fingerPair, distance) / len(allPairs)

      if isCrossover(fingerPair, distance):
        totalcost += 2
    
  return totalcost

def vcost(fingerPair, distance):
  fingerPairStr = ''.join(str(i) for i in fingerPair)
  distanceChart = vcosts[fingerPairStr]
  return distanceChart[distance] if distance in distanceChart else 5

def verticalCost(individual, chords):
  totalcost = 0
  for i in range(len(individual)):
    assignedFingerings = [(finger, note) for finger, note in zip(individual[i], chords[i].pitches)]

    if assignedFingerings[0][0] == 0 and isBlackKey(assignedFingerings[0][1]):
      totalCost += 2

    allPairs = list(combinations(assignedFingerings, 2))
    for pair in allPairs:
      fingerPair = (pair[0][0], pair[1][0])
      distance = pair[1][1].midi-pair[0][1].midi
      totalcost += vcost(fingerPair, distance)

  return totalcost

def evaluate(individual, chords):
  v = verticalCost(individual, chords)
  h = horizontalCost(individual, chords)
  return v + h * 2