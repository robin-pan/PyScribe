from constants import crossoverPb, FINGER_COUNT, mutationPb
from deap import creator, base, tools, algorithms
from random import randint, sample
from runner import Runner

CHORD_SIZES = [1, 3, 5, 3, 4, 1, 3, 5, 3, 4, 1, 3, 5, 3, 4, 1, 3, 5, 3, 4, 5, 3, 4, 1, 3, 5, 3, 4, 1, 3, 5, 3, 4]
SONG_LENGTH = len(CHORD_SIZES)

def generateFingering(chordSize):
  return tuple(sorted(sample(range(1, 6), chordSize)))

def generateFingerings(chordSizes):
  return [generateFingering(chordSize) for chordSize in chordSizes]

def evaluateInd(individual):
  return sum([sum(allele) for allele in individual])

def myMutation(individual):
  i = randint(0, FINGER_COUNT - 1)

  oldAllele = individual[i]
  if len(oldAllele) == FINGER_COUNT:
    return individual

  newAllele = oldAllele
  while newAllele == oldAllele:
    newAllele = generateFingering(CHORD_SIZES[i])

  individual[i] = newAllele
  
  return individual

##

creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", list, fitness=creator.FitnessMin)

##
toolbox = base.Toolbox()
toolbox.register("generateFingerings", generateFingerings, CHORD_SIZES)
toolbox.register("individual", tools.initIterate, creator.Individual, toolbox.generateFingerings)

toolbox.register("population", tools.initRepeat, list, toolbox.individual)

##
toolbox.register("mate", tools.cxTwoPoint)
toolbox.register("select", tools.selBest)
toolbox.register("evaluate", evaluateInd)
toolbox.register("mutate", myMutation)

runner = Runner(toolbox, SONG_LENGTH * 4, SONG_LENGTH * 4, crossoverPb, mutationPb)
pop, hof = runner.Run()

runner = Runner(toolbox, int(SONG_LENGTH * 2), SONG_LENGTH * 4, crossoverPb, mutationPb, hof)
pop, hof = runner.Run()