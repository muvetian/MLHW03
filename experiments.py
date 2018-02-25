import numpy as np
import pandas as pd
import os

def main():
    ag_frame = aggregate_all()
    #
    # for i in range(bic_man.shape[0]):
    #     bic_man.loc[i]["filename"]

def get_data_path(index,categories):
    data_dir = os.getcwd()+'/data/'+categories[index]+'/'
    return data_dir
def get_man_path(index,categories):
    man_dir = os.getcwd()+'/data/'+categories[index]+'/MANIFEST.txt'
    return man_dir
def aggregate_all():
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
            bic_list.append(patient)
    bic_frame = pd.concat(bic_list, ignore_index=True)
    bic_frame["type"] = 0
    print bic_frame.shape

    #Aggregating all the files under KidneyRenalClearCellCarcinoma category
    krccc_path = os.getcwd()+'/data/'
    krccc_frame = pd.DataFrame()
    krccc_list = []
    for file_ in range(krccc_man.shape[0]):
        path = get_data_path("krccc",categories) + krccc_man.loc[file_]["filename"]
        patient = pd.read_csv(get_data_path("krccc",categories) + krccc_man.loc[file_]["filename"],
        sep = '\t', index_col = None, header = 0)
        if "annotations.txt" not in path:
            krccc_list.append(patient)
    krccc_frame = pd.concat(krccc_list, ignore_index=True)
    krccc_frame["type"] = 1
    print krccc_frame.shape

    #Aggregating all the files under LungAdenocarcinoma category
    la_path = os.getcwd()+'/data/'
    la_frame = pd.DataFrame()
    la_list = []
    for file_ in range(la_man.shape[0]):
        path = get_data_path("la",categories) + la_man.loc[file_]["filename"]
        patient = pd.read_csv(get_data_path("la",categories) + la_man.loc[file_]["filename"],
        sep = '\t', index_col = None, header = 0)
        if "annotations.txt" not in path:
            la_list.append(patient)
    la_frame = pd.concat(la_list, ignore_index=True)
    la_frame["type"] = 2
    print la_frame.shape

    #Aggregating all the files under LungSquamousCellCarcinoma category
    lscc_path = os.getcwd()+'/data/'
    lscc_frame = pd.DataFrame()
    lscc_list = []
    for file_ in range(lscc_man.shape[0]):
        patient = pd.read_csv(get_data_path("lscc",categories) + lscc_man.loc[file_]["filename"],
        sep = '\t', index_col = None, header = 0)
        if "annotations.txt" not in get_data_path("lscc",categories) + lscc_man.loc[file_]["filename"]:
            lscc_list.append(patient)
    lscc_frame = pd.concat(lscc_list, ignore_index=True)
    lscc_frame["type"] = 3
    print lscc_frame.shape

    #Aggregating all the files under PancreaticAdenocarcinoma category
    pa_path = os.getcwd()+'/data/'
    pa_frame = pd.DataFrame()
    pa_list = []
    for file_ in range(pa_man.shape[0]):
        patient = pd.read_csv(get_data_path("pa",categories) + pa_man.loc[file_]["filename"],
        sep = '\t', index_col = None, header = 0)
        if "annotations.txt" not in get_data_path("pa",categories) + pa_man.loc[file_]["filename"]:
            pa_list.append(patient)
    pa_frame = pd.concat(pa_list, ignore_index=True)
    pa_frame["type"] = 4
    print pa_frame.shape

    #Aggregating all the files under UvealMelanoma category
    um_path = os.getcwd()+'/data/'
    um_frame = pd.DataFrame()
    um_list = []
    for file_ in range(um_man.shape[0]):
        patient = pd.read_csv(get_data_path("um",categories) + um_man.loc[file_]["filename"],
        sep = '\t', index_col = None, header = 0)
        if "annotations.txt" not in get_data_path("um",categories) + um_man.loc[file_]["filename"]:
            um_list.append(patient)
    um_frame = pd.concat(um_list, ignore_index=True)
    um_frame["type"] = 5
    print um_frame.shape

    aggregate_list = []
    aggregate_list.append(bic_frame)
    aggregate_list.append(krccc_frame)
    aggregate_list.append(la_frame)
    aggregate_list.append(lscc_frame)
    aggregate_list.append(pa_frame)
    aggregate_list.append(um_frame)
    ag_frame = pd.concat(aggregate_list, ignore_index=True)
    return ag_frame

if __name__ == "__main__":
    main()
