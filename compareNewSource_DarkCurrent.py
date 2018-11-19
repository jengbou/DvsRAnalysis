#!/usr/bin/python
import os, sys, math, datetime
from ROOT import gROOT, gStyle, TFile, TTree, TH1F, TH1D, TCanvas, TPad, TMath, TF1, TLegend, gPad, gDirectory
from ROOT import kRed, kBlue, kGreen, kWhite

from collections import OrderedDict
import numpy

sys.path.append(os.path.abspath(os.path.curdir))

from Plotter import parseLYAnaInputArgs
options = parseLYAnaInputArgs()

from Plotter.CommonTools import CalcD, AlphaSourceFitter

gROOT.SetBatch()
gROOT.LoadMacro("Plotter/AtlasStyle.C")
from ROOT import SetAtlasStyle
SetAtlasStyle()

####################################################################################################
####################################################################################################
if __name__ == '__main__':
    #gROOT.SetStyle("Plain")
    #gStyle.SetOptFit()
    #gStyle.SetOptStat(0)
    print options
    myfile = {}
    mytree = {}
    myhist = {}
    myfit = {}
    valphys = {}
    valsyst = {}
    vEng   = {}
    uncEng = {}
    sFit   = {}
    uncFit = {}
    valphys = {}
    valsyst = {}
    runSyst = False
    mypedcut = 0.0
    if options.myPedCut:
        mypedcut = float(options.myPedCut)


    fitter_ = AlphaSourceFitter()
    GausFitEngPeak = fitter_.GausFitEngPeak
    TwoGausFitEngPeak = fitter_.TwoGausFitEngPeak

    ## Dark Current
    ## Random trigger 43 ms
    myfile["DC_AT43ms_1"] = TFile("root/AlphaSource/DarkCurrent_AutoTrig43ms_20160816.root")
    mytree["DC_AT43ms_1"] = myfile["DC_AT43ms_1"].Get("tree")

    myfile["DC_AT43ms_2"] = TFile("root/AlphaSource/DarkCurrent_AutoTrig43ms_20160817.root")
    mytree["DC_AT43ms_2"] = myfile["DC_AT43ms_2"].Get("tree")

    ## Dark Current
    ## Random trigger 60 ms
    myfile["DC_AT60ms_1"] = TFile("root/AlphaSource/DarkCurrent_AutoTrig60ms_20160816.root")
    mytree["DC_AT60ms_1"] = myfile["DC_AT60ms_1"].Get("tree")

    myfile["DC_AT60ms_2"] = TFile("root/AlphaSource/DarkCurrent_AutoTrig60ms_20160817.root")
    mytree["DC_AT60ms_2"] = myfile["DC_AT60ms_2"].Get("tree")

    ## Dark Current
    ## Random trigger 2 ms
    myfile["DC_AT2ms_1"] = TFile("root/AlphaSource/DarkCurrent_AutoTrig2ms_20160817.root")
    mytree["DC_AT2ms_1"] = myfile["DC_AT2ms_1"].Get("tree")

    c1 = TCanvas("c1","c1",800,600)


    ## 43 ms
    myhist["DC_AT43ms_1"] = TH1D("myhist_DC_AT43ms_1","DC_AT43ms_1",51,-0.1,0.3)
    mytree["DC_AT43ms_1"].Draw("areaFromScope>>myhist_DC_AT43ms_1","time > 3600 && abs(amplitude)>%f"%mypedcut)

    myhist["DC_AT43ms_1p"] = TH1D("myhist_DC_AT43ms_1p","DC_AT43ms_1p",141,-0.2,2.)
    mytree["DC_AT43ms_1"].Draw("areaFromScope>>myhist_DC_AT43ms_1p","time > 3600 && abs(amplitude)>%f"%mypedcut)

    myhist["DC_AT43ms_2"] = TH1D("myhist_DC_AT43ms_2","DC_AT43ms_2",51,-0.1,0.3)
    mytree["DC_AT43ms_2"].Draw("areaFromScope>>myhist_DC_AT43ms_2","time > 3600 && abs(amplitude)>%f"%mypedcut)

    myhist["DC_AT43ms_2p"] = TH1D("myhist_DC_AT43ms_2p","DC_AT43ms_2p",141,-0.2,2.)
    mytree["DC_AT43ms_2"].Draw("areaFromScope>>myhist_DC_AT43ms_2p","time > 3600 && abs(amplitude)>%f"%mypedcut)

    ## 60 ms
    myhist["DC_AT60ms_1"] = TH1D("myhist_DC_AT60ms_1","DC_AT60ms_1",51,-0.1,0.3)
    mytree["DC_AT60ms_1"].Draw("areaFromScope>>myhist_DC_AT60ms_1","time > 3600 && abs(amplitude)>%f"%mypedcut)

    myhist["DC_AT60ms_1p"] = TH1D("myhist_DC_AT60ms_1p","DC_AT60ms_1p",141,-0.2,2.)
    mytree["DC_AT60ms_1"].Draw("areaFromScope>>myhist_DC_AT60ms_1p","time > 3600 && abs(amplitude)>%f"%mypedcut)

    myhist["DC_AT60ms_2"] = TH1D("myhist_DC_AT60ms_2","DC_AT60ms_2",51,-0.1,0.3)
    mytree["DC_AT60ms_2"].Draw("areaFromScope>>myhist_DC_AT60ms_2","time > 3600 && abs(amplitude)>%f"%mypedcut)

    myhist["DC_AT60ms_2p"] = TH1D("myhist_DC_AT60ms_2p","DC_AT60ms_2p",141,-0.2,2.)
    mytree["DC_AT60ms_2"].Draw("areaFromScope>>myhist_DC_AT60ms_2p","time > 3600 && abs(amplitude)>%f"%mypedcut)


    ## 2 ms
    myhist["DC_AT2ms_1"] = TH1D("myhist_DC_AT2ms_1","DC_AT2ms_1",51,-0.1,0.3)
    mytree["DC_AT2ms_1"].Draw("areaFromScope>>myhist_DC_AT2ms_1","time > 100 && abs(amplitude)>%f"%mypedcut)

    myhist["DC_AT2ms_1p"] = TH1D("myhist_DC_AT2ms_1p","DC_AT2ms_1p",141,-0.2,2.)
    mytree["DC_AT2ms_1"].Draw("areaFromScope>>myhist_DC_AT2ms_1p","time > 100 && abs(amplitude)>%f"%mypedcut)



    ###############################
    ## Normalized to same number of events
    nevt_num = myhist["DC_AT43ms_1p"].Integral()
    print nevt_num
    nscale = 1.


    ###############################
    ## first plot

    ###############################
    ## Dark current
    ###############################
    nevt_den = myhist["DC_AT43ms_1p"].Integral()
    print nevt_den
    nscale = float(nevt_num)/float(nevt_den)
    print nscale

    ## for plot only
    myhist["DC_AT43ms_1p"].Scale(nscale)
    myhist["DC_AT43ms_1p"].SetLineColor(1)
    myhist["DC_AT43ms_1p"].SetLineStyle(1)
    myhist["DC_AT43ms_1p"].Draw()

    ## for fit only
    myhist["DC_AT43ms_1"].Scale(nscale)
    myhist["DC_AT43ms_1"].SetLineColor(1)
    myhist["DC_AT43ms_1"].SetLineStyle(2)

    ## Find overall max (this is energy offset)
    sigName = "DC_AT43ms_1"
    vEng[sigName],sFit[sigName],myfit[sigName]=GausFitEngPeak(myhist[sigName],sigName,[0.2,0.2],nscale)

    ###############################
    ## Needed for the first plot ##
    myhist["DC_AT43ms_1p"].GetXaxis().SetTitle("Energy [V#timesns]")
    myhist["DC_AT43ms_1p"].GetYaxis().SetTitle("A.U.")
    ##myhist["DC_AT43ms_1p"].GetYaxis().SetRangeUser(1.,1.e7)

    gPad.SetLogy()
    gPad.Update()
    c1.Update()
    ## Needed for the first plot ##
    ###############################


    ###############################
    ## 43 ms try2
    nevt_den = myhist["DC_AT43ms_2p"].Integral()
    print nevt_den
    nscale = float(nevt_num)/float(nevt_den)
    print nscale

    ## for plot only
    myhist["DC_AT43ms_2p"].Scale(nscale)
    myhist["DC_AT43ms_2p"].SetLineColor(2)
    myhist["DC_AT43ms_2p"].SetLineStyle(1)
    myhist["DC_AT43ms_2p"].Draw("same")

    ## for fit only
    myhist["DC_AT43ms_2"].Scale(nscale)
    myhist["DC_AT43ms_2"].SetLineColor(2)
    myhist["DC_AT43ms_2"].SetLineStyle(2)

    ## Find overall max (this is energy offset)
    sigName = "DC_AT43ms_2"
    vEng[sigName],sFit[sigName],myfit[sigName]=GausFitEngPeak(myhist[sigName],sigName,[0.2,0.2],nscale)


    ###############################
    ## 60 ms
    nevt_den = myhist["DC_AT60ms_1p"].Integral()
    print nevt_den
    nscale = float(nevt_num)/float(nevt_den)
    print nscale

    ## for plot only
    myhist["DC_AT60ms_1p"].Scale(nscale)
    myhist["DC_AT60ms_1p"].SetLineColor(4)
    myhist["DC_AT60ms_1p"].SetLineStyle(1)
    myhist["DC_AT60ms_1p"].Draw("same")

    ## for fit only
    myhist["DC_AT60ms_1"].Scale(nscale)
    myhist["DC_AT60ms_1"].SetLineColor(4)
    myhist["DC_AT60ms_1"].SetLineStyle(2)

    ## Find overall max (this is energy offset)
    sigName = "DC_AT60ms_1"
    vEng[sigName],sFit[sigName],myfit[sigName]=GausFitEngPeak(myhist[sigName],sigName,[0.2,0.2],nscale)



    ###############################
    ## 60 ms try2
    nevt_den = myhist["DC_AT60ms_2p"].Integral()
    print nevt_den
    nscale = float(nevt_num)/float(nevt_den)
    print nscale

    ## for plot only
    myhist["DC_AT60ms_2p"].Scale(nscale)
    myhist["DC_AT60ms_2p"].SetLineColor(6)
    myhist["DC_AT60ms_2p"].SetLineStyle(1)
    myhist["DC_AT60ms_2p"].Draw("same")

    ## for fit only
    myhist["DC_AT60ms_2"].Scale(nscale)
    myhist["DC_AT60ms_2"].SetLineColor(6)
    myhist["DC_AT60ms_2"].SetLineStyle(2)

    ## Find overall max (this is energy offset)
    sigName = "DC_AT60ms_2"
    vEng[sigName],sFit[sigName],myfit[sigName]=GausFitEngPeak(myhist[sigName],sigName,[0.2,0.2],nscale)



    ###############################
    ## 2 ms
    nevt_den = myhist["DC_AT2ms_1p"].Integral()
    print nevt_den
    nscale = float(nevt_num)/float(nevt_den)
    print nscale

    ## for plot only
    myhist["DC_AT2ms_1p"].Scale(nscale)
    myhist["DC_AT2ms_1p"].SetLineColor(8)
    myhist["DC_AT2ms_1p"].SetLineStyle(1)
    myhist["DC_AT2ms_1p"].Draw("same")

    ## for fit only
    myhist["DC_AT2ms_1"].Scale(nscale)
    myhist["DC_AT2ms_1"].SetLineColor(8)
    myhist["DC_AT2ms_1"].SetLineStyle(2)

    ## Find overall max (this is energy offset)
    sigName = "DC_AT2ms_1"
    vEng[sigName],sFit[sigName],myfit[sigName]=GausFitEngPeak(myhist[sigName],sigName,[0.2,0.2],nscale)


    ###############################
    ## Legend
    ###############################
    leg = TLegend(0.42,0.65,0.9,0.93)
    leg.SetFillColor(kWhite)
    leg.SetLineColor(kWhite)

    leg.AddEntry(myhist["DC_AT43ms_1p"],"Dark Current (43 ms)","l")
    leg.AddEntry(myhist["DC_AT43ms_2p"],"Dark Current (43 ms; try2)","l")

    leg.AddEntry(myhist["DC_AT60ms_1p"],"Dark Current (60 ms)","l")
    leg.AddEntry(myhist["DC_AT60ms_2p"],"Dark Current (60 ms; try2)","l")

    leg.AddEntry(myhist["DC_AT2ms_1p"],"Dark Current (2 ms)","l")

    leg.Draw()

    today = datetime.date.today()
    fTag = today.strftime("%Y%m%d")
    fnameTag = "%s_p%s"%(options.outtag,fTag)

    c1.SaveAs("Results/comp_newsource/DarkCurrent_eng_%s.png"%fnameTag)
    c1.SaveAs("Results/comp_newsource/DarkCurrent_eng_%s.pdf"%fnameTag)
    c1.SaveAs("Results/comp_newsource/DarkCurrent_eng_%s.root"%fnameTag)

