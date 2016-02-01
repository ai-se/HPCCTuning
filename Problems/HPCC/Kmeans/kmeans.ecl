IMPORT ML;

lMatrix:={UNSIGNED id;REAL x;REAL y;};
dEntityMatrix:=DATASET([
{1,2.4639,7.8579},
{2,0.5573,9.4681},
{3,4.6054,8.4723},
{4,1.24,7.3835},
{5,7.8253,4.8205},
{6,3.0965,3.4085},
{7,8.8631,1.4446},
{8,5.8085,9.1887},
{9,1.3813,0.515},
{10,2.7123,9.2429},
{11,6.786,4.9368},
{12,9.0227,5.8075},
{13,8.55,0.074},
{14,1.7074,3.9685},
{15,5.7943,3.4692},
{16,8.3931,8.5849},
{17,4.7333,5.3947},
{18,1.069,3.2497},
{19,9.3669,7.7855},
{20,2.3341,8.5196}
],lMatrix);
ML.ToField(dEntityMatrix,dEntities);

dCentroidMatrix:= DATASET('C:\\Users\\Vivek\\GIT\\HPCCTuning\\Problems\\HPCC\\Kmeans\\temp.csv', lMatrix, CSV);
OUTPUT(dEntityMatrix);


//ML.ToField(dCentroidMatrix,dCentroids);

//MyKMeans:=ML.Cluster.KMeans(dEntities,dCentroids,30,.3);

//MyKMeans.Convergence;