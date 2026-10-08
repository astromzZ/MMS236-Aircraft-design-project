# VSP geometry and drag audit

Original model and notebooks were not modified. OpenVSP 3.54.0 portable was used.

## Baseline geometry analysis
WaveDrag at Mach 1, Shown set, original geometry tessellation. Reported MaxArea: 80 slices 97.7986 m2; 160 slices 96.8054 m2; 320 slices 96.8276 m2. These are fitted equivalent-body maxima, not raw sampled maxima. OpenVSP source WaveDragMgr.cpp calculates MaxArea from its fitted area curve. Slice-count convergence does not establish geometry-tessellation convergence.

At x=33.3732 m: body 46.9901 m2; body+wing 72.2939 m2; whole external aircraft 95.7911 m2. Motor contribution 23.4972 m2.

## Hollow nacelles: avoid a second subtraction
Direct intersections of the exported engine STL give, for ONE engine at x=33.3732 m: outer contour 19.2516 m2; inner contour 7.5030 m2. Twice their difference is 23.4972 m2, matching the whole-aircraft incremental motor contribution. Thus the geometric hole is already excluded. Zero Inlet_Area/Exit_Area metadata does not mean this duct was treated as solid. No flow-through subsurfaces are specified. A Raymer capture-area correction cannot safely be applied by blindly subtracting inlet area again from these material-area results. Capture-streamtube area requires the engine operating condition and is not necessarily the local geometric passage area.

Exported outer dimensions of ONE engine: length 4.403 m, maximum transverse width about 5.047 m and height about 5.032 m. The saved Width=Height=4.022 m parameters describe the duct spine rather than maximum outer diameter. Its section thickness parameter 0.2327504 times chord 4.403 m gives approximately 1.025 m maximum duct-profile thickness. This represents geometric nacelle envelope thickness, not metal skin thickness. No engine specification was provided to validate these dimensions.

## Effective length
Lecture 7, slide 41 specifies aircraft length excluding constant total-cross-section portions. Measured total area over x=12..27 m is 46.52..46.84 m2; over x=47..53 m it is 47.33..47.46 m2. These are approximately flat, not mathematically constant. l=82.53-15-6=61.53 m is a reasonable preliminary approximation with those selected endpoints. It should be re-evaluated after moving/changing geometry. Including wing region is necessary wherever TOTAL area changes.

## Geometry sensitivities (not adopted designs)
Each case reloads original model. 160 slices, 3 angular sections, Mach 1. Baseline 160-slice run used 10 angular sections (all coincide at Mach 1).

| Change | MaxArea m2 |
|---|---:|
| Baseline | 96.8054 |
| Engine profile t/c from 0.23275 to 0.12, other engine parameters retained | 84.9242 |
| Engines 5 m forward | 82.4790 |
| Engines 5 m aft | 105.5290 |
| Refine engine Tess_U/Tess_W to 65/65 | 96.6863 |
| Main-wing root thickness 14% to 12% | 94.2589 |

Forward relocation is a sensitivity experiment, not a feasible mounting recommendation. Engine installation, clearance, pylon, loads and CG must be checked. Reducing nacelle section thickness requires a real engine envelope. Main-wing modification requires structural checks.

At fixed CD0=0.01407, e=.8, AR=10, CL=.389136, l=61.53 m, Sref=530.36 m2, MddL0=.82, LF=.93, Mddfus=.77: the area-only sensitivity gives cruise L/D about 11.33 baseline, 12.20 for thinner nacelles, 12.38 for forward relocation. These are NOT complete redesign predictions: CD0, effective length, installation effects and other quantities were held fixed.

The isolated-engine WaveDrag solve was interrupted after not completing promptly; its planar slices and STL intersections completed. Whole-aircraft baseline and geometry sensitivity solves completed.

## Comparison with other group scripts
Read sources: C:/Users/cevin/Downloads/sizing_cont_iter9.py and transonic_drag_v9.py. The sizing calculation was executed after removing its unused matplotlib import, with outputs captured. No source edits.

Other group: S=396.1621 m2, CL=.5182101, CD0=.01639, e=1, AR=10, CDwave=.004568; CD=.03117848; cruise L/D=16.62076; LDmax variable=19.19257 via division by .866. That conversion does not independently determine maximum L/D. Their CL uses takeoff mass without a cruise mass fraction.

Their wave inputs: Amax=50 m2, l=56 m, Sref=396.12 m2, sweep=32 deg, MddL0=.921, LF=.9727, Mddfus=.82. Wing Mdd=.869946 but min selects fuselage .82. Our current notebook inputs give wing-limited Mdd=.743143. Their Mcrit=.74 vs ours=.663143. Their Cd at Mach1.2 is .051212 vs ours .124296.

They use scipy make_smoothing_spline with lambda=.00005; we use PCHIP slopes with CubicHermiteSpline. A separate NumPy solution of the natural cubic smoothing spline objective gives their CDwave(.85)=.0045405, close to hardcoded .004568. Our PCHIP construction with their inputs gives .0035740. Our inputs with their smoothing method give .0139003 versus our .0139252. Hence changing only our interpolator does not explain the L/D gap. This reconstruction was not a direct SciPy run.

Holding all our current inputs fixed except CDwave=.004568 raises L/D from 11.17 to 15.28; additionally setting e=1 gives 16.04. These are diagnostic substitutions, not transferable design inputs. Their box-wing geometry and the consistency of its reference area, AR, e and chart readouts have not been verified.
