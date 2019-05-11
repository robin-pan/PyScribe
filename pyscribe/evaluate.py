from itertools import combinations, product

def cost(fingerPair, distance):
  return 0

def verticalCost(individual, chords):
  vcost = 0
  for i in range(len(individual)):
    assignedFingerings = [(finger, note) for finger, note in zip(individual[i], chords[i].pitches)]
    allPairs = list(combinations(assignedFingerings, 2))
    for pair in allPairs:
      fingerPair = (pair[0][0], pair[1][0])
      distance = abs(pair[1][1].midi-pair[0][1].midi)
      vcost += cost(fingerPair, distance)

  return vcost

def horizontalCost(individual, chords):
  hcost = 0
  for i in range(len(individual) - 1):
    assignedFingeringsCurr = [(finger, note) for finger, note in zip(individual[i], chords[i].pitches)]
    assignedFingeringsNext = [(finger, note) for finger, note in zip(individual[i+1], chords[i+1].pitches)]

    allPairs = list(product(assignedFingeringsCurr, assignedFingeringsNext))
    for pair in allPairs:
      fingerPair = (pair[0][0], pair[1][0])
      distance = abs(pair[1][1].midi-pair[0][1].midi)
      hcost += (1/len(allPairs) * cost(fingerPair, distance))
    
  return hcost

def evaluate(individual, chords):
  return verticalCost(individual, chords) + horizontalCost(individual, chords)
  # return sum([sum(allele) for allele in individual])