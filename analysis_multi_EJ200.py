#!/usr/bin/python
import os, sys, math
from ROOT import gROOT, gStyle, TFile, TTree, TH1, TH1F, TH1D, TCanvas, TPad, TMath, TF1, TLegend, gPad, gEnv
from ROOT import kRed, kBlue, kGreen, kWhite
#gEnv.SetValue("Canvas.SavePrecision", "16")
#TH1F.SetDefaultSumw2(True)

import datetime
sys.path.append(os.path.abspath(os.path.curdir))
from Plotter import parseLYAnaInputArgs
options = parseLYAnaInputArgs()

from collections import OrderedDict
from Plotter import utils

from Plotter.CommonTools import CalcD
from Plotter.CommonToolsCosmic import LYCosmicAna, EstimateSPE, PrintResults, PrintResults2
import numpy as np

gROOT.Reset()
gROOT.LoadMacro("Plotter/UMDStyle.C")
from ROOT import SetUMDStyle
SetUMDStyle()
gStyle.SetStatBorderSize(1)

##gStyle.SetNdivisions(305, "X")
##gStyle.SetNdivisions(305, "Y")
###gStyle.SetTitleFont(82, "xy")
##gStyle.SetTitleSize(0.06, "x")
##gStyle.SetTitleSize(0.06, "y")
##gStyle.SetLabelSize(0.04, "y")
##gStyle.SetTitleOffset(1., "x")
##gStyle.SetTitleOffset(1.1, "y")


####################################################################################################
####################################################################################################
if __name__ == '__main__':

    print options
    myfile  = {}
    mytree  = {}
    valPhys = {}
    myHists = {}
    valsyst = {}
    runSyst = False

    dosescheme_ = "GSFC"
    doselabel_  = "0.38 Mrad@ 0.3 krad/hr"

    fitrng = {}
    ## S10362-33-050C EJ200
    fitrng["amp"]   = [250,-0.05,0.75] # energy_amp in V*ns
    fitrng["ped"]   = [100,-1.0,0.0]   # energy_ped in V*ns
    fitrng["sig"]   = [20,-0.5,25.]    # energy_sig in V*ns
    fitrng["eng"]   = [10,-2.0,160.]   # energy_all in Npe
    fitrng["plot"]  = [10,-2.0,200.]   # energy_all in Npe
    fitrng["stats"] = [0.65,0.65,0.92,0.92]   # stats box pos/size

    today = datetime.date.today()
    fTag_ = today.strftime("%Y%m%d")
    fTag_ = "%s_p%s"%(options.outtag,fTag_)
    sampleSet_ = options.sampleSet

    print "[Run Init] Pedestal cuts:",options.myPedCut
    mypedcut = options.myPedCut.split(",")

    print len(options.input)
    if (len(options.input)==0):
        if (options.input==None):
            options.input=raw_input("Enter the list file name: ")
            print options.input
            print options.input[len(options.input)-4:]
            if (len(options.input)>=4 and
                options.input[len(options.input)-4:]==".txt"):
                options.input=options.input[0:len(options.input)-4]

        print "Input list file: ",options.input


    list_input = open("Runfiles/%s.txt"%options.input)            

    ## Estimate SPE first
    vSPE = EstimateSPE(list_input,mypedcut,fTag_,fitrng,options)
    muSPE = np.mean(vSPE)
    print "*"*150
    print "Single PE position = %8.5f [V x ns]"%muSPE
    print "*"*150
    #exit()

    fidx=0
    myinputs={}
    ana = {}
    list_input.seek(0)
    for line in list_input:
        tline=[]
        tline = line.split(" ")
        ##print tline[0], tline[1]
        if tline[0].find("#") != -1: continue
        fileName = tline[0]
        print "+"*150
        print "+"*150
        print ">>>>>>> Processing files [ %-100s]"%fileName
        tmpTxt = (line.split("/")[1]).replace("-","_").replace(" ","_")
        sampleName = tline[1]
        sample = tline[1].split("-")[0]
        print "Sample Name:", sampleName
        print "TagName:", fTag_

        if(len(fileName)>=4 and (fileName[len(fileName)-4:]==".out" or fileName[len(fileName)-4:]==".txt")):
            fileName=fileName[:len(fileName)-4]

        if len(tline) == 5:
            myinputs[fileName]=(tline[2],sampleName,tline[3],tline[4].rstrip("\n"),int(fidx))
        elif len(tline) == 4:
            myinputs[fileName]=(tline[2],sampleName,tline[3].rstrip("\n"),"1",int(fidx))
        else:
            print "Missing items in input txt file [%f]. Make sure each line contains: filename title order color style."%fileName
            exit()

        valPhys[sampleName] = {}
        myHists[sampleName] = {}
        ## use lase available pedcut as default
        if fidx > len(mypedcut)-1: mypedcut.append(mypedcut[len(mypedcut)-1])
        ana[sampleName] = LYCosmicAna(fileName,sampleName,options,mypedcut[fidx],fTag_,options.verbose)
        ana[sampleName].SPE = muSPE
        valPhys[sampleName], myHists[sampleName] = ana[sampleName].run_energy_all2(fitrange=fitrng)

        fidx+=1
        print "\n\n"

        ## DEBUG only
        if options.verbose:
            print "*"*150
            print valPhys[sampleName]
            print "*"*150
            print myHists[sampleName]
            print "*"*150

    print "*"*150
    for n,v in sorted(valPhys.items()):
        print "[Nominal] %-25s : <N_{PE}> = %s"%(n,"%1.4f +/- %1.4f"%v["npe"])

    print "*"*150
    #############################################################################################
    ## Calculate dose constant: light loss = exp (-dose/D); D = dose constant
    #############################################################################################
    print "\n"
    print "="*150
    uncEng_  = {}
    uncFit_  = {}
    vDconst_ = {}
    vInput_  = {}
    refPlots_ = []
    irrPlots_ = []

    ###############################
    # dose
    # Note: sigma_d = 1.6% (NIST);
    # 20% for Castor table; 5% for UMD high dose;
    # Goddard (GSFC) 10% temporary
    ###############################
    vDose_ = {}
    vDose_["NIST"]  = [2.95,0.016]
    vDose_["NIST1"] = [4.00,0.017]
    vDose_["NIST2"] = [5.82,0.016]
    vDose_["NIST3"] = [6.95,0.017]
    vDose_["NIST4"] = [7.00,0.017]
    vDose_["CT"]    = [0.24,0.2]   # 2015
    #vDose_["CT16"]  = [0.xx,0.yy] # 2016 unknown
    vDose_["UMD30"] = [30.0,0.05]
    vDose_["UMD50"] = [50.0,0.05]
    vDose_["GSFC"]  = [0.38,0.038]

    vOffset = [0.,0.]

    ###############################################
    ## Calculate measurement uncertainty:
    ###############################################
    vposPed = {}
    vRefNpe = {}
    uncMeas = {}
    for key_,val_ in sorted(myinputs.items(), key=lambda x: x[1]):
        sampleName = val_[1]
        #print ">>>> samplaName = %s : val_[0] = %s"%(sampleName,val_[0])
        mu_nPE, sig_nPE = valPhys[sampleName]["npe"]
        if val_[0]=="0": #get uncEng_[Un-irr ref]
            refPlots_.append(sampleName)
            ## FIXME: currently used ped/sig peaks and fit uncertainties of ref measurement as measurement uncertainty.
            ## Need to investigate whether to include more measurements.
            ## 2% is used for temperature dependence uncertainty; this maybe under-estimated; need better estimation
            vposPed[sampleName] = valPhys[sampleName]["ped"]
            vRefNpe[sampleName] = mu_nPE-vposPed[sampleName][0]
            uncMeas[sampleName] = math.sqrt(math.pow(sig_nPE/mu_nPE,2)+0.02*0.02)

    if options.verbose:
        print uncMeas.values()
        print vposPed.values()
        print vRefNpe.values()
    if len(uncMeas.values())==1:
        uncEng_["Measurement"]=uncMeas.values()[0]
        vOffset = vposPed.values()[0]
        print vOffset
    else:
        uncEng_["Measurement"]=np.std(vRefNpe.values())/np.mean(vRefNpe.values())
        vOffset[0] = (np.mean(vposPed.values(),axis=0))[0]
        vOffset[1] = (np.std(vposPed.values(),axis=0))[0]
        
    print "Uncertainty of %-34s = %-6.3f %%"%("data taking measurement",uncEng_["Measurement"]*100.)
    if options.verbose: print vOffset
    ###############################################
    ## Calculate uncertainties of separate samples:
    ###############################################
    for key_,val_ in sorted(myinputs.items(), key=lambda x: x[1]):
        sampleName = val_[1]
        if val_[0]!="0": irrPlots_.append(sampleName)
        if options.verbose: print ">>>> samplaName = %s : val_[0] = %s"%(sampleName,val_[0])
        mu_nPE, sig_nPE = valPhys[sampleName]["npe"]
        uncFit_[sampleName] = sig_nPE/mu_nPE
        print "Fit uncertainty of %-30s = %-6.3f %%"%("%s"%sampleName,uncFit_[sampleName]*100.)
        uncEng_[sampleName]  = math.sqrt(math.pow(uncEng_["Measurement"],2)+math.pow(uncFit_[sampleName],2))
        vInput_[sampleName]  = [mu_nPE, uncEng_[sampleName]*mu_nPE]

    ## print uncertainties
    print "*"*150
    print ">>>>>>>>>>>>> %-35s = %-8.5f"%("Offset",vOffset[0])
    print "*"*150
    print "Uncertainty of [ %-31s] = %6.3f %%"%("Offset",math.fabs(vOffset[1]*100.))
    for n,v in sorted(uncEng_.items()):
        ## Tot. unc. = meas. unc. + fit unc.
        if n.find("Measurement")==-1:
            print "Uncertainty of [ %-31s] = %6.3f %%"%(n,v*100.)

    ###############################
    # The calculation
    # CalcD(dose,v_o,v_i,offset,uncV)
    ###############################
    print irrPlots_
    ## Loop un-irr samples
    header_ = "" ## FIXME currently only good for one kind of sample
    for refName in refPlots_:
        vDconst_[refName]={}
        ## Loop irradiated samples
        for sampleName in irrPlots_:
            #if options.verbose:
            print ">>>> samplaName = %s"%(sampleName)
            print "="*50
            print ">>>>>>>>>> Calculating Dose Constant for :", sampleName
            sample_ = "%s"%(sampleName.split("-")[0])
            header_ = "%s-%s"%(sample_.split("_")[0],sample_.split("_")[1])
            tag_ = "%s_%s"%(sample_,refName)
            vDconst_[refName][sampleName] = CalcD(vDose_[dosescheme_],vInput_[sampleName],vInput_[refName],vOffset,"Cosmic")

        ## Print all results for each ref separately
        PrintResults(vDconst_[refName], vInput_, vOffset, sampleSet_, header_, doselabel_, [refName], irrPlots_, fTag_, options)

    ## Print all results in one go
    PrintResults2(vDconst_, vInput_, vOffset, sampleSet_, header_, doselabel_, refPlots_, irrPlots_, fTag_, options)

    print "\n\n"
    print "="*150
    print "="*150


    ##############
    ## Final check
    ##############
    if options.verbose:
        print "*"*150
        print valPhys
        print "*"*150
        print myHists
        print "*"*150

    ######################
    ## Save all histograms
    ######################
    fileTag = "_".join((options.input).split("_")[1:])

    fout = "Results/hists/%s_pedCut%s_%s.root"%(fileTag,("_".join(options.myPedCut.split(","))).replace(".","p"),fTag_)
    for data in myHists.values():
        if isinstance(data,dict):
            print data.keys()
            for h in data.values():
                if isinstance(h,list):
                    print hh
                    for hh in h: utils.save_object(hh,fout)
                elif isinstance(h,TH1):
                    print h
                    utils.save_object(h,fout)
        elif isinstance(data,list):
            print data
            for h in data: utils.save_object(h,fout)
        elif isinstance(data,TH1):
            print data
            utils.save_object(data,fout)
        else:
            print 'Type of data is not implemented, which is %s'%(type(data))
