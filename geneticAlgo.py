from random import randint, random
from operator import add

def individual(length, min, max):
    # create a member of pepulation
    return [randint(min, max) for x in xrange(length)]

def population(count, length, min, max):
    """
    create a number of individual/a population
    :param count: the number of individuals in the population
    :param length: the number of values per individual
    :param min: the min possible value in an individual's list of values
    :param max: the max possible value in an individual's list of values
    """
    return [individual(length, min, max) for x in xrange(count)]


def fitness(individual, target):
    """
    determine the fitness of an individuak. lower is better

    :param individual: the individual to evaluate
    :param target: the sum of numbers that individuals are aiming for
    :return:
    """
    sum = reduce(add, individual, 0)
    return abs(target-sum)

def grade(pop, target):
    # find average fitness for a population
    summed = reduce(add, (fitness(x, target) for x in pop), 0)
    return summed / (len(pop) * 1.0)

def evolve(pop, target, retain = 0.2, random_select=0.05, mutate = 0.01):
    graded = [ (fitness(x, target), x) for x in pop ]
    graded = [ x[1] for x in sorted(graded) ]
    retain_length = int(len(graded)*retain)
    parents = graded[:retain_length]

    # randomly add other individuals to promote generic diversity
    for individual in graded[retain_length:]:
        if random_select > random():
            parents.append(individual)

    # mutate some individuals
    for individual in parents:
        if mutate > random():
            pos_to_mutate = randint(0, len(individual)-1)
            individual[pos_to_mutate] = randint(
                min(individual), max(individual)
            )
    # crossover parents to create children
    parents_length = len(parents)
    desired_length = len(pop) - parents_length
    children = []
    while len(children) < desired_length:
        male = randint(0, parents_length-1)
        female = randint(0, parents_length-1)
        if male != female:
            male = parents[male]
            female = parents[female]
            half = len(male)/2
            child = male[:half] + female[:half]
            children.append(child)

    parents.extend(children)
    return parents
