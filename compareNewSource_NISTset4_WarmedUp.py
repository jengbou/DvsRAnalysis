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

    ## NISTset4
    sampleSet = "NISTset4"
    #doselabel = "#splitline{7 Mrad@ 74.9 krad/hr@ -30#circC;}{115 days aft. irr. (14 days aft. warmed up}"
    doselabel = "7 Mrad@ 74.9 krad/hr@ -30#circC"

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
    ## [1.3,1.1,0,0.3112]

    ## PVT 1X1P
    myfile["EJ200PVT_1X1P_N1-UnIrr"] = [
        "EJ200",TFile("root/AlphaSource/Pu239new_EJ200PVT-1X1P_N1_Default_Nofoil_FastFrame_20170122_merged.root"),[1.3,1.1,"G2",0.3112]]
    myfile["EJ200PVT_1X1P_N3-099d"]  = [
        "EJ200",TFile("root/AlphaSource/Pu239new_EJ200PVT-1X1P_N3_Default_Nofoil_FastFrame_20170224_merged.root"),[1.1,1.1,"G2",0.3112]]
    myfile["EJ200PVT_1X1P_N3-115d"]  = [
        "EJ200",TFile("root/AlphaSource/Pu239new_EJ200PVT-1X1P_N3_Default_Nofoil_FastFrame_20170310_merged.root"),[1.1,1.1,"G2",0.3112]]
    myfile["EJ200PVT_1X1P_N3-136d"]  = [
        "EJ200",TFile("root/AlphaSource/Pu239new_EJ200PVT-1X1P_N3_Default_Nofoil_FastFrame_20170331_merged.root"),[1.1,1.1,"G2",0.3112]]
    myfile["EJ200PVT_1X1P_N3-150d"]  = [
        "EJ200",TFile("root/AlphaSource/Pu239new_EJ200PVT-1X1P_N3_Default_Nofoil_FastFrame_20170414_merged.root"),[1.1,1.1,"G2",0.3112]]
    myfile["EJ200PVT_1X1P_N3-199d"]  = [
        "EJ200",TFile("root/AlphaSource/Pu239new_EJ200PVT-1X1P_N3_Default_Nofoil_FastFrame_20170602_merged.root"),[1.1,1.1,"G2",0.3112]]

    ## PVT 1X2P
    myfile["EJ200PVT_1X2P_N1-UnIrr"] = [
        "EJ200",TFile("root/AlphaSource/Pu239new_EJ200PVT-1X2P_N1_Default_Nofoil_FastFrame_20170122_merged.root"),[1.3,1.1,"G2",0.3112]]
    myfile["EJ200PVT_1X2P_N3-099d"]  = [
        "EJ200",TFile("root/AlphaSource/Pu239new_EJ200PVT-1X2P_N3_Default_Nofoil_FastFrame_20170224_merged.root"),[1.1,1.1,"G2",0.3112]]
    myfile["EJ200PVT_1X2P_N3-115d"]  = [
        "EJ200",TFile("root/AlphaSource/Pu239new_EJ200PVT-1X2P_N3_Default_Nofoil_FastFrame_20170310_merged.root"),[1.1,1.1,"G2",0.3112]]
    myfile["EJ200PVT_1X2P_N3-136d"]  = [
        "EJ200",TFile("root/AlphaSource/Pu239new_EJ200PVT-1X2P_N3_Default_Nofoil_FastFrame_20170331_merged.root"),[1.1,1.1,"G2",0.3112]]
    myfile["EJ200PVT_1X2P_N3-150d"]  = [
        "EJ200",TFile("root/AlphaSource/Pu239new_EJ200PVT-1X2P_N3_Default_Nofoil_FastFrame_20170414_merged.root"),[1.1,1.1,"G2",0.3112]]
    myfile["EJ200PVT_1X2P_N3-199d"]  = [
        "EJ200",TFile("root/AlphaSource/Pu239new_EJ200PVT-1X2P_N3_Default_Nofoil_FastFrame_20170602_merged.root"),[1.1,1.1,"G2",0.3112]]

    ## PS 1X1P
    myfile["EJ200PS_1X1P_1-UnIrr"] = [
        "EJ200",TFile("root/AlphaSource/Pu239new_EJ200PS-1X1P_1_Default_Nofoil_FastFrame_20170122_merged.root"),[1.3,1.1,"G2",0.3112]]
    myfile["EJ200PS_1X1P_3-099d"]  = [
        "EJ200",TFile("root/AlphaSource/Pu239new_EJ200PS-1X1P_3_Default_Nofoil_FastFrame_20170224_merged.root"),[1.1,1.1,"G2",0.3112]]
    myfile["EJ200PS_1X1P_3-115d"]  = [
        "EJ200",TFile("root/AlphaSource/Pu239new_EJ200PS-1X1P_3_Default_Nofoil_FastFrame_20170310_merged.root"),[1.1,1.1,"G2",0.3112]]
    myfile["EJ200PS_1X1P_3-136d"]  = [
        "EJ200",TFile("root/AlphaSource/Pu239new_EJ200PS-1X1P_3_Default_Nofoil_FastFrame_20170331_merged.root"),[1.1,1.1,"G2",0.3112]]
    myfile["EJ200PS_1X1P_3-150d"]  = [
        "EJ200",TFile("root/AlphaSource/Pu239new_EJ200PS-1X1P_3_Default_Nofoil_FastFrame_20170414_merged.root"),[1.1,1.1,"G2",0.3112]]
    myfile["EJ200PS_1X1P_3-199d"]  = [
        "EJ200",TFile("root/AlphaSource/Pu239new_EJ200PS-1X1P_3_Default_Nofoil_FastFrame_20170602_merged.root"),[1.1,1.1,"G2",0.3112]]

    ## PS 1X2P
    myfile["EJ200PS_1X2P_1-UnIrr"] = [
        "EJ200",TFile("root/AlphaSource/Pu239new_EJ200PS-1X2P_1_Default_Nofoil_FastFrame_20170122_merged.root"),[1.3,1.1,"G2",0.3112]]
    myfile["EJ200PS_1X2P_3-099d"]  = [
        "EJ200",TFile("root/AlphaSource/Pu239new_EJ200PS-1X2P_3_Default_Nofoil_FastFrame_20170224_merged.root"),[1.1,1.1,"G2",0.3112]]
    myfile["EJ200PS_1X2P_3-115d"]  = [
        "EJ200",TFile("root/AlphaSource/Pu239new_EJ200PS-1X2P_3_Default_Nofoil_FastFrame_20170310_merged.root"),[1.1,1.1,"G2",0.3112]]
    myfile["EJ200PS_1X2P_3-136d"]  = [
        "EJ200",TFile("root/AlphaSource/Pu239new_EJ200PS-1X2P_3_Default_Nofoil_FastFrame_20170331_merged.root"),[1.1,1.1,"G2",0.3112]]
    myfile["EJ200PS_1X2P_3-150d"]  = [
        "EJ200",TFile("root/AlphaSource/Pu239new_EJ200PS-1X2P_3_Default_Nofoil_FastFrame_20170414_merged.root"),[1.1,1.1,"G2",0.3112]]
    myfile["EJ200PS_1X2P_3-199d"]  = [
        "EJ200",TFile("root/AlphaSource/Pu239new_EJ200PS-1X2P_3_Default_Nofoil_FastFrame_20170602_merged.root"),[1.1,1.1,"G2",0.3112]]


    ## Results calculated w.r.t. old ref (old scope config no longer available)
    plotSets = {}
    plotSets['EJ200PVT1X1P'] = ["EJ200PVT_1X1P_N1-UnIrr","EJ200PVT_1X1P_N3-099d","EJ200PVT_1X1P_N3-115d","EJ200PVT_1X1P_N3-136d","EJ200PVT_1X1P_N3-150d","EJ200PVT_1X1P_N3-199d"]
    plotSets['EJ200PVT1X2P'] = ["EJ200PVT_1X2P_N1-UnIrr","EJ200PVT_1X2P_N3-099d","EJ200PVT_1X2P_N3-115d","EJ200PVT_1X2P_N3-136d","EJ200PVT_1X2P_N3-150d","EJ200PVT_1X2P_N3-199d"]
    plotSets['EJ200PS1X1P'] = ["EJ200PS_1X1P_1-UnIrr","EJ200PS_1X1P_3-099d","EJ200PS_1X1P_3-115d","EJ200PS_1X1P_3-136d","EJ200PS_1X1P_3-150d","EJ200PS_1X1P_3-199d"]
    plotSets['EJ200PS1X2P'] = ["EJ200PS_1X2P_1-UnIrr","EJ200PS_1X2P_3-099d","EJ200PS_1X2P_3-115d","EJ200PS_1X2P_3-136d","EJ200PS_1X2P_3-150d","EJ200PS_1X2P_3-199d"]

    #DrawDvsTHist(myfile, plotSets, outDir, "%s"%(sampleSet), fTag, doselabel, hxrng, options, "EJ200", "NIST4", debug)
    DrawDvsTHist(myfile, plotSets, outDir, "%s"%(sampleSet), fTag, doselabel, hxrng, options, "EJ200SP1P", "NIST4", debug)



