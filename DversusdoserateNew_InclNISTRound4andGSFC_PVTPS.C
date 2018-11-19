#include <map>
#include "TObject.h"


void DversusdoserateNew_InclNISTRound4andGSFC_PVTPS() {
    // Preambles
    gROOT->SetStyle("UMD");
    // overwrite style para
    gStyle->SetEndErrorSize(2.5);
    gStyle->SetPadTickX(0);

    //gStyle->SetPadTopMargin(0.05);
    gStyle->SetPadRightMargin(0.02);
    //gStyle->SetPadBottomMargin(0.16);
    gStyle->SetPadLeftMargin(0.12);
    //gStyle->SetTitleXOffset(1.4);
    gStyle->SetTitleYOffset(1.2);

    TString tagTime("20181116_InclNISTRound4andGSFC_PVTPS");
    std::cout << "File date tag = " << tagTime << std::endl;

    // ======================================================================================================
    // Begin of results section
    // ======================================================================================================
    // The section containing all data
    map<string,int> colors_;
    colors_["insitu"] = 9;


    // ********************************************************
    // From Marek (CMS in-situ)
    // ********************************************************
    // CMS laser insitu data layer 1
    const Int_t n = 7;
    Float_t x[n]  = {0.00426,0.00639,0.00972,0.0146,0.0253,0.0399,0.0639};
    Float_t y[n]  = {0.0909,0.119,0.15,0.173,0.237,0.339,0.322};
    Float_t ex[n] = {0.,0.,0.,0.,0.,0.,0.};
    Float_t ey[n] = {0.,0.,0.,0.,0.,0.,0.};

    // CMS laser insitu data layer 7
    const Int_t n4 = 7;
    Float_t x4[n4]  = {0.000342,0.000746,0.000972,0.00172,0.00318,0.00543,0.0194};
    Float_t y4[n4]  = {0.0218,0.0363,0.0412,0.0477,0.0767,0.112,0.1796};
    Float_t ex4[n4] = {0.,0.,0.,0.,0.,0.,0.};
    Float_t ey4[n4] = {0.,0.,0.,0.,0.,0.,0.};


    // 2012 points for towers 27,28,29 depth 2; these use new rate & FLUKA
    const Int_t n5c = 3;
    Float_t x5c[n5c]  = {0.02,0.035,0.058};
    Float_t y5c[n5c]  = {0.35,0.22,0.5};
    Float_t ex5c[n5c] = {0.,0.,0.};
    Float_t ey5c[n5c] = {0.,0.,0.};
    // add depth 1 points (from Dan); using Fluka & new rate
    const Int_t n5d = 10;
    Float_t x5d[n5d]  = {0.0019,0.0026,0.0036,0.0052,0.0075,0.013,0.02,0.04,0.06,0.12};
    Float_t y5d[n5d]  = {0.08,0.08,0.08,0.11,0.12,0.15,0.18,0.33,0.34,0.78};
    Float_t ex5d[n5d] = {0.,0.,0.,0.,0.,0.,0.,0.,0.,0.};
    Float_t ey5d[n5d] = {0.,0.,0.,0.,0.,0.,0.,0.,0.,0.};

    // insitu data 14 TeV
    const Int_t n5 = 1;
    Float_t x5[n5]  = {0.0195};
    Float_t y5[n5]  = {0.25};
    Float_t ex5[n5] = {0.};
    Float_t ey5[n5] = {0.};
    // ********************************************************


    // ********************************************************
    //  UMD alpha source
    // ********************************************************

    // NIST room temperature (23 degree C)
    // ********************************************************
    // 1X1P


    // ********************************************************
    // EJ200PVT-1X1P 7Mrad (NIST4)
    const Int_t n7 = 2;//N5, N9
    Float_t x7[n7]  = {8.53,390};
    Float_t y7[n7]  = {12.46,16.06};
    Float_t ex7[n7] = {1.706,78.0};
    Float_t ey7[n7] = {0.28,0.57};


    // EJ200PS-1X1P 7Mrad (NIST4)
    const Int_t n7l = 2;//5, 9
    Float_t x7l[n7l]  = {8.53,390};
    Float_t y7l[n7l]  = {12.26,9.96};
    Float_t ex7l[n7l] = {1.706,78.0};
    Float_t ey7l[n7l] = {0.26,0.21};
    // Note: EJ200PVT-1X1P-5 seems giving too much light (~1X2P which is inconsistent to other rounds of irradiations)

    // ********************************************************


    // ********************************************************
    // 2X or 2P


    // ********************************************************
    // EJ200PVT-1X2P 7Mrad (NIST4)
    const Int_t n8 = 2;//N5,N9
    Float_t x8[n8]  = {8.53,390};
    Float_t y8[n8]  = {12.99,17.62};
    Float_t ex8[n8] = {1.706,78.0};
    Float_t ey8[n8] = {0.30,0.69};

    // EJ200PS-1X2P 7Mrad (NIST4)
    const Int_t n8l = 2;//5,9
    Float_t x8l[n8l]  = {8.53,390};
    Float_t y8l[n8l]  = {12.62,11.90};
    Float_t ex8l[n8l] = {1.706,78.0};
    Float_t ey8l[n8l] = {0.28,0.32};
    // ********************************************************


    // ********************************************************
    // EJ200PVT-2X1P 7Mrad (NIST4 set 2&6)
    const Int_t n9 = 2;//N5,N9
    Float_t x9[n9]  = {8.34,390};
    Float_t y9[n9]  = {13.54,16.92};
    Float_t ex9[n9] = {1.668,78.0};
    Float_t ey9[n9] = {0.30,0.56};

    // EJ200PS-2X1P 7Mrad (NIST4 set 2&6)
    // High dose rate (390 krad/h) sample "EJ200PS-2X1P_9" is bad; face A and B show very different results
//     const Int_t n9l = 2;//5,9
//     Float_t x9l[n9l]  = {8.34,390};
//     Float_t y9l[n9l]  = {12.14,9.41};
//     Float_t ex9l[n9l] = {1.668,78.0};
//     Float_t ey9l[n9l] = {0.23,0.17};


    // ********************************************************
    // EJ260 1X1P 7Mrad (NIST4)

    // EJ260PVT-1X1P 7Mrad (NIST4 set 2&6)
    const Int_t n9m = 2;//N4,N9
    Float_t x9m[n9m]  = {8.34,390};
    Float_t y9m[n9m]  = {12.53,13.92};
    Float_t ex9m[n9m] = {1.668,78.0};
    Float_t ey9m[n9m] = {0.30,0.43};

    // EJ260PS-1X1P 7Mrad (NIST4 set 2&6)
//     const Int_t n9n = 2;//4,9
//     Float_t x9n[n9n]  = {8.34,390};
//     Float_t y9n[n9n]  = {14.80,11.94}; ==> weird result
//     Float_t ex9n[n9n] = {1.668,78.0};
//     Float_t ey9n[n9n] = {0.41,0.31};
    // ********************************************************


    // ********************************************************
    // EJ200 high dose (30Mrad@1.1Mrad/hr)
    // 1X
    const Int_t n7h = 1;
    Float_t x7h[n7h]  = {1100};
    Float_t y7h[n7h]  = {20.23249};
    Float_t ex7h[n7h] = {55.0};
    Float_t ey7h[n7h] = {1.21206};

    // 2X
    const Int_t n8h = 1;
    Float_t x8h[n8h]  = {1100};
    Float_t y8h[n8h]  = {21.18318};
    Float_t ex8h[n8h] = {55.0};
    Float_t ey8h[n8h] = {1.13311};
    // ********************************************************


    // ********************************************************
    // NIST room temperature (23 degree C)

    // ********************************************************
    // NIST R1
    // PVT 1X1P only
    const Int_t n7n0 = 1;
    Float_t x7n0[n7n0]  = {80};
    Float_t y7n0[n7n0]  = {14.08224};
    Float_t ex7n0[n7n0] = {1.28};
    Float_t ey7n0[n7n0] = {1.14007};

    // ********************************************************
    // NIST4 set5
    // room temperature (23 degree C)
    // EJ200 PVT 1X1P only
    const Int_t n7n1 = 1;//N4
    Float_t x7n1[n7n1]  = {74.4};
    Float_t y7n1[n7n1]  = {13.64};
    Float_t ex7n1[n7n1] = {14.88};
    Float_t ey7n1[n7n1] = {0.25};

    // NIST4 set5
    // room temperature (23 degree C)
    // EJ200 PVT 1X2P only
    const Int_t n7n2 = 1;//N4
    Float_t x7n2[n7n2]  = {74.4};
    Float_t y7n2[n7n2]  = {13.97};
    Float_t ex7n2[n7n2] = {14.88};
    Float_t ey7n2[n7n2] = {0.26};

    // NIST4 set5
    // room temperature (23 degree C)
    // EJ200 PS 1X1P only
    const Int_t n7n3 = 1;//8
    Float_t x7n3[n7n3]  = {74.4};
    Float_t y7n3[n7n3]  = {10.63};
    Float_t ex7n3[n7n3] = {14.88};
    Float_t ey7n3[n7n3] = {0.11};

    // NIST4 set5
    // room temperature (23 degree C)
    // EJ200 PS 1X2P only
    const Int_t n7n4 = 1;//8
    Float_t x7n4[n7n4]  = {74.4};
    Float_t y7n4[n7n4]  = {12.17};
    Float_t ex7n4[n7n4] = {14.88};
    Float_t ey7n4[n7n4] = {0.15};
    // End NIST room temperature (23 degree c)
    // ********************************************************



    // ********************************************************
    // NIST low temperature (-30 degree C)

    // ********************************************************
    // NIST R1
    // PVT 1X1P only
    const Int_t n7t0 = 1;
    Float_t x7t0[n7t0]  = {80};
    Float_t y7t0[n7t0]  = {20.78784};
    Float_t ex7t0[n7t0] = {1.28};
    Float_t ey7t0[n7t0] = {2.60179};

    // ********************************************************
    // NIST4 set4
    // PVT 1X1P only
    const Int_t n7t1 = 1;
    Float_t x7t1[n7t1]  = {74.9};
    Float_t y7t1[n7t1]  = {16.16};
    Float_t ex7t1[n7t1] = {14.98};
    Float_t ey7t1[n7t1] = {0.44};

    // NIST4 set4
    // PVT 1X2P only
    const Int_t n7t2 = 1;
    Float_t x7t2[n7t2]  = {74.9};
    Float_t y7t2[n7t2]  = {17.05};
    Float_t ex7t2[n7t2] = {14.98};
    Float_t ey7t2[n7t2] = {0.50};

    // NIST4 set4
    // PS 1X1P only
    const Int_t n7t3 = 1;
    Float_t x7t3[n7t3]  = {74.9};
    Float_t y7t3[n7t3]  = {9.56};
    Float_t ex7t3[n7t3] = {14.98};
    Float_t ey7t3[n7t3] = {0.17};

    // NIST4 set4
    // PS 1X2P only
    const Int_t n7t4 = 1;
    Float_t x7t4[n7t4]  = {74.9};
    Float_t y7t4[n7t4]  = {12.58};
    Float_t ex7t4[n7t4] = {14.98};
    Float_t ey7t4[n7t4] = {0.27};
    // End NIST low temperature (-30 degree C)
    // ********************************************************


    // ********************************************************
    // Goddard (GSFC) samples
    // G1: -30\deC
    // G2: 23\deC

    // ********************************************************
    // EJ200PVT-1X2P
    // warm (G2)
    const Int_t n11 = 1;
    Float_t x11[n11]  = {0.28};//offset for plotting
    Float_t y11[n11]  = {5.02};
    Float_t ex11[n11] = {0.03};
    Float_t ey11[n11] = {1.08};

    // cold (G1)
    const Int_t n11c = 1;
    Float_t x11c[n11c]  = {0.31};//offset for plotting
    Float_t y11c[n11c]  = {3.62};
    Float_t ex11c[n11c] = {0.03};
    Float_t ey11c[n11c] = {0.73};

    // cold (G1) - warmed up
    const Int_t n11cw = 1;
    Float_t x11cw[n11cw]  = {0.31};//offset for plotting
    Float_t y11cw[n11cw]  = {4.55};
    Float_t ex11cw[n11cw] = {0.03};
    Float_t ey11cw[n11cw] = {0.76};
    // End EJ200PVT-1X2P
    // ********************************************************


    // ********************************************************
    // EJ260PVT-1X2P
    // warm (G2)
    const Int_t n12 = 1;
    Float_t x12[n12]  = {0.28};//offset for plotting
    Float_t y12[n12]  = {5.03};
    Float_t ex12[n12] = {0.03};
    Float_t ey12[n12] = {1.18};

    // cold (G1)
    const Int_t n12c = 1;
    Float_t x12c[n12c]  = {0.31};//offset for plotting
    Float_t y12c[n12c]  = {2.28};
    Float_t ex12c[n12c] = {0.03};
    Float_t ey12c[n12c] = {0.21};

    // cold (G1) - warmed up
    const Int_t n12cw = 1;
    Float_t x12cw[n12cw]  = {0.31};//offset for plotting
    Float_t y12cw[n12cw]  = {6.91};
    Float_t ex12cw[n12cw] = {0.03};
    Float_t ey12cw[n12cw] = {1.86};

    // End EJ260PVT-1X2P
    // ********************************************************


    // ********************************************************
    // EJ200PS-1X2P
    // warm (G2)
    const Int_t n13 = 1;
    Float_t x13[n13]  = {0.29};//offset for plotting
    Float_t y13[n13]  = {5.75};
    Float_t ex13[n13] = {0.03};
    Float_t ey13[n13] = {1.36};

    // cold (G1)
    const Int_t n13c = 1;
    Float_t x13c[n13c]  = {0.32};//offset for plotting
    Float_t y13c[n13c]  = {3.09};
    Float_t ex13c[n13c] = {0.03};
    Float_t ey13c[n13c] = {0.43};

    // cold (G1) - warmed up
    const Int_t n13cw = 1;
    Float_t x13cw[n13cw]  = {0.32};//offset for plotting
    Float_t y13cw[n13cw]  = {4.55};
    Float_t ex13cw[n13cw] = {0.03};
    Float_t ey13cw[n13cw] = {0.76};
    // End EJ200PS-1X2P
    // ********************************************************


    // ********************************************************
    // EJ260PS-1X2P
    // warm
    // G2
    const Int_t n14 = 1;
    Float_t x14[n14]  = {0.29};//offset for plotting
    Float_t y14[n14]  = {5.10};
    Float_t ex14[n14] = {0.03};
    Float_t ey14[n14] = {1.18};

    // cold
    // G1
    const Int_t n14c = 1;
    Float_t x14c[n14c]  = {0.32};//offset for plotting
    Float_t y14c[n14c]  = {2.17};
    Float_t ex14c[n14c] = {0.03};
    Float_t ey14c[n14c] = {0.18};

    // G1 - warmed up
    const Int_t n14cw = 1;
    Float_t x14cw[n14cw]  = {0.32};//offset for plotting
    Float_t y14cw[n14cw]  = {7.2};
    Float_t ex14cw[n14cw] = {0.03};
    Float_t ey14cw[n14cw] = {2.00};
    // End EJ260PS-1X2P
    // ********************************************************

    // End of Goddard (GSFC) samples
    // ********************************************************



    // ********************************************************
    // All the graphs
    TGraphErrors *gr = new TGraphErrors(n,x,y,ex,ey);
    gr->SetTitle("D (Mrad) versus dose rate (krad/hr)");
    gr->SetMarkerColor(kBlue);
    gr->SetMarkerSize(1.5);
    gr->SetMarkerStyle(34);

    TGraph *gr4 = new TGraphErrors(n4,x4,y4,ex4,ey4);
    //gr4->SetMarkerColor(kViolet);
    gr4->SetMarkerColor(kBlue);
    gr4->SetMarkerStyle(26);

    TGraph *gr5 = new TGraphErrors(n5,x5,y5,ex5,ey5);
    //gr5->SetMarkerColor(kPink);
    gr5->SetMarkerColor(kBlue);
    gr5->SetMarkerStyle(25);

    //CMS collisions 2012 #20-29, d2
    TGraph *gr5c = new TGraphErrors(n5c,x5c,y5c,ex5c,ey5c);
    //gr5c->SetMarkerColor(kPink);
    gr5c->SetMarkerColor(4);
    gr5c->SetMarkerStyle(25);

    //CMS collisions 2012 #20-29, d1
    TGraph *gr5d = new TGraphErrors(n5d,x5d,y5d,ex5d,ey5d);
    //gr5d->SetMarkerColor(8);
    gr5d->SetMarkerColor(4);
    gr5d->SetMarkerSize(1.5);
    gr5d->SetMarkerStyle(27);

    TGraph *gr7 = new TGraphErrors(n7,x7,y7,ex7,ey7);
    gr7->SetMarkerColor(2);
    gr7->SetLineColor(2);
    //gr7->SetMarkerSize(1.2);
    gr7->SetMarkerStyle(32);

    TGraph *gr7l = new TGraphErrors(n7l,x7l,y7l,ex7l,ey7l);
    gr7l->SetMarkerColor(4);
    gr7l->SetLineColor(4);
    //gr7l->SetMarkerSize(2.);
    gr7l->SetMarkerStyle(32);

    TGraph *gr7h = new TGraphErrors(n7h,x7h,y7h,ex7h,ey7h);
    gr7h->SetMarkerColor(2);
    gr7h->SetLineColor(2);
    gr7h->SetMarkerSize(1.4);
    gr7h->SetMarkerStyle(28);

    TGraph *gr7n0 = new TGraphErrors(n7n0,x7n0,y7n0,ex7n0,ey7n0);
    gr7n0->SetMarkerColor(2);
    gr7n0->SetLineColor(2);
    gr7n0->SetMarkerSize(1.5);
    gr7n0->SetMarkerStyle(30);

    TGraph *gr7n1 = new TGraphErrors(n7n1,x7n1,y7n1,ex7n1,ey7n1);
    gr7n1->SetMarkerColor(46);
    gr7n1->SetLineColor(46);
    gr7n1->SetMarkerSize(1.5);
    gr7n1->SetMarkerStyle(30);

    TGraph *gr7n2 = new TGraphErrors(n7n2,x7n2,y7n2,ex7n2,ey7n2);
    gr7n2->SetMarkerColor(2);
    gr7n2->SetLineColor(2);
    //gr7n2->SetMarkerSize(1.5);
    gr7n2->SetMarkerStyle(26);//30

    TGraph *gr7n3 = new TGraphErrors(n7n3,x7n3,y7n3,ex7n3,ey7n3);
    gr7n3->SetMarkerColor(6);
    gr7n3->SetLineColor(6);
    gr7n3->SetMarkerSize(1.5);
    gr7n3->SetMarkerStyle(30);

    TGraph *gr7n4 = new TGraphErrors(n7n4,x7n4,y7n4,ex7n4,ey7n4);
    gr7n4->SetMarkerColor(4);
    gr7n4->SetLineColor(4);
    //gr7n4->SetMarkerSize(1.5);
    gr7n4->SetMarkerStyle(25);//30

    TGraph *gr7t0 = new TGraphErrors(n7t0,x7t0,y7t0,ex7t0,ey7t0);
    gr7t0->SetMarkerColor(6);
    gr7t0->SetLineColor(6);
    //gr7t0->SetMarkerSize(1.5);
    gr7t0->SetMarkerStyle(21);

    TGraph *gr7t1 = new TGraphErrors(n7t1,x7t1,y7t1,ex7t1,ey7t1);
    gr7t1->SetMarkerColor(46);
    gr7t1->SetLineColor(46);
    gr7t1->SetMarkerSize(1.5);
    gr7t1->SetMarkerStyle(29);

    TGraph *gr7t2 = new TGraphErrors(n7t2,x7t2,y7t2,ex7t2,ey7t2);
    gr7t2->SetMarkerColor(2);//6
    gr7t2->SetLineColor(2);//6
    gr7t2->SetMarkerSize(1.6);
    gr7t2->SetMarkerStyle(29);

    TGraph *gr7t3 = new TGraphErrors(n7t3,x7t3,y7t3,ex7t3,ey7t3);
    gr7t3->SetMarkerColor(7);
    gr7t3->SetLineColor(7);
    gr7t3->SetMarkerSize(1.5);
    gr7t3->SetMarkerStyle(29);

    TGraph *gr7t4 = new TGraphErrors(n7t4,x7t4,y7t4,ex7t4,ey7t4);
    gr7t4->SetMarkerColor(4);
    gr7t4->SetLineColor(4);
    gr7t4->SetMarkerSize(1.6);
    gr7t4->SetMarkerStyle(29);

    TGraph *gr8 = new TGraphErrors(n8,x8,y8,ex8,ey8);
    gr8->SetFillColor(2);
    gr8->SetMarkerColor(2);
    gr8->SetLineColor(2);
    //gr8->SetMarkerSize(1.2);
    gr8->SetMarkerStyle(26);

    TGraph *gr8l = new TGraphErrors(n8l,x8l,y8l,ex8l,ey8l);
    gr8l->SetFillColor(4);
    gr8l->SetMarkerColor(4);
    gr8l->SetLineColor(4);
    //gr8l->SetMarkerSize(1.2);
    gr8l->SetMarkerStyle(25);

    TGraph *gr8h = new TGraphErrors(n8h,x8h,y8h,ex8h,ey8h);
    gr8h->SetFillColor(2);
    gr8h->SetMarkerColor(2);
    gr8h->SetLineColor(2);
    //gr8h->SetMarkerSize(1.4);
    gr8h->SetMarkerStyle(8);

    // EJ200PVT-1X2P
    // G2
    TGraph *gr11 = new TGraphErrors(n11,x11,y11,ex11,ey11);
    gr11->SetMarkerColor(2);
    gr11->SetLineColor(2);
    //gr11->SetLineStyle(2);
    gr11->SetLineWidth(2);
    //gr11->SetMarkerSize(1.5);
    gr11->SetMarkerStyle(26);//25

    // G1
    TGraph *gr11c = new TGraphErrors(n11c,x11c,y11c,ex11c,ey11c);
    gr11c->SetMarkerColor(6);
    gr11c->SetLineColor(6);
    //gr11c->SetLineStyle(2);
    gr11c->SetLineWidth(2);
    //gr11c->SetMarkerSize(0.8);
    gr11c->SetMarkerStyle(25);

    // G1 warmed up
    TGraph *gr11cw = new TGraphErrors(n11cw,x11cw,y11cw,ex11cw,ey11cw);
    gr11cw->SetMarkerColor(6);
    gr11cw->SetLineColor(6);
    //gr11cw->SetLineStyle(2);
    gr11cw->SetLineWidth(2);
    //gr11cw->SetMarkerSize(0.8);
    gr11cw->SetMarkerStyle(25);


    // EJ260PVT-1X2P
    // G2
    TGraph *gr12 = new TGraphErrors(n12,x12,y12,ex12,ey12);
    gr12->SetMarkerColor(2);
    gr12->SetLineColor(2);
    //gr12->SetLineStyle(2);
    gr12->SetLineWidth(2);
    gr12->SetMarkerSize(1.5);
    gr12->SetMarkerStyle(30);

    // G1
    TGraph *gr12c = new TGraphErrors(n12c,x12c,y12c,ex12c,ey12c);
    gr12c->SetMarkerColor(6);
    gr12c->SetLineColor(6);
    //gr12c->SetLineStyle(2);
    gr12c->SetLineWidth(2);
    gr12c->SetMarkerSize(1.5);
    gr12c->SetMarkerStyle(30);

    // EJ200PS-1X2P
    // G2
    TGraph *gr13 = new TGraphErrors(n13,x13,y13,ex13,ey13);
    gr13->SetMarkerColor(4);
    gr13->SetLineColor(4);
    //gr13->SetLineStyle(2);
    gr13->SetLineWidth(2);
    //gr13->SetMarkerSize(1.5);
    //gr13->SetMarkerStyle(21);
    gr13->SetMarkerStyle(25);

    // G1
    TGraph *gr13c = new TGraphErrors(n13c,x13c,y13c,ex13c,ey13c);
    gr13c->SetMarkerColor(7);
    gr13c->SetLineColor(7);
    //gr13c->SetLineStyle(2);
    gr13c->SetLineWidth(2);
    //gr13c->SetMarkerSize(0.8);
    //gr13c->SetMarkerStyle(21);
    gr13c->SetMarkerStyle(25);

    // G1 warmed up
    TGraph *gr13cw = new TGraphErrors(n13cw,x13cw,y13cw,ex13cw,ey13cw);
    gr13cw->SetMarkerColor(7);
    gr13cw->SetLineColor(7);
    //gr13cw->SetLineStyle(2);
    gr13cw->SetLineWidth(2);
    //gr13cw->SetMarkerSize(0.8);
    //gr13cw->SetMarkerStyle(21);
    gr13cw->SetMarkerStyle(25);

    // EJ260PS-1X2P
    // G2
    TGraph *gr14 = new TGraphErrors(n14,x14,y14,ex14,ey14);
    gr14->SetMarkerColor(4);
    gr14->SetLineColor(4);
    //gr14->SetLineStyle(2);
    gr14->SetLineWidth(2);
    gr14->SetMarkerSize(1.5);
    gr14->SetMarkerStyle(33);

    // G1
    TGraph *gr14c = new TGraphErrors(n14c,x14c,y14c,ex14c,ey14c);
    gr14c->SetMarkerColor(7);
    gr14c->SetLineColor(7);
    //gr14c->SetLineStyle(2);
    gr14c->SetLineWidth(2);
    gr14c->SetMarkerSize(1.5);
    gr14c->SetMarkerStyle(33);


    // ======================================================================================================
    // End of results section
    // ======================================================================================================

    // ======================================================================================================
    // Drawing
    // ======================================================================================================
    // Canvas
    TCanvas *c1 = new TCanvas("c1","D versus doserate",200,10,800,600);
    c1->SetFillColor(0);
    //c1->SetGrid();
    c1->SetLogy();
    c1->SetLogx();

    // MultiGraph with all data points
    TMultiGraph *mgall = new TMultiGraph();

    // UMD
    // PVT
    //mgall->Add(gr7);//EJ200PVT 1X1P NIST4
    mgall->Add(gr8);//EJ200PVT 1X2P NIST4

    //mgall->Add(gr7n1);//EJ200PVT 1X1P 23 degC
    mgall->Add(gr7n2);//EJ200PVT 1X2P 23 degC

    //mgall->Add(gr7t1);//EJ200PVT 1X1P -30 degC
    mgall->Add(gr7t2);//EJ200PVT 1X2P -30 degC

//     mgall->Add(gr7h);//1X 1.1Mrad/hr
//     mgall->Add(gr8h);//2X 1.1Mrad/hr

    mgall->Add(gr11);//EJ200PVT 1X2P G2
//     mgall->Add(gr11c);//EJ200PVT 1X2P G1
//     mgall->Add(gr11cw);//EJ200PVT 1X2P G1 warmed up
    //mgall->Add(gr11d);// G2 Tile; EJ200-1X-6 warm

    //mgall->Add(gr12);//EJ260PVT 1X2P G2
    //mgall->Add(gr12c);//EJ260PVT 1X2P G1
    //mgall->Add(gr12cw);//EJ260PVT 1X2P G1 warmed up

    // PS
    //mgall->Add(gr7l);//EJ200PS 1X1P NIST4
    mgall->Add(gr8l);//EJ200PS 1X2P NIST4

    //mgall->Add(gr7n3);//EJ200PS 1X1P 23 degC
    mgall->Add(gr7n4);//EJ200PS 1X2P 23 degC

    //mgall->Add(gr7t3);//EJ200PS 1X1P -30 degC
    mgall->Add(gr7t4);//EJ200PS 1X2P -30 degC

    mgall->Add(gr13);//EJ200PS 1X2P G2
//     mgall->Add(gr13c);//EJ200PS 1X2P G1
//     mgall->Add(gr13cw);//EJ200PS 1X2P G1 warmed up

    //mgall->Add(gr14);//EJ260PS 1X2P G2
    //mgall->Add(gr14c);//EJ260PS 1X2P G1
    //mgall->Add(gr14cw);//EJ260PS 1X2P G1 warmed up


    // Others
    //mgall->Add(gr);
    //mgall->Add(gr4);

    mgall->Draw("AP");
    mgall->GetXaxis()->SetTitle("Dose rate (krad/hr)");
    mgall->GetYaxis()->SetTitle("Dose Constant (Mrad)");
//     mgall->SetMinimum(0.01);
//     mgall->SetMaximum(300);
    mgall->SetMinimum(1.0);
    mgall->SetMaximum(50.0);
    double xmin = 1.e-2;//1.e-4;
    double xmax = 2.e3;//2.e3;
    mgall->GetXaxis()->SetLimits(xmin,xmax);


    // ====================================
    // Fits (CMS in-situ)
    // ====================================
    TMultiGraph *mginsitu = new TMultiGraph();

    mginsitu->Add(gr);
    mginsitu->Add(gr4);
//     mginsitu->Add(gr5);
//     mginsitu->Add(gr5c);
//     mginsitu->Add(gr5d);

    //mginsitu->Draw("ap");

    double fitxmin = TMath::MinElement(gr4->GetN(),gr4->GetX());
    double fitxmax = TMath::MaxElement(gr->GetN(),gr->GetX());

    // ====================================
    // CMS in-situ; 2016 HPD corrected scenario 4
    // ====================================

    TF1 *fpowHPDsc4 = new TF1("fpowHPDsc4","[0]*pow(x,[1])",fitxmin,fitxmax);
    fpowHPDsc4->SetParameters(3.4,0.49);
    //fpowHPDsc4->SetLineColor(colors_["insitu"]);
    fpowHPDsc4->SetLineColor(kGreen+3);
    //fpowHPDsc4->SetLineStyle(3);
    fpowHPDsc4->SetLineWidth(2);
    //fpowHPDsc4->SetRange(fitxmin,0.3);
    fpowHPDsc4->SetRange(2.e-4,2.e-1);
//     fpowHPDsc4->Draw("same");


    // ====================================
    // UMD PVT
    // ====================================
    TMultiGraph *mgUMD = new TMultiGraph();

    mgUMD->Add(gr11);
    mgUMD->Add(gr7n2);
    mgUMD->Add(gr8);
    //mgUMD->Add(gr7h);
    //mgUMD->Add(gr8h);

    //mgUMD->Draw("ap");

    double fitxmin1 = TMath::MinElement(gr11->GetN(),gr11->GetX());
    double fitxmax1 = TMath::MaxElement(gr8h->GetN(),gr8h->GetX());

    TF1 *fpowUMDPVT = new TF1("fpowUMDPVT","sqrt(x)/([0]+[1]*sqrt(x))",fitxmin1,fitxmax1);
    fpowUMDPVT->SetParameters(0.08,0.05);

    TFitResultPtr resfitUMDPVT = mgUMD->Fit("fpowUMDPVT","SREM0","");
    cout << "[FIT UMD PVT]: p0 = " << resfitUMDPVT->Parameter(0) << endl;
    cout << "[FIT UMD PVT]: p1 = " << resfitUMDPVT->Parameter(1) << endl;
    cout << "[FIT UMD PVT]: chi2/ndof = " << resfitUMDPVT->Chi2()/(resfitUMDPVT->Ndf()+1.) << endl;
    fpowUMDPVT->SetLineColor(2);
    fpowUMDPVT->SetLineStyle(4);
    fpowUMDPVT->SetLineWidth(2);
    //fpowUMDPVT->SetRange(fitxmin,0.3);
    fpowUMDPVT->SetRange(2.e-4,1.e3);
    fpowUMDPVT->Draw("same");


    // ====================================
    // UMD PS
    // ====================================
    TMultiGraph *mgUMDPS = new TMultiGraph();

    // PS
    mgUMDPS->Add(gr13);
    mgUMDPS->Add(gr8l);
    mgUMDPS->Add(gr7n4);

    //mgUMDPS->Draw("ap");

    double fitxmin2 = TMath::MinElement(gr11->GetN(),gr11->GetX());
    double fitxmax2 = TMath::MaxElement(gr8h->GetN(),gr8h->GetX());

    TF1 *fpowUMDPS = new TF1("fpowUMDPS","sqrt(x)/([0]+[1]*sqrt(x))",fitxmin2,fitxmax2);
    fpowUMDPS->SetParameters(0.08,0.05);

    TFitResultPtr resfitUMDPS = mgUMDPS->Fit("fpowUMDPS","SREM0","");
    cout << "[FIT UMD PS]: p0 = " << resfitUMDPS->Parameter(0) << endl;
    cout << "[FIT UMD PS]: p1 = " << resfitUMDPS->Parameter(1) << endl;
    cout << "[FIT UMD PS]: chi2/ndof = " << resfitUMDPS->Chi2()/(resfitUMDPS->Ndf()+1.) << endl;
    fpowUMDPS->SetLineColor(4);
    fpowUMDPS->SetLineStyle(9);
    fpowUMDPS->SetLineWidth(2);
    //fpowUMDPS->SetRange(fitxmin,0.3);
    fpowUMDPS->SetRange(2.e-4,1.e3);
    //fpowUMDPS->Draw("same");



    // ====================================
    // Print fit paras
    // ====================================
    TLatex* fitlatexumd = new TLatex();
    fitlatexumd->SetNDC(true);
    fitlatexumd->SetTextAlign(12);
    fitlatexumd->SetTextSize(0.03);

//     TString sfpowinsitu;
//     sfpowinsitu.Form("D_{in-situ}^{2017 SiPM} = 3.4 #bullet R^{0.49}");

    TString sfpowUMDPVT;
    //sfpowUMDPVT.Form("D_{5 #times 1 #times 1 cm^{3}}^{EJ200PVT} = #frac{#sqrt{R}}{%5.3f + %5.3f #sqrt{R}}",resfitUMDPVT->Parameter(0),resfitUMDPVT->Parameter(1));
    sfpowUMDPVT.Form("D_{5 #times 1 #times 1 cm^{3}}^{EJ200PVT-1X2P} = #frac{#sqrt{R}}{%5.3f + %5.3f #sqrt{R}}",resfitUMDPVT->Parameter(0),resfitUMDPVT->Parameter(1));

    TString sfpowUMDPS;
    sfpowUMDPS.Form("D_{rod} = #frac{#sqrt{R}}{%5.3f + %5.3f #sqrt{R}}",resfitUMDPS->Parameter(0),resfitUMDPS->Parameter(1));


    fitlatexumd->SetTextColor(2);

    TLegend *legendAllR = new TLegend(0.57,0.22,0.92,0.42);
    legendAllR->SetBorderSize(0);
    legendAllR->SetFillColor(0);
    //legendAllR->AddEntry(fpowUMDPVT,sfpowUMDPVT.Data(),"l");
    //legendAllR->AddEntry(fpowHPDsc4,sfpowinsitu.Data(),"l");
    //legendAllR->AddEntry(gr,"CMS in-situ 8 TeV L1","p");
    //legendAllR->AddEntry(gr4,"CMS in-situ 8 TeV L7","p");

    //legendAllR->AddEntry(gr7n1,"UMD,^{60}Co (EJ200PVT-1X1P; 23#circC)","p");//23degC
    //legendAllR->AddEntry(gr7n2,"UMD,^{60}Co (EJ200PVT-1X2P; 23#circC)","p");//23degC
    //legendAllR->AddEntry(gr7n3,"UMD,^{60}Co (EJ200PS-1X1P; 23#circC)","p");//23degC
    //legendAllR->AddEntry(gr7n4,"UMD,^{60}Co (EJ200PS-1X2P; 23#circC)","p");//23degC

    //legendAllR->AddEntry(gr7t1,"UMD,^{60}Co (EJ200PVT-1X1P; -30#circC)","p");//-30degC
    legendAllR->AddEntry(gr7t2,"UMD,^{60}Co (EJ200PVT-1X2P; -30#circC)","p");//-30degC
    //legendAllR->AddEntry(gr7t3,"UMD,^{60}Co (EJ200PS-1X1P; -30#circC)","p");//-30degC
    legendAllR->AddEntry(gr7t4,"UMD,^{60}Co (EJ200PS-1X2P; -30#circC)","p");//-30degC


    legendAllR->Draw();

    TLegend *legendUMD = new TLegend(0.15,0.7,0.58,0.92);

    //legendUMD-> SetNColumns(2);
    legendUMD->SetBorderSize(0);
    legendUMD->SetFillColor(0);

    //legendUMD->AddEntry(fpowUMDPVT,sfpowUMDPVT.Data(),"l");

//     legendUMD->AddEntry(gr11,"UMD,^{60}Co (EJ200PVT-1X2P)","p");
//     legendUMD->AddEntry(gr13,"UMD,^{60}Co (EJ200PS-1X2P)","p");

    legendUMD->AddEntry(fpowUMDPVT,sfpowUMDPVT.Data(),"l");
//     //legendUMD->AddEntry(gr12,"UMD,^{60}Co (EJ260PVT-1X2P)","p");

    legendUMD->AddEntry(gr7,"UMD,^{60}Co (EJ200PVT-1X1P)","p");
    legendUMD->AddEntry(gr7l,"UMD,^{60}Co (EJ200PS-1X1P)","p");

    legendUMD->AddEntry(gr8,"UMD,^{60}Co (EJ200PVT-1X2P)","p");
    legendUMD->AddEntry(gr8l,"UMD,^{60}Co (EJ200PS-1X2P)","p");

//     legendUMD->AddEntry(gr8,"UMD,^{60}Co (EJ200PVT-1X2P; 5#times1#times1 cm^{3})","p");
//     legendUMD->AddEntry(gr8l,"UMD,^{60}Co (EJ200PS-1X2P; 5#times1#times1 cm^{3})","p");

    //legendUMD->AddEntry(gr11d,"UMD,^{60}Co (EJ200PVT; 10#times10#times0.4 cm^{3})","p");

//     legendUMD->AddEntry(gr7h,"UMD,^{60}Co (EJ200-1X; 30 Mrad)","p");
//     legendUMD->AddEntry(gr8h,"UMD,^{60}Co (EJ200-2X; 30 Mrad)","p");

    legendUMD->Draw();


    // legend
    TLegend *legendSym = new TLegend(0.8,0.85,0.95,0.94);
    legendSym->SetBorderSize(1);
    legendSym->SetFillColor(0);
    legendSym->AddEntry(gr8l,"PS based","f");
    legendSym->AddEntry(gr8,"PVT based","f");
    legendSym->Draw();

    c1->Update();


    TString filename = TString("doserate_");
    filename+=tagTime;
    filename+="_OffsetSubtracted_InclNISTRound4andGSFC_PVTPS_p20181116";

    c1->SaveAs(filename+".png");
    c1->SaveAs(filename+".pdf");
    c1->SaveAs(filename+".root");

    //exit();
}
