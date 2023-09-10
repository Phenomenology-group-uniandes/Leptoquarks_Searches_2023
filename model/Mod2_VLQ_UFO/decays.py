# This file was automatically created by FeynRules 2.3.47
# Mathematica version: 11.1.0 for Linux x86 (64-bit) (March 13, 2017)
# Date: Fri 4 Feb 2022 10:50:38


from object_library import all_decays, Decay
import particles as P


Decay_Gp = Decay(
    name="Decay_Gp",
    particle=P.Gp,
    partial_widths={
        (
            P.b,
            P.b__tilde__,
        ): "(MGp**2*(8*gGp**2*kappaL3x3**2*MGp**2 + 8*gGp**2*kappaRd3x3**2*MGp**2))/(384.*cmath.pi*abs(MGp)**3)",
        (
            P.c,
            P.c__tilde__,
        ): "(MGp**2*(8*gGp**2*kappaRu2x2**2*MGp**2 + 8*gGp**2*I5a22*MGp**2*complexconjugate(I5a22)))/(384.*cmath.pi*abs(MGp)**3)",
        (
            P.c,
            P.t__tilde__,
        ): "((MGp**2 - MT**2)*(8*gGp**2*I5a23*MGp**2*complexconjugate(I5a23) - 4*gGp**2*I5a23*MT**2*complexconjugate(I5a23) - (4*gGp**2*I5a23*MT**4*complexconjugate(I5a23))/MGp**2))/(384.*cmath.pi*abs(MGp)**3)",
        (
            P.c,
            P.u__tilde__,
        ): "(gGp**2*I5a21*MGp**4*complexconjugate(I5a21))/(48.*cmath.pi*abs(MGp)**3)",
        (
            P.d,
            P.d__tilde__,
        ): "(MGp**2*(8*gGp**2*kappaL1x1**2*MGp**2 + 8*gGp**2*kappaRd1x1**2*MGp**2))/(384.*cmath.pi*abs(MGp)**3)",
        (
            P.g,
            P.g,
        ): "(-19*G**2*kappaG1**2*MGp**4*f(2,3,1)**2)/(1536.*cmath.pi*abs(MGp)**3)",
        (
            P.s,
            P.s__tilde__,
        ): "(MGp**2*(8*gGp**2*kappaL2x2**2*MGp**2 + 8*gGp**2*kappaRd2x2**2*MGp**2))/(384.*cmath.pi*abs(MGp)**3)",
        (
            P.t,
            P.c__tilde__,
        ): "((MGp**2 - MT**2)*(8*gGp**2*I5a32*MGp**2*complexconjugate(I5a32) - 4*gGp**2*I5a32*MT**2*complexconjugate(I5a32) - (4*gGp**2*I5a32*MT**4*complexconjugate(I5a32))/MGp**2))/(384.*cmath.pi*abs(MGp)**3)",
        (
            P.t,
            P.t__tilde__,
        ): "((8*gGp**2*kappaRu3x3**2*MGp**2 + 24*gGp**2*I5a33*kappaRu3x3*MT**2 - 8*gGp**2*kappaRu3x3**2*MT**2 + 8*gGp**2*I5a33*MGp**2*complexconjugate(I5a33) - 8*gGp**2*I5a33*MT**2*complexconjugate(I5a33) + 24*gGp**2*kappaRu3x3*MT**2*complexconjugate(I5a33))*cmath.sqrt(MGp**4 - 4*MGp**2*MT**2))/(384.*cmath.pi*abs(MGp)**3)",
        (
            P.t,
            P.u__tilde__,
        ): "((MGp**2 - MT**2)*(8*gGp**2*I5a31*MGp**2*complexconjugate(I5a31) - 4*gGp**2*I5a31*MT**2*complexconjugate(I5a31) - (4*gGp**2*I5a31*MT**4*complexconjugate(I5a31))/MGp**2))/(384.*cmath.pi*abs(MGp)**3)",
        (
            P.u,
            P.c__tilde__,
        ): "(gGp**2*I5a12*MGp**4*complexconjugate(I5a12))/(48.*cmath.pi*abs(MGp)**3)",
        (
            P.u,
            P.t__tilde__,
        ): "((MGp**2 - MT**2)*(8*gGp**2*I5a13*MGp**2*complexconjugate(I5a13) - 4*gGp**2*I5a13*MT**2*complexconjugate(I5a13) - (4*gGp**2*I5a13*MT**4*complexconjugate(I5a13))/MGp**2))/(384.*cmath.pi*abs(MGp)**3)",
        (
            P.u,
            P.u__tilde__,
        ): "(MGp**2*(8*gGp**2*kappaRu1x1**2*MGp**2 + 8*gGp**2*I5a11*MGp**2*complexconjugate(I5a11)))/(384.*cmath.pi*abs(MGp)**3)",
    },
)

Decay_H = Decay(
    name="Decay_H",
    particle=P.H,
    partial_widths={
        (
            P.t,
            P.t__tilde__,
        ): "((3*MH**2*yt**2 - 12*MT**2*yt**2)*cmath.sqrt(MH**4 - 4*MH**2*MT**2))/(16.*cmath.pi*abs(MH)**3)",
        (
            P.W__minus__,
            P.W__plus__,
        ): "(((3*ee**4*vev**2)/(4.*sw**4) + (ee**4*MH**4*vev**2)/(16.*MW**4*sw**4) - (ee**4*MH**2*vev**2)/(4.*MW**2*sw**4))*cmath.sqrt(MH**4 - 4*MH**2*MW**2))/(16.*cmath.pi*abs(MH)**3)",
        (
            P.Z,
            P.Z,
        ): "(((9*ee**4*vev**2)/2. + (3*ee**4*MH**4*vev**2)/(8.*MZ**4) - (3*ee**4*MH**2*vev**2)/(2.*MZ**2) + (3*cw**4*ee**4*vev**2)/(4.*sw**4) + (cw**4*ee**4*MH**4*vev**2)/(16.*MZ**4*sw**4) - (cw**4*ee**4*MH**2*vev**2)/(4.*MZ**2*sw**4) + (3*cw**2*ee**4*vev**2)/sw**2 + (cw**2*ee**4*MH**4*vev**2)/(4.*MZ**4*sw**2) - (cw**2*ee**4*MH**2*vev**2)/(MZ**2*sw**2) + (3*ee**4*sw**2*vev**2)/cw**2 + (ee**4*MH**4*sw**2*vev**2)/(4.*cw**2*MZ**4) - (ee**4*MH**2*sw**2*vev**2)/(cw**2*MZ**2) + (3*ee**4*sw**4*vev**2)/(4.*cw**4) + (ee**4*MH**4*sw**4*vev**2)/(16.*cw**4*MZ**4) - (ee**4*MH**2*sw**4*vev**2)/(4.*cw**4*MZ**2))*cmath.sqrt(MH**4 - 4*MH**2*MZ**2))/(32.*cmath.pi*abs(MH)**3)",
    },
)

Decay_t = Decay(
    name="Decay_t",
    particle=P.t,
    partial_widths={
        (
            P.Gp,
            P.c,
        ): "((-MGp**2 + MT**2)*(-8*gGp**2*I5a23*MGp**2*complexconjugate(I5a23) + 4*gGp**2*I5a23*MT**2*complexconjugate(I5a23) + (4*gGp**2*I5a23*MT**4*complexconjugate(I5a23))/MGp**2))/(96.*cmath.pi*abs(MT)**3)",
        (
            P.Gp,
            P.u,
        ): "((-MGp**2 + MT**2)*(-8*gGp**2*I5a13*MGp**2*complexconjugate(I5a13) + 4*gGp**2*I5a13*MT**2*complexconjugate(I5a13) + (4*gGp**2*I5a13*MT**4*complexconjugate(I5a13))/MGp**2))/(96.*cmath.pi*abs(MT)**3)",
        (
            P.VLQ,
            P.vt,
        ): "((MT**2 - MVLQ**2)*((3*betaL3x3**2*gU**2*MT**2*newCKM3x3*complexconjugate(newCKM3x3))/2. + (3*betaL3x3**2*gU**2*MT**4*newCKM3x3*complexconjugate(newCKM3x3))/(2.*MVLQ**2) - 3*betaL3x3**2*gU**2*MVLQ**2*newCKM3x3*complexconjugate(newCKM3x3)))/(96.*cmath.pi*abs(MT)**3)",
        (
            P.W__plus__,
            P.b,
        ): "((MT**2 - MW**2)*((3*CKM3x3*ee**2*MT**2*complexconjugate(CKM3x3))/(2.*sw**2) + (3*CKM3x3*ee**2*MT**4*complexconjugate(CKM3x3))/(2.*MW**2*sw**2) - (3*CKM3x3*ee**2*MW**2*complexconjugate(CKM3x3))/sw**2))/(96.*cmath.pi*abs(MT)**3)",
        (
            P.W__plus__,
            P.d,
        ): "((MT**2 - MW**2)*((3*CKM3x1*ee**2*MT**2*complexconjugate(CKM3x1))/(2.*sw**2) + (3*CKM3x1*ee**2*MT**4*complexconjugate(CKM3x1))/(2.*MW**2*sw**2) - (3*CKM3x1*ee**2*MW**2*complexconjugate(CKM3x1))/sw**2))/(96.*cmath.pi*abs(MT)**3)",
        (
            P.W__plus__,
            P.s,
        ): "((MT**2 - MW**2)*((3*CKM3x2*ee**2*MT**2*complexconjugate(CKM3x2))/(2.*sw**2) + (3*CKM3x2*ee**2*MT**4*complexconjugate(CKM3x2))/(2.*MW**2*sw**2) - (3*CKM3x2*ee**2*MW**2*complexconjugate(CKM3x2))/sw**2))/(96.*cmath.pi*abs(MT)**3)",
        (
            P.Zp,
            P.c,
        ): "((MT**2 - MZp**2)*((gZp**2*I6a23*MT**2*complexconjugate(I6a23))/8. + (gZp**2*I6a23*MT**4*complexconjugate(I6a23))/(8.*MZp**2) - (gZp**2*I6a23*MZp**2*complexconjugate(I6a23))/4.))/(96.*cmath.pi*abs(MT)**3)",
        (
            P.Zp,
            P.u,
        ): "((MT**2 - MZp**2)*((gZp**2*I6a13*MT**2*complexconjugate(I6a13))/8. + (gZp**2*I6a13*MT**4*complexconjugate(I6a13))/(8.*MZp**2) - (gZp**2*I6a13*MZp**2*complexconjugate(I6a13))/4.))/(96.*cmath.pi*abs(MT)**3)",
    },
)

Decay_VLQ = Decay(
    name="Decay_VLQ",
    particle=P.VLQ,
    partial_widths={
        (
            P.b,
            P.ta__plus__,
        ): "(MVLQ**2*(3*betaL3x3**2*gU**2*MVLQ**2 + 3*betaRd3x3**2*gU**2*MVLQ**2))/(144.*cmath.pi*abs(MVLQ)**3)",
        (
            P.t,
            P.vt__tilde__,
        ): "((-MT**2 + MVLQ**2)*((-3*betaL3x3**2*gU**2*MT**2*newCKM3x3*complexconjugate(newCKM3x3))/2. - (3*betaL3x3**2*gU**2*MT**4*newCKM3x3*complexconjugate(newCKM3x3))/(2.*MVLQ**2) + 3*betaL3x3**2*gU**2*MVLQ**2*newCKM3x3*complexconjugate(newCKM3x3)))/(144.*cmath.pi*abs(MVLQ)**3)",
    },
)

Decay_W__plus__ = Decay(
    name="Decay_W__plus__",
    particle=P.W__plus__,
    partial_widths={
        (
            P.c,
            P.b__tilde__,
        ): "(CKM2x3*ee**2*MW**4*complexconjugate(CKM2x3))/(16.*cmath.pi*sw**2*abs(MW)**3)",
        (
            P.c,
            P.d__tilde__,
        ): "(CKM2x1*ee**2*MW**4*complexconjugate(CKM2x1))/(16.*cmath.pi*sw**2*abs(MW)**3)",
        (
            P.c,
            P.s__tilde__,
        ): "(CKM2x2*ee**2*MW**4*complexconjugate(CKM2x2))/(16.*cmath.pi*sw**2*abs(MW)**3)",
        (
            P.t,
            P.b__tilde__,
        ): "((-MT**2 + MW**2)*((-3*CKM3x3*ee**2*MT**2*complexconjugate(CKM3x3))/(2.*sw**2) - (3*CKM3x3*ee**2*MT**4*complexconjugate(CKM3x3))/(2.*MW**2*sw**2) + (3*CKM3x3*ee**2*MW**2*complexconjugate(CKM3x3))/sw**2))/(48.*cmath.pi*abs(MW)**3)",
        (
            P.t,
            P.d__tilde__,
        ): "((-MT**2 + MW**2)*((-3*CKM3x1*ee**2*MT**2*complexconjugate(CKM3x1))/(2.*sw**2) - (3*CKM3x1*ee**2*MT**4*complexconjugate(CKM3x1))/(2.*MW**2*sw**2) + (3*CKM3x1*ee**2*MW**2*complexconjugate(CKM3x1))/sw**2))/(48.*cmath.pi*abs(MW)**3)",
        (
            P.t,
            P.s__tilde__,
        ): "((-MT**2 + MW**2)*((-3*CKM3x2*ee**2*MT**2*complexconjugate(CKM3x2))/(2.*sw**2) - (3*CKM3x2*ee**2*MT**4*complexconjugate(CKM3x2))/(2.*MW**2*sw**2) + (3*CKM3x2*ee**2*MW**2*complexconjugate(CKM3x2))/sw**2))/(48.*cmath.pi*abs(MW)**3)",
        (
            P.u,
            P.b__tilde__,
        ): "(CKM1x3*ee**2*MW**4*complexconjugate(CKM1x3))/(16.*cmath.pi*sw**2*abs(MW)**3)",
        (
            P.u,
            P.d__tilde__,
        ): "(CKM1x1*ee**2*MW**4*complexconjugate(CKM1x1))/(16.*cmath.pi*sw**2*abs(MW)**3)",
        (
            P.u,
            P.s__tilde__,
        ): "(CKM1x2*ee**2*MW**4*complexconjugate(CKM1x2))/(16.*cmath.pi*sw**2*abs(MW)**3)",
        (P.ve, P.e__plus__): "(ee**2*MW**4)/(48.*cmath.pi*sw**2*abs(MW)**3)",
        (P.vm, P.mu__plus__): "(ee**2*MW**4)/(48.*cmath.pi*sw**2*abs(MW)**3)",
        (P.vt, P.ta__plus__): "(ee**2*MW**4)/(48.*cmath.pi*sw**2*abs(MW)**3)",
    },
)

Decay_Z = Decay(
    name="Decay_Z",
    particle=P.Z,
    partial_widths={
        (
            P.b,
            P.b__tilde__,
        ): "(MZ**2*(ee**2*MZ**2 + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) + (5*ee**2*MZ**2*sw**2)/(6.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)",
        (
            P.c,
            P.c__tilde__,
        ): "(MZ**2*(-(ee**2*MZ**2) + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) + (17*ee**2*MZ**2*sw**2)/(6.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)",
        (
            P.d,
            P.d__tilde__,
        ): "(MZ**2*(ee**2*MZ**2 + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) + (5*ee**2*MZ**2*sw**2)/(6.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)",
        (
            P.e__minus__,
            P.e__plus__,
        ): "(MZ**2*(-(ee**2*MZ**2) + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (5*ee**2*MZ**2*sw**2)/(2.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)",
        (
            P.mu__minus__,
            P.mu__plus__,
        ): "(MZ**2*(-(ee**2*MZ**2) + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (5*ee**2*MZ**2*sw**2)/(2.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)",
        (
            P.s,
            P.s__tilde__,
        ): "(MZ**2*(ee**2*MZ**2 + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) + (5*ee**2*MZ**2*sw**2)/(6.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)",
        (
            P.t,
            P.t__tilde__,
        ): "((-11*ee**2*MT**2 - ee**2*MZ**2 - (3*cw**2*ee**2*MT**2)/(2.*sw**2) + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) + (7*ee**2*MT**2*sw**2)/(6.*cw**2) + (17*ee**2*MZ**2*sw**2)/(6.*cw**2))*cmath.sqrt(-4*MT**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)",
        (
            P.ta__minus__,
            P.ta__plus__,
        ): "(MZ**2*(-(ee**2*MZ**2) + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (5*ee**2*MZ**2*sw**2)/(2.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)",
        (
            P.u,
            P.u__tilde__,
        ): "(MZ**2*(-(ee**2*MZ**2) + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) + (17*ee**2*MZ**2*sw**2)/(6.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)",
        (
            P.ve,
            P.ve__tilde__,
        ): "(MZ**2*(ee**2*MZ**2 + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (ee**2*MZ**2*sw**2)/(2.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)",
        (
            P.VLQ__tilde__,
            P.VLQ,
        ): "(((-16*ee**2*MVLQ**2*sw**2)/cw**2 - (68*ee**2*MZ**2*sw**2)/(3.*cw**2) + (80*ee**2*kappaUtilde*MZ**2*sw**2)/(3.*cw**2) - (16*ee**2*kappaUtilde**2*MZ**2*sw**2)/(3.*cw**2) + (16*ee**2*MZ**4*sw**2)/(3.*cw**2*MVLQ**2) - (4*ee**2*kappaUtilde*MZ**4*sw**2)/(cw**2*MVLQ**2) + (ee**2*MZ**6*sw**2)/(3.*cw**2*MVLQ**4) - (2*ee**2*kappaUtilde*MZ**6*sw**2)/(3.*cw**2*MVLQ**4) + (ee**2*kappaUtilde**2*MZ**6*sw**2)/(3.*cw**2*MVLQ**4))*cmath.sqrt(-4*MVLQ**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)",
        (
            P.vm,
            P.vm__tilde__,
        ): "(MZ**2*(ee**2*MZ**2 + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (ee**2*MZ**2*sw**2)/(2.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)",
        (
            P.vt,
            P.vt__tilde__,
        ): "(MZ**2*(ee**2*MZ**2 + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (ee**2*MZ**2*sw**2)/(2.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)",
        (
            P.W__minus__,
            P.W__plus__,
        ): "(((-12*cw**2*ee**2*MW**2)/sw**2 - (17*cw**2*ee**2*MZ**2)/sw**2 + (4*cw**2*ee**2*MZ**4)/(MW**2*sw**2) + (cw**2*ee**2*MZ**6)/(4.*MW**4*sw**2))*cmath.sqrt(-4*MW**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)",
    },
)

Decay_Zp = Decay(
    name="Decay_Zp",
    particle=P.Zp,
    partial_widths={
        (
            P.b,
            P.b__tilde__,
        ): "(MZp**2*((gZp**2*MZp**2*zetaq3x3**2)/4. + (gZp**2*MZp**2*zetaRd3x3**2)/4.))/(48.*cmath.pi*abs(MZp)**3)",
        (
            P.c,
            P.c__tilde__,
        ): "(MZp**2*((gZp**2*MZp**2*zetaRu2x2**2)/4. + (gZp**2*I6a22*MZp**2*complexconjugate(I6a22))/4.))/(48.*cmath.pi*abs(MZp)**3)",
        (
            P.c,
            P.t__tilde__,
        ): "((-MT**2 + MZp**2)*(-(gZp**2*I6a23*MT**2*complexconjugate(I6a23))/8. - (gZp**2*I6a23*MT**4*complexconjugate(I6a23))/(8.*MZp**2) + (gZp**2*I6a23*MZp**2*complexconjugate(I6a23))/4.))/(48.*cmath.pi*abs(MZp)**3)",
        (
            P.c,
            P.u__tilde__,
        ): "(gZp**2*I6a21*MZp**4*complexconjugate(I6a21))/(192.*cmath.pi*abs(MZp)**3)",
        (
            P.d,
            P.d__tilde__,
        ): "(MZp**2*((gZp**2*MZp**2*zetaq1x1**2)/4. + (gZp**2*MZp**2*zetaRd1x1**2)/4.))/(48.*cmath.pi*abs(MZp)**3)",
        (
            P.mu__minus__,
            P.mu__plus__,
        ): "(MZp**2*((3*gZp**2*MZp**2*zetal2x2**2)/4. + (3*gZp**2*MZp**2*zetaRe2x2**2)/4.))/(48.*cmath.pi*abs(MZp)**3)",
        (
            P.mu__minus__,
            P.ta__plus__,
        ): "(gZp**2*MZp**4*zetal2x3**2)/(64.*cmath.pi*abs(MZp)**3)",
        (
            P.s,
            P.s__tilde__,
        ): "(MZp**2*((gZp**2*MZp**2*zetaq2x2**2)/4. + (gZp**2*MZp**2*zetaRd2x2**2)/4.))/(48.*cmath.pi*abs(MZp)**3)",
        (
            P.t,
            P.c__tilde__,
        ): "((-MT**2 + MZp**2)*(-(gZp**2*I6a32*MT**2*complexconjugate(I6a32))/8. - (gZp**2*I6a32*MT**4*complexconjugate(I6a32))/(8.*MZp**2) + (gZp**2*I6a32*MZp**2*complexconjugate(I6a32))/4.))/(48.*cmath.pi*abs(MZp)**3)",
        (
            P.t,
            P.t__tilde__,
        ): "(((3*gZp**2*I6a33*MT**2*zetaRu3x3)/4. - (gZp**2*MT**2*zetaRu3x3**2)/4. + (gZp**2*MZp**2*zetaRu3x3**2)/4. - (gZp**2*I6a33*MT**2*complexconjugate(I6a33))/4. + (gZp**2*I6a33*MZp**2*complexconjugate(I6a33))/4. + (3*gZp**2*MT**2*zetaRu3x3*complexconjugate(I6a33))/4.)*cmath.sqrt(-4*MT**2*MZp**2 + MZp**4))/(48.*cmath.pi*abs(MZp)**3)",
        (
            P.t,
            P.u__tilde__,
        ): "((-MT**2 + MZp**2)*(-(gZp**2*I6a31*MT**2*complexconjugate(I6a31))/8. - (gZp**2*I6a31*MT**4*complexconjugate(I6a31))/(8.*MZp**2) + (gZp**2*I6a31*MZp**2*complexconjugate(I6a31))/4.))/(48.*cmath.pi*abs(MZp)**3)",
        (
            P.ta__minus__,
            P.mu__plus__,
        ): "(gZp**2*MZp**4*zetal3x2**2)/(64.*cmath.pi*abs(MZp)**3)",
        (
            P.ta__minus__,
            P.ta__plus__,
        ): "(MZp**2*((3*gZp**2*MZp**2*zetal3x3**2)/4. + (3*gZp**2*MZp**2*zetaRe3x3**2)/4.))/(48.*cmath.pi*abs(MZp)**3)",
        (
            P.u,
            P.c__tilde__,
        ): "(gZp**2*I6a12*MZp**4*complexconjugate(I6a12))/(192.*cmath.pi*abs(MZp)**3)",
        (
            P.u,
            P.t__tilde__,
        ): "((-MT**2 + MZp**2)*(-(gZp**2*I6a13*MT**2*complexconjugate(I6a13))/8. - (gZp**2*I6a13*MT**4*complexconjugate(I6a13))/(8.*MZp**2) + (gZp**2*I6a13*MZp**2*complexconjugate(I6a13))/4.))/(48.*cmath.pi*abs(MZp)**3)",
        (
            P.u,
            P.u__tilde__,
        ): "(MZp**2*((gZp**2*MZp**2*zetaRu1x1**2)/4. + (gZp**2*I6a11*MZp**2*complexconjugate(I6a11))/4.))/(48.*cmath.pi*abs(MZp)**3)",
        (
            P.VLQ__tilde__,
            P.VLQ,
        ): "((-12*KappaZp**2*MZp**2 + (3*KappaZp**2*MZp**6)/(4.*MVLQ**4))*cmath.sqrt(-4*MVLQ**2*MZp**2 + MZp**4))/(48.*cmath.pi*abs(MZp)**3)",
        (P.vm, P.vm__tilde__): "(gZp**2*MZp**4*zetal2x2**2)/(64.*cmath.pi*abs(MZp)**3)",
        (P.vm, P.vt__tilde__): "(gZp**2*MZp**4*zetal2x3**2)/(64.*cmath.pi*abs(MZp)**3)",
        (P.vt, P.vm__tilde__): "(gZp**2*MZp**4*zetal3x2**2)/(64.*cmath.pi*abs(MZp)**3)",
        (P.vt, P.vt__tilde__): "(gZp**2*MZp**4*zetal3x3**2)/(64.*cmath.pi*abs(MZp)**3)",
    },
)
