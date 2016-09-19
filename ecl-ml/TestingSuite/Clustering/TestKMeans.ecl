IMPORT Std;
IMPORT ML;
IMPORT ML.Tests.Explanatory as TE;
IMPORT ML.Types;
IMPORT TestingSuite.Utils AS Utils;
IMPORT TestingSuite.Clustering as Clustering;

TestKMeans(raw_dataset_name, repeats, no_clusters) := FUNCTIONMACRO
        AnyDataSet :=  raw_dataset_name;
 
        RunKMeans(DATASET(Types.NumericField) dDocuments, DATASET(Types.NumericField) dCentroids):= FUNCTION
                learner := ML.Cluster.KMeans(dDocuments,dCentroids, 100);  
                result := learner.Allegiances();
                RETURN SUM(result, value);
        END;
                

        
        WrapperRunKmeansClusterer(DATASET(RECORDOF(AnyDataSet)) AnyDataSet, number_of_clusters):= FUNCTION
                raw_dCentroidMatrix := DATASET(number_of_clusters, TRANSFORM(
                                                        RECORDOF(AnyDataSet), 
                                                        SELF := AnyDataSet[RANDOM() % COUNT(AnyDataSet)]));
                t := OUTPUT(raw_dCentroidMatrix);
                Utils.ToTraining(AnyDataSet, dDocumentMatrix);
                Utils.ToTraining(raw_dCentroidMatrix, dCentroidMatrix);                                                     
                                                       
                ML.ToField(dDocumentMatrix,dDocuments);
                ML.ToField(dCentroidMatrix,dCentroids);
                accuracy := RunKMeans(dDocuments, dCentroids);   
                RETURN WHEN(accuracy, t);    
        END; 
        
        IMPORT Std;

        results := DATASET(#EXPAND(repeats),
                                        TRANSFORM(TestingSuite.Utils.Types.result_rec,
                                        SELF.dataset_id := COUNTER; // Since this information is never used. The variable name in this case doesn't mean anything.
                                        SELF.scores := WrapperRunKmeansClusterer(raw_dataset_name, no_clusters);
                                        ));
        
        RETURN results; 
ENDMACRO;


TestKMeans(Clustering.Datasets.ionek_f_two_c_twoDS.content, 1, 2);

