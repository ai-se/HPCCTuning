def modify_file(dataset_name, no_features, centroids, number_of_loops, convergence, tuning_instances):
    from os import system
    system("rm -f kmeans.ecl")

    modified_file_name = "/home/vivek/GIT/HPCCTuning/Problems/HPCC/Kmeans/kmeans.ecl"
    original_file_name = "/home/vivek/GIT/HPCCTuning/Problems/HPCC/Kmeans/kmeans_original.ecl"
    content = open(original_file_name, "r").readlines()


    from string import ascii_lowercase

    layout_data = "layout_data := RECORD\n  INTEGER id;"
    for i in xrange(no_features):
        layout_data += "DECIMAL2 "
        layout_data += ascii_lowercase[i%len(ascii_lowercase)] + str(i/len(ascii_lowercase))
        layout_data += ";\n"
    layout_data += "END;\n"

    refined_data = "refined_data := RECORD \n"
    for i in xrange(no_features):
        refined_data += "DECIMAL2 "
        refined_data += ascii_lowercase[i%len(ascii_lowercase)] + str(i/len(ascii_lowercase))
        refined_data += ";\n"
    refined_data += "END;\n"

    remove_id = "refined_data remove_id(layout_data l) := TRANSFORM\n"
    for i in xrange(no_features):
        name = ascii_lowercase[i%len(ascii_lowercase)] + str(i/len(ascii_lowercase))
        remove_id += "SELF." + name + " := l." + name +";\n"
    remove_id  += "END;\n"


    new_content = content[:4]

    new_content += layout_data + "\n" + refined_data + "\n" + remove_id + "\n"
    new_content += "raw_data := DATASET(\'~" + dataset_name +"\', layout_data, csv(separator(\',\')));\n"
    new_content += "SET OF INTEGER raw_datapoints := [" + ",".join(map(str, tuning_instances)) + "];\n"
    new_content += "SET OF INTEGER raw_centroids := [" + ",".join(map(str, centroids)) + "];\n"
    new_content += content[39:45]
    new_content += "x3 := Kmeans(d,c," + str(number_of_loops) + "," + str(convergence) + ");\n"
    new_content += content[46:]

    new_content = "".join(new_content)
    f = open(modified_file_name, "w")
    f.write(new_content)
    f.close()


if __name__ == "__main__":
    centroids = [1, 3, 5]
    tuning_instances = [3, 4, 2, 45, 23, 34, 12, 9,10, 11]
    nol = 50
    cov = 0.01
    modify_file("testing", 7,  centroids, nol, cov, tuning_instances)
