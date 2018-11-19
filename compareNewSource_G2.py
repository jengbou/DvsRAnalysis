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

    ## G2
    sampleSet = "G2"
    doselabel = "0.38 Mrad@ 0.3 krad/hr@ 23#circC"

    ## Un-irr samples
    ## PVT 1X2P
    myfile["EJ200PVT_1X2P_N1-20170122"] = ["Ref",TFile("root/AlphaSource/Pu239new_EJ200PVT-1X2P_N1_Default_Nofoil_FastFrame_20170122_merged.root")]
    ## PS 1X2P
    myfile["EJ200PS_1X2P_1_20170122"] = ["Ref",TFile("root/AlphaSource/Pu239new_EJ200PS-1X2P_1_Default_Nofoil_FastFrame_20170122_merged.root")]
    ## EJ260 PVT 1X2P
    myfile["EJ260PVT_1X2P_N1_20170122"] = ["Ref",TFile("root/AlphaSource/Pu239new_EJ260PVT-1X2P_N1_Default_Nofoil_FastFrame_20161201_merged.root")]
    ## EJ260 PS 1X2P
    myfile["EJ260PS_1X2P_1-20170122"] = ["Ref",TFile("root/AlphaSource/Pu239new_EJ260PS-1X2P_1_Default_Nofoil_FastFrame_20161201_merged.root")]


    ## [fitrng0,fitrng1,fitterType,biasOffset]
    ## [1.3,1.1,0,0.3112]

    ## PVT 1X2P
    myfile["EJ200PVT_1X2P_N1-UnIrr"] = [
        "EJ200",TFile("root/AlphaSource/Pu239new_EJ200PVT-1X2P_N1_Default_Nofoil_FastFrame_20161203_merged.root"),[1.3,1.1,"G2",0.3152]]
    myfile["EJ200PVT_1X2P_N11-003d"]  = [
        "EJ200",TFile("root/AlphaSource/Pu239new_EJ200PVT-1X2P_N11_Default_Nofoil_FastFrame_20161201_merged.root"),[1.1,1.1,"G2",0.3152]]
    myfile["EJ200PVT_1X2P_N11-007d"]  = [
        "EJ200",TFile("root/AlphaSource/Pu239new_EJ200PVT-1X2P_N11_Default_Nofoil_FastFrame_20161205_merged.root"),[1.1,1.1,"G2",0.3152]]
    myfile["EJ200PVT_1X2P_N11-014d"]  = [
        "EJ200",TFile("root/AlphaSource/Pu239new_EJ200PVT-1X2P_N11_Default_Nofoil_FastFrame_20161212_merged.root"),[1.1,1.1,"G2",0.3152]]
    myfile["EJ200PVT_1X2P_N11-056d"]  = [
        "EJ200",TFile("root/AlphaSource/Pu239new_EJ200PVT-1X2P_N11_Default_Nofoil_FastFrame_20170123_merged.root"),[1.1,1.1,"G2",0.3152]]
    myfile["EJ200PVT_1X2P_N11-084d"]  = [
        "EJ200",TFile("root/AlphaSource/Pu239new_EJ200PVT-1X2P_N11_Default_Nofoil_FastFrame_20170220_merged.root"),[1.1,1.1,"G2",0.3152]]

    ## PS 1X2P
    myfile["EJ200PS_1X2P_1-UnIrr"] = [
        "EJ200",TFile("root/AlphaSource/Pu239new_EJ200PS-1X2P_1_Default_Nofoil_FastFrame_20161203_merged.root"),[1.3,1.1,"G2",0.3152]]
    myfile["EJ200PS_1X2P_11-003d"]  = [
        "EJ200",TFile("root/AlphaSource/Pu239new_EJ200PS-1X2P_11_Default_Nofoil_FastFrame_20161201_merged.root"),[1.1,1.1,"G2",0.3152]]
    myfile["EJ200PS_1X2P_11-007d"]  = [
        "EJ200",TFile("root/AlphaSource/Pu239new_EJ200PS-1X2P_11_Default_Nofoil_FastFrame_20161205_merged.root"),[1.1,1.1,"G2",0.3152]]
    myfile["EJ200PS_1X2P_11-014d"]  = [
        "EJ200",TFile("root/AlphaSource/Pu239new_EJ200PS-1X2P_11_Default_Nofoil_FastFrame_20161212_merged.root"),[1.1,1.1,"G2",0.3152]]
    myfile["EJ200PS_1X2P_11-056d"]  = [
        "EJ200",TFile("root/AlphaSource/Pu239new_EJ200PS-1X2P_11_Default_Nofoil_FastFrame_20170123_merged.root"),[1.1,1.1,"G2",0.3152]]
    myfile["EJ200PS_1X2P_11-084d"]  = [
        "EJ200",TFile("root/AlphaSource/Pu239new_EJ200PS-1X2P_11_Default_Nofoil_FastFrame_20170220_merged.root"),[1.1,1.1,"G2",0.3152]]

    ## EJ260 PVT 1X2P
    myfile["EJ260PVT_1X2P_N1-UnIrr"] = [
        "EJ260",TFile("root/AlphaSource/Pu239new_EJ260PVT-1X2P_N1_Default_Nofoil_FastFrame_20161201_merged.root"),[1.3,1.1,"G2",0.3152]]
    myfile["EJ260PVT_1X2P_N3-003d"]  = [
        "EJ260",TFile("root/AlphaSource/Pu239new_EJ260PVT-1X2P_N3_Default_Nofoil_FastFrame_20161201_merged.root"),[1.1,1.1,"G2",0.3152]]
    myfile["EJ260PVT_1X2P_N3-007d"]  = [
        "EJ260",TFile("root/AlphaSource/Pu239new_EJ260PVT-1X2P_N3_Default_Nofoil_FastFrame_20161205_merged.root"),[1.1,1.1,"G2",0.3152]]
    myfile["EJ260PVT_1X2P_N3-014d"]  = [
        "EJ260",TFile("root/AlphaSource/Pu239new_EJ260PVT-1X2P_N3_Default_Nofoil_FastFrame_20161212_merged.root"),[1.1,1.1,"G2",0.3152]]
    myfile["EJ260PVT_1X2P_N3-056d"]  = [
        "EJ260",TFile("root/AlphaSource/Pu239new_EJ260PVT-1X2P_N3_Default_Nofoil_FastFrame_20170123_merged.root"),[1.1,1.1,"G2",0.3152]]
    myfile["EJ260PVT_1X2P_N3-084d"]  = [
        "EJ260",TFile("root/AlphaSource/Pu239new_EJ260PVT-1X2P_N3_Default_Nofoil_FastFrame_20170220_merged.root"),[1.1,1.1,"G2",0.3152]]

    ## EJ260 PS 1X2P
    myfile["EJ260PS_1X2P_1-UnIrr"] = [
        "EJ260",TFile("root/AlphaSource/Pu239new_EJ260PS-1X2P_1_Default_Nofoil_FastFrame_20161201_merged.root"),[1.3,1.1,"G2",0.3152]]
    myfile["EJ260PS_1X2P_8-003d"]  = [
        "EJ260",TFile("root/AlphaSource/Pu239new_EJ260PS-1X2P_8_Default_Nofoil_FastFrame_20161201_merged.root"),[1.1,1.1,"G2",0.3152]]
    myfile["EJ260PS_1X2P_8-007d"]  = [
        "EJ260",TFile("root/AlphaSource/Pu239new_EJ260PS-1X2P_8_Default_Nofoil_FastFrame_20161205_merged.root"),[1.1,1.1,"G2",0.3152]]
    myfile["EJ260PS_1X2P_8-014d"]  = [
        "EJ260",TFile("root/AlphaSource/Pu239new_EJ260PS-1X2P_8_Default_Nofoil_FastFrame_20161212_merged.root"),[1.1,1.1,"G2",0.3152]]
    myfile["EJ260PS_1X2P_8-056d"]  = [
        "EJ260",TFile("root/AlphaSource/Pu239new_EJ260PS-1X2P_8_Default_Nofoil_FastFrame_20170123_merged.root"),[1.1,1.1,"G2",0.3152]]
    myfile["EJ260PS_1X2P_8-084d"]  = [
        "EJ260",TFile("root/AlphaSource/Pu239new_EJ260PS-1X2P_8_Default_Nofoil_FastFrame_20170220_merged.root"),[1.1,1.1,"G2",0.3152]]


    ## Results calculated w.r.t. old ref (old scope config no longer available)
    plotSets = {}
    plotSets['EJ200PVT1X2P'] = ["EJ200PVT_1X2P_N1-UnIrr","EJ200PVT_1X2P_N11-003d","EJ200PVT_1X2P_N11-007d","EJ200PVT_1X2P_N11-014d","EJ200PVT_1X2P_N11-056d","EJ200PVT_1X2P_N11-084d"]
    plotSets['EJ200PS1X2P'] = ["EJ200PS_1X2P_1-UnIrr","EJ200PS_1X2P_11-003d","EJ200PS_1X2P_11-007d","EJ200PS_1X2P_11-014d","EJ200PS_1X2P_11-056d","EJ200PS_1X2P_11-084d"]

    DrawDvsTHist(myfile, plotSets, outDir, "%s"%(sampleSet), fTag, doselabel, hxrng, options, "EJ200", "GSFC", debug)


    plotSetsA = {}
    plotSetsA['EJ260PVT1X2P'] = ["EJ260PVT_1X2P_N1-UnIrr","EJ260PVT_1X2P_N3-003d","EJ260PVT_1X2P_N3-007d","EJ260PVT_1X2P_N3-014d","EJ260PVT_1X2P_N3-056d","EJ260PVT_1X2P_N3-084d"]
    plotSetsA['EJ260PS1X2P'] = ["EJ260PS_1X2P_1-UnIrr","EJ260PS_1X2P_8-003d","EJ260PS_1X2P_8-007d","EJ260PS_1X2P_8-014d","EJ260PS_1X2P_8-056d","EJ260PS_1X2P_8-084d"]

    DrawDvsTHist(myfile, plotSetsA, outDir, "%s"%(sampleSet), fTag, doselabel, hxrng, options, "EJ260N", "GSFC", debug)

