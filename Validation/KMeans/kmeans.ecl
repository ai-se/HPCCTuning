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
// SET OF INTEGER raw_datapoints := [
SET OF INTEGER raw_centroids := [126,298];
// clean_data := PROJECT(raw_data(id IN raw_datapoints), remove_id(LEFT));
centroid := PROJECT(raw_data(id IN raw_centroids), remove_id(LEFT));

ML.ToField(raw_data, d);
ML.ToField(centroid, c);

x3 := Kmeans(d,c,79,0.01);

OUTPUT(x3.convergence);