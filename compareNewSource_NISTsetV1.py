#!/usr/bin/python
import os, sys, math, datetime
from ROOT import gROOT, gStyle, TFile, TTree, TH1F, TH1D, TCanvas, TPad, TMath, TF1, TLegend, gPad, gDirectory

from collections import OrderedDict
import numpy

sys.path.append(os.path.abspath(os.path.curdir))

from Plotter import parseLYAnaInputArgs
from Plotter.CommonTools import DrawHistSimple, DrawDvsTHist
options = parseLYAnaInputArgs()

gROOT.LoadMacro("Plotter/UMDStyle.C")
from ROOT import SetUMDStyle
SetUMDStyle()
gROOT.SetBatch()

####################################################################################################
####################################################################################################
if __name__ == '__main__':
    print options

    myfile = {}

    ## binbase, xmin, xmax : nbins = binbase*(xmax-xmin)
    hxrng = {}
    hxrng["Ref"]   = [32,-1,8]
    hxrng["EJ200"] = [32,-1,6]
    hxrng["EJ260"] = [32,-0.5,4]

    hxrng["T1"] = [32,-1,8.0]
    hxrng["T2"] = [32,-1,8.5]
    hxrng["T3"] = [32,-1,9.0]
    hxrng["T4"] = [33,-1,9.5]

    today = datetime.date.today()
    fTag = today.strftime("%Y%m%d")

    ## Output directory
    outDir = "Results/comp_newsource"
    try:
        os.makedirs(outDir)
    except:
        pass

    ## NIST setV1
    sampleSet = "NISTV1"
    doselabel = "7 Mrad@ 370 krad/hr"

    ## Un-irr samples
    myfile["EJ200PVT_T1_1-20161103"] = ["T1",TFile("root/AlphaSource/Pu239new_EJ200PVT-T1_1_Default_Nofoil_FastFrame_20161103_merged.root")]
    myfile["EJ200PVT_T1_1-20161108"] = ["T1",TFile("root/AlphaSource/Pu239new_EJ200PVT-T1_1_Default_Nofoil_FastFrame_20161108_merged.root")]
    ## Un-irr samples
    myfile["EJ200PVT_T2_1-20161103"] = ["T2",TFile("root/AlphaSource/Pu239new_EJ200PVT-T2_1_Default_Nofoil_FastFrame_20161103_merged.root")]
    myfile["EJ200PVT_T2_1-20161108"] = ["T2",TFile("root/AlphaSource/Pu239new_EJ200PVT-T2_1_Default_Nofoil_FastFrame_20161108_merged.root")]
    ## Un-irr samples
    myfile["EJ200PVT_T3_1-20161103"] = ["T3",TFile("root/AlphaSource/Pu239new_EJ200PVT-T3_1_Default_Nofoil_FastFrame_20161103_merged.root")]
    myfile["EJ200PVT_T3_1-20161108"] = ["T3",TFile("root/AlphaSource/Pu239new_EJ200PVT-T3_1_Default_Nofoil_FastFrame_20161108_merged.root")]
    ## Un-irr samples
    myfile["EJ200PVT_T4_1-20161103"] = ["T4",TFile("root/AlphaSource/Pu239new_EJ200PVT-T4_1_Default_Nofoil_FastFrame_20161103_merged.root")]
    myfile["EJ200PVT_T4_1-20161108"] = ["T4",TFile("root/AlphaSource/Pu239new_EJ200PVT-T4_1_Default_Nofoil_FastFrame_20161108_merged.root")]

    ## [fitrng0,fitrng1,fitterType,biasOffset]
    ## [1.3,1.1,"G2",0.3112]

    myfile["EJ200PVT_T1_1-UnIrr"] = [
        "T1",TFile("root/AlphaSource/Pu239new_EJ200PVT-T1_1_Default_Nofoil_FastFrame_20161108_merged.root"),[1.3,1.1,"G2",0.]]
    myfile["EJ200PVT_T1_3-000d"]  = [
        "T1",TFile("root/AlphaSource/Pu239new_EJ200PVT-T1_3_Default_Nofoil_FastFrame_20170302_merged.root"),[1.1,1.1,"G1",0.3112]]
    myfile["EJ200PVT_T1_3-028d"]  = [
        "T1",TFile("root/AlphaSource/Pu239new_EJ200PVT-T1_3_Default_Nofoil_FastFrame_20170330_merged.root"),[1.1,1.1,"G2",0.3112]]
    myfile["EJ200PVT_T1_3-063d"]  = [
        "T1",TFile("root/AlphaSource/Pu239new_EJ200PVT-T1_3_Default_Nofoil_FastFrame_20170504_merged.root"),[1.1,1.1,"G2",0.3112]]

    myfile["EJ200PVT_T2_1-UnIrr"] = [
        "T2",TFile("root/AlphaSource/Pu239new_EJ200PVT-T2_1_Default_Nofoil_FastFrame_20161108_merged.root"),[1.35,1.1,"G2",0.]]
    myfile["EJ200PVT_T2_3-000d"]  = [
        "T2",TFile("root/AlphaSource/Pu239new_EJ200PVT-T2_3_Default_Nofoil_FastFrame_20170302_merged.root"),[1.1,1.1,"G2",0.3112]]
    myfile["EJ200PVT_T2_3-028d"]  = [
        "T2",TFile("root/AlphaSource/Pu239new_EJ200PVT-T2_3_Default_Nofoil_FastFrame_20170330_merged.root"),[1.1,1.1,"G2",0.3112]]
    myfile["EJ200PVT_T2_3-063d"]  = [
        "T2",TFile("root/AlphaSource/Pu239new_EJ200PVT-T2_3_Default_Nofoil_FastFrame_20170504_merged.root"),[1.1,1.1,"G2",0.3112]]

    myfile["EJ200PVT_T3_1-UnIrr"] = [
        "T3",TFile("root/AlphaSource/Pu239new_EJ200PVT-T3_1_Default_Nofoil_FastFrame_20161108_merged.root"),[1.4,1.1,"G2",0.]]
    myfile["EJ200PVT_T3_3-000d"]  = [
        "T3",TFile("root/AlphaSource/Pu239new_EJ200PVT-T3_3_Default_Nofoil_FastFrame_20170302_merged.root"),[1.1,1.1,"G2",0.3112]]
    myfile["EJ200PVT_T3_3-028d"]  = [
        "T3",TFile("root/AlphaSource/Pu239new_EJ200PVT-T3_3_Default_Nofoil_FastFrame_20170330_merged.root"),[1.1,1.1,"G2",0.3112]]
    myfile["EJ200PVT_T3_3-063d"]  = [
        "T3",TFile("root/AlphaSource/Pu239new_EJ200PVT-T3_3_Default_Nofoil_FastFrame_20170504_merged.root"),[1.1,1.1,"G2",0.3112]]

    myfile["EJ200PVT_T4_1-UnIrr"] = [
        "T4",TFile("root/AlphaSource/Pu239new_EJ200PVT-T4_1_Default_Nofoil_FastFrame_20161108_merged.root"),[1.55,1.1,"G2",0.]]
    myfile["EJ200PVT_T4_3-000d"]  = [
        "T4",TFile("root/AlphaSource/Pu239new_EJ200PVT-T4_3_Default_Nofoil_FastFrame_20170302_merged.root"),[1.1,1.1,"G2",0.3112]]
    myfile["EJ200PVT_T4_3-028d"]  = [
        "T4",TFile("root/AlphaSource/Pu239new_EJ200PVT-T4_3_Default_Nofoil_FastFrame_20170330_merged.root"),[1.1,1.1,"G2",0.3112]]
    myfile["EJ200PVT_T4_3-063d"]  = [
        "T4",TFile("root/AlphaSource/Pu239new_EJ200PVT-T4_3_Default_Nofoil_FastFrame_20170504_merged.root"),[1.1,1.1,"G2",0.3112]]

    plotSets = {}

    plotSets['1'] = ["EJ200PVT_T1_1-UnIrr","EJ200PVT_T1_3-000d","EJ200PVT_T1_3-028d","EJ200PVT_T1_3-063d"]
    plotSets['2'] = ["EJ200PVT_T2_1-UnIrr","EJ200PVT_T2_3-000d","EJ200PVT_T2_3-028d","EJ200PVT_T2_3-063d"]
    plotSets['3'] = ["EJ200PVT_T3_1-UnIrr","EJ200PVT_T3_3-000d","EJ200PVT_T3_3-028d","EJ200PVT_T3_3-063d"]
    plotSets['4'] = ["EJ200PVT_T4_1-UnIrr","EJ200PVT_T4_3-000d","EJ200PVT_T4_3-028d","EJ200PVT_T4_3-063d"]


    DrawDvsTHist(myfile, plotSets, outDir, sampleSet, fTag, doselabel, hxrng, options, "EJ200PVT", "NIST4")


##    plotSetsA = {}
##    plotSetsA['1'] = ["EJ200PVT_T1_1-20161103","EJ200PVT_T1_1-20161108"]
##    plotSetsA['2'] = ["EJ200PVT_T2_1-20161103","EJ200PVT_T2_1-20161108"]
##    plotSetsA['3'] = ["EJ200PVT_T3_1-20161103","EJ200PVT_T3_1-20161108"]
##    plotSetsA['4'] = ["EJ200PVT_T4_1-20161103","EJ200PVT_T4_1-20161108"]

##    DrawHistSimple(myfile, plotSetsA, outDir, fTag, doselabel, hxrng, options)
