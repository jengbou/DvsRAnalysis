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

    ## NIST setV2
    sampleSet = "NISTV2"
    doselabel = "7 Mrad@ 364 krad/hr"

    ## Un-irr samples
    myfile["EJ200PS_T1_1-20161203"] = ["T1",TFile("root/AlphaSource/Pu239new_EJ200PS-T1_1_Default_Nofoil_FastFrame_20161203_merged.root")]
    ## Un-irr samples
    myfile["EJ200PS_T2_1-20161203"] = ["T2",TFile("root/AlphaSource/Pu239new_EJ200PS-T2_1_Default_Nofoil_FastFrame_20161203_merged.root")]
    ## Un-irr samples
    myfile["EJ200PS_T3_1-20161203"] = ["T3",TFile("root/AlphaSource/Pu239new_EJ200PS-T3_1_Default_Nofoil_FastFrame_20161203_merged.root")]
    ## Un-irr samples
    myfile["EJ200PS_T4_1-20161203"] = ["T4",TFile("root/AlphaSource/Pu239new_EJ200PS-T4_1_Default_Nofoil_FastFrame_20161203_merged.root")]

    ## [fitrng0,fitrng1,fitterType,biasOffset]
    ## [1.3,1.1,"G2",0.3112]

    myfile["EJ200PS_T1_1-UnIrr"] = [
        "T1",TFile("root/AlphaSource/Pu239new_EJ200PS-T1_1_Default_Nofoil_FastFrame_20161203_merged.root"),[1.3,1.1,"G2",0.3112]]
    myfile["EJ200PS_T1_3-000d"]  = [
        "T1",TFile("root/AlphaSource/Pu239new_EJ200PS-T1_3_Default_Nofoil_FastFrame_20170413_merged.root"),[1.1,1.1,"G1",0.3112]]
    myfile["EJ200PS_T1_3-014d"]  = [
        "T1",TFile("root/AlphaSource/Pu239new_EJ200PS-T1_3_Default_Nofoil_FastFrame_20170427_merged.root"),[1.1,1.1,"G2",0.3112]]
    myfile["EJ200PS_T1_3-028d"]  = [
        "T1",TFile("root/AlphaSource/Pu239new_EJ200PS-T1_3_Default_Nofoil_FastFrame_20170511_merged.root"),[1.1,1.1,"G2",0.3112]]
    myfile["EJ200PS_T1_3-056d"]  = [
        "T1",TFile("root/AlphaSource/Pu239new_EJ200PS-T1_3_Default_Nofoil_FastFrame_20170608_merged.root"),[1.1,1.1,"G2",0.3112]]

    myfile["EJ200PS_T2_1-UnIrr"] = [
        "T2",TFile("root/AlphaSource/Pu239new_EJ200PS-T2_1_Default_Nofoil_FastFrame_20161203_merged.root"),[1.35,1.1,"G2",0.3112]]
    myfile["EJ200PS_T2_3-000d"]  = [
        "T2",TFile("root/AlphaSource/Pu239new_EJ200PS-T2_3_Default_Nofoil_FastFrame_20170413_merged.root"),[1.1,1.1,"G1",0.3112]]
    myfile["EJ200PS_T2_3-014d"]  = [
        "T2",TFile("root/AlphaSource/Pu239new_EJ200PS-T2_3_Default_Nofoil_FastFrame_20170427_merged.root"),[1.1,1.1,"G2",0.3112]]
    myfile["EJ200PS_T2_3-028d"]  = [
        "T2",TFile("root/AlphaSource/Pu239new_EJ200PS-T2_3_Default_Nofoil_FastFrame_20170511_merged.root"),[1.1,1.1,"G2",0.3112]]
    myfile["EJ200PS_T2_3-056d"]  = [
        "T2",TFile("root/AlphaSource/Pu239new_EJ200PS-T2_3_Default_Nofoil_FastFrame_20170608_merged.root"),[1.1,1.1,"G2",0.3112]]

    myfile["EJ200PS_T3_1-UnIrr"] = [
        "T3",TFile("root/AlphaSource/Pu239new_EJ200PS-T3_1_Default_Nofoil_FastFrame_20161203_merged.root"),[1.4,1.1,"G2",0.3112]]
    myfile["EJ200PS_T3_3-000d"]  = [
        "T3",TFile("root/AlphaSource/Pu239new_EJ200PS-T3_3_Default_Nofoil_FastFrame_20170413_merged.root"),[1.1,1.1,"G1",0.3112]]
    myfile["EJ200PS_T3_3-014d"]  = [
        "T3",TFile("root/AlphaSource/Pu239new_EJ200PS-T3_3_Default_Nofoil_FastFrame_20170427_merged.root"),[1.1,1.1,"G2",0.3112]]
    myfile["EJ200PS_T3_3-028d"]  = [
        "T3",TFile("root/AlphaSource/Pu239new_EJ200PS-T3_3_Default_Nofoil_FastFrame_20170511_merged.root"),[1.1,1.1,"G2",0.3112]]
    myfile["EJ200PS_T3_3-056d"]  = [
        "T3",TFile("root/AlphaSource/Pu239new_EJ200PS-T3_3_Default_Nofoil_FastFrame_20170608_merged.root"),[1.1,1.1,"G2",0.3112]]

    myfile["EJ200PS_T4_1-UnIrr"] = [
        "T4",TFile("root/AlphaSource/Pu239new_EJ200PS-T4_1_Default_Nofoil_FastFrame_20161203_merged.root"),[1.55,1.1,"G2",0.3112]]
    myfile["EJ200PS_T4_3-000d"]  = [
        "T4",TFile("root/AlphaSource/Pu239new_EJ200PS-T4_3_Default_Nofoil_FastFrame_20170413_merged.root"),[1.1,1.1,"G1",0.3112]]
    myfile["EJ200PS_T4_3-014d"]  = [
        "T4",TFile("root/AlphaSource/Pu239new_EJ200PS-T4_3_Default_Nofoil_FastFrame_20170427_merged.root"),[1.1,1.1,"G2",0.3112]]
    myfile["EJ200PS_T4_3-028d"]  = [
        "T4",TFile("root/AlphaSource/Pu239new_EJ200PS-T4_3_Default_Nofoil_FastFrame_20170511_merged.root"),[1.1,1.1,"G2",0.3112]]
    myfile["EJ200PS_T4_3-056d"]  = [
        "T4",TFile("root/AlphaSource/Pu239new_EJ200PS-T4_3_Default_Nofoil_FastFrame_20170608_merged.root"),[1.1,1.1,"G2",0.3112]]

    plotSets = {}

    plotSets['1'] = ["EJ200PS_T1_1-UnIrr","EJ200PS_T1_3-000d","EJ200PS_T1_3-014d","EJ200PS_T1_3-028d","EJ200PS_T1_3-056d"]
    plotSets['2'] = ["EJ200PS_T2_1-UnIrr","EJ200PS_T2_3-000d","EJ200PS_T2_3-014d","EJ200PS_T2_3-028d","EJ200PS_T2_3-056d"]
    plotSets['3'] = ["EJ200PS_T3_1-UnIrr","EJ200PS_T3_3-000d","EJ200PS_T3_3-014d","EJ200PS_T3_3-028d","EJ200PS_T3_3-056d"]
    plotSets['4'] = ["EJ200PS_T4_1-UnIrr","EJ200PS_T4_3-000d","EJ200PS_T4_3-014d","EJ200PS_T4_3-028d","EJ200PS_T4_3-056d"]


    DrawDvsTHist(myfile, plotSets, outDir, sampleSet, fTag, doselabel, hxrng, options, "EJ200PS", "NIST4")

