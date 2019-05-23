#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 10:47:32 2018

@author: prubbens
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import seaborn as sns
sns.set_color_codes()
tips = sns.load_dataset("tips")

import warnings
warnings.simplefilter(action = "ignore", category = FutureWarning)
sns.set_style("ticks")

df_fcm = pd.read_excel('Results/FCM_LPO_Results_test_Strat_GMM_RFR_CLASS_L400_AUC.xlsx')
df_fcm['Analysis'] = 'Flow cytometry'
df_16S = pd.read_excel('Results/16S_LPO_Results_test_Strat_RFR_CLASS_L400_AUC.xlsx')
df_16S['Analysis'] = '16S sequencing' 
df = pd.concat([df_fcm,df_16S], axis=0)

 
def patch_violinplot():
    """Patch seaborn's violinplot in current axis to workaround matplotlib's bug ##5423."""
    from matplotlib.collections import PolyCollection
    ax = plt.gca()
    for art in ax.get_children():
        if isinstance(art, PolyCollection):
            art.set_edgecolor((0.1, 0.1, 0.1))
            
def plot_class_auc(df): 
    pal = sns.color_palette("colorblind")
    g = sns.catplot(x='Analysis',y='AUC',data=df, kind='box', size=4.5, aspect=0.75, sharey=True, color='white',linewidth=3)
    pal = sns.color_palette('cubehelix')[0:1]
    h = sns.swarmplot(x='Analysis', y='AUC', data=df, dodge=True, palette=pal)   
    g.set_titles(size=20)
    g.set_xlabels(fontsize=18)
    g.set_ylabels('AUROC',fontsize=18)
    g.set(ylim=(0.0, 1.05))
    plt.savefig('Figures/Fig1C_Results_test_FCM_vs_16S_AUROC.png',bbox_inches='tight', dpi=500)
    plt.show()
    return df

df = plot_class_auc(df)