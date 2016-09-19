IMPORT Std;
IMPORT TS;
IMPORT * FROM TS.Types;
IMPORT * FROM TestingSuite.Utils;
IMPORT TestingSuite.Regression as Regression;
  

EXPORT TestArima(raw_dataset_name, params) := FUNCTIONMACRO
        AnyDataSet := raw_dataset_name;        

        RunArima(SET OF REAL AnyDataSet, SET OF REAL params) := FUNCTION     
                my_time_series:= AnyDataSet;
                ts_0 := DATASET(my_time_series, {TS.Types.t_value dependent});
                
                TS.Types.UniObservation enum_recs(RECORDOF(ts_0) lr, UNSIGNED cnt) := TRANSFORM
                                  SELF.period := cnt;
                                  SELF.dependent := lr.dependent;
                                END;
                                
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
                
                ts_1 := PROJECT(ts_0, enum_recs(LEFT, COUNTER));
                pdq_parms := params;
                want_const := TRUE;
                
                model_spec := DATASET([{1, pdq_parms[2], pdq_parms[1], pdq_parms[3], want_const}], TS.Types.Model_Spec);
                model_parms := TS.Estimation(ts_1, model_spec, 100);
                scored := TS.Diagnosis(ts_1, model_parms);
                
                RETURN scored[1].s_measure;
        END;

        RETURN RunArima(AnyDataSet, params);
ENDMACRO;
// TestArima(