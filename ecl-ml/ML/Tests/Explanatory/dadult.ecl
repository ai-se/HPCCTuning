IMPORT ML;
EXPORT dadult:= MODULE
    cTypeRecord := RECORD
        INTEGER field1;
        INTEGER field2;
        INTEGER field3;
        INTEGER field4;
        INTEGER field5;
        INTEGER field6;
        INTEGER field7;
        INTEGER field8;
        INTEGER field9;
        INTEGER field10;
        INTEGER field11;
        INTEGER field12;
        INTEGER field13;
        INTEGER field14;
        INTEGER class;
    END;

    ctype := RECORD
       INTEGER id;
       cTypeRecord;
    END;
    sensorDS:= DATASET('~vivek::pt::dadult.csv', cTypeRecord, CSV);
    SHARED DS:= PROJECT(sensorDS, TRANSFORM(cType, SELF.id:=COUNTER, SELF:= LEFT));
    SHARED number_of_records := COUNT(DS);
    EXPORT Training := DS(id < 0.4 * number_of_records);
    EXPORT Tuning := DS(0.4 * number_of_records <= id AND id <0.6 * number_of_records);
    EXPORT Testing := DS(0.6 * number_of_records < id);
END;