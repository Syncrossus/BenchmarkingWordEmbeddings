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
        if models == []:
            print("Missing model argument(s), proceeding with all embeddings")
            models = all_models
        if datasets == []:
            print("Missing dataset argument(s), proceeding with all datasets")
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
                correlation = model.wv.evaluate_word_pairs(pairs=NEW_CSV_DIR + dataset, delimiter=',', case_insensitive=True)
                avgCorrelation = (correlation[0][0] + correlation[1][0]) / 2
                print("   ", dataset, ':', avgCorrelation, "correlation between model and human evaluation")
            else:
                accuracy = model.wv.accuracy(RAW_CSV_DIR + dataset)
                sum_correct = len(accuracy[-1]['correct'])
                total = sum_correct + len(accuracy[-1]['incorrect'])
                print("   ", dataset, ':', sum_correct / total * 100, "% correct")


if __name__ == '__main__':
    main(sys.argv)
