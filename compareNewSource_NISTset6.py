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

    ## NISTset6
    sampleSet = "NISTset6"
    doselabel = "7 Mrad@ 8.34 krad/hr"

    ## Un-irr samples
    ## EJ200 PVT 2X1P
    myfile["EJ200PVT_2X1P_N1-20170122"] = ["Ref",TFile("root/AlphaSource/Pu239new_EJ200PVT-2X1P_N1_Default_Nofoil_FastFrame_20170122_merged.root")]
    ## EJ200 PS 2X1P
    myfile["EJ200PS_2X1P_1-20170122"] = ["Ref",TFile("root/AlphaSource/Pu239new_EJ200PS-2X1P_1_Default_Nofoil_FastFrame_20170122_merged.root")]

    ## EJ260 PVT 1X1P
    myfile["EJ260PVT_1X1P_N1-20170123"] = ["Ref",TFile("root/AlphaSource/Pu239new_EJ260PVT-1X1P_N1_Default_Nofoil_FastFrame_20170123_merged.root")]
    ## EJ260 PS 1X1P
    myfile["EJ260PS_1X1P_1-20170123"] = ["Ref",TFile("root/AlphaSource/Pu239new_EJ260PS-1X1P_1_Default_Nofoil_FastFrame_20170123_merged.root")]


    ## [fitrng0,fitrng1,fitterType,biasOffset]
    ## [1.3,1.1,"G2",0.3112]

    ## EJ200 PVT 2X1P
    myfile["EJ200PVT_2X1P_N1-UnIrr"] = [
        "EJ200",TFile("root/AlphaSource/Pu239new_EJ200PVT-2X1P_N1_Default_Nofoil_FastFrame_20170122_merged.root"),[1.3,1.1,"G2",0.3112]]
    myfile["EJ200PVT_2X1P_N5-001d"]  = [
        "EJ200",TFile("root/AlphaSource/Pu239new_EJ200PVT-2X1P_N5_Default_Nofoil_FastFrame_20170112_merged.root"),[1.1,1.1,"G2",0.3112]]
    myfile["EJ200PVT_2X1P_N5-007d"]  = [
        "EJ200",TFile("root/AlphaSource/Pu239new_EJ200PVT-2X1P_N5_Default_Nofoil_FastFrame_20170118_merged.root"),[1.1,1.1,"G2",0.3112]]
    myfile["EJ200PVT_2X1P_N5-015d"]  = [
        "EJ200",TFile("root/AlphaSource/Pu239new_EJ200PVT-2X1P_N5_Default_Nofoil_FastFrame_20170126_merged.root"),[1.1,1.1,"G2",0.3112]]
    myfile["EJ200PVT_2X1P_N5-028d"]  = [
        "EJ200",TFile("root/AlphaSource/Pu239new_EJ200PVT-2X1P_N5_Default_Nofoil_FastFrame_20170208_merged.root"),[1.1,1.1,"G2",0.3112]]
    myfile["EJ200PVT_2X1P_N5-056d"]  = [
        "EJ200",TFile("root/AlphaSource/Pu239new_EJ200PVT-2X1P_N5_Default_Nofoil_FastFrame_20170308_merged.root"),[1.1,1.1,"G2",0.3112]]
    myfile["EJ200PVT_2X1P_N5-099d"]  = [
        "EJ200",TFile("root/AlphaSource/Pu239new_EJ200PVT-2X1P_N5_Default_Nofoil_FastFrame_20170420_merged.root"),[1.1,1.1,"G2",0.3112]]

    ## EJ200 PS 2X1P
    myfile["EJ200PS_2X1P_1-UnIrr"] = [
        "EJ200",TFile("root/AlphaSource/Pu239new_EJ200PS-2X1P_1_Default_Nofoil_FastFrame_20170122_merged.root"),[1.3,1.1,"G2",0.3112]]
    myfile["EJ200PS_2X1P_5-001d"]  = [
        "EJ200",TFile("root/AlphaSource/Pu239new_EJ200PS-2X1P_5_Default_Nofoil_FastFrame_20170112_merged.root"),[1.1,1.1,"G2",0.3112]]
    myfile["EJ200PS_2X1P_5-007d"]  = [
        "EJ200",TFile("root/AlphaSource/Pu239new_EJ200PS-2X1P_5_Default_Nofoil_FastFrame_20170118_merged.root"),[1.1,1.1,"G2",0.3112]]
    myfile["EJ200PS_2X1P_5-015d"]  = [
        "EJ200",TFile("root/AlphaSource/Pu239new_EJ200PS-2X1P_5_Default_Nofoil_FastFrame_20170126_merged.root"),[1.1,1.1,"G2",0.3112]]
    myfile["EJ200PS_2X1P_5-028d"]  = [
        "EJ200",TFile("root/AlphaSource/Pu239new_EJ200PS-2X1P_5_Default_Nofoil_FastFrame_20170208_merged.root"),[1.1,1.1,"G2",0.3112]]
    myfile["EJ200PS_2X1P_5-056d"]  = [
        "EJ200",TFile("root/AlphaSource/Pu239new_EJ200PS-2X1P_5_Default_Nofoil_FastFrame_20170308_merged.root"),[1.1,1.1,"G2",0.3112]]
    myfile["EJ200PS_2X1P_5-099d"]  = [
        "EJ200",TFile("root/AlphaSource/Pu239new_EJ200PS-2X1P_5_Default_Nofoil_FastFrame_20170420_merged.root"),[1.1,1.1,"G2",0.3112]]

    ## EJ260 PVT 1X1P
    myfile["EJ260PVT_1X1P_N1-UnIrr"] = [
        "EJ260",TFile("root/AlphaSource/Pu239new_EJ260PVT-1X1P_N1_Default_Nofoil_FastFrame_20170123_merged.root"),[1.1,1.1,"G2",0.3112]]
    myfile["EJ260PVT_1X1P_N4-001d"]  = [
        "EJ260",TFile("root/AlphaSource/Pu239new_EJ260PVT-1X1P_N4_Default_Nofoil_FastFrame_20170112_merged.root"),[0.3,0.3,"G1",0.3112]]
    myfile["EJ260PVT_1X1P_N4-007d"]  = [
        "EJ260",TFile("root/AlphaSource/Pu239new_EJ260PVT-1X1P_N4_Default_Nofoil_FastFrame_20170118_merged.root"),[0.3,0.3,"G1",0.3112]]
    myfile["EJ260PVT_1X1P_N4-015d"]  = [
        "EJ260",TFile("root/AlphaSource/Pu239new_EJ260PVT-1X1P_N4_Default_Nofoil_FastFrame_20170126_merged.root"),[0.3,0.3,"G1",0.3112]]
    myfile["EJ260PVT_1X1P_N4-028d"]  = [
        "EJ260",TFile("root/AlphaSource/Pu239new_EJ260PVT-1X1P_N4_Default_Nofoil_FastFrame_20170208_merged.root"),[0.3,0.3,"G1",0.3112]]
    myfile["EJ260PVT_1X1P_N4-056d"]  = [
        "EJ260",TFile("root/AlphaSource/Pu239new_EJ260PVT-1X1P_N4_Default_Nofoil_FastFrame_20170308_merged.root"),[0.3,0.3,"G1",0.3112]]
    myfile["EJ260PVT_1X1P_N4-099d"]  = [
        "EJ260",TFile("root/AlphaSource/Pu239new_EJ260PVT-1X1P_N4_Default_Nofoil_FastFrame_20170420_merged.root"),[0.3,0.3,"G1",0.3112]]

    ## EJ260 PS 1X1P
    myfile["EJ260PS_1X1P_1-UnIrr"] = [
        "EJ260",TFile("root/AlphaSource/Pu239new_EJ260PS-1X1P_1_Default_Nofoil_FastFrame_20170123_merged.root"),[1.1,1.1,"G2",0.3112]]
    myfile["EJ260PS_1X1P_4-001d"]  = [
        "EJ260",TFile("root/AlphaSource/Pu239new_EJ260PS-1X1P_4_Default_Nofoil_FastFrame_20170112_merged.root"),[0.3,0.3,"G1",0.3112]]
    myfile["EJ260PS_1X1P_4-007d"]  = [
        "EJ260",TFile("root/AlphaSource/Pu239new_EJ260PS-1X1P_4_Default_Nofoil_FastFrame_20170118_merged.root"),[0.3,0.3,"G1",0.3112]]
    myfile["EJ260PS_1X1P_4-015d"]  = [
        "EJ260",TFile("root/AlphaSource/Pu239new_EJ260PS-1X1P_4_Default_Nofoil_FastFrame_20170126_merged.root"),[0.3,0.3,"G1",0.3112]]
    myfile["EJ260PS_1X1P_4-028d"]  = [
        "EJ260",TFile("root/AlphaSource/Pu239new_EJ260PS-1X1P_4_Default_Nofoil_FastFrame_20170208_merged.root"),[0.3,0.3,"G1",0.3112]]
    myfile["EJ260PS_1X1P_4-056d"]  = [
        "EJ260",TFile("root/AlphaSource/Pu239new_EJ260PS-1X1P_4_Default_Nofoil_FastFrame_20170308_merged.root"),[0.3,0.3,"G1",0.3112]]
    myfile["EJ260PS_1X1P_4-099d"]  = [
        "EJ260",TFile("root/AlphaSource/Pu239new_EJ260PS-1X1P_4_Default_Nofoil_FastFrame_20170420_merged.root"),[0.3,0.3,"G1",0.3112]]


    ## Results calculated w.r.t. old ref (old scope config no longer available)
    plotSets = {}
    plotSets['EJ200PVT2X1P'] = ["EJ200PVT_2X1P_N1-UnIrr","EJ200PVT_2X1P_N5-001d","EJ200PVT_2X1P_N5-007d","EJ200PVT_2X1P_N5-015d","EJ200PVT_2X1P_N5-028d","EJ200PVT_2X1P_N5-056d","EJ200PVT_2X1P_N5-099d"]
    plotSets['EJ200PS2X1P'] = ["EJ200PS_2X1P_1-UnIrr","EJ200PS_2X1P_5-001d","EJ200PS_2X1P_5-007d","EJ200PS_2X1P_5-015d","EJ200PS_2X1P_5-028d","EJ200PS_2X1P_5-056d","EJ200PS_2X1P_5-099d"]


    #DrawDvsTHist(myfile, plotSets, outDir, "%s"%(sampleSet), fTag, doselabel, hxrng, options, "EJ200", "NIST4", debug)
    DrawDvsTHist(myfile, plotSets, outDir, "%s"%(sampleSet), fTag, doselabel, hxrng, options, "EJ200SP1P", "NIST4", debug)


    plotSets1 = {}
    plotSets1['EJ260PVT1X1P'] = ["EJ260PVT_1X1P_N1-UnIrr","EJ260PVT_1X1P_N4-001d","EJ260PVT_1X1P_N4-007d","EJ260PVT_1X1P_N4-015d","EJ260PVT_1X1P_N4-028d","EJ260PVT_1X1P_N4-056d","EJ260PVT_1X1P_N4-099d"]
    plotSets1['EJ260PS1X1P'] = ["EJ260PS_1X1P_1-UnIrr","EJ260PS_1X1P_4-001d","EJ260PS_1X1P_4-007d","EJ260PS_1X1P_4-015d","EJ260PS_1X1P_4-028d","EJ260PS_1X1P_4-056d","EJ260PS_1X1P_4-099d"]

    DrawDvsTHist(myfile, plotSets1, outDir, "%s"%(sampleSet), fTag, doselabel, hxrng, options, "EJ260N", "NIST4", debug)

