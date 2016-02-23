IMPORT * FROM ML;
IMPORT * FROM ML.Cluster;
IMPORT * FROM ML.Types;

layout_data := RECORD
  INTEGER id;DECIMAL2 a0;
DECIMAL2 b0;
DECIMAL2 c0;
DECIMAL2 d0;
DECIMAL2 e0;
DECIMAL2 f0;
DECIMAL2 g0;
END;

refined_data := RECORD 
DECIMAL2 a0;
DECIMAL2 b0;
DECIMAL2 c0;
DECIMAL2 d0;
DECIMAL2 e0;
DECIMAL2 f0;
DECIMAL2 g0;
END;

refined_data remove_id(layout_data l) := TRANSFORM
SELF.a0 := l.a0;
SELF.b0 := l.b0;
SELF.c0 := l.c0;
SELF.d0 := l.d0;
SELF.e0 := l.e0;
SELF.f0 := l.f0;
SELF.g0 := l.g0;
END;

raw_data := DATASET('~testing', layout_data, csv(separator(',')));
SET OF INTEGER raw_datapoints := [53,197,10,55,93,253,322,163,115,27,187,223,233,215,51,221,196,85,5,244,328,68,103,297,334,220,89,278,108,95,87,122,225,16,29,130,345,65,156,161,338,113,107,323,91,267,23,216,257,153,33,46,74,11,242,38,181,186,148,318,41,333,247,303,81,272,279,126,174];
SET OF INTEGER raw_centroids := [180];
clean_data := PROJECT(raw_data(id IN raw_datapoints), remove_id(LEFT));
centroid := PROJECT(raw_data(id IN raw_centroids), remove_id(LEFT));

ML.ToField(clean_data, d);
ML.ToField(centroid, c);

x3 := Kmeans(d,c,117,0.3);

OUTPUT(x3.convergence);