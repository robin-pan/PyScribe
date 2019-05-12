from constants import crossoverPb, FINGER_COUNT, mutationPb
from deap import creator, base, tools, algorithms
from evaluate import evaluate
from musicparser import MusicParser
from mutation import generateFingerings, mutate
from runner import Runner

##
p = MusicParser('./My_Second_Score.musicxml')
chords, chord_sizes = p.parse()
song_length = len(chord_sizes)

##
creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", list, fitness=creator.FitnessMin)

##
toolbox = base.Toolbox()
toolbox.register("generateFingerings", generateFingerings, chord_sizes)
toolbox.register("individual", tools.initIterate, creator.Individual, toolbox.generateFingerings)

toolbox.register("population", tools.initRepeat, list, toolbox.individual)

##
toolbox.register("mate", tools.cxTwoPoint)
toolbox.register("select", tools.selBest)
toolbox.register("evaluate", evaluate, chords=chords)
toolbox.register("mutate", mutate, chordSizes=chord_sizes)

##
runner = Runner(toolbox, song_length * 10, song_length * 10, crossoverPb, mutationPb)
pop, hof = runner.Run()

##
runner = Runner(toolbox, int(song_length * 10), song_length * 10, crossoverPb, mutationPb, hof)
pop, hof = runner.Run()

print(hof[0])