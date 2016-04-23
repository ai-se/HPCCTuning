IMPORT * FROM ML;
IMPORT ML.Tests.Explanatory as TE;

//Tiny dataset for tests
weatherRecord := RECORD
	Types.t_RecordID id;
	Types.t_FieldNumber outlook;
	Types.t_FieldNumber temperature;
	Types.t_FieldNumber humidity;
	Types.t_FieldNumber windy;
	Types.t_FieldNumber play;
END;
weather_Data := DATASET([
{1,0,0,1,0,0},
{2,0,0,1,1,0},
{3,1,0,1,0,1},
{4,2,1,1,0,1},
{5,2,2,0,0,1},
{6,2,2,0,1,0},
{7,1,2,0,1,1},
{8,0,1,1,0,0},
{9,0,2,0,0,1},
{10,2,1,0,0,1},
{11,0,1,0,1,1},
{12,1,1,1,1,1},
{13,1,0,0,0,1},
{14,2,1,1,1,0}],
weatherRecord);
OUTPUT(weather_Data, NAMED('weather_Data'));
indep_Data:= TABLE(weather_Data,{id, outlook, temperature, humidity, windy});
dep_Data:= TABLE(weather_Data,{id, play});

ToField(indep_data, pr_indep);
indepData := ML.Discretize.ByRounding(pr_indep);
ToField(dep_data, pr_dep);
depData := ML.Discretize.ByRounding(pr_dep);

/* 
// Wont work with the largest dataset, delete " , ALL"
// As well as further commented lines will ", ALL"

// Using a small dataset to facilitate understanding of algorithm
OUTPUT(indepData, NAMED('indepData'), ALL);
OUTPUT(depData, NAMED('depData'), ALL);
*/

// Generating a random forest of 100 trees selecting 7 features for splits using impurity:=1.0 and max depth:= 100.
learner := Classify.RandomForest(100, 7, 1.0, 100, FALSE);  // GiniSplit = FALSE uses Info Gain Ratio as split criteria
result := learner.LearnD(IndepData, DepData); // model to use when classifying
model:= learner.model(result);  // transforming model to a easier way to read it

//Class distribution for each Instance
ClassDist:= learner.ClassProbDistribD(IndepData, result);
class:= learner.classifyD(IndepData, result); // classifying

//Measuring Performance of Classifier
performance:= Classify.Compare(depData, class);
OUTPUT(performance.Accuracy, NAMED('Accuracy'));

