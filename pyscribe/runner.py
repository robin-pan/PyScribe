import numpy as np
from random import random, shuffle

class Runner:
  def __init__(self, toolbox, popSize, ngen, crossoverPb, mutationPb, pop=None):
    self.toolbox = toolbox
    self.popSize = popSize
    self.ngen = ngen
    self.crossoverPb = crossoverPb
    self.mutationPb = mutationPb
    self.pop = pop
      
  def Run(self):
    if not self.pop:
      self.pop = self.toolbox.population(n=self.popSize)
    hof = []
    fitnesses = list(map(self.toolbox.evaluate, self.pop))

    for ind, fit in zip(self.pop, fitnesses):
      ind.fitness.values = (fit,)

    for g in range(self.ngen):
      # Select the next generation individuals
      offspring = self.toolbox.select(self.pop, len(self.pop))
      # Clone the selected individuals
      offspring = list(map(self.toolbox.clone, offspring))

      # Apply crossover and mutation on the offspring
      for child1, child2 in zip(offspring[::2], offspring[1::2]):
        if random() < self.crossoverPb:
          self.toolbox.mate(child1, child2)
          del child1.fitness.values
          del child2.fitness.values

      for mutant in offspring:
        if random() < self.mutationPb:
          self.toolbox.mutate(mutant)
          del mutant.fitness.values

      # Evaluate the individuals with an invalid fitness
      invalid_ind = [ind for ind in offspring if not ind.fitness.valid]
      fitnesses = list(map(self.toolbox.evaluate, invalid_ind))
      for ind, fit in zip(invalid_ind, fitnesses):
        ind.fitness.values = (fit,)
        
      hof.extend(offspring)
      hof.sort(key=lambda ind: ind.fitness.values)
      hof = hof[:int(self.popSize/2)]
      self.pop[:] = offspring
      print(self.toolbox.evaluate(hof[0]))

    return self.pop, hof
