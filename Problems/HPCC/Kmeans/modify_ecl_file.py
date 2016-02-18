def modify_file(centroids, number_of_loops, convergence):

    from os import system
    system("rm -f kmeans.ecl")

    modified_file_name = "./kmeans.ecl"
    original_file_name = "./kmeans_original.ecl"
    content = open(original_file_name, "r").readlines()

    new_content = content[:14]  # get all the data
    new_content += centroids + "\n"
    new_content += "x3 := Kmeans(x2,c," + str(number_of_loops) + "," +str(convergence) +");\n"
    new_content += content[20:23]

    print new_content
    f = open(modified_file_name, "w")
    f.write(new_content)
    f.close()



if __name__ == "__main__":
    centroids = "c := DATASET([{1, 1, 1}, {1, 2, 5},{2, 1, 5}, {2, 2, 7}],NumericField);"
    nol = 50
    cov = 0.01
    modify_file(centroids, nol, cov)