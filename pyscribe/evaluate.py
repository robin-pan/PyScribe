from constants import DEFAULT_PENALTY
from cost import hcosts, vcosts
from itertools import combinations, product

def hcost(fingerPair, distance):
  fingerPairLst = [str(i) for i in fingerPair]
  fingerPairStr = ''.join(fingerPairLst)
  distanceChart =  hcosts[fingerPairStr]
  return distanceChart[distance] if distance in distanceChart else DEFAULT_PENALTY

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
    
  return totalcost

def vcost(fingerPair, distance):
  fingerPairStr = ''.join(str(i) for i in fingerPair)
  distanceChart = vcosts[fingerPairStr]
  return distanceChart[distance] if distance in distanceChart else DEFAULT_PENALTY

def verticalCost(individual, chords):
  totalcost = 0
  for i in range(len(individual)):
    assignedFingerings = [(finger, note) for finger, note in zip(individual[i], chords[i].pitches)]

    allPairs = list(combinations(assignedFingerings, 2))
    for pair in allPairs:
      fingerPair = (pair[0][0], pair[1][0])
      distance = pair[1][1].midi-pair[0][1].midi
      totalcost += vcost(fingerPair, distance)

  return totalcost

def evaluate(individual, chords):
  v = verticalCost(individual, chords)
  h = horizontalCost(individual, chords)
  return v + h