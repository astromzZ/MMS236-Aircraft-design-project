"""Reproduce candidate screening at M=.85. No source notebook is changed.
Graph readouts are approximate; effective length excludes x=12..27 m only.
Mass fractions are the previous mission's values, not a re-sized mission.
"""
import math
A_MAX=80.3871616352
S_REF=530.36
L_EFFECTIVE=82.53-(27-12)
CD0=0.009779765062227528
AR=10.0
E=0.8
MACH=0.85
MDD0=0.866
MDD_FUSELAGE=0.7865
MASS_TO=295985.59
Q=0.5*0.3796*(MACH*296.5)**2

def evaluate(fraction,lf):
    cl=fraction*MASS_TO*9.82/(Q*S_REF)
    mdd_wing=MDD0*lf-0.05*cl
    mdd=min(mdd_wing,MDD_FUSELAGE)
    # Only interval Mdd<M=.85<1 is used. These are the exact PCHIP
    # interior slopes used by the notebook's CubicHermiteSpline there.
    cd12=1.8*9*math.pi/2*(A_MAX/L_EFFECTIVE)**2/S_REF
    x=[mdd-.08,mdd,1.0,1.05]
    y=[0.0,.002,cd12/2,cd12]
    h=[x[i+1]-x[i] for i in range(3)]
    d=[(y[i+1]-y[i])/h[i] for i in range(3)]
    slopes=[]
    for j in [1,2]:
        w1=2*h[j]+h[j-1];w2=h[j]+2*h[j-1]
        slopes.append((w1+w2)/(w1/d[j-1]+w2/d[j]))
    assert mdd<MACH<1
    t=(MACH-mdd)/h[1]
    wave=(2*t**3-3*t*t+1)*y[1]+(t**3-2*t*t+t)*h[1]*slopes[0]+(-2*t**3+3*t*t)*y[2]+(t**3-t*t)*h[1]*slopes[1]
    cd=CD0+(.38*CD0+1/(math.pi*E*AR))*cl**2+wave
    return cl,mdd_wing,mdd,wave,cd,cl/cd

if __name__=='__main__':
    for label,f,lf in [('start',.9813,.935),('mass_midpoint',(.9813+.856)/2,.941),('end',.856,.947)]:
        print(label, dict(zip(['CL','Mdd_wing','Mdd','CDwave','CD','LD'],evaluate(f,lf))))
