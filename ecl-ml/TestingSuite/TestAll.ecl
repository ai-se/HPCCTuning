IMPORT Std;
IMPORT TS;
IMPORT ML;
IMPORT ML.Types;
IMPORT TestingSuite;
IMPORT TestingSuite.BenchmarkResults AS BenchmarkResults;
IMPORT TestingSuite.Utils AS Utils;
IMPORT TestingSuite.Classification as Classification;
IMPORT TestingSuite.Clustering as Clustering;
IMPORT TestingSuite.Regression as Regression;
IMPORT TestingSuite.TimeSeries as TimeSeries;


QualifiedName(prefix, datasetname):=  FUNCTIONMACRO
        RETURN prefix + datasetname + '.content';
ENDMACRO;

INTEGER repeat_no := 10;

SET OF STRING classificationDatasetNamesD := ['discrete_GermanDS', 'discrete_houseVoteDS',
        'discrete_letterrecognitionDS','discrete_liverDS', 'discrete_satimagesDS',
        'discrete_soybeanDS', 'discrete_VehicleDS'];   
                                               
// For Testing KMeans        
SET OF STRING clusteringDatasetNames := ['ionek_f_eight_c_sixDS',  
                                        'ionek_f_four_c_fourDS', 
                                        'ionek_f_sixteen_c_eightDS', 
                                        'ionek_f_thirty_two_c_eightDS', 
                                        'ionek_f_two_c_twoDS' ];    
SET OF INTEGER ClusterNumbers := [6, 4, 8, 8, 2]; 

SET OF STRING classificationDatasetNamesC := ['continious_ecoliDS',
                                                'continious_glassDS',
                                                'continious_ionosphereDS',
                                                'continious_ringnormDataDS',
                                                'continious_segmentationDS', 
                                                'continious_waveformDS'
                                                ];   
                                               
SET OF STRING regressionDatasetNames := ['AbaloneDS', 'friedman1DS', 'friedman2DS', 'friedman3DS', 'housingDS', 'servoDS'];                                                                                
                                        

timeseriesDatasetNames := ['default', 'milk', 'barley', 'pigs', 'sheep', 'unemployed'];
ts_no_of_elements := COUNT(timeseriesDatasetNames);

INTEGER c_no_of_elementsD := COUNT(classificationDatasetNamesD);
INTEGER c_no_of_elementsC := COUNT(classificationDatasetNamesC);
INTEGER cluster_no_of_elements := COUNT(clusteringDatasetNames);
INTEGER r_no_of_elements := COUNT(regressionDatasetNames);


// rf_resultsC := GenerateCode('Classification.TestRandomForestClassificationC',  classificationDatasetNamesC, rfc_performance_scoresC, c_no_of_elementsC);
// rf_resultsD := GenerateCode('Classification.TestRandomForestClassificationD',  classificationDatasetNamesD, rfc_performance_scoresD, c_no_of_elementsD);
// dt_results := GenerateCode('Classification.TestDecisionTreeClassifier',  classificationDatasetNamesD, dtc_performance_scores, c_no_of_elementsD);
// kmeans_results := GenerateCode_K('Clustering.TestKmeans', clusteringDatasetNames, ClusterNumbers, km_performance_scores);
// lr_results := GenerateCode_R('Regression.TestLinearRegression', regressionDatasetNames);
IMPORT STD;
start_rfcc := ROUND((STD.date.CurrentTimestamp() + STD.date.LocalTimeZoneOffset())/1000);
action1 := OUTPUT(Utils.GenerateCode('Classification.TestRandomForestClassificationC',  classificationDatasetNamesC, BenchmarkResults.rfc_performance_scores_c, c_no_of_elementsC, repeat_no), NAMED('Classification_RandomForestC'));
action2 := OUTPUT(Utils.GenerateCode('Classification.TestRandomForestClassificationD',  classificationDatasetNamesD, BenchmarkResults.rfc_performance_scores_d, c_no_of_elementsD, repeat_no), NAMED('Classification_RandomForestD'));
action3 := OUTPUT(Utils.GenerateCode('Classification.TestDecisionTreeClassifier',  classificationDatasetNamesD, BenchmarkResults.dtc_performance_scores, c_no_of_elementsD, repeat_no), NAMED('Classification_DecisionTree'));
//action4 := OUTPUT(Utils.GenerateCode_K('Clustering.TestKmeans', clusteringDatasetNames, ClusterNumbers, BenchmarkResults.kmeans_performance_scores, repeat_no), NAMED('Clustering_KMeans'));
action5 := OUTPUT(Utils.GenerateCode_R('Regression.TestLinearRegression', regressionDatasetNames), NAMED('Regression_LR'));
action6 := OUTPUT(Utils.GenerateCodeTS('TimeSeries.TestArima', timeseriesDatasetNames), NAMED('ARIMA'));

SEQUENTIAL(
    action1,
    action2,
    action3,
    action4,
    action5,
    action6
);


                                                                              
                                        
