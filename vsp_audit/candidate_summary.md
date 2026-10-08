# Candidate reaching cruise L/D 17 in the course model

Status: aerodynamic screening candidate, not a fully resized or structurally validated aircraft. Original files unchanged.

## Candidate inputs
- Main wing quarter-chord sweep approximately 40 deg, leading edge sweep 42.1692 deg on both panels.
- Main wing thickness/chord 0.10 at all three stations; original symmetric airfoil shapes scaled in thickness.
- Sref 530.36 m2, AR 10, e 0.8, Mach 0.85, altitude 35000 ft, takeoff mass 295985.59 kg.
- WaveDrag at Mach 1: MaxArea 80.3651 m2 with 160 slices, 80.3872 m2 with 320 slices (3 angular sections).
- ParasiteDrag rerun using the saved original analysis settings: baseline CD0 0.00998015, candidate CD0 0.00977977. No excrescence allowance in saved settings.
- Effective length about 67.53 m: retain the approximately constant 12..27 m interval. The previous 47..53 m plateau disappears: areas approximately 57.25,55.59,54.08,52.71 m2 at x=47,49,51,53 m respectively in candidate160. Do NOT continue subtracting that six-metre interval.
- Approximate supplied-chart readout for t/c=.10, quarter sweep40: MddL0 .866. LF .935 at CL .4461, .941 at CL .4176, .947 at CL .3891. These are approximate chart inputs, not CFD predictions.
- Retain assumed fuselage Mdd .7865; equivalent-circle diameter by itself is not proof that the chart definition permits that choice.

## Results
| Point | CL | Mdd wing | Mdd actual | CDwave | CD | L/D |
|---|---:|---:|---:|---:|---:|---:|
| Start, mass fraction .9813 | .446097 | .787405 | .7865 | .0062644 | .0247018 | 18.0593 |
| Arithmetic mass midpoint | .417617 | .794025 | .7865 | .0062644 | .0236316 | 17.6719 |
| End, mass fraction .8560 | .389136 | .800645 | .7865 | .0062644 | .0226320 | 17.1941 |

The midpoint is not an integrated mission-average L/D. The mass fractions remain from the old mission, so rerun mission fuel/weight/tank sizing for a complete DT2 iteration. Approximate chart readings and unchanged e make the small end-cruise margin uncertain. Check low-speed CLmax, structure, stability/CG, engine capability and geometry consistency before adopting. Parasite drag results have been recomputed; no corresponding validation of e or low-speed performance has been performed.

## Reproduction
candidate_ld.py evaluates the same Hermite interpolation interval used by the notebook at Mach .85, with independent NumPy/SciPy-free arithmetic. candidate_q40_tc10.vsp3 is a saved geometry candidate before analysis meshing. candidate_parasite.vspscript and candidate_verify.vspscript reproduce VSP runs. Raw CSV files: parasite_baseline.csv, parasite_candidate.csv, candidate_final320.csv. The portable runtime is local in runtime/.
