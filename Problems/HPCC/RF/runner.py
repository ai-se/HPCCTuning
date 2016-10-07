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
from random import random
from euclidean_distance import euclidean_distance
from os import system
from random import sample

# for count in xrange(1, 10):
#     command = "ecl run rf_original.ecl -I\"C:\ecl-ml-master\"  --target=thor --server=192.168.56.101:8010"
#     import subprocess
#
#     output = subprocess.check_output(command, shell=True)
#     print output
#     raw_input()


class hpcc_random_forest(jmoo_problem):
    "hpcc_kmeans"

    def __init__(prob, dataset_name, features=20):
        prob.name = "hpcc_rf_" + dataset_name
        prob.dataset_name = dataset_name
        prob.decisions = [jmoo_decision("no_trees", 80, 120),
                          jmoo_decision("no_features", 4, features),
                          jmoo_decision("purity", 0.6, 1),
                          jmoo_decision("depth", 80, 120 )
                          ]
        prob.objectives = [jmoo_objective("accuracy", True)]
        prob.is_binary = False

    def evaluate(prob, input=None):
        if input:
            for i, decision in enumerate(prob.decisions):
                decision.value = input[i]
        input = [decision.value for decision in prob.decisions]

        no_trees = int(input[0])
        no_features = int(input[1])
        purity = input[2]
        depth = int(input[3])

        from modify_ecl_file import modify_file
        from random import randint
        modify_file(prob.dataset_name, no_trees, no_features, purity, depth)

        print "# ",
        sys.stdout.flush()
        command = "ecl run c:\\GIT\\HPCCTuning\\Problems\\HPCC\\RF\\rf.ecl -I\"c:\\GIT\\HPCCTuning\\ecl-ml\" --target=hthor --server=10.239.227.6 --port=8010"

        import subprocess
        DEVNULL = open(os.devnull, "wb")
        output = subprocess.check_output(command, shell=True)
        result = output.split("\n")[3]
        import re
        res = re.search(r"accuracy>(.*)</accuracy>", result)
        return_value = res.group(1)

        return [1-float(return_value)] # Since max value of accuracy = 1

    def evalConstraints(prob, input=None):
        return False  # no constraints
