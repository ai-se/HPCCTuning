IMPORT * FROM ML;
		 
IMPORT * FROM ML.Cluster;
 
IMPORT * FROM ML.Types;
 
x2 := DATASET([
{1, 1, 1}, {1, 2, 5},
{2, 1, 5}, {2, 2, 7},
{3, 1, 8}, {3, 2, 1},
{4, 1, 0}, {4, 2, 0},
{5, 1, 9}, {5, 2, 3},
{6, 1, 1}, {6, 2, 4},
{7, 1, 9}, {7, 2, 4}],NumericField);
c := DATASET([{1, 1, 1}, {1, 2, 5},{2, 1, 5}, {2, 2, 7}],NumericField);
x3 := Kmeans(x2,c,50,0.01);
 
OUTPUT(x3);
