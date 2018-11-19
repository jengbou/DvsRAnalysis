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

    ## NISTset3
    sampleSet = "NISTset3"
    doselabel = "7 Mrad@ 8.53 krad/hr"

    ## Un-irr samples
    ## PVT 1X1P
    myfile["EJ200PVT_1X1P_N1-20160908"] = ["Ref",TFile("root/AlphaSource/Pu239new_EJ200PVT-1X1P_N1_Default_Nofoil_FastFrame_20160908_merged.root")]
    myfile["EJ200PVT_1X1P_N1-20160909"] = ["Ref",TFile("root/AlphaSource/Pu239new_EJ200PVT-1X1P_N1_Default_Nofoil_FastFrame_20160909_merged.root")]
    myfile["EJ200PVT_1X1P_N1-20161011"] = ["Ref",TFile("root/AlphaSource/Pu239new_EJ200PVT-1X1P_N1_Default_Nofoil_FastFrame_20161011_merged.root")]
    myfile["EJ200PVT_1X1P_N1-20161210"] = ["Ref",TFile("root/AlphaSource/Pu239new_EJ200PVT-1X1P_N1_Default_Nofoil_FastFrame_20161210_merged.root")]
    myfile["EJ200PVT_1X1P_N1-20170122"] = ["Ref",TFile("root/AlphaSource/Pu239new_EJ200PVT-1X1P_N1_Default_Nofoil_FastFrame_20170122_merged.root")]
    ## PVT 1X2P
    myfile["EJ200PVT_1X2P_N1_20160913"] = ["Ref",TFile("root/AlphaSource/Pu239new_EJ200PVT-1X2P_N1_Default_Nofoil_FastFrame_20160913_merged.root")]
    ## PS 1X1P
    myfile["EJ200PS_1X1P_1_20170122"] = ["Ref",TFile("root/AlphaSource/Pu239new_EJ200PS-1X1P_1_Default_Nofoil_FastFrame_20170122_merged.root")]
    ## PS 1X2P
    myfile["EJ200PS_1X2P_1-20170122"] = ["Ref",TFile("root/AlphaSource/Pu239new_EJ200PS-1X2P_1_Default_Nofoil_FastFrame_20170122_merged.root")]


    ## [fitrng0,fitrng1,fitterType,biasOffset]
    ## [1.3,1.1,0,0.3112]

    ## PVT 1X1P
    myfile["EJ200PVT_1X1P_N1-UnIrr"] = [
        "PVT1X1P",TFile("root/AlphaSource/Pu239new_EJ200PVT-1X1P_N1_Default_Nofoil_FastFrame_20161011_merged.root"),[1.3,1.1,"G2"]]
    myfile["EJ200PVT_1X1P_N5-000d"]  = [
        "PVT1X1P",TFile("root/AlphaSource/Pu239new_EJ200PVT-1X1P_N5_Default_Nofoil_FastFrame_20161109_merged.root"),[1.1,1.1,"G2"]]
    myfile["EJ200PVT_1X1P_N5-001d"]  = [
        "PVT1X1P",TFile("root/AlphaSource/Pu239new_EJ200PVT-1X1P_N5_Default_Nofoil_FastFrame_20161110_merged.root"),[1.1,1.1,"G2"]]
    myfile["EJ200PVT_1X1P_N5-008d"]  = [
        "PVT1X1P",TFile("root/AlphaSource/Pu239new_EJ200PVT-1X1P_N5_Default_Nofoil_FastFrame_20161117_merged.root"),[1.1,1.1,"G2"]]
    myfile["EJ200PVT_1X1P_N5-014d"]  = [
        "PVT1X1P",TFile("root/AlphaSource/Pu239new_EJ200PVT-1X1P_N5_Default_Nofoil_FastFrame_20161123_merged.root"),[1.1,1.1,"G2",0.3112]]
    myfile["EJ200PVT_1X1P_N5-021d"]  = [
        "PVT1X1P",TFile("root/AlphaSource/Pu239new_EJ200PVT-1X1P_N5_Default_Nofoil_FastFrame_20161130_merged.root"),[1.1,1.1,"G2",0.3112]]
    myfile["EJ200PVT_1X1P_N5-028d"]  = [
        "PVT1X1P",TFile("root/AlphaSource/Pu239new_EJ200PVT-1X1P_N5_Default_Nofoil_FastFrame_20161207_merged.root"),[1.1,1.1,"G2",0.3112]]
    ## new ref
    myfile["EJ200PVT_1X1P_N1-UnIrrNew"] = [
        "PVT1X1P",TFile("root/AlphaSource/Pu239new_EJ200PVT-1X1P_N1_Default_Nofoil_FastFrame_20170122_merged.root"),[1.3,1.1,"G2",0.3112]]
    myfile["EJ200PVT_1X1P_N5-099d"]  = [
        "PVT1X1P",TFile("root/AlphaSource/Pu239new_EJ200PVT-1X1P_N5_Default_Nofoil_FastFrame_20170216_merged.root"),[1.1,1.1,"G2",0.3112]]

    ## PVT 1X2P
    myfile["EJ200PVT_1X2P_N1-UnIrr"] = [
        "PVT1X2P",TFile("root/AlphaSource/Pu239new_EJ200PVT-1X2P_N1_Default_Nofoil_FastFrame_20160913_merged.root"),[1.1,1.1,"G2"]]
    myfile["EJ200PVT_1X2P_N5-000d"]  = [
        "PVT1X2P",TFile("root/AlphaSource/Pu239new_EJ200PVT-1X2P_N5_Default_Nofoil_FastFrame_20161109_merged.root"),[1.1,1.1,"G2"]]
    myfile["EJ200PVT_1X2P_N5-001d"]  = [
        "PVT1X2P",TFile("root/AlphaSource/Pu239new_EJ200PVT-1X2P_N5_Default_Nofoil_FastFrame_20161110_merged.root"),[1.1,1.1,"G2"]]
    myfile["EJ200PVT_1X2P_N5-008d"]  = [
        "PVT1X2P",TFile("root/AlphaSource/Pu239new_EJ200PVT-1X2P_N5_Default_Nofoil_FastFrame_20161117_merged.root"),[1.1,1.1,"G2"]]
    myfile["EJ200PVT_1X2P_N5-014d"]  = [
        "PVT1X2P",TFile("root/AlphaSource/Pu239new_EJ200PVT-1X2P_N5_Default_Nofoil_FastFrame_20161123_merged.root"),[1.1,1.1,"G2",0.3112]]
    myfile["EJ200PVT_1X2P_N5-021d"]  = [
        "PVT1X2P",TFile("root/AlphaSource/Pu239new_EJ200PVT-1X2P_N5_Default_Nofoil_FastFrame_20161130_merged.root"),[1.1,1.1,"G2",0.3112]]
    myfile["EJ200PVT_1X2P_N5-028d"]  = [
        "PVT1X2P",TFile("root/AlphaSource/Pu239new_EJ200PVT-1X2P_N5_Default_Nofoil_FastFrame_20161207_merged.root"),[1.1,1.1,"G2",0.3112]]
    ## new ref
    myfile["EJ200PVT_1X2P_N1-UnIrrNew"] = [
        "PVT1X2P",TFile("root/AlphaSource/Pu239new_EJ200PVT-1X2P_N1_Default_Nofoil_FastFrame_20170122_merged.root"),[1.3,1.1,"G2",0.3112]]
    myfile["EJ200PVT_1X2P_N5-099d"]  = [
        "PVT1X2P",TFile("root/AlphaSource/Pu239new_EJ200PVT-1X2P_N5_Default_Nofoil_FastFrame_20170216_merged.root"),[1.1,1.1,"G2",0.3112]]

    ## PS 1X1P
    myfile["EJ200PS_1X1P_1-UnIrr"] = [
        "PS1X1P",TFile("root/AlphaSource/Pu239new_EJ200PS-1X1P_1_Default_Nofoil_FastFrame_20160907_merged.root"),[1.3,1.1,"G2"]]
    myfile["EJ200PS_1X1P_5-000d"]  = [
        "PS1X1P",TFile("root/AlphaSource/Pu239new_EJ200PS-1X1P_5_Default_Nofoil_FastFrame_20161109_merged.root"),[1.1,1.1,"G2"]]
    myfile["EJ200PS_1X1P_5-001d"]  = [
        "PS1X1P",TFile("root/AlphaSource/Pu239new_EJ200PS-1X1P_5_Default_Nofoil_FastFrame_20161110_merged.root"),[1.1,1.1,"G2"]]
    myfile["EJ200PS_1X1P_5-008d"]  = [
        "PS1X1P",TFile("root/AlphaSource/Pu239new_EJ200PS-1X1P_5_Default_Nofoil_FastFrame_20161117_merged.root"),[1.1,1.1,"G2"]]
    myfile["EJ200PS_1X1P_5-014d"]  = [
        "PS1X1P",TFile("root/AlphaSource/Pu239new_EJ200PS-1X1P_5_Default_Nofoil_FastFrame_20161123_merged.root"),[1.1,1.1,"G2",0.3112]]
    myfile["EJ200PS_1X1P_5-021d"]  = [
        "PS1X1P",TFile("root/AlphaSource/Pu239new_EJ200PS-1X1P_5_Default_Nofoil_FastFrame_20161130_merged.root"),[1.1,1.1,"G2",0.3112]]
    myfile["EJ200PS_1X1P_5-028d"]  = [
        "PS1X1P",TFile("root/AlphaSource/Pu239new_EJ200PS-1X1P_5_Default_Nofoil_FastFrame_20161207_merged.root"),[1.1,1.1,"G2",0.3112]]
    ## new ref
    myfile["EJ200PS_1X1P_1-UnIrrNew"] = [
        "PS1X1P",TFile("root/AlphaSource/Pu239new_EJ200PS-1X1P_1_Default_Nofoil_FastFrame_20170122_merged.root"),[1.3,1.1,"G2",0.3112]]
    myfile["EJ200PS_1X1P_5-099d"]  = [
        "PS1X1P",TFile("root/AlphaSource/Pu239new_EJ200PS-1X1P_5_Default_Nofoil_FastFrame_20170216_merged.root"),[1.1,1.1,"G2",0.3112]]

    ## PS 1X2P
    myfile["EJ200PS_1X2P_1-UnIrr"] = [
        "PS1X2P",TFile("root/AlphaSource/Pu239new_EJ200PS-1X2P_1_Default_Nofoil_FastFrame_20160912_merged.root"),[1.1,1.1,"G2"]]
    myfile["EJ200PS_1X2P_5-000d"]  = [
        "PS1X2P",TFile("root/AlphaSource/Pu239new_EJ200PS-1X2P_5_Default_Nofoil_FastFrame_20161109_merged.root"),[1.1,1.1,"G2"]]
    myfile["EJ200PS_1X2P_5-001d"]  = [
        "PS1X2P",TFile("root/AlphaSource/Pu239new_EJ200PS-1X2P_5_Default_Nofoil_FastFrame_20161110_merged.root"),[1.1,1.1,"G2"]]
    myfile["EJ200PS_1X2P_5-008d"]  = [
        "PS1X2P",TFile("root/AlphaSource/Pu239new_EJ200PS-1X2P_5_Default_Nofoil_FastFrame_20161117_merged.root"),[1.1,1.1,"G2"]]
    myfile["EJ200PS_1X2P_5-014d"]  = [
        "PS1X2P",TFile("root/AlphaSource/Pu239new_EJ200PS-1X2P_5_Default_Nofoil_FastFrame_20161123_merged.root"),[1.1,1.1,"G2",0.3112]]
    myfile["EJ200PS_1X2P_5-021d"]  = [
        "PS1X2P",TFile("root/AlphaSource/Pu239new_EJ200PS-1X2P_5_Default_Nofoil_FastFrame_20161130_merged.root"),[1.1,1.1,"G2",0.3112]]
    myfile["EJ200PS_1X2P_5-028d"]  = [
        "PS1X2P",TFile("root/AlphaSource/Pu239new_EJ200PS-1X2P_5_Default_Nofoil_FastFrame_20161207_merged.root"),[1.1,1.1,"G2",0.3112]]
    ## new ref
    myfile["EJ200PS_1X2P_1-UnIrrNew"] = [
        "PS1X2P",TFile("root/AlphaSource/Pu239new_EJ200PS-1X2P_1_Default_Nofoil_FastFrame_20170122_merged.root"),[1.3,1.1,"G2",0.3112]]
    myfile["EJ200PS_1X2P_5-099d"]  = [
        "PS1X2P",TFile("root/AlphaSource/Pu239new_EJ200PS-1X2P_5_Default_Nofoil_FastFrame_20170216_merged.root"),[1.1,1.1,"G2",0.3112]]


    ## Results calculated w.r.t. old ref (old scope config no longer available)
    plotSets = {}
    plotSets['PVT1X1P'] = ["EJ200PVT_1X1P_N1-UnIrr","EJ200PVT_1X1P_N5-000d","EJ200PVT_1X1P_N5-001d","EJ200PVT_1X1P_N5-008d",
                           "EJ200PVT_1X1P_N5-014d","EJ200PVT_1X1P_N5-021d","EJ200PVT_1X1P_N5-028d"]
    plotSets['PVT1X2P'] = ["EJ200PVT_1X2P_N1-UnIrr","EJ200PVT_1X2P_N5-000d","EJ200PVT_1X2P_N5-001d","EJ200PVT_1X2P_N5-008d",
                           "EJ200PVT_1X2P_N5-014d","EJ200PVT_1X2P_N5-021d","EJ200PVT_1X2P_N5-028d"]

    plotSets['PS1X1P'] = ["EJ200PS_1X1P_1-UnIrr","EJ200PS_1X1P_5-000d","EJ200PS_1X1P_5-001d","EJ200PS_1X1P_5-008d",
                          "EJ200PS_1X1P_5-014d","EJ200PS_1X1P_5-021d","EJ200PS_1X1P_5-028d"]
    plotSets['PS1X2P'] = ["EJ200PS_1X2P_1-UnIrr","EJ200PS_1X2P_5-000d","EJ200PS_1X2P_5-001d","EJ200PS_1X2P_5-008d",
                          "EJ200PS_1X2P_5-014d","EJ200PS_1X2P_5-021d","EJ200PS_1X2P_5-028d"]

    DrawDvsTHist(myfile, plotSets, outDir, "%s_OldRef"%(sampleSet), fTag, doselabel, hxrng, options, "EJ200", "NIST4", debug)

    ## Results calculated w.r.t. new ref (new scope config)
    plotSetsNew = {}
    plotSetsNew['PVT1X1P'] = ["EJ200PVT_1X1P_N1-UnIrrNew","EJ200PVT_1X1P_N5-000d","EJ200PVT_1X1P_N5-001d","EJ200PVT_1X1P_N5-008d","EJ200PVT_1X1P_N5-014d","EJ200PVT_1X1P_N5-021d","EJ200PVT_1X1P_N5-028d","EJ200PVT_1X1P_N5-099d"]
    plotSetsNew['PVT1X2P'] = ["EJ200PVT_1X2P_N1-UnIrrNew","EJ200PVT_1X2P_N5-000d","EJ200PVT_1X2P_N5-001d","EJ200PVT_1X2P_N5-008d","EJ200PVT_1X2P_N5-014d","EJ200PVT_1X2P_N5-021d","EJ200PVT_1X2P_N5-028d","EJ200PVT_1X2P_N5-099d"]

    plotSetsNew['PS1X1P'] = ["EJ200PS_1X1P_1-UnIrrNew","EJ200PS_1X1P_5-000d","EJ200PS_1X1P_5-001d","EJ200PS_1X1P_5-008d","EJ200PS_1X1P_5-014d","EJ200PS_1X1P_5-021d","EJ200PS_1X1P_5-028d","EJ200PS_1X1P_5-099d"]
    plotSetsNew['PS1X2P'] = ["EJ200PS_1X2P_1-UnIrrNew","EJ200PS_1X2P_5-000d","EJ200PS_1X2P_5-001d","EJ200PS_1X2P_5-008d","EJ200PS_1X2P_5-014d","EJ200PS_1X2P_5-021d","EJ200PS_1X2P_5-028d","EJ200PS_1X2P_5-099d"]

    DrawDvsTHist(myfile, plotSetsNew, outDir, sampleSet, fTag, doselabel, hxrng, options, "EJ200", "NIST4", debug)

