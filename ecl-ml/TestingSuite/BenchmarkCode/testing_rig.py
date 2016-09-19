import pandas as pd
import numpy as np
import sys, time


def test_linear_regression(filename):
    start_time = time.time()
    coeffs = []
    rss = []
    from sklearn import datasets, linear_model
    df = pd.read_csv(filename)
    h_indep = [d for d in df.columns if "A" in d]
    h_dep = [d for d in df.columns if "A" not in d]
    for _ in xrange(10):
        print "- ",
        sys.stdout.flush()
        msk = np.random.rand(len(df)) < 0.5
        train_data = df[msk]
        test_data = df[msk]

        assert(len(train_data) == len(test_data)), "Something is wrong"

        train_indep = train_data[h_indep]
        train_dep = train_data[h_dep]

        test_indep = test_data[h_indep]
        test_dep = test_data[h_dep]

        regr = linear_model.LinearRegression()
        regr.fit(train_indep, train_dep)

        coeffs.append(regr.coef_)

        rss.append(np.mean((regr.predict(test_indep) - test_dep) ** 2))

    extract_name = filename.split("/")[-1].split(".")[0] + ".p"
    import pickle
    pickle.dump(coeffs, open("./Results_Linear_Regression/coeffs_" + extract_name, "wb"))
    pickle.dump(rss, open("./Results_Linear_Regression/rss_" + extract_name, "wb"))
    print
    print "Total Time: ", time.time() - start_time


def _test_linear_regression():
    folder_name = "./RData/"
    from os import listdir
    files = sorted([folder_name + file for file in listdir(folder_name)])
    for file in files:
        print file
        test_linear_regression(file)


def test_logistic_regression(filename):
    start_time = time.time()
    coeffs = []
    acc = []
    from sklearn import datasets, linear_model
    df = pd.read_csv(filename)
    h_indep = [d for d in df.columns if "A" in d]
    h_dep = [d for d in df.columns if "A" not in d]
    for _ in xrange(10):
        print "- ",
        sys.stdout.flush()
        msk = np.random.rand(len(df)) < 0.5
        train_data = df[msk]
        test_data = df[msk]

        assert (len(train_data) == len(test_data)), "Something is wrong"

        train_indep = train_data[h_indep]
        train_dep = train_data[h_dep]

        test_indep = test_data[h_indep]
        test_dep = test_data[h_dep]
        logistic = linear_model.LogisticRegression()
        logistic.fit(train_indep, [i[-1] for i in train_dep.values.tolist()])
        coeffs.append(logistic.coef_)
        acc.append(logistic.score(X=test_indep, y=[i[-1] for i in test_dep.values.tolist()]))

    extract_name = filename.split("/")[-1].split(".")[0] + ".p"
    import pickle
    pickle.dump(coeffs, open("./Results_Logistic_Regression/coeffs_" + extract_name, "wb"))
    pickle.dump(acc, open("./Results_Logistic_Regression/rss_" + extract_name, "wb"))
    print
    print "Total Time: ", time.time() - start_time


def _test_logistic_regression(filename):
    folder_name = "./CData/"
    from os import listdir
    files = sorted([folder_name + file for file in listdir(folder_name)])
    for file in files:
        print file
        # file = "./CData/Classification_10000_32_2_50.0.csv"
        test_logistic_regression(file)


def test_random_forest_classification(filename):
    # start_time = time.time()
    accuracies = []
    from sklearn.ensemble import RandomForestClassifier
    df = pd.read_csv(filename)
    h_indep = df.columns[:-1]
    h_dep = df.columns[-1]
    for _ in xrange(10):
            print "- ",
            sys.stdout.flush()
            msk = np.random.rand(len(df)) < 0.4
            train_data = df[msk]
            test_data = df[~msk]

            assert (len(train_data) + len(test_data) == len(df)), "Something is wrong"

            train_indep = train_data[h_indep]
            train_dep = train_data[h_dep]

            test_indep = test_data[h_indep]
            test_dep = test_data[h_dep]
            rf = RandomForestClassifier(n_estimators=100,  max_features=min(7, len(train_indep.iloc[0])),  criterion='gini', max_depth=100)
            rf.fit(train_indep, [i for i in train_dep.values.tolist()])
            prediction = rf.predict(test_indep)
            from sklearn.metrics import accuracy_score
            accuracies.append(accuracy_score(test_dep, prediction))

    return np.mean(accuracies)


def _test_random_forest_classification():
    """ Storing the confusion Matrix for classification Tasks"""
    folder_name = "./ML/ClassificationData/"
    from os import listdir
    files = sorted([folder_name + file for file in listdir(folder_name) if "csv" in file])
    for file in files:
        print file, " : ",
        print test_random_forest_classification(file)


def test_kmeans(filename):
    stripped_name = filename.split("/")[-1].split(".")[0]
    from sklearn.cluster import KMeans
    contents = stripped_name.split("_")
    no_clusters = int(contents[4].split(".")[0])
    confusion_matrices = []
    start_time = time.time()

    df = pd.read_csv(filename)
    h_indep = [d for d in df.columns if "features" in d]
    h_dep = [d for d in df.columns if "class" in d]
    for _ in xrange(10):
        try:
            print "- ",
            sys.stdout.flush()

            indep = df[h_indep]
            dep = df[h_dep]

            kmeans = KMeans(n_clusters =no_clusters)
            kmeans.fit(indep)
            print kmeans.inertia_
            import pdb
            pdb.set_trace()
        except:
            import traceback
            traceback.extract_stack()


    import pickle
    pickle.dump(confusion_matrices, open("./Results_K_Means/Kmeans_" + extract_name, "wb"))
    print " Total Time: ", time.time() - start_time


def _test_kmeans():
    folder_name = "./ML/ClusteringData/"
    from os import listdir

    files = sorted([folder_name + file for file in listdir(folder_name) if "csv" in file])
    for file in files:
        print file, " : ",
        print test_kmeans(file)

def test_decision_tree_classification(filename):
    start_time = time.time()
    accuracy = []
    from sklearn.tree import DecisionTreeClassifier
    df = pd.read_csv(filename)
    h_indep = df.columns[:-1]
    h_dep = df.columns[-1]
    for _ in xrange(10):
            # print "- ",
            sys.stdout.flush()
            msk = np.random.rand(len(df)) < 0.4
            train_data = df[msk]
            test_data = df[~msk]

            # print len(train_data), len(test_data)
            assert (len(train_data) + len(test_data) == len(df)), "Something is wrong"
            train_indep = train_data[h_indep]
            train_dep = train_data[h_dep]

            test_indep = test_data[h_indep]
            test_dep = test_data[h_dep]
            dt = DecisionTreeClassifier()
            dt.fit(train_indep, [i for i in train_dep.values.tolist()])
            prediction = dt.predict(test_indep)
            from sklearn.metrics import accuracy_score
            # print confusion_matrix(test_dep, prediction)

            if len(set(test_dep)) > 2:
                accuracy.append(accuracy_score(test_dep, prediction))
            else:
                accuracy.append(accuracy_score(test_dep, prediction))
                # print len(confusion_matrices),
            # print len(confusion_matrices),

    print accuracy


def _test_decision_tree_classification():
    """ Storing the confusion Matrix for classification Tasks"""
    folder_name = "./ML/ClassificationData/"
    from os import listdir
    files = sorted([folder_name + file for file in listdir(folder_name) if "csv" in file])
    for file in files:
        print file,
        test_decision_tree_classification(file)

if __name__ == "__main__":
    _test_decision_tree_classification()
    # _test_kmeans()
    # _test_random_forest_classification()
    # folder_name = "./Cluster_Data/"
    # from os import listdir
    # files = sorted([folder_name + file for file in listdir(folder_name)])


