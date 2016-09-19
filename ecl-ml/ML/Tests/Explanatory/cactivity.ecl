// Localization Data for Person Activity Data Set (https://archive.ics.uci.edu/ml/datasets/Localization+Data+for+Person+Activity)
IMPORT ML;
EXPORT cactivity:= MODULE
    cTypeRecord := RECORD
        INTEGER field1;
        INTEGER field2;
        REAL field3;
        REAL field4;
        REAL field5;
        INTEGER class;
    END;

    ctype := RECORD
       INTEGER id;
       cTypeRecord;
    END;
    sensorDS:= DATASET('~vivek::pt::sensordata.csv', cTypeRecord, CSV);
    SHARED DS:= PROJECT(sensorDS, TRANSFORM(cType, SELF.id:=COUNTER, SELF:= LEFT));
    SHARED number_of_records := COUNT(DS);
    EXPORT Training := DS(id < 0.4 * number_of_records);
    EXPORT Tuning := DS(0.4 * number_of_records <= id AND id <0.6 * number_of_records);
    EXPORT Testing := DS(0.6 * number_of_records < id);
END;