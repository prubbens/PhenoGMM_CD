# Cytometric fingerprints of gut microbiota predict Crohn's disease state

This repository accompanies the manscript "*Cytometric fingerprints of gut microbiota predict Crohn's disease state*" by P. Rubbens, R. Props, F.-M. Kerckhof, N. Boon and W. Waegeman. Biorxiv ID: []().

## Structure of repository: 

### Workflow: Prediction of Crohn's Disease state
Two jupyter notebooks are provided. The first shows how to derive cytometric fingerprints to predict the label of a randomly selected pair of samples (one 'CD' and one 'HC') that make up the test set. The results in the manuscript are the aggregation of 29 randomly selected pairs, in such a way that each 'CD'-sample is chosen once. The parameter `index_pair` determines this pair, and can be set from 0, ..., 28. 
- [CD_vs_HC_prediction_analysis.ipynb](https://github.com/prubbens/PhenoGMM_CD/blob/master/CD_vs_HC_prediction_analysis.ipynb). 

The results in the manuscript are the aggregation of 10 times running the workflow for all `index_pair's. They can be accessed in the [Results](https://github.com/prubbens/PhenoGMM_CD/tree/master/Results) folder. To plot the ROC-curves, run the script [plot_Fig1AB_ROCcurves.py](https://github.com/prubbens/PhenoGMM_CD/blob/master/plot_Fig1AB_ROCcurves.py). 
To plot the resulting AUROC-values, run the script [plot_Fig1C_AUCtest.py](https://github.com/prubbens/PhenoGMM_CD/blob/master/plot_Fig1C_AUCtest.py). 

