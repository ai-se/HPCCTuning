//RandomForest.ecl
IMPORT ML;
IMPORT ML.Tests.Explanatory as TE;
IMPORT TestingSuite.Utils AS Utils;

//Medium Large dataset for tests//
raw_train_data := TE.dconnect4.Training;
raw_test_data := TE.dconnect4.Tuning;

// Splitting data into train and test
Utils.ToTraining(raw_train_data, train_data_independent);
Utils.ToTesting(raw_train_data, train_data_dependent);
Utils.ToTraining(raw_test_data, test_data_independent);
Utils.ToTesting(raw_test_data, test_data_dependent);

ML.ToField(train_data_independent, pr_indep);
trainIndepData := ML.Discretize.ByRounding(pr_indep);
ML.ToField(train_data_dependent, pr_dep);
trainDepData := ML.Discretize.ByRounding(pr_dep);

ML.ToField(test_data_independent, tr_indep);
testIndepData := ML.Discretize.ByRounding(tr_indep);
ML.ToField(test_data_dependent, tr_dep);
testDepData := ML.Discretize.ByRounding(tr_dep);

learner := ML.Classify.RandomForest(99,32,0.906904726879,93, False);
result := learner.LearnD(trainIndepData, trainDepData); // model to use when classifying
model:= learner.model(result);  // transforming model to a easier way to read it

class:= learner.classifyD(testIndepData, result); // classifying

//Measuring Performance of Classifier
performance:= ML.Classify.Compare(testDepData, class);

OUTPUT(performance.Accuracy, Named('accuracy'));
OUTPUT(performance.MacroAveragePrecision, Named('map'));
OUTPUT(performance.MacroAverageRecall, Named('mar'));

