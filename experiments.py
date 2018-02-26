import numpy as np
import pandas as pd
import os
from sklearn import linear_model
from sklearn import preprocessing
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
def main():
    # ag_frame = save_aggregate_all()
    df = load_pkl()
    train_set = df.loc[1:2315]
    train_feat = train_set.drop(columns=['type'])
    # processing train set
    X_train = preprocessing.Imputer().fit_transform(train_feat)
    train_target_p=preprocessing.Imputer().fit_transform([train_set['type']])
    print train_target_p
    y_train = np.reshape(train_target_p, (-1, 1))
    print y_train

    # processing test set
    test_set = df.loc[2315:df.shape[0]]
    test_feat = train_set.drop(columns=['type'])
    X_test = preprocessing.Imputer().fit_transform(train_feat)
    test_target_p=preprocessing.Imputer().fit_transform([test_set['type']])
    y_test = np.reshape(train_target_p, (-1, 1))

    print SGDclassifier(X_train,y_train,X_test,y_test)
    # print X_train
    # X_imputed=preprocessing.Imputer().fit_transform(X_train)
    # for i in range(train_set.shape[0]-1):
    #     try:
    #         float(train_set.loc[i+1])
    #     except:
    #         print "error", "on row",i

    # print train_set


    # train_feat = train_set.columns.drop('type')
    # train_target = train_set['type']




    # aggregate_test()
    #
    # for i in range(bic_man.shape[0]):
    #     bic_man.loc[i]["filename"]
def SGDclassifier(X_train,y_train,X_test,y_test):
    clf = linear_model.SGDClassifier()
    clf.fit(X_train, y_train)
    counter = 0
    y_true = []
    y_pred = []

    for i in range(X_test.shape[0]):
        true = y_test[i]
        predict = clf.predict([X_test[i]])
        y_true.append(true)
        y_pred.append(predict)
    precision = precision_score(y_true, y_pred, average='weighted')
    recall = recall_score(y_true, y_pred, average='weighted')
    f1 = f1_score(y_true, y_pred, average='weighted')
    return [precision,recall,f1]

def load_pkl():
    df = pd.read_pickle("aggregate.pkl")
    return df
def get_data_path(index,categories):
    data_dir = os.getcwd()+'/data/'+categories[index]+'/'
    return data_dir
def get_man_path(index,categories):
    man_dir = os.getcwd()+'/data/'+categories[index]+'/MANIFEST.txt'
    return man_dir
def aggregate_test():
    man_dir = os.getcwd()+'/data/Uveal\ Melanoma/MANIFEST.csv'
    categories = {
		 "bic": "BreastInvasiveCarcinoma",
		 "krccc": "KidneyRenalClearCellCarcinoma",
		 "la": "LungAdenocarcinoma",
		 "lscc": "LungSquamousCellCarcinoma" ,
		 "pa": "PancreaticAdenocarcinoma",
		 "um" : "UvealMelanoma"
	}
    um_man = pd.read_csv(get_man_path("um",categories),sep = '\t')
    #Aggregating all the files under UvealMelanoma category
    um_path = os.getcwd()+'/data/'
    um_frame = pd.DataFrame()
    um_list = []
    for file_ in range(um_man.shape[0]):
        patient = pd.read_csv(get_data_path("um",categories) + um_man.loc[file_]["filename"],
        sep = '\t', index_col = None, header = 0)
        patient.drop(['read_count','cross-mapped'],1, inplace=True)
        patient.set_index('miRNA_ID',inplace=True)
        patient_trans = patient.transpose()
        if "annotations.txt" not in get_data_path("um",categories) + um_man.loc[file_]["filename"]:
            um_list.append(patient_trans)
    um_frame = pd.concat(um_list, ignore_index=True)
    um_frame["type"] = 5
    print um_frame
    # printum_frame
def save_aggregate_all():
    man_dir = os.getcwd()+'/data/Uveal\ Melanoma/MANIFEST.csv'
    categories = {
		 "bic": "BreastInvasiveCarcinoma",
		 "krccc": "KidneyRenalClearCellCarcinoma",
		 "la": "LungAdenocarcinoma",
		 "lscc": "LungSquamousCellCarcinoma" ,
		 "pa": "PancreaticAdenocarcinoma",
		 "um" : "UvealMelanoma"
	}
    bic_man = pd.read_csv(get_man_path("bic",categories),sep = '\t')
    krccc_man = pd.read_csv(get_man_path("krccc",categories),sep = '\t')
    la_man = pd.read_csv(get_man_path("la",categories),sep = '\t')
    lscc_man = pd.read_csv(get_man_path("lscc",categories),sep = '\t')
    pa_man = pd.read_csv(get_man_path("pa",categories),sep = '\t')
    um_man = pd.read_csv(get_man_path("um",categories),sep = '\t')


    #Aggregating all the files under BreastInvasiveCarcinoma category
    bic_path = os.getcwd()+'/data/'
    bic_frame = pd.DataFrame()
    bic_list = []
    for file_ in range(bic_man.shape[0]):
        path = get_data_path("bic",categories) + bic_man.loc[file_]["filename"]
        patient = pd.read_csv(get_data_path("bic",categories) + bic_man.loc[file_]["filename"],
        sep = '\t', index_col = None, header = 0)
        if "annotations.txt" not in path:
            patient.drop(['read_count','cross-mapped'],1, inplace=True)
            patient.set_index('miRNA_ID',inplace=True)
            patient_trans = patient.transpose()
            bic_list.append(patient_trans)
    bic_frame = pd.concat(bic_list, ignore_index=True)
    bic_frame["type"] = 0


    #Aggregating all the files under KidneyRenalClearCellCarcinoma category
    krccc_path = os.getcwd()+'/data/'
    krccc_frame = pd.DataFrame()
    krccc_list = []
    for file_ in range(krccc_man.shape[0]):
        path = get_data_path("krccc",categories) + krccc_man.loc[file_]["filename"]
        patient = pd.read_csv(get_data_path("krccc",categories) + krccc_man.loc[file_]["filename"],
        sep = '\t', index_col = None, header = 0)

        if "annotations.txt" not in path:
            patient.drop(['read_count','cross-mapped'],1, inplace=True)
            patient.set_index('miRNA_ID',inplace=True)
            patient_trans = patient.transpose()
            krccc_list.append(patient_trans)
    krccc_frame = pd.concat(krccc_list, ignore_index=True)
    krccc_frame["type"] = 1


    #Aggregating all the files under LungAdenocarcinoma category
    la_path = os.getcwd()+'/data/'
    la_frame = pd.DataFrame()
    la_list = []
    for file_ in range(la_man.shape[0]):
        path = get_data_path("la",categories) + la_man.loc[file_]["filename"]
        patient = pd.read_csv(get_data_path("la",categories) + la_man.loc[file_]["filename"],
        sep = '\t', index_col = None, header = 0)

        if "annotations.txt" not in path:
            patient.drop(['read_count','cross-mapped'],1, inplace=True)
            patient.set_index('miRNA_ID',inplace=True)
            patient_trans = patient.transpose()
            la_list.append(patient_trans)
    la_frame = pd.concat(la_list, ignore_index=True)
    la_frame["type"] = 2


    #Aggregating all the files under LungSquamousCellCarcinoma category
    lscc_path = os.getcwd()+'/data/'
    lscc_frame = pd.DataFrame()
    lscc_list = []
    for file_ in range(lscc_man.shape[0]):
        patient = pd.read_csv(get_data_path("lscc",categories) + lscc_man.loc[file_]["filename"],
        sep = '\t', index_col = None, header = 0)

        if "annotations.txt" not in get_data_path("lscc",categories) + lscc_man.loc[file_]["filename"]:
            patient.drop(['read_count','cross-mapped'],1, inplace=True)
            patient.set_index('miRNA_ID',inplace=True)
            patient_trans = patient.transpose()
            lscc_list.append(patient_trans)
    lscc_frame = pd.concat(lscc_list, ignore_index=True)
    lscc_frame["type"] = 3


    #Aggregating all the files under PancreaticAdenocarcinoma category
    pa_path = os.getcwd()+'/data/'
    pa_frame = pd.DataFrame()
    pa_list = []
    for file_ in range(pa_man.shape[0]):
        patient = pd.read_csv(get_data_path("pa",categories) + pa_man.loc[file_]["filename"],
        sep = '\t', index_col = None, header = 0)

        if "annotations.txt" not in get_data_path("pa",categories) + pa_man.loc[file_]["filename"]:
            patient.drop(['read_count','cross-mapped'],1, inplace=True)
            patient.set_index('miRNA_ID',inplace=True)
            patient_trans = patient.transpose()
            pa_list.append(patient_trans)
    pa_frame = pd.concat(pa_list, ignore_index=True)
    pa_frame["type"] = 4


    #Aggregating all the files under UvealMelanoma category
    um_path = os.getcwd()+'/data/'
    um_frame = pd.DataFrame()
    um_list = []
    for file_ in range(um_man.shape[0]):
        patient = pd.read_csv(get_data_path("um",categories) + um_man.loc[file_]["filename"],
        sep = '\t', index_col = None, header = 0)
        if "annotations.txt" not in get_data_path("um",categories) + um_man.loc[file_]["filename"]:
            patient.drop(['read_count','cross-mapped'],1, inplace=True)
            patient.set_index('miRNA_ID',inplace=True)
            patient_trans = patient.transpose()
            um_list.append(patient_trans)
    um_frame = pd.concat(um_list, ignore_index=True)
    um_frame["type"] = 5


    aggregate_list = []
    aggregate_list.append(bic_frame)
    aggregate_list.append(krccc_frame)
    aggregate_list.append(la_frame)
    aggregate_list.append(lscc_frame)
    aggregate_list.append(pa_frame)
    aggregate_list.append(um_frame)
    ag_frame = pd.concat(aggregate_list, ignore_index=True)
    ag_frame = ag_frame.sample(frac=1).reset_index(drop=True)
    ag_frame.to_pickle("aggregate.pkl")
    return ag_frame

if __name__ == "__main__":
    main()
