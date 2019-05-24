# Cytometric fingerprints of gut microbiota predict Crohn's disease state

This repository accompanies the manscript "*Cytometric fingerprints of gut microbiota predict Crohn's disease state*" by P. Rubbens, R. Props, F.-M. Kerckhof, N. Boon and W. Waegeman. Biorxiv ID: []().

## Abstract: 
Variations in the gut microbiome have been associated with changes in health state such as Crohn's disease. Most surveys characterize the microbiome through analysis of the 16S rRNA gene. An alternative technology that can be used is flow cytometry. In this report we analyzed a disease cohort that have been characterized by both technologies. Changes in microbial community structure are reflected in both types of data. We demonstrate that cytometric fingerprints can be used as a diagnostic tool in order to classify samples according to Crohn's disease state. These results highlight the potential of flow cytometry to perform rapid diagnostics of microbiome-associated diseases. 


## Jupyter notebooks: 

### Workflow: Prediction of Crohn's Disease state
Two jupyter notebooks are provided. The first shows how to derive cytometric fingerprints to predict the label of a randomly selected pair of samples (one 'CD' and one 'HC') that make up the test set. The results in the manuscript are the aggregation of 29 randomly selected pairs, in such a way that each 'CD'-sample is chosen once. The parameter `index_pair` determines this pair, and can be set from 0, ..., 28. 
- [CD_vs_HC_prediction_analysis.ipynb](https://github.com/prubbens/PhenoGMM_CD/blob/master/CD_vs_HC_prediction_analysis.ipynb). 

The results in the manuscript are the aggregation of 10 times running the workflow for all `index_pair's. They can be accessed in the [Results](https://github.com/prubbens/PhenoGMM_CD/tree/master/Results) folder. To plot the ROC-curves, run the script [plot_Fig1AB_ROCcurves.py](https://github.com/prubbens/PhenoGMM_CD/blob/master/plot_Fig1AB_ROCcurves.py). 
To plot the resulting AUROC-values, run the script [plot_Fig1C_AUCtest.py](https://github.com/prubbens/PhenoGMM_CD/blob/master/plot_Fig1C_AUCtest.py). 

### Workflow: Differences in within-sample diversity in function of Crohn's disease state 
The second jupyter notebook can be use to determine the *cytometric* diversity (based on flow cytometry data) and the *taxonomic* diversity, based on 16S rRNA gene sequencing data. Running the notebook will assess the statistical correspondence between the cytometric and taxonomic diversity, and assess the null hypothesis that the diversity of communitie diagnosed with Crohn's disease belong to the same population as those that belong to the Healthy Control group. 
- [https://github.com/prubbens/PhenoGMM_CD/blob/master/CD_vs_HC_diversity_analysis.ipynb](https://github.com/prubbens/PhenoGMM_CD/blob/master/CD_vs_HC_diversity_analysis.ipynb)

### Requirements to run notebooks: 
- Python 3
- Numpy
- Pandas
- Scikit-Learn
- Scipy
- Seaborn
- Statsmodels

### Data availability: 
All data is available on this repository. 
  - Denoised FCM data in `CSV`-format can be found in the folder [QC_flowAI_CSV](https://github.com/prubbens/PhenoGMM_CD/tree/master/QC_flowAI_CSV). Data was cleaned by means of the [flowAI](https://academic.oup.com/bioinformatics/article/32/16/2473/2240408) package. 
  - Preprocessed FCM data in `FCS`-format can be found on FlowRepository (ID:FR-FCM-ZYVH). 
  - Genus abundances can be found in the folder [Genus_tables](https://github.com/prubbens/PhenoGMM_CD/tree/master/Genus_tables). It's also available as Supporting Information to the original publication by [Vandeputte et al., (2017)](https://www.nature.com/articles/nature24460). 
  
### A note on the background removal: 
We carefully gated our data. An [illustration](https://github.com/prubbens/PhenoGMM_CD/blob/master/Gating/gating_strat_1_truecomm.pdf) of the gating template can be found here, an explanation with illustrations can be found in the folder [Gating](https://github.com/prubbens/PhenoGMM_CD/tree/master/Gating). 
