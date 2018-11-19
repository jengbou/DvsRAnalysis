#!/usr/bin/python
import os, sys, math, datetime
from ROOT import gROOT, gStyle, TFile, TTree, TH1F, TH1D, TCanvas, TPad, TMath, TF1, TLegend, gPad, gDirectory

from collections import OrderedDict
import numpy

sys.path.append(os.path.abspath(os.path.curdir))

from Plotter import parseLYAnaInputArgs
from Plotter.CommonTools import DrawHistSimple, DrawDvsTHist
options = parseLYAnaInputArgs()

gROOT.Reset()
gROOT.LoadMacro("Plotter/UMDStyle.C")
from ROOT import SetUMDStyle
SetUMDStyle()
gROOT.SetBatch()

####################################################################################################
####################################################################################################
debug=False
if __name__ == '__main__':
    print options
    if debug: print "Style = ",gStyle.GetName()
    myfile = {}

    ## binbase, xmin, xmax : nbins = binbase*(xmax-xmin)
    hxrng = {}
    hxrng["Ref"]     = [32,-1.0,8.0]
    hxrng["EJ200"]   = [32,-1.0,8.0]
    hxrng["EJ260"]   = [32,-0.5,6.0]

    hxrng["PVT1X1P"] = [32,-1.0,8.0]
    hxrng["PVT1X2P"] = [32,-1.0,8.0]
    hxrng["PS1X1P"]  = [32,-1.0,8.0]
    hxrng["PS1X2P"]  = [32,-1.0,8.0]

    today = datetime.date.today()
    fTag = today.strftime("%Y%m%d")

    ## Output directory
    outDir = "Results/comp_newsource"
    try:
        os.makedirs(outDir)
    except:
        pass

    ## NISTset5
    sampleSet = "NISTset5"
    doselabel = "7 Mrad@ 74.4 krad/hr@ 23#circC"

    ## Un-irr samples
    ## PVT 1X1P
    myfile["EJ200PVT_1X1P_N1-20170122"] = ["Ref",TFile("root/AlphaSource/Pu239new_EJ200PVT-1X1P_N1_Default_Nofoil_FastFrame_20170122_merged.root")]
    ## PVT 1X2P
    myfile["EJ200PVT_1X2P_N1-20170122"] = ["Ref",TFile("root/AlphaSource/Pu239new_EJ200PVT-1X2P_N1_Default_Nofoil_FastFrame_20170122_merged.root")]
    ## PS 1X1P
    myfile["EJ200PS_1X1P_1-20170122"] = ["Ref",TFile("root/AlphaSource/Pu239new_EJ200PS-1X1P_1_Default_Nofoil_FastFrame_20170122_merged.root")]
    ## PS 1X2P
    myfile["EJ200PS_1X2P_1-20170122"] = ["Ref",TFile("root/AlphaSource/Pu239new_EJ200PS-1X2P_1_Default_Nofoil_FastFrame_20170122_merged.root")]


    ## [fitrng0,fitrng1,fitterType,biasOffset]
    ## [1.3,1.1,"G2",0.3112]

    ## PVT 1X1P
    myfile["EJ200PVT_1X1P_N1-UnIrr"] = [
        "EJ200",TFile("root/AlphaSource/Pu239new_EJ200PVT-1X1P_N1_Default_Nofoil_FastFrame_20170122_merged.root"),[1.3,1.1,"G2",0.3112]]
    myfile["EJ200PVT_1X1P_N4-000d"]  = [
        "EJ200",TFile("root/AlphaSource/Pu239new_EJ200PVT-1X1P_N4_Default_Nofoil_FastFrame_20161202_merged.root"),[0.5,0.5,"G1",0.3112]]
    myfile["EJ200PVT_1X1P_N4-007d"]  = [
        "EJ200",TFile("root/AlphaSource/Pu239new_EJ200PVT-1X1P_N4_Default_Nofoil_FastFrame_20161209_merged.root"),[1.1,1.1,"G2",0.3112]]
    myfile["EJ200PVT_1X1P_N4-056d"]  = [
        "EJ200",TFile("root/AlphaSource/Pu239new_EJ200PVT-1X1P_N4_Default_Nofoil_FastFrame_20170127_merged.root"),[1.1,1.1,"G2",0.3112]]
    myfile["EJ200PVT_1X1P_N4-120d"]  = [
        "EJ200",TFile("root/AlphaSource/Pu239new_EJ200PVT-1X1P_N4_Default_Nofoil_FastFrame_20170401_merged.root"),[1.1,1.1,"G2",0.3112]]
    myfile["EJ200PVT_1X1P_N4-136d"]  = [
        "EJ200",TFile("root/AlphaSource/Pu239new_EJ200PVT-1X1P_N4_Default_Nofoil_FastFrame_20170417_merged.root"),[1.1,1.1,"G2",0.3112]]
    myfile["EJ200PVT_1X1P_N4-199d"]  = [
        "EJ200",TFile("root/AlphaSource/Pu239new_EJ200PVT-1X1P_N4_Default_Nofoil_FastFrame_20170612_merged.root"),[1.1,1.1,"G2",0.3112]]

    ## PVT 1X2P
    myfile["EJ200PVT_1X2P_N1-UnIrr"] = [
        "EJ200",TFile("root/AlphaSource/Pu239new_EJ200PVT-1X2P_N1_Default_Nofoil_FastFrame_20170122_merged.root"),[1.3,1.1,"G2",0.3112]]
    myfile["EJ200PVT_1X2P_N4-000d"]  = [
        "EJ200",TFile("root/AlphaSource/Pu239new_EJ200PVT-1X2P_N4_Default_Nofoil_FastFrame_20161202_merged.root"),[0.5,0.5,"G1",0.3112]]
    myfile["EJ200PVT_1X2P_N4-007d"]  = [
        "EJ200",TFile("root/AlphaSource/Pu239new_EJ200PVT-1X2P_N4_Default_Nofoil_FastFrame_20161209_merged.root"),[1.1,1.1,"G2",0.3112]]
    myfile["EJ200PVT_1X2P_N4-056d"]  = [
        "EJ200",TFile("root/AlphaSource/Pu239new_EJ200PVT-1X2P_N4_Default_Nofoil_FastFrame_20170127_merged.root"),[1.1,1.1,"G2",0.3112]]
    myfile["EJ200PVT_1X2P_N4-120d"]  = [
        "EJ200",TFile("root/AlphaSource/Pu239new_EJ200PVT-1X2P_N4_Default_Nofoil_FastFrame_20170401_merged.root"),[1.1,1.1,"G2",0.3112]]
    myfile["EJ200PVT_1X2P_N4-136d"]  = [
        "EJ200",TFile("root/AlphaSource/Pu239new_EJ200PVT-1X2P_N4_Default_Nofoil_FastFrame_20170417_merged.root"),[1.1,1.1,"G2",0.3112]]
    myfile["EJ200PVT_1X2P_N4-199d"]  = [
        "EJ200",TFile("root/AlphaSource/Pu239new_EJ200PVT-1X2P_N4_Default_Nofoil_FastFrame_20170612_merged.root"),[1.1,1.1,"G2",0.3112]]

    ## PS 1X1P
    myfile["EJ200PS_1X1P_1-UnIrr"] = [
        "EJ200",TFile("root/AlphaSource/Pu239new_EJ200PS-1X1P_1_Default_Nofoil_FastFrame_20170122_merged.root"),[1.3,1.1,"G2",0.3112]]
    myfile["EJ200PS_1X1P_8-000d"]  = [
        "EJ200",TFile("root/AlphaSource/Pu239new_EJ200PS-1X1P_8_Default_Nofoil_FastFrame_20161202_merged.root"),[0.3,0.3,"G1",0.3112]]
    myfile["EJ200PS_1X1P_8-007d"]  = [
        "EJ200",TFile("root/AlphaSource/Pu239new_EJ200PS-1X1P_8_Default_Nofoil_FastFrame_20161209_merged.root"),[0.5,0.5,"G1",0.3112]]
    myfile["EJ200PS_1X1P_8-056d"]  = [
        "EJ200",TFile("root/AlphaSource/Pu239new_EJ200PS-1X1P_8_Default_Nofoil_FastFrame_20170127_merged.root"),[0.5,0.5,"G1",0.3112]]
    myfile["EJ200PS_1X1P_8-120d"]  = [
        "EJ200",TFile("root/AlphaSource/Pu239new_EJ200PS-1X1P_8_Default_Nofoil_FastFrame_20170401_merged.root"),[0.5,0.5,"G1",0.3112]]
    myfile["EJ200PS_1X1P_8-136d"]  = [
        "EJ200",TFile("root/AlphaSource/Pu239new_EJ200PS-1X1P_8_Default_Nofoil_FastFrame_20170417_merged.root"),[0.5,0.5,"G1",0.3112]]
    myfile["EJ200PS_1X1P_8-137d"]  = [
        "EJ200",TFile("root/AlphaSource/Pu239new_EJ200PS-1X1P_8_Default_Nofoil_FastFrame_20170418_merged.root"),[0.5,0.5,"G1",0.3112]]
    myfile["EJ200PS_1X1P_8-199d"]  = [
        "EJ200",TFile("root/AlphaSource/Pu239new_EJ200PS-1X1P_8_Default_Nofoil_FastFrame_20170612_merged.root"),[0.5,0.5,"G1",0.3112]]

    ## PS 1X2P
    myfile["EJ200PS_1X2P_1-UnIrr"] = [
        "EJ200",TFile("root/AlphaSource/Pu239new_EJ200PS-1X2P_1_Default_Nofoil_FastFrame_20170122_merged.root"),[1.3,1.1,"G2",0.3112]]
    myfile["EJ200PS_1X2P_8-000d"]  = [
        "EJ200",TFile("root/AlphaSource/Pu239new_EJ200PS-1X2P_8_Default_Nofoil_FastFrame_20161202_merged.root"),[0.5,0.5,"G1",0.3112]]
    myfile["EJ200PS_1X2P_8-007d"]  = [
        "EJ200",TFile("root/AlphaSource/Pu239new_EJ200PS-1X2P_8_Default_Nofoil_FastFrame_20161209_merged.root"),[0.5,0.5,"G1",0.3112]]
    myfile["EJ200PS_1X2P_8-056d"]  = [
        "EJ200",TFile("root/AlphaSource/Pu239new_EJ200PS-1X2P_8_Default_Nofoil_FastFrame_20170127_merged.root"),[0.5,0.5,"G1",0.3112]]
    myfile["EJ200PS_1X2P_8-120d"]  = [
        "EJ200",TFile("root/AlphaSource/Pu239new_EJ200PS-1X2P_8_Default_Nofoil_FastFrame_20170401_merged.root"),[0.5,0.5,"G1",0.3112]]
    myfile["EJ200PS_1X2P_8-136d"]  = [
        "EJ200",TFile("root/AlphaSource/Pu239new_EJ200PS-1X2P_8_Default_Nofoil_FastFrame_20170417_merged.root"),[0.5,0.5,"G1",0.3112]]
    myfile["EJ200PS_1X2P_8-137d"]  = [
        "EJ200",TFile("root/AlphaSource/Pu239new_EJ200PS-1X2P_8_Default_Nofoil_FastFrame_20170418_merged.root"),[0.5,0.5,"G1",0.3112]]
    myfile["EJ200PS_1X2P_8-199d"]  = [
        "EJ200",TFile("root/AlphaSource/Pu239new_EJ200PS-1X2P_8_Default_Nofoil_FastFrame_20170612_merged.root"),[0.5,0.5,"G1",0.3112]]


    ## Results calculated w.r.t. old ref (old scope config no longer available)
    plotSets = {}
    plotSets['EJ200PVT1X1P'] = ["EJ200PVT_1X1P_N1-UnIrr","EJ200PVT_1X1P_N4-000d","EJ200PVT_1X1P_N4-007d","EJ200PVT_1X1P_N4-056d","EJ200PVT_1X1P_N4-120d","EJ200PVT_1X1P_N4-136d","EJ200PVT_1X1P_N4-199d"]
    plotSets['EJ200PVT1X2P'] = ["EJ200PVT_1X2P_N1-UnIrr","EJ200PVT_1X2P_N4-000d","EJ200PVT_1X2P_N4-007d","EJ200PVT_1X2P_N4-056d","EJ200PVT_1X2P_N4-120d","EJ200PVT_1X2P_N4-136d","EJ200PVT_1X2P_N4-199d"]
    plotSets['EJ200PS1X1P'] = ["EJ200PS_1X1P_1-UnIrr","EJ200PS_1X1P_8-000d","EJ200PS_1X1P_8-007d","EJ200PS_1X1P_8-056d","EJ200PS_1X1P_8-120d","EJ200PS_1X1P_8-136d","EJ200PS_1X1P_8-137d","EJ200PS_1X1P_8-199d"]
    plotSets['EJ200PS1X2P'] = ["EJ200PS_1X2P_1-UnIrr","EJ200PS_1X2P_8-000d","EJ200PS_1X2P_8-007d","EJ200PS_1X2P_8-056d","EJ200PS_1X2P_8-120d","EJ200PS_1X2P_8-136d","EJ200PS_1X2P_8-137d","EJ200PS_1X2P_8-199d"]

    #DrawDvsTHist(myfile, plotSets, outDir, "%s"%(sampleSet), fTag, doselabel, hxrng, options, "EJ200", "NIST4", debug)
    DrawDvsTHist(myfile, plotSets, outDir, "%s"%(sampleSet), fTag, doselabel, hxrng, options, "EJ200SP1P", "NIST4", debug)



