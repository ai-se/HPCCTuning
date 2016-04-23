def modify_file(no_trees, no_features, purity, depth, gini_split):
    from os import system
    system("rm -f rf.ecl")

    modified_file_name = "/home/vnair2/GIT/HPCCTuning/Problems/HPCC/Kmeans/rf.ecl"
    # modified_file_name = "rf.ecl"
    original_file_name = "/home/vnair2/GIT/HPCCTuning/Problems/HPCC/Kmeans/rf_original.ecl"
    # original_file_name = "rf_original.ecl"
    content = open(original_file_name, "r").readlines()

    content[26] = "learner := Classify.RandomForest(" + str(no_trees) + "," + str(no_features) + "," + str(purity) + "," + str(depth) + "," + gini_split + ");\n"
    f = open(modified_file_name, "w")
    f.write("".join(content))
    f.close()



if __name__ == "__main__":
    centroids = [1, 3, 5]
    tuning_instances = [3, 4, 2, 45, 23, 34, 12, 9,10, 11]
    nol = 50
    cov = 0.01
    modify_file(200, 5, 1, 50, "True")

