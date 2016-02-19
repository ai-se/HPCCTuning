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

raw_data := DATASET('~testing', layout_data, csv(separator(',')));
SET OF INTEGER raw_centroids := [3, 45, 2];
raw_centroid := raw_data(id IN raw_centroids);

refined_data remove_id(layout_data l) := TRANSFORM
	SELF.a := l.a;
	SELF.b := l.b;
	SELF.c := l.c;
	SELF.d := l.d;
	SELF.e := l.e;
	SELF.f := l.f;
	SELF.g := l.g;
END;

clean_data := PROJECT(raw_data, remove_id(LEFT));
centroid := PROJECT(raw_centroid, remove_id(LEFT));

ML.ToField(clean_data, d);
ML.ToField(centroid, c);

x3 := Kmeans(d, c);

OUTPUT(x3.convergence);