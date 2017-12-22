import sys
import os
import gc
from constants import *
from loadModels import *


def main(args):
    if not os.path.isdir(NEW_CSV_DIR):
        import formatDatasets
        formatDatasets.main()
    all_models = [TEXT8, GOOGLE_NEWS, GLOVE]
    all_datasets = [RELATEDNESS, SYNONYMY, UMNSRS_REL, UMNSRS_SIM, COS_BRM_CSV, GOOGLE_QST]
    if args is not None:
        models = [model for model in all_models if model in args]
        datasets = [dataset for dataset in all_datasets if dataset in args]
        if models == [] or datasets == []:
            print("Missing embeddings or datasets arguments, proceeding with all embeddings and datasets")
            models = all_models
            datasets = all_datasets
    else:
        models = all_models
        datasets = all_datasets

    for modelname in models:
        model = load(modelname)
        gc.collect()  # collecting previous model
        print(modelname, ':')
        for dataset in datasets:
            if dataset != GOOGLE_QST:
                print(dataset, ':', model.wv.evaluate_word_pairs(pairs=NEW_CSV_DIR + dataset, delimiter=',', case_insensitive=True))
            else:
                print(dataset, ':', model.wv.accuracy(RAW_CSV_DIR + dataset))


if __name__ == '__main__':
    main(sys.argv)
