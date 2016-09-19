def modify_file(dataset_name, no_trees, no_features, purity, depth):
    from os import system
    system("del /f rf.ecl")

    modified_file_name = "c:/GIT/HPCCTuning/Problems/HPCC/RF/rf.ecl"
    # modified_file_name = "rf.ecl"
    original_file_name = "c:/GIT/HPCCTuning/Problems/HPCC/RF/rf_original.ecl"
    # original_file_name = "rf_original.ecl"
    content = open(original_file_name, "r").readlines()

    content[6] = "raw_train_data := TE." + dataset_name + ".Training;\n"
    content[7] = "raw_test_data := TE." + dataset_name + ".Tuning;\n"
    content[25] = "learner := ML.Classify.RandomForest(" + str(no_trees) + "," + str(no_features) + "," + str(purity) + "," + str(depth) + ", False);\n"
    f = open(modified_file_name, "w")
    f.write("".join(content))
    f.close()

if __name__ == "__main__":
    modify_file('dataset_name', 200, 5, 0.87, 50, "True")

