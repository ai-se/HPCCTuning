from __future__ import division
import sys, os, inspect

parentdir = os.path.realpath(
    os.path.abspath(os.path.join(os.path.split(inspect.getfile(inspect.currentframe()))[0], "../../")))
if parentdir not in sys.path:
    sys.path.insert(0, parentdir)

parentdir = os.path.realpath(
    os.path.abspath(os.path.join(os.path.split(inspect.getfile(inspect.currentframe()))[0], "../../Techniques")))
if parentdir not in sys.path:
    sys.path.insert(0, parentdir)
from jmoo_objective import *
from jmoo_decision import *
from jmoo_problem import jmoo_problem
from euclidean_distance import euclidean_distance
from os import system


# for count in xrange(1, 10):
#     command = "ecl run kmeans_original.ecl -I\"C:\ecl-ml-master\"  --target=thor --server=192.168.56.101:8010"
#     import subprocess
#
#     output = subprocess.check_output(command, shell=True)
#     print output
#     raw_input()


class hpcc_kmeans(jmoo_problem):
    "hpcc_kmeans"

    def __init__(prob,instances=100, features=20, k=3, nol=30, noc=4, norows=None):
        prob.name = "hpcc_kmeans"
        prob.instances = instances
        prob.decisions = [jmoo_decision("k", 1, int(features**0.5)), jmoo_decision("number_of_loops", 1, nol), jmoo_decision("no_of_centroids", 1, noc)]
        prob.objectives = [jmoo_objective("convergence", True)]
        prob.no_of_columns = norows
        prob.is_binary = False

    def evaluate(prob, input=None):
        if input:
            for i, decision in enumerate(prob.decisions):
                decision.value = input[i]
        input = [decision.value for decision in prob.decisions]

        k = int(input[0])
        t_nol = int(input[1])
        t_noc = int(input[2])

        from modify_ecl_file import modify_file
        from random import randint
        modify_file([randint(1, prob.instances) for _ in xrange(k)], t_nol, t_noc)
        # generates centroids
        if prob.no_of_columns is None:
            assert ()
        else:
            from random import random

        command = "ecl run /home/vivek/GIT/HPCCTuning/Problems/HPCC/Kmeans/kmeans.ecl -I\"/home/vivek/ecl-ml-master\" --target=thor"

        print command

        import subprocess
        output = subprocess.check_output(command, shell=True)
        print output
        exit()

        return [objective.value for objective in prob.objectives]

    def evalConstraints(prob, input=None):
        return False  # no constraints
