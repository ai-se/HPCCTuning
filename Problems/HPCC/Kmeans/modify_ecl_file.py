def modify_file(centroids, number_of_loops, convergence):

   from os import system
   system("rm -f kmeans.ecl")

   modified_file_name = "/home/vivek/GIT/HPCCTuning/Problems/HPCC/Kmeans/kmeans.ecl"
   original_file_name = "/home/vivek/GIT/HPCCTuning/Problems/HPCC/Kmeans/kmeans_original.ecl"
   content = open(original_file_name, "r").readlines()

   new_content = content[:26]  # get all the data
   new_content += "SET OF INTEGER raw_centroids := [" +",".join(map(str, centroids)) +"];\n"
   new_content += content[27:45]
   new_content += "x3 := Kmeans(d,c," + str(number_of_loops) + "," +str(convergence) +");\n"
   new_content += content[46:]

   new_content = "".join(new_content)
   f = open(modified_file_name, "w")
   f.write(new_content)
   f.close()



if __name__ == "__main__":
   centroids = [1, 3, 5]
   nol = 50
   cov = 0.01
   modify_file(centroids, nol, cov)
