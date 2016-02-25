import os, sys
def modify_file(dataset_name, k, number_of_loops, no_features, no_instances):
    from os import system
    from random import randint
    system("rm -f kmeans.ecl")

    centroids = [randint(1, no_instances) for _ in xrange(k)]
    modified_file_name = "/Users/viveknair/GIT/HPCCTuning/Validation/KMeans/kmeans.ecl"
    original_file_name = "/Users/viveknair/GIT/HPCCTuning/Validation/KMeans/kmeans_original.ecl"
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
    new_content += "// SET OF INTEGER raw_datapoints := ["+"\n"
    new_content += "SET OF INTEGER raw_centroids := [" + ",".join(map(str, centroids)) + "];\n"
    new_content += content[39:45]
    new_content += "x3 := Kmeans(d,c," + str(number_of_loops) + "," + str(0.01) + ");\n"
    new_content += content[46:]

    new_content = "".join(new_content)
    f = open(modified_file_name, "w")
    f.write(new_content)
    f.close()



datasets = ["testing", "nursery.csv", "letter.csv", "poker.csv"]
searchers = ["DE", "GALE"]
parameters = ["k", "nol"]

parameters = {}

parameters["testing"] = {}
parameters["testing"]["DE"] = {}
parameters["testing"]["DE"]["k"]=1
parameters["testing"]["DE"]["nol"]=1
parameters["testing"]["GALE"] = {}
parameters["testing"]["GALE"]["k"]=2
parameters["testing"]["GALE"]["nol"]=79

parameters["letter.csv"] = {}
parameters["testing"]["DE"] = {}
parameters["letter.csv"]["DE"]["k"]=3
parameters["letter.csv"]["DE"]["nol"]=117
parameters["testing"]["GALE"] = {}
parameters["letter.csv"]["GALE"]["k"]=4
parameters["letter.csv"]["GALE"]["nol"]=200

parameters["nursery.csv"] = {}
parameters["nursery.csv"]["DE"] = {}
parameters["nursery.csv"]["DE"]["k"]=1
parameters["nursery.csv"]["DE"]["nol"]=196
parameters["nursery.csv"]["GALE"] = {}
parameters["nursery.csv"]["GALE"]["k"]=2
parameters["nursery.csv"]["GALE"]["nol"]=200

parameters["poker.csv"] = {}
parameters["testing"]["DE"] = {}
parameters["poker.csv"]["DE"]["k"]=2
parameters["poker.csv"]["DE"]["nol"]=197
parameters["poker.csv"]["GALE"] = {}
parameters["poker.csv"]["GALE"]["k"]=3
parameters["poker.csv"]["GALE"]["nol"]=71


for dataset in datasets:
    for searcher in searchers:
        k = parameters[dataset][searcher]["k"]
        nol = parameters[dataset][searcher]["nol"]
        modify_file(dataset, k, nol,  no_instances=345, no_features=7)
         print "# ",
        sys.stdout.flush()
        command = "ecl run /home/vivek/GIT/HPCCTuning/Problems/HPCC/Kmeans/kmeans.ecl -I\"/home/vivek/ecl-ml-master\" --target=thor"

        import subprocess
        DEVNULL = open(os.devnull, "wb")
        output = subprocess.check_output(command, shell=True)
        result = output.split("\n")[3]
        import re
        res = re.search(r"_1>(.*)</Result_1>", result)
        return_value = int(res.group(1))
        print dataset, searcher, [return_value]