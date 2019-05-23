#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  6 11:46:24 2018

@author: prubbens
"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import interp
from scipy.stats import ttest_rel
from sklearn.metrics import roc_auc_score, roc_curve, auc, precision_score, recall_score
from sklearn.preprocessing import LabelEncoder#, OneHotEncoder

df_fcm = pd.read_excel('Results/Proper_gating_LPO_PRED_probaStrat_test_GMM_RFR_CLASS_L400_asinh.xlsx', index_col=0, header=0)
df_16S = pd.read_excel('Results/16S_LPO_PRED_probaStrat_test_RFR_CLASS_L400.xlsx', index_col=0, header=0)

target = pd.read_csv('Metadata_DC.csv', index_col=0, header=0)
label_y = 'Health status'
le = LabelEncoder()
target.loc[:,label_y] = le.fit_transform(target.loc[:,label_y])
target.loc[:,label_y] = target.loc[:,label_y].replace({0:1, 1:0})
y_test = target.loc[df_fcm.index,label_y]

auc_fcm = np.zeros(10)
auc_16S = np.zeros(10)
auc_fcm_avg = np.zeros(10)
auc_16S_avg = np.zeros(10)
prec_fcm = np.zeros(10)
prec_16S = np.zeros(10)
rec_fcm = np.zeros(10)
rec_16S = np.zeros(10)

df_fcm_bin = df_fcm.round()
df_16S_bin = df_16S.round()

for i in df_fcm.columns: 
    auc_fcm[i] = roc_auc_score(y_test,df_fcm.loc[:,i])
    auc_16S[i] = roc_auc_score(y_test,df_16S.loc[:,i])
    prec_fcm[i] = precision_score(y_test,df_fcm_bin.loc[:,i], average='macro')
    prec_16S[i] = precision_score(y_test,df_16S_bin.loc[:,i], average='macro')
    rec_fcm[i] = recall_score(y_test,df_fcm_bin.loc[:,i], average='macro')
    rec_16S[i] = recall_score(y_test,df_16S_bin.loc[:,i], average='macro')

fpr_fcm = dict()
tpr_fcm = dict()
fpr_16S = dict()
tpr_16S = dict()
roc_auc_fcm = dict()
roc_auc_16S = dict()
tprs_fcm = []
tprs_16S = []
base_fpr = np.linspace(0, 1, 101)

plt.figure()
lw = 2
for i in np.arange(10): 
    fpr_fcm[0], tpr_fcm[0], _ = roc_curve(y_test, df_fcm.loc[:, i])
    roc_auc_fcm[0] = auc(fpr_fcm[0], tpr_fcm[0])
    plt.plot(fpr_fcm[0], tpr_fcm[0], color='dodgerblue',
         lw=lw, label='ROC curve (area = %0.2f)' % roc_auc_fcm[0], alpha=0.25)
    tpr = interp(base_fpr, fpr_fcm[0], tpr_fcm[0])
    tpr[0] = 0.0
    tprs_fcm.append(tpr)
  
plt.plot([0, 1], [0, 1], color='black', lw=lw, linestyle='--')

tprs_fcm = np.array(tprs_fcm)
mean_fcm = tprs_fcm.mean(axis=0)
std_fcm = tprs_fcm.std(axis=0)
tprs_upper_fcm = np.minimum(mean_fcm+ std_fcm, 1)
tprs_lower_fcm = mean_fcm - std_fcm

plt.plot(base_fpr, mean_fcm, 'b')
plt.fill_between(base_fpr, tprs_lower_fcm, tprs_upper_fcm, color='grey', alpha=0.3)

plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate',size=18)
plt.ylabel('True Positive Rate',size=18)
plt.title('Flow cytometry',size=20)
plt.savefig('Figures/Fig1A_ROC_test_FCM_RFR.png',bbox_tight=True,dpi=500)
plt.show()

for i in np.arange(10): 

    fpr_16S[0], tpr_16S[0], _ = roc_curve(y_test, df_16S.loc[:, i])
    roc_auc_16S[0] = auc(fpr_16S[0], tpr_16S[0])
    tprs_16S.append(tpr)
    plt.plot(fpr_16S[0], tpr_16S[0], color='orange',
         lw=lw, label='ROC curve (area = %0.2f)' % roc_auc_16S[0], alpha=0.25)
    tpr = interp(base_fpr, fpr_16S[0], tpr_16S[0])
    tpr[0] = 0.0
    tprs_16S.append(tpr)
    
plt.plot([0, 1], [0, 1], color='black', lw=lw, linestyle='--')

tprs_16S = np.array(tprs_16S)
mean_16S = tprs_16S.mean(axis=0)
std_16S = tprs_16S.std(axis=0)
tprs_upper_16S = np.minimum(mean_16S+ std_16S, 1)
tprs_lower_16S = mean_16S - std_16S

plt.plot(base_fpr, mean_16S, 'darkorange')
plt.fill_between(base_fpr, tprs_lower_16S, tprs_upper_16S, color='grey', alpha=0.3)

plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate',size=18)
plt.ylabel('True Positive Rate',size=18)
plt.title('16S rRNA gene sequencing',size=20)
#plt.legend(loc="lower right")
plt.savefig('Figures/Fig1B_ROC_test_16S_RFR.png',bbox_tight=True,dpi=500)
plt.show()

mean_auc_fcm = np.mean(auc_fcm)
median_auc_fcm = np.median(auc_fcm)
mean_auc_16S = np.mean(auc_16S)
median_auc_16S = np.median(auc_16S)

t, p = ttest_rel(auc_16S,auc_fcm)

for run in np.arange(0,10): 
    for k in np.arange(0,58,2): 
        if df_fcm.iloc[k,run] > df_fcm.iloc[(k+1),run]: 
            auc_fcm_avg[run]+=1
        if df_16S.iloc[k,run] > df_16S.iloc[(k+1),run]: 
            auc_16S_avg[run]+=1

auc_fcm_avg = auc_fcm_avg/29
auc_16S_avg = auc_16S_avg/29
            
mean_auc_fcm_avg = np.mean(auc_fcm_avg)
median_auc_fcm_avg = np.median(auc_fcm_avg)
mean_auc_16S_avg = np.mean(auc_16S_avg)
median_auc_16S_avg = np.median(auc_16S_avg)    

results_fcm = pd.DataFrame({'Precision':prec_fcm,'Recall':rec_fcm,'AUC':auc_fcm_avg})
results_16S = pd.DataFrame({'Precision':prec_16S,'Recall':rec_16S,'AUC':auc_16S_avg})
results_fcm.to_excel('Results/FCM_LPO_Results_test_Strat_GMM_RFR_CLASS_L400_asinh.xlsx')
results_16S.to_excel('Results/16S_LPO_Results_test_Strat_RFR_CLASS_L400_asinh.xlsx')
 