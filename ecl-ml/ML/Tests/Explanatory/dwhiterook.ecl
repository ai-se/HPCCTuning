IMPORT ML;
EXPORT dwhiterook:= MODULE
    cTypeRecord := RECORD
        INTEGER field1;
        INTEGER field2;
        INTEGER field3;
        INTEGER field4;
        INTEGER field5;
        INTEGER field6;
        INTEGER class;
    END;

    ctype := RECORD
       INTEGER id;
       cTypeRecord;
    END;
    sensorDS:= DATASET('~vivek::pt::dwhiterook.csv', cTypeRecord, CSV);
    SHARED DS:= PROJECT(sensorDS, TRANSFORM(cType, SELF.id:=COUNTER, SELF:= LEFT));
    SHARED number_of_records := COUNT(DS);
    EXPORT Training := DS(id < 0.4 * number_of_records);
    EXPORT Tuning := DS(0.4 * number_of_records <= id AND id <0.6 * number_of_records);
    EXPORT Testing := DS(0.6 * number_of_records < id);
END;