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

    def __init__(prob, nol=30, noc=4, norows=None):
        prob.name = "hpcc_kmeans"
        prob.decisions = [jmoo_decision("number_of_loops", 1, nol), jmoo_decision("no_of_centroids", 1, noc)]
        prob.objectives = [jmoo_objective("convergence", True)]
        prob.no_of_columns = norows
        prob.is_binary = False

    def evaluate(prob, input=None):
        if input:
            for i, decision in enumerate(prob.decisions):
                decision.value = input[i]
        input = [decision.value for decision in prob.decisions]

        t_nol = int(input[0])
        t_noc = int(input[1])

        # generates centroids
        if prob.no_of_columns is None:
            assert ()
        else:
            from random import random
            # assuming the data is normalized
            centroids = "\n".join([str(count) + "," + ",".join([str(random()) for _ in xrange(prob.no_of_columns)]) for count in xrange(t_noc)])

        f = open(".\\Problems\\HPCC\\Kmeans\\temp.csv", "w")
        f.write(centroids)
        f.close()

        input_string = "--input=\"<request>"
        input_string += "<nol>" + str(t_nol) + "</nol>"
        input_string += "</request>\""

        command = "ecl run kmeans.ecl -I\"C:\ecl-ml-master\" " + input_string + "--target=thor --server=192.168.56.101:8010"

        print command

        import subprocess
        output = subprocess.check_output(command, shell=True)
        print output
        exit()

        return [objective.value for objective in prob.objectives]

    def evalConstraints(prob, input=None):
        return False  # no constraints
