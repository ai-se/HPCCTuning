IMPORT Std;
IMPORT TS;
IMPORT * FROM ML.Types;
IMPORT * FROM TestingSuite.Utils;
IMPORT TestingSuite.Regression as Regression;


EXPORT TestRArima(datasetname, params, RResults):=FUNCTIONMACRO
        AnyDataSet := datasetname;
        my_time_series:= AnyDataSet;
        ts_0 := DATASET(my_time_series, {TS.Types.t_value dependent});
        TS.Types.UniObservation enum_recs(RECORDOF(ts_0) lr, UNSIGNED cnt) := TRANSFORM
          SELF.period := cnt;
          SELF.dependent := lr.dependent;
        END;
        ts_1 := PROJECT(ts_0, enum_recs(LEFT, COUNTER));
        SET OF REAL8 r_model_set := RResults;
        r_model_out := DATASET(r_model_set, {REAL4 coeff});
        
        TS.Types.Co_efficient make_coef({TS.Types.t_value cv} lr, UNSIGNED cnt) := TRANSFORM
                                  SELF.cv := lr.cv;
                                  SELF.lag := cnt;
                                END;
                                
        TS.Types.Model_Parameters makeParms(SET OF UNSIGNED inp, SET OF REAL8 coeff, BOOLEAN want_const) := TRANSFORM
                          values := DATASET(coeff, {TS.Types.t_value cv});
                          SELF.model_id := 1;
                          SELF.degree := inp[2];
                          SELF.ar_terms := inp[1];
                          SELF.ma_terms := inp[3];
                          SELF.constant_term := want_const;
                          SELF.ar := PROJECT(values[1..inp[1]], make_coef(LEFT, COUNTER));
                          SELF.ma := PROJECT(values[1+inp[1]..inp[1]+inp[3]], make_coef(LEFT, COUNTER));
                          SELF.c := IF(want_const, coeff[1+inp[1]+inp[3]], 0.0);
                        END;               
        
        pdq_parms := params;
        want_const := TRUE;
        
        r_model := DATASET(1, makeParms(pdq_parms, r_model_set, want_const));
        r_scored := TS.Diagnosis(ts_1, r_model);
        RETURN r_scored[1].s_measure;
ENDMACRO;                
           