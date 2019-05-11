from constants import FINGER_COUNT
from random import randint, sample

def generateFingering(chordSize):
  return tuple(sorted(sample(range(0, 5), chordSize)))

def generateFingerings(chordSizes):
  return [generateFingering(chordSize) for chordSize in chordSizes]

def mutate(individual, chordSizes):
  i = randint(0, FINGER_COUNT - 1)

  oldAllele = individual[i]
  if len(oldAllele) == FINGER_COUNT:
    return individual

  newAllele = oldAllele
  while newAllele == oldAllele:
    newAllele = generateFingering(chordSizes[i])

  individual[i] = newAllele
  
  return individual