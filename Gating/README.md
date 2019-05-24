## Some explanation concerning the gating strategy

Upon inspection of the flow cytometry data, three groups can be detected. 
- Left bottom: (in)organic noise. 
- Left top: (in)noise. 
- Right: bacterial community. 

To make sure this conclusion holds, we created two visualizations. [Figure A](https://github.com/prubbens/PhenoGMM_CD/blob/master/Gating/gating_strat_1_truecomm.pdf) contains the gate that allows to extract the bacterial community. We visualized the cells inside the gate in red in multiple bivariate histograms. This shows that this group of cells stays outside the region of background noise. 

[Figure B](https://github.com/prubbens/PhenoGMM_CD/blob/master/Gating/gating_strat_2_falsecomm.pdf) contains the gate that extracts the noise on the top left. Upon inspection of these cells (again visualized in red) shows that these are amongst the background signal in a number of cells. This is why we excluded this subset of cells from our analysis. 