# DvsRAnalysis
Plotting scripts for plastic scintillator D vs R studies

# Steps to analyze alpha source measurements
#
## 1. create list of measurements to make them into root format, e.g., grap all the measurements taken during January in 2018: 
### ll Data/AlphaSource |grep -ir txt|grep 201801 |awk '{if (index($10,"area")==0) {print substr($10,0,length($10))}}' > RunLists/List-AlphaSource.txt
## 2. make root tree:
### python makeTree.py - -i RunLists/List-AlphaSource.txt -d Data/AlphaSource
## 3. run comparison script according to sample category, e.g., NIST round 4 set 6, 99 days after irradiation, processed on 2018/11/16:
### python compareNewSource_NISTset6.py -t 99DaysAftIrr_p20181116 >& logs/compareNewSource_NISTset6_99DaysAftIrr_p20181116.log



# Fitting cosmic ray measurement
## Langaus fit
### root [0] .L Plotter/langaus.C+
### root [1] PyLandGaus *fobj = new PyLandGaus()
### root [2] double fitRng[] = {10,-2,28}     ## note: nbins = int(10*(28-(-2)))=300 in this e.g.
### root [3] double fitRngPed[] = {20,-1.5,-0.1} ## note: nbins = 20 in this e.g.; this line is optional; if not specified the default fit range=[-1.5,-0.15] and nbin=10
### root [4] fobj->langaus("root/cosmic/EJ200_1X_6_CosmicStand20170307_CH2_NonMirr_UnIrrFiber_HV70p89_Tcomp25p7C_20170823.root",fitRng,true,fitRngPed)
### root [l] double fitRngPed10[] = {20,-0.8,-0.4} ## note: another example range for fitting pedestal


### root [m] fobj->langaus("root/Na22/EJ260_2p1s_N4_Na22Source20170413_CH2FF_Tcomp25p5C_20170413.root",fitRng,true)
### root [n] fobj->langaus("root/cosmic/EJ200_1X_6_CosmicStand20170307_CH2_NonMirr_UnIrrFiber_HV70p89_Tcomp25p7C_20170823.root",fitRng,true)
### root [o] fobj->langaus("root/cosmic/EJ200_10_CosmicStand20170307_CH2_NonMirr_HV70p82_Tcomp24p5C_20180114.root",fitRng,true,fitRngPed10)

## for EJ200 1X un-irr.
### root [2] double fitRng1[] = {10,-2,35}
## for EJ260 2p1s
### root [2] double fitRng[] = {10,-2,15}



# cosmic ray measurement analysis
## EJ200 G2
### python analysis_multi_EJ200.py - -p -i list_EJ200_1X_G2_20170619 -t PostRecovery_Ref8_0329 -c 0.1,0.1 -b -u -s --sampleSet EJ200_1X > logs/EJ200_1X_20170619_p20170620.log

### python analysis_multi_EJ200.py - -p -i list_EJ200_1X_G2_20170620 -t PostRecovery_Refs_plus_IrrFiber -c 0.1,0.1 -b -u -s --sampleSet EJ200_1X > logs/EJ200_1X_20170620_p20170620.log

### python analysis_multi_EJ200.py - -p -i list_EJ200_1X_G2_20170620_UnIrrFiber -t PostRecovery_UnIrrFiber -c 0.1,0.1 -b -u -s --sampleSet EJ200_1X > logs/EJ200_1X_20170620_UnIrrFiber_p20170620.log

## EJ260 2p1s G2
### python analysis_multi_EJ260.py - -p -i list_EJ260_2p1s_G2_20170620 -t PostRecovery_N1 -c 0.01,0.01 -b -u -s --sampleSet EJ260_2p1s > logs/EJ260_2p1s_20170620_p20170620.log

