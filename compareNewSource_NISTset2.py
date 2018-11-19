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

    ## NISTset2
    sampleSet = "NISTset2"
    doselabel = "7 Mrad@ 390 krad/hr"

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
        "EJ200",TFile("root/AlphaSource/Pu239new_EJ200PVT-2X1P_N1_Default_Nofoil_FastFrame_20160914_merged.root"),[1.1,1.1,"G2"]]
    # N9 1 day ## Do not use the 1005_merged since it's an avg. of 1005 and 1006
    myfile["EJ200PVT_2X1P_N9-001d"]  = [
        "EJ200",TFile("root/AlphaSource/Pu239new_EJ200PVT-2X1P_N9_Default_Nofoil_FaceB_FastFrame_20161006.root"),[1.1,1.1,"G2"]]
    myfile["EJ200PVT_2X1P_N9-007d"]  = [
        "EJ200",TFile("root/AlphaSource/Pu239new_EJ200PVT-2X1P_N9_Default_Nofoil_FastFrame_20161012_merged.root"),[1.1,1.1,"G2"]]
    myfile["EJ200PVT_2X1P_N9-014d"]  = [
        "EJ200",TFile("root/AlphaSource/Pu239new_EJ200PVT-2X1P_N9_Default_Nofoil_FastFrame_20161019_merged.root"),[1.1,1.1,"G2"]]
    myfile["EJ200PVT_2X1P_N9-021d"]  = [
        "EJ200",TFile("root/AlphaSource/Pu239new_EJ200PVT-2X1P_N9_Default_Nofoil_FastFrame_20161026_merged.root"),[1.1,1.1,"G2"]]
    myfile["EJ200PVT_2X1P_N9-028d"]  = [
        "EJ200",TFile("root/AlphaSource/Pu239new_EJ200PVT-2X1P_N9_Default_Nofoil_FastFrame_20161102_merged.root"),[1.1,1.1,"G2"]]

    ## new ref
    myfile["EJ200PVT_2X1P_N1-UnIrrNew"] = [
        "EJ200",TFile("root/AlphaSource/Pu239new_EJ200PVT-2X1P_N1_Default_Nofoil_FastFrame_20170122_merged.root"),[1.3,1.1,"G2",0.3112]]
    myfile["EJ200PVT_2X1P_N9-046d"]  = [
        "EJ200",TFile("root/AlphaSource/Pu239new_EJ200PVT-2X1P_N9_Default_Nofoil_FastFrame_20161121_merged.root"),[1.1,1.1,"G2",0.3112]]
    myfile["EJ200PVT_2X1P_N9-112d"]  = [
        "EJ200",TFile("root/AlphaSource/Pu239new_EJ200PVT-2X1P_N9_Default_Nofoil_FastFrame_20170125_merged.root"),[1.1,1.1,"G2",0.3112]]

    ## EJ200 PS 2X1P
    myfile["EJ200PS_2X1P_1-UnIrr"] = [
        "EJ200",TFile("root/AlphaSource/Pu239new_EJ200PS-2X1P_1_Default_Nofoil_FastFrame_20160914_merged.root"),[1.1,1.1,"G2"]]
    # 9 1 day ## Do not use the 1005_merged since it's an avg. of 1005 and 1006
    # bad sample face a and b show very different results
    myfile["EJ200PS_2X1P_9-001d"]  = [
        "EJ200",TFile("root/AlphaSource/Pu239new_EJ200PS-2X1P_9_Default_Nofoil_FaceB_FastFrame_20161006.root"),[0.2,0.2,"G1"]]
    myfile["EJ200PS_2X1P_9-007d"]  = [
        "EJ200",TFile("root/AlphaSource/Pu239new_EJ200PS-2X1P_9_Default_Nofoil_FaceB_FastFrame_20161012.root"),[0.2,0.2,"G1"]]
    myfile["EJ200PS_2X1P_9-014d"]  = [
        "EJ200",TFile("root/AlphaSource/Pu239new_EJ200PS-2X1P_9_Default_Nofoil_FaceB_FastFrame_20161019.root"),[0.2,0.2,"G1"]]
    myfile["EJ200PS_2X1P_9-021d"]  = [
        "EJ200",TFile("root/AlphaSource/Pu239new_EJ200PS-2X1P_9_Default_Nofoil_FaceB_FastFrame_20161026.root"),[0.2,0.2,"G1"]]
    myfile["EJ200PS_2X1P_9-028d"]  = [
        "EJ200",TFile("root/AlphaSource/Pu239new_EJ200PS-2X1P_9_Default_Nofoil_FaceB_FastFrame_20161102.root"),[0.2,0.2,"G1"]]

    # new ref
    myfile["EJ200PS_2X1P_1-UnIrrNew"] = [
        "EJ200",TFile("root/AlphaSource/Pu239new_EJ200PS-2X1P_1_Default_Nofoil_FastFrame_20170122_merged.root"),[1.1,1.1,"G2",0.3112]]
    myfile["EJ200PS_2X1P_9-046d"]  = [
        "EJ200",TFile("root/AlphaSource/Pu239new_EJ200PS-2X1P_9_Default_Nofoil_FaceB_FastFrame_20161121.root"),[0.5,0.5,"G1",0.3112]]
    myfile["EJ200PS_2X1P_9-112d"]  = [
        "EJ200",TFile("root/AlphaSource/Pu239new_EJ200PS-2X1P_9_Default_Nofoil_FaceB_FastFrame_20170125.root"),[0.5,0.5,"G1",0.3112]]

    ## EJ260 PVT 1X1P
    myfile["EJ260PVT_1X1P_N1-UnIrr"] = [
        "EJ260",TFile("root/AlphaSource/Pu239new_EJ260PVT-1X1P_N1_Default_Nofoil_FastFrame_20161006_merged.root"),[1.1,1.1,"G2"]]
    myfile["EJ260PVT_1X1P_N9-001d"]  = [
        "EJ260",TFile("root/AlphaSource/Pu239new_EJ260PVT-1X1P_N9_Default_Nofoil_FastFrame_20161005_merged.root"),[0.5,0.5,"G1"]]
    myfile["EJ260PVT_1X1P_N9-007d"]  = [
        "EJ260",TFile("root/AlphaSource/Pu239new_EJ260PVT-1X1P_N9_Default_Nofoil_FastFrame_20161012_merged.root"),[0.5,0.5,"G1"]]
    myfile["EJ260PVT_1X1P_N9-014d"]  = [
        "EJ260",TFile("root/AlphaSource/Pu239new_EJ260PVT-1X1P_N9_Default_Nofoil_FastFrame_20161019_merged.root"),[0.5,0.5,"G1"]]
    myfile["EJ260PVT_1X1P_N9-021d"]  = [
        "EJ260",TFile("root/AlphaSource/Pu239new_EJ260PVT-1X1P_N9_Default_Nofoil_FastFrame_20161026_merged.root"),[0.5,0.5,"G1"]]
    myfile["EJ260PVT_1X1P_N9-028d"]  = [
        "EJ260",TFile("root/AlphaSource/Pu239new_EJ260PVT-1X1P_N9_Default_Nofoil_FastFrame_20161102_merged.root"),[0.5,0.5,"G1"]]

    # new ref
    myfile["EJ260PVT_1X1P_N1-UnIrrNew"] = [
        "EJ260",TFile("root/AlphaSource/Pu239new_EJ260PVT-1X1P_N1_Default_Nofoil_FastFrame_20170123_merged.root"),[1.3,1.1,"G2",0.3112]]
    myfile["EJ260PVT_1X1P_N9-046d"]  = [
        "EJ260",TFile("root/AlphaSource/Pu239new_EJ260PVT-1X1P_N9_Default_Nofoil_FastFrame_20161121_merged.root"),[0.5,0.5,"G1",0.3112]]
    myfile["EJ260PVT_1X1P_N9-112d"]  = [
        "EJ260",TFile("root/AlphaSource/Pu239new_EJ260PVT-1X1P_N9_Default_Nofoil_FastFrame_20170125_merged.root"),[0.5,0.5,"G1",0.3112]]

    ## EJ260 PS 1X1P
    myfile["EJ260PS_1X1P_1-UnIrr"] = [
        "EJ260",TFile("root/AlphaSource/Pu239new_EJ260PS-1X1P_1_Default_Nofoil_FastFrame_20161006_merged.root"),[1.1,1.1,"G2"]]
    myfile["EJ260PS_1X1P_9-001d"]  = [
        "EJ260",TFile("root/AlphaSource/Pu239new_EJ260PS-1X1P_9_Default_Nofoil_FastFrame_20161005_merged.root"),[0.5,0.5,"G1"]]
    myfile["EJ260PS_1X1P_9-007d"]  = [
        "EJ260",TFile("root/AlphaSource/Pu239new_EJ260PS-1X1P_9_Default_Nofoil_FastFrame_20161012_merged.root"),[0.5,0.5,"G1"]]
    myfile["EJ260PS_1X1P_9-014d"]  = [
        "EJ260",TFile("root/AlphaSource/Pu239new_EJ260PS-1X1P_9_Default_Nofoil_FastFrame_20161019_merged.root"),[0.5,0.5,"G1"]]
    myfile["EJ260PS_1X1P_9-021d"]  = [
        "EJ260",TFile("root/AlphaSource/Pu239new_EJ260PS-1X1P_9_Default_Nofoil_FastFrame_20161026_merged.root"),[0.5,0.5,"G1"]]
    myfile["EJ260PS_1X1P_9-028d"]  = [
        "EJ260",TFile("root/AlphaSource/Pu239new_EJ260PS-1X1P_9_Default_Nofoil_FastFrame_20161102_merged.root"),[0.5,0.5,"G1"]]

    # new ref
    myfile["EJ260PS_1X1P_1-UnIrrNew"] = [
        "EJ260",TFile("root/AlphaSource/Pu239new_EJ260PS-1X1P_1_Default_Nofoil_FastFrame_20170123_merged.root"),[1.3,1.1,"G2",0.3112]]
    myfile["EJ260PS_1X1P_9-046d"]  = [
        "EJ260",TFile("root/AlphaSource/Pu239new_EJ260PS-1X1P_9_Default_Nofoil_FastFrame_20161121_merged.root"),[0.5,0.5,"G1",0.3112]]
    myfile["EJ260PS_1X1P_9-112d"]  = [
        "EJ260",TFile("root/AlphaSource/Pu239new_EJ260PS-1X1P_9_Default_Nofoil_FastFrame_20170125_merged.root"),[0.5,0.5,"G1",0.3112]]

    ## Results calculated w.r.t. old ref (old scope config no longer available)


    plotSets0 = {}
    plotSets0['EJ200PVT2X1P'] = ["EJ200PVT_2X1P_N1-UnIrr","EJ200PVT_2X1P_N9-001d","EJ200PVT_2X1P_N9-007d","EJ200PVT_2X1P_N9-014d","EJ200PVT_2X1P_N9-021d","EJ200PVT_2X1P_N9-028d"]
    plotSets0['EJ200PS2X1P'] = ["EJ200PS_2X1P_1-UnIrr","EJ200PS_2X1P_9-001d","EJ200PS_2X1P_9-007d","EJ200PS_2X1P_9-014d","EJ200PS_2X1P_9-021d","EJ200PS_2X1P_9-028d"]

    ##DrawDvsTHist(myfile, plotSets0, outDir, "%s_OldRef"%(sampleSet), fTag, doselabel, hxrng, options, "EJ200SP1P", "NIST4", debug)
    DrawDvsTHist(myfile, plotSets0, outDir, "%s_OldRef"%(sampleSet), fTag, doselabel, hxrng, options, "EJ200", "NIST4", debug)


    plotSets1 = {}
    plotSets1['EJ200PVT2X1P'] = ["EJ200PVT_2X1P_N1-UnIrrNew","EJ200PVT_2X1P_N9-046d","EJ200PVT_2X1P_N9-112d"]
    plotSets1['EJ200PS2X1P'] = ["EJ200PS_2X1P_1-UnIrrNew","EJ200PS_2X1P_9-046d","EJ200PS_2X1P_9-112d"]

    DrawDvsTHist(myfile, plotSets1, outDir, "%s"%(sampleSet), fTag, doselabel, hxrng, options, "EJ200", "NIST4", debug)


    plotSets2 = {}
    plotSets2['EJ260PVT1X1P'] = ["EJ260PVT_1X1P_N1-UnIrr","EJ260PVT_1X1P_N9-001d","EJ260PVT_1X1P_N9-007d","EJ260PVT_1X1P_N9-014d","EJ260PVT_1X1P_N9-021d","EJ260PVT_1X1P_N9-028d"]
    plotSets2['EJ260PS1X1P'] = ["EJ260PS_1X1P_1-UnIrr","EJ260PS_1X1P_9-001d","EJ260PS_1X1P_9-007d","EJ260PS_1X1P_9-014d","EJ260PS_1X1P_9-021d","EJ260PS_1X1P_9-028d"]

    DrawDvsTHist(myfile, plotSets2, outDir, "%s_OldRef"%(sampleSet), fTag, doselabel, hxrng, options, "EJ260N", "NIST4", debug)


    plotSets3 = {}
    plotSets3['EJ260PVT1X1P'] = ["EJ260PVT_1X1P_N1-UnIrrNew","EJ260PVT_1X1P_N9-046d","EJ260PVT_1X1P_N9-112d"]
    plotSets3['EJ260PS1X1P'] = ["EJ260PS_1X1P_1-UnIrrNew","EJ260PS_1X1P_9-046d","EJ260PS_1X1P_9-112d"]

    DrawDvsTHist(myfile, plotSets3, outDir, "%s"%(sampleSet), fTag, doselabel, hxrng, options, "EJ260N", "NIST4", debug)
