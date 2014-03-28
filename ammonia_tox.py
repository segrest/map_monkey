# coding= utf-8
# Function to calculate ammonia toxicity in salt water.
import math
# AmmoniaToxSaline key tuple (salinity PPT, Temp C, pH) = Ccmc published 
#   value in EPA 1989 Ammonia Toxicity paper for Saltwater pgs 30-31
AmmoniaToxSaline={(10,0,7.0):270,(10,5,7.0):191,(10,10,7.0):131,
                 (10,15,7.0):92,(10,20,7.0):62,(10,25,7.0):44,
                 (10,30,7.0):29,(10,35,7.0):21,(10,0,7.2):175,
                 (10,5,7.2):121,(10,10,7.2):83,(10,15,7.2):58,
                 (10,20,7.2):40,(10,25,7.2):27,(10,30,7.2):19,
                 (10,35,7.2):13,(10,0,7.4):110,(10,5,7.4):77,
                 (10,10,7.4):52,(10,15,7.4):35,(10,20,7.4):25,
                 (10,25,7.4):17,(10,30,7.4):12,(10,35,7.4):8.3,
                 (10,0,7.6):69,(10,5,7.6):48,(10,10,7.6):33,
                 (10,15,7.6):23,(10,20,7.6):16,(10,25,7.6):11,
                 (10,30,7.6):7.7,(10,35,7.6):5.6,(10,0,7.8):44,
                 (10,5,7.8):31,(10,10,7.8):21,(10,15,7.8):15,
                 (10,20,7.8):10,(10,25,7.8):7.1,(10,30,7.8):5,
                 (10,35,7.8):3.5,(10,0,8.0):27,(10,5,8.0):19,
                 (10,10,8.0):13,(10,15,8.0):9.4,(10,20,8.0):6.4,
                 (10,25,8.0):4.6,(10,30,8.0):3.1,(10,35,8.0):2.3,
                 (10,0,8.2):18,(10,5,8.2):12,(10,10,8.2):8.5,
                 (10,15,8.2):5.8,(10,20,8.2):4.2,(10,25,8.2):2.9,
                 (10,30,8.2):2.1,(10,35,8.2):1.5,(10,0,8.4):11,
                 (10,5,8.4):7.9,(10,10,8.4):5.4,(10,15,8.4):3.7,
                 (10,20,8.4):2.7,(10,25,8.4):1.9,(10,30,8.4):1.4,
                 (10,35,8.4):1,(10,0,8.6):7.3,(10,5,8.6):5,
                 (10,10,8.6):3.5,(10,15,8.6):2.5,(10,20,8.6):1.8,
                 (10,25,8.6):1.3,(10,30,8.6):0.98,(10,35,8.6):0.75,
                 (10,0,8.8):4.6,(10,5,8.8):3.3,(10,10,8.8):2.3,
                 (10,15,8.8):1.7,(10,20,8.8):1.2,(10,25,8.8):0.92,
                 (10,30,8.8):0.71,(10,35,8.8):0.56,(10,0,9.0):2.9,
                 (10,5,9.0):2.1,(10,10,9.0):1.5,(10,15,9.0):1.1,
                 (10,20,9.0):0.85,(10,25,9.0):0.67,(10,30,9.0):0.52,
                 (10,35,9.0):0.44,(20,0,7.0):291,(20,5,7.0):200,
                 (20,20,7.0):137,(20,15,7.0):96,(20,20,7.0):64,
                 (20,25,7.0):44,(20,30,7.0):31,(20,35,7.0):21,
                 (20,0,7.2):183,(20,5,7.2):125,(20,10,7.2):87,
                 (20,15,7.2):60,(20,20,7.2):42,(20,25,7.2):29,
                 (20,30,7.2):20,(20,35,7.2):14,(20,0,7.4):116,
                 (20,5,7.4):79,(20,10,7.4):54,(20,15,7.4):37,
                 (20,20,7.4):27,(20,25,7.4):18,(20,30,7.4):12,
                 (20,35,7.4):8.7,(20,0,7.6):73,(20,5,7.6):50,
                 (20,10,7.6):35,(20,15,7.6):23,(20,20,7.6):17,
                 (20,25,7.6):11,(20,30,7.6):7.9,(20,35,7.6):5.6,
                 (20,0,7.8):46,(20,5,7.8):31,(20,10,7.8):23,
                 (20,15,7.8):15,(20,20,7.8):11,(20,25,7.8):7.5,
                 (20,30,7.8):5.2,(20,35,7.8):3.5,(20,0,8.0):29,
                 (20,5,8.0):20,(20,10,8.0):14,(20,15,8.0):9.8,
                 (20,20,8.0):6.7,(20,25,8.0):4.8,(20,30,8.0):3.3,
                 (20,35,8.0):2.3,(20,0,8.2):19,(20,5,8.2):13,
                 (20,10,8.2):8.9,(20,15,8.2):6.2,(20,20,8.2):4.4,
                 (20,25,8.2):3.1,(20,30,8.2):2.1,(20,35,8.2):1.6,
                 (20,0,8.4):12,(20,5,8.4):8.1,(20,10,8.4):5.6,
                 (20,15,8.4):4,(20,20,8.4):2.9,(20,25,8.4):2,
                 (20,30,8.4):1.5,(20,35,8.4):1.1,(20,0,8.6):7.5,
                 (20,5,8.6):5.2,(20,10,8.6):3.7,(20,15,8.6):2.7,
                 (20,20,8.6):1.9,(20,25,8.6):1.4,(20,30,8.6):1,
                 (20,35,8.6):0.77,(20,0,8.8):4.8,(20,5,8.8):3.3,
                 (20,10,8.8):2.5,(20,15,8.8):1.7,(20,20,8.8):1.3,
                 (20,25,8.8):0.94,(20,30,8.8):0.73,(20,35,8.8):0.56,
                 (20,0,9.0):3.1,(20,5,9.0):2.3,(20,10,9.0):1.6,
                 (20,15,9.0):1.2,(20,20,9.0):0.87,(20,25,9.0):0.69,
                 (20,30,9.0):0.54,(20,35,9.0):0.44,(30,0,7.0):312,
                 (30,5,7.0):208,(30,20,7.0):148,(30,15,7.0):102,
                 (30,20,7.0):71,(30,25,7.0):48,(30,30,7.0):33,
                 (30,35,7.0):23,(30,0,7.2):196,(30,5,7.2):135,
                 (30,10,7.2):94,(30,15,7.2):64,(30,20,7.2):44,
                 (30,25,7.2):31,(30,30,7.2):21,(30,35,7.2):15,
                 (30,0,7.4):125,(30,5,7.4):85,(30,10,7.4):58,
                 (30,15,7.4):40,(30,20,7.4):27,(30,25,7.4):19,
                 (30,30,7.4):13,(30,35,7.4):9.4,(30,0,7.6):79,
                 (30,5,7.6):54,(30,10,7.6):37,(30,15,7.6):25,
                 (30,20,7.6):21,(30,25,7.6):12,(30,30,7.6):8.5,
                 (30,35,7.6):6,(30,0,7.8):50,(30,5,7.8):33,
                 (30,10,7.8):23,(30,15,7.8):16,(30,20,7.8):11,
                 (30,25,7.8):7.9,(30,30,7.8):5.4,(30,35,7.8):3.7,
                 (30,0,8.0):31,(30,5,8.0):21,(30,10,8.0):15,
                 (30,15,8.0):10,(30,20,8.0):7.5,(30,25,8.0):5,
                 (30,30,8.0):3.5,(30,35,8.0):2.5,(30,0,8.2):20,
                 (30,5,8.2):11,(30,10,8.2):9.6,(30,15,8.2):6.7,
                 (30,20,8.2):4.6,(30,25,8.2):3.3,(30,30,8.2):2.3,
                 (30,35,8.2):1.7,(30,0,8.4):12.7,(30,5,8.4):8.7,
                 (30,10,8.4):6,(30,15,8.4):4.2,(30,20,8.4):2.9,
                 (30,25,8.4):2.1,(30,30,8.4):1.6,(30,35,8.4):1.1,
                 (30,0,8.6):8.1,(20,5,8.6):5.6,(30,10,8.6):4,
                 (30,15,8.6):2.7,(30,20,8.6):2,(30,25,8.6):1.4,
                 (30,30,8.6):1.1,(30,35,8.6):0.81,(30,0,8.8):5.2,
                 (30,5,8.8):3.6,(30,10,8.8):2.5,(30,15,8.8):1.8,
                 (30,20,8.8):1.3,(30,25,8.8):1,(30,30,8.8):0.75,
                 (30,35,8.8):0.58,(30,0,9.0):3.3,(30,5,9.0):2.3,
                 (30,10,9.0):1.7,(30,15,9.0):1.2,(30,20,9.0):0.94,
                 (30,25,9.0):0.71,(30,30,9.0):0.56,(30,35,9.0):0.46}
print "\n\ncompare(nh3,temp,pH,S)  compare to the published 1989 table for Ccmc\
Ammonia Toxicity in Saltwater"
print "assess(nh3,temp,pH,S)   calculate with function from the published 1989\
Ccmc Ammonia Toxicity in Saltwater"
print "both(nh3,temp,pH,S)     use both methods simplified output\n\n"
def round5(n):
    if n%5==0:
        return n
    elif n%5>0 and n%5<2.5:
        return n-(n%5)
    else:
        return n+(5-n%5)
    
def round10(n):
    if n%10==0:
        return n
    elif n%10>0 and n%10<5:
        return n-(n%10)
    else:
        return n+(10-n%10)

def roundPt2(n):
    return round(float(math.ceil(n/0.2)*0.2),1)


def compare(nh3,temp,pH,S):
    print "Ammonia Toxicity Direct Comparison to published table in"
    print " 1989 National Criteria."
    print "input   values:"
    print "  %s DEG C , %s pH, %s PPT Salinity" % (temp,pH,S)
    print "compare values:"
    print "  %s DEG C , %s pH, %s PPT Salinity" % (round5(temp),roundPt2(pH),\
    round10(S))
    '''print "compare values %s DEG C , %s pH, %s PPT Salinity" % (int(math.ceil
    (temp/5)*5),float(math.ceil(pH/0.2)*0.2),int(math.ceil(S/10)*10))'''
    compareTemp=round5(temp)
    comparepH=roundPt2(pH)
    compareSalinity=round10(S)
    #comparepH=float(math.ceil(pH/0.2)*0.2)
    #compareSalinity=int(math.ceil((round(S,0)/10)*10))
    print "NH3 Criteria Table Value:"
    print "  "+str(AmmoniaToxSaline[compareSalinity,compareTemp,comparepH])
    print "NH3 collected Value"
    print "  "+str(nh3)
    print nh3<AmmoniaToxSaline[compareSalinity,compareTemp,comparepH]
    return AmmoniaToxSaline[compareSalinity,compareTemp,comparepH]

def assess(nh3,temp,pH,S): # San Francisco Calculation
    print "calulation based on Dorn paper from San Francisco\nwhich is based on\
    USEPA 1989 criteria\n"
    #print "calulation based on Dorn paper from San Francisco"
    T=(temp+273.15) #convert Celcius to Kelvin
    salinity=float(S)
    P = 1.0
    I=(19.9273*salinity)/(1000.0-1.005109*salinity)
    pKa = 9.245+0.116*I
    fNH3=1*(1+(10**(pKa+0.0324*(298-T)+((0.0415)*P)*(T**(-1))-pH)))**-1
    accute = (0.233)/fNH3
    totalNaccute=((0.233)/fNH3)*17/14
    if accute>=10:
        accute=round(0.233/fNH3,0)
    elif accute<10 and accute>=1:
        accute=round(0.233/fNH3,1)
    else:
        accute=round(0.233/fNH3,2)
    print "accute " +str(accute) +" Ccmc USEPA Method"
    chronic = (0.035)/fNH3
    if accute>nh3:
        print "pass for accute\n"
    else:
        print "fail for accute\n"
    print "chronic " +str(chronic)
    return 2.33/fNH3
    
def both(nh3,temp,pH,S):
    print "Ammonia Toxicity comparison between Calculation and Published Table \
    results\n\n\n"
    if pH<7.0:
        comparepH=7.0
    elif pH>9.0:
        comparepH=9.0
    else:
        comparepH=roundPt2(pH)
    if temp<0.0:
        compareTemp=0.0
    elif temp>35:
        compareTemp=35
    else:
        compareTemp=round5(temp)
    if S<10.0:
        compareSalinity=10.0
    elif S>30:
        compareSalinity=30
    else:
        compareSalinity=round10(S)
    T=(temp+273.15) #convert Celcius to Kelvin
    salinity=float(S)
    P = 1.0
    I=(19.9273*salinity)/(1000.0-1.005109*salinity)
    pKa = 9.245+0.116*I
    fNH3=1*(1+(10**(pKa+0.0324*(298-T)+((0.0415)*P)*(T**(-1))-pH)))**-1
    accuteCalc = round((0.233)/fNH3,2)
    calculation= nh3<accuteCalc
    accuteTable=AmmoniaToxSaline[compareSalinity,compareTemp,comparepH]
    table=nh3<accuteTable
    
    print "input       %s    mg/L NH3  values %s DEG C , %s pH, %s PPT Salinity" \
    % (nh3,temp,pH,S)
    print "table       %s    mg/L NH3  values %s DEG C , %s pH, %s PPT Salinity  \
    Pass  %s" % (accuteTable,compareTemp,comparepH,compareSalinity,table)
    print "calculation %s mg/L NH3  values %s DEG C , %s pH, %s PPT Salinity   \
    Pass  %s" % (accuteCalc,temp,pH,S,calculation)
    

def floridaMethod(nh3,temp,pH,salinity):
    T=temp
    I=(19.9273*salinity)/(1000.0-1.005109*salinity)
    pKsa = 0.0901821+2729.2/(T+273.2)+(0.1552-0.0003142*(T))*I
    fs=1/(10**(pKsa-pH)+1)
    fNH3=nh3*1/fs
    unIonizedAmmonia_mgL=fNH3*17/14
    print "Accute/fs"
    print .233/fs
    print "Accute/fNH3"
    print .233/fNH3
    print "FL Excel CCalculation"
    #return unIonizedAmmonia_mgL    
    return (17*nh3)/(14*(1+10**((0.09018+(2729.92/(temp+273.15))+((0.1552-\
    (0.0003142*temp))*((19.9273*salinity)/(1000-(1.2005109*salinity)))))-pH)))
