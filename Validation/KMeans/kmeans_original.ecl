IMPORT * FROM ML;
IMPORT * FROM ML.Cluster;
IMPORT * FROM ML.Types;

layout_data := RECORD
  INTEGER id;
	DECIMAL a;
	DECIMAL b;
	DECIMAL c;
	DECIMAL d;
	DECIMAL e;
	DECIMAL f;
	DECIMAL g;
END;

refined_data := RECORD
	DECIMAL a;
	DECIMAL b;
	DECIMAL c;
	DECIMAL d;
	DECIMAL e;
	DECIMAL f;
	DECIMAL g;
END;

refined_data remove_id(layout_data l) := TRANSFORM
	SELF.a := l.a;
	SELF.b := l.b;
	SELF.c := l.c;
	SELF.d := l.d;
	SELF.e := l.e;
	SELF.f := l.f;
	SELF.g := l.g;
END;

raw_data := DATASET('~testing', layout_data, csv(separator(',')));
// SET OF INTEGER raw_datapoints := [3,4,2,45,23,34,12,9,10,11];
SET OF INTEGER raw_centroids := [3, 45, 2];

// clean_data := PROJECT(raw_data(id IN raw_datapoints), remove_id(LEFT));
centroid := PROJECT(raw_data(id IN raw_centroids), remove_id(LEFT));

ML.ToField(raw_data, d);
ML.ToField(centroid, c);

x3 := Kmeans(d, c);

OUTPUT(x3.convergence);