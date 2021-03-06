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
from random import sample

# for count in xrange(1, 10):
#     command = "ecl run rf_original.ecl -I\"C:\ecl-ml-master\"  --target=thor --server=192.168.56.101:8010"
#     import subprocess
#
#     output = subprocess.check_output(command, shell=True)
#     print output
#     raw_input()


class hpcc_kmeans(jmoo_problem):
    "hpcc_kmeans"

    def __init__(prob,dataset_name, instances=100, features=20, nol=30, noc=0.3,tuning_precent=20):
        prob.name = "hpcc_kmeans_" + dataset_name
        prob.features = features
        prob.instances = instances
        prob.dataset_name = dataset_name
        prob.tuning_instances = sample(range(1, prob.instances+1), int(prob.instances * tuning_precent/100))
        prob.conv = noc
        prob.decisions = [jmoo_decision("k", 1, int(features**0.5)), jmoo_decision("number_of_loops", 1, nol)]
        prob.objectives = [jmoo_objective("convergence", True)]
        prob.is_binary = False

    def evaluate(prob, input=None):
        if input:
            for i, decision in enumerate(prob.decisions):
                decision.value = input[i]
        input = [decision.value for decision in prob.decisions]

        k = int(input[0])
        t_nol = int(input[1])

        from modify_ecl_file import modify_file
        from random import randint
        modify_file(prob.dataset_name, prob.features, [randint(1, prob.instances) for _ in xrange(k)],
                    t_nol, prob.conv, prob.tuning_instances)

        print "# ",
        sys.stdout.flush()
        command = "ecl run /home/vnair2/GIT/HPCCTuning/Problems/HPCC/Kmeans/kmeans.ecl -I\"/home/vnair2/GIT/ecl-ml\" --target=thor"

        import subprocess
        DEVNULL = open(os.devnull, "wb")
        output = subprocess.check_output(command, shell=True)
        result = output.split("\n")[3]
        import re
        res = re.search(r"_1>(.*)</Result_1>", result)
        return_value = int(res.group(1))
        return [return_value]

    def evalConstraints(prob, input=None):
        return False  # no constraints
