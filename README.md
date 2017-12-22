# BenchmarkingWordEmbeddings
## Français
Exécuter le script : Ouvrez une console dans le répertoire du projet et lancez `python main.py [modele] [dataset]`. Vous pouvez renseigner les modèles que vous voulez évaluer ainsi que les datasets que vous voulez utiliser dans l'évaluation.
Les modèles disponibles sont : `GoogleNews-vectors-negative300.bin`, `text8` et `glove.840B.300d.txt`. Les datasets disponibles sont `cos_matrix_brm_IFR.csv`, `UMNSRS_relatedness.csv`, `UMNSRS_similarity.csv`, `synonymy.csv`, `relatedness.csv`, et `google_questions-words.txt`. Tout argument ne correspondant pas exactement à une de ces options sera ignoré. Si aucun modèle (resp. dataset) n'est passé en argument, tous les modèles (resp. datasets) seront utilisés.
Pour lancer le script, il est conseillé d'avoir au moins 16Go de mémoire voire 24. Cette mémoire peut être partiellement constituée de mémoire virtuelle (_swap_ ou _pagefile_). Si vous pensez ne pas avoir suffisamment de mémoire, vous pouvez augmenter votre mémoire virtuelle en suivant un de ces tutoriels pour [Windows](https://www.online-tech-tips.com/computer-tips/simple-ways-to-increase-your-computers-performace-configuring-the-paging-file/) ou [Linux](https://www.linux.com/learn/increase-your-available-swap-space-swap-file). Vous pouvez également renoncer à évaluer les modèles GloVe et / ou Google News, puisque ce sont ceux qui sont particulièrement consommateurs en ressources.

## English
Running the script : Open a console in the directory of the project and run `python main.py [model] [dataset]`. You may specify which models you would like to benchmark as well as which datasets you would like to use in the benchmark.
The available models are : `GoogleNews-vectors-negative300.bin`, `text8` and `glove.840B.300d.txt`. The available datasets are `cos_matrix_brm_IFR.csv`, `UMNSRS_relatedness.csv`, `UMNSRS_similarity.csv`, `synonymy.csv`, `relatedness.csv`, and `google_questions-words.txt`. Any argument that does not exactly correspond to one of these options will be ignored. If no model and / or no dataset is passed as argument, all models and / or datasets will be used.
To run this script, it is recommended to have at least 16 and preferably 24 GB of available memory. This may include virtual memory (_swap_ or _pagefile_). If you believe you may not have enough memory, you may increase the amount of virtual memory by following a tutorial for [Windows](https://www.online-tech-tips.com/computer-tips/simple-ways-to-increase-your-computers-performace-configuring-the-paging-file/) or [Linux](https://www.linux.com/learn/increase-your-available-swap-space-swap-file). You may also relinquish the idea of evaluating the GloVe and / or Google News models, as they are particularly demanding in resources.