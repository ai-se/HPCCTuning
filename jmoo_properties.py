
"""
##########################################################
### @Author Joe Krall      ###############################
### @copyright see below   ###############################

    This file is part of JMOO,
    Copyright Joe Krall, 2014.

    JMOO is free software: you can redistribute it and/or modify
    it under the terms of the GNU Lesser General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    JMOO is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Lesser General Public License for more details.

    You should have received a copy of the GNU Lesser General Public License
    along with JMOO.  If not, see <http://www.gnu.org/licenses/>.

###                        ###############################
##########################################################
"""

"Brief notes"
"Property File.  Defines default settings."

from jmoo_algorithms import *
from jmoo_problems import *

# from Problems.CPM.cpm import *
# from Problems.CPM.cpm_reduction import *
from Problems.NRP.nrp import *
# from Problems.MONRP.monrp import *
from Problems.POM3.POM3B import POM3B
from Problems.POM3.POM3A import POM3A
from Problems.POM3.POM3C import POM3C
from Problems.POM3.POM3D import POM3D
from Problems.Feature_Models.feature_model import FeatureTreeModel
from Problems.XOMO.XOMO_flight import XOMO_flight
from Problems.XOMO.XOMO_all import XOMO_all
from Problems.XOMO.XOMO_ground import XOMO_ground
from Problems.XOMO.XOMO_osp import XOMO_osp
from Problems.XOMO.XOMO_osp2 import XOMO_osp2
from Problems.Constrained.Type1 import c1_dtlz1,c1_dtlz3
from Problems.Constrained.Type2 import c2_dtlz2, c2_convex_dtlz2
from Problems.Constrained.Type3 import c3_dtlz1, c3_dtlz4
from Problems.HPCC.Kmeans.runner import hpcc_kmeans

# JMOO Experimental Definitions
algorithms = [
                # jmoo_GALE2(),
                jmoo_GALE(),
                jmoo_DE(),
                # jmoo_MOEAD_TCH(),
                # jmoo_NSGAIII(),
                # jmoo_GALE_no_mutation(),
                # jmoo_NSGAII(),
                # jmoo_SPEA2(),
                # jmoo_GALE4(),
                # jmoo_DE(),
                # jmoo_MOEAD_TCH(),
                # jmoo_NSGAIII(),
                # jmoo_STORM()
              ]

problems =[
    hpcc_kmeans(dataset_name="testing", instances=345, features=7, nol=200, tuning_precent=20),
    hpcc_kmeans(dataset_name="nursery.csv", instances=12960, features=8, nol=200, tuning_precent=20),
    hpcc_kmeans(dataset_name="letter.csv", instances=20000, features=16, nol=200, tuning_precent=20),
    hpcc_kmeans(dataset_name="poker.csv", instances=1025010, features=11, nol=200, tuning_precent=20)

]

build_new_pop = False                                       # Whether or not to rebuild the initial population

Configurations = {
    "Universal": {
        "Repeats" : 1,
        "Population_Size" : 20,
        "No_of_Generations" : 20
    },
    "NSGAIII": {
        "SBX_Probability": 1,
        "ETA_C_DEFAULT_" : 30,
        "ETA_M_DEFAULT_" : 20
    },
    "GALE": {
        "GAMMA" : 0.15,  #Constrained Mutation Parameter
        "EPSILON" : 1.00,  #Continuous Domination Parameter
        "LAMBDA" :  3,     #Number of lives for bstop
        "DELTA"  : 3       # Accelerator that increases mutation size
    },
    "DE": {
        "F" : 0.75, # extrapolate amount
        "CF" : 0.3, # prob of cross over
    },
    "MOEAD" : {
        "niche" : 20,  # Neighbourhood size
        "SBX_Probability": 1,
        "ETA_C_DEFAULT_" : 20,
        "ETA_M_DEFAULT_" : 20,
        "Theta" : 5
    },
    "STORM": {
        "STORM_EXPLOSION" : 5,
        "STORM_POLES" : 20,  # number of actual poles is 2 * ANYWHERE_POLES
        "F" : 0.75, # extrapolate amount
        "CF" : 0.3, # prob of cross over
        "STORM_SPLIT": 6,  # Break and split into pieces
        "GAMMA" : 0.15,
    }
}


# File Names
DATA_PREFIX        = "Data/"
DEFECT_PREDICT_PREFIX = "defect_prediction/"
VERSION_SPACE_PREFIX = "version_space/"

"decision bin tables are a list of decisions and objective scores for a certain model"
DECISION_BIN_TABLE = "decision_bin_table"

"result scores are the per-generation list of IBD, IBS, numeval,scores and change percents for each objective - for a certain model"
RESULT_SCORES      = "result_"

SUMMARY_RESULTS    = "summary_"

RRS_TABLE = "RRS_TABLE_"
DATA_SUFFIX        = ".datatable"


