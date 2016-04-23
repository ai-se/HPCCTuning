//RandomForest.ecl
IMPORT * FROM ML;
IMPORT ML.Tests.Explanatory as TE;

//Medium Large dataset for tests//
indep_data:= TABLE(TE.AdultDS.Train_Data,{id, Age, WorkClass, education, education_num, marital_status, occupation, relationship, race, sex, capital_gain, capital_loss, hours_per_week, native_country});
dep_data:= TABLE(TE.AdultDS.Train_Data,{id, Outcome});

//train Data
train_indep_data := indep_data(id<16280);
train_dep_data := dep_data(id<16280);

//tune Data
tune_indep_data := indep_data(id>16280);
tune_dep_data := dep_data(id>16280);

ToField(train_indep_data, train_pr_indep);
trainIndepData := ML.Discretize.ByRounding(train_pr_indep);
ToField(train_dep_data, train_pr_dep);
trainDepData := ML.Discretize.ByRounding(train_pr_dep);

ToField(tune_indep_data, tune_pr_indep);
tuneIndepData := ML.Discretize.ByRounding(tune_pr_indep);
ToField(tune_dep_data, tune_pr_dep);
tuneDepData := ML.Discretize.ByRounding(tune_pr_dep);

learner := Classify.RandomForest(100, 7, 1.0, 100, FALSE);  // GiniSplit = FALSE uses Info Gain Ratio as split criteria
result := learner.LearnD(trainIndepData, trainDepData); // model to use when classifying
model:= learner.model(result);  // transforming model to a easier way to read it

class:= learner.classifyD(tuneIndepData, result); // classifying

//Measuring Performance of Classifier
performance:= Classify.Compare(tuneDepData, class);
OUTPUT(performance.Accuracy, NAMED('Accuracy'));

