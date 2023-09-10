# This file was automatically created by FeynRules 2.3.47
# Mathematica version: 11.1.0 for Linux x86 (64-bit) (March 13, 2017)
# Date: Fri 4 Feb 2022 10:50:38


from object_library import all_couplings, Coupling

from function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot


GC_1 = Coupling(name="GC_1", value="-(ee*complex(0,1))/3.", order={"QED": 1})

GC_2 = Coupling(name="GC_2", value="(2*ee*complex(0,1))/3.", order={"QED": 1})

GC_3 = Coupling(name="GC_3", value="-(ee*complex(0,1))", order={"QED": 1})

GC_4 = Coupling(name="GC_4", value="ee*complex(0,1)", order={"QED": 1})

GC_5 = Coupling(name="GC_5", value="(4*ee**2*complex(0,1))/9.", order={"QED": 2})

GC_6 = Coupling(name="GC_6", value="ee**2*complex(0,1)", order={"QED": 2})

GC_7 = Coupling(name="GC_7", value="2*ee**2*complex(0,1)", order={"QED": 2})

GC_8 = Coupling(name="GC_8", value="-ee**2/(2.*cw)", order={"QED": 2})

GC_9 = Coupling(name="GC_9", value="(ee**2*complex(0,1))/(2.*cw)", order={"QED": 2})

GC_10 = Coupling(name="GC_10", value="ee**2/(2.*cw)", order={"QED": 2})

GC_11 = Coupling(name="GC_11", value="-G", order={"QCD": 1})

GC_12 = Coupling(name="GC_12", value="complex(0,1)*G", order={"QCD": 1})

GC_13 = Coupling(name="GC_13", value="G", order={"QCD": 1})

GC_14 = Coupling(
    name="GC_14", value="(2*ee*complex(0,1)*G)/3.", order={"QCD": 1, "QED": 1}
)

GC_15 = Coupling(name="GC_15", value="complex(0,1)*G**2", order={"QCD": 2})

GC_16 = Coupling(
    name="GC_16", value="(betaL3x3*complex(0,1)*gU)/cmath.sqrt(2)", order={"NP": 1}
)

GC_17 = Coupling(
    name="GC_17", value="(betaRd3x3*complex(0,1)*gU)/cmath.sqrt(2)", order={"NP": 1}
)

GC_18 = Coupling(name="GC_18", value="-I2a13", order={"QED": 1})

GC_19 = Coupling(name="GC_19", value="-I2a23", order={"QED": 1})

GC_20 = Coupling(name="GC_20", value="-I2a33", order={"QED": 1})

GC_21 = Coupling(name="GC_21", value="I3a31", order={"QED": 1})

GC_22 = Coupling(name="GC_22", value="I3a32", order={"QED": 1})

GC_23 = Coupling(name="GC_23", value="I3a33", order={"QED": 1})

GC_24 = Coupling(name="GC_24", value="complex(0,1)*gGp*I5a11", order={"NP": 1})

GC_25 = Coupling(name="GC_25", value="complex(0,1)*gGp*I5a12", order={"NP": 1})

GC_26 = Coupling(name="GC_26", value="complex(0,1)*gGp*I5a13", order={"NP": 1})

GC_27 = Coupling(name="GC_27", value="complex(0,1)*gGp*I5a21", order={"NP": 1})

GC_28 = Coupling(name="GC_28", value="complex(0,1)*gGp*I5a22", order={"NP": 1})

GC_29 = Coupling(name="GC_29", value="complex(0,1)*gGp*I5a23", order={"NP": 1})

GC_30 = Coupling(name="GC_30", value="complex(0,1)*gGp*I5a31", order={"NP": 1})

GC_31 = Coupling(name="GC_31", value="complex(0,1)*gGp*I5a32", order={"NP": 1})

GC_32 = Coupling(name="GC_32", value="complex(0,1)*gGp*I5a33", order={"NP": 1})

GC_33 = Coupling(
    name="GC_33", value="(complex(0,1)*gZp*I6a11)/(2.*cmath.sqrt(6))", order={"NP": 1}
)

GC_34 = Coupling(
    name="GC_34", value="(complex(0,1)*gZp*I6a12)/(2.*cmath.sqrt(6))", order={"NP": 1}
)

GC_35 = Coupling(
    name="GC_35", value="(complex(0,1)*gZp*I6a13)/(2.*cmath.sqrt(6))", order={"NP": 1}
)

GC_36 = Coupling(
    name="GC_36", value="(complex(0,1)*gZp*I6a21)/(2.*cmath.sqrt(6))", order={"NP": 1}
)

GC_37 = Coupling(
    name="GC_37", value="(complex(0,1)*gZp*I6a22)/(2.*cmath.sqrt(6))", order={"NP": 1}
)

GC_38 = Coupling(
    name="GC_38", value="(complex(0,1)*gZp*I6a23)/(2.*cmath.sqrt(6))", order={"NP": 1}
)

GC_39 = Coupling(
    name="GC_39", value="(complex(0,1)*gZp*I6a31)/(2.*cmath.sqrt(6))", order={"NP": 1}
)

GC_40 = Coupling(
    name="GC_40", value="(complex(0,1)*gZp*I6a32)/(2.*cmath.sqrt(6))", order={"NP": 1}
)

GC_41 = Coupling(
    name="GC_41", value="(complex(0,1)*gZp*I6a33)/(2.*cmath.sqrt(6))", order={"NP": 1}
)

GC_42 = Coupling(name="GC_42", value="G*kappaG1", order={"QCD": 1})

GC_43 = Coupling(name="GC_43", value="-(complex(0,1)*G**2*kappaG1)", order={"QCD": 2})

GC_44 = Coupling(name="GC_44", value="2*G*kappaG2", order={"QCD": 1})

GC_45 = Coupling(name="GC_45", value="-2*complex(0,1)*G**2*kappaG2", order={"QCD": 2})

GC_46 = Coupling(name="GC_46", value="complex(0,1)*gGp*kappaL1x1", order={"NP": 1})

GC_47 = Coupling(name="GC_47", value="complex(0,1)*gGp*kappaL2x2", order={"NP": 1})

GC_48 = Coupling(name="GC_48", value="complex(0,1)*gGp*kappaL3x3", order={"NP": 1})

GC_49 = Coupling(name="GC_49", value="complex(0,1)*gGp*kappaRd1x1", order={"NP": 1})

GC_50 = Coupling(name="GC_50", value="complex(0,1)*gGp*kappaRd2x2", order={"NP": 1})

GC_51 = Coupling(name="GC_51", value="complex(0,1)*gGp*kappaRd3x3", order={"NP": 1})

GC_52 = Coupling(name="GC_52", value="complex(0,1)*gGp*kappaRu1x1", order={"NP": 1})

GC_53 = Coupling(name="GC_53", value="complex(0,1)*gGp*kappaRu2x2", order={"NP": 1})

GC_54 = Coupling(name="GC_54", value="complex(0,1)*gGp*kappaRu3x3", order={"NP": 1})

GC_55 = Coupling(name="GC_55", value="-(complex(0,1)*G*kappaU)", order={"QCD": 1})

GC_56 = Coupling(name="GC_56", value="G**2 - G**2*kappaU", order={"QCD": 2})

GC_57 = Coupling(
    name="GC_57", value="(-2*ee*complex(0,1)*kappaUtilde)/3.", order={"QED": 1}
)

GC_58 = Coupling(name="GC_58", value="complex(0,1)*KappaZp", order={"NP": 1})

GC_59 = Coupling(name="GC_59", value="-2*complex(0,1)*lam", order={"QED": 2})

GC_60 = Coupling(name="GC_60", value="-4*complex(0,1)*lam", order={"QED": 2})

GC_61 = Coupling(name="GC_61", value="-6*complex(0,1)*lam", order={"QED": 2})

GC_62 = Coupling(
    name="GC_62",
    value="(betaL3x3*complex(0,1)*gU*newCKM3x3)/cmath.sqrt(2)",
    order={"NP": 1},
)

GC_63 = Coupling(
    name="GC_63", value="(ee**2*complex(0,1))/(2.*sw**2)", order={"QED": 2}
)

GC_64 = Coupling(name="GC_64", value="-((ee**2*complex(0,1))/sw**2)", order={"QED": 2})

GC_65 = Coupling(
    name="GC_65", value="(cw**2*ee**2*complex(0,1))/sw**2", order={"QED": 2}
)

GC_66 = Coupling(name="GC_66", value="-ee/(2.*sw)", order={"QED": 1})

GC_67 = Coupling(name="GC_67", value="-(ee*complex(0,1))/(2.*sw)", order={"QED": 1})

GC_68 = Coupling(name="GC_68", value="(ee*complex(0,1))/(2.*sw)", order={"QED": 1})

GC_69 = Coupling(
    name="GC_69", value="(ee*complex(0,1))/(sw*cmath.sqrt(2))", order={"QED": 1}
)

GC_70 = Coupling(
    name="GC_70", value="(CKM1x1*ee*complex(0,1))/(sw*cmath.sqrt(2))", order={"QED": 1}
)

GC_71 = Coupling(
    name="GC_71", value="(CKM1x2*ee*complex(0,1))/(sw*cmath.sqrt(2))", order={"QED": 1}
)

GC_72 = Coupling(
    name="GC_72", value="(CKM1x3*ee*complex(0,1))/(sw*cmath.sqrt(2))", order={"QED": 1}
)

GC_73 = Coupling(
    name="GC_73", value="(CKM2x1*ee*complex(0,1))/(sw*cmath.sqrt(2))", order={"QED": 1}
)

GC_74 = Coupling(
    name="GC_74", value="(CKM2x2*ee*complex(0,1))/(sw*cmath.sqrt(2))", order={"QED": 1}
)

GC_75 = Coupling(
    name="GC_75", value="(CKM2x3*ee*complex(0,1))/(sw*cmath.sqrt(2))", order={"QED": 1}
)

GC_76 = Coupling(
    name="GC_76", value="(CKM3x1*ee*complex(0,1))/(sw*cmath.sqrt(2))", order={"QED": 1}
)

GC_77 = Coupling(
    name="GC_77", value="(CKM3x2*ee*complex(0,1))/(sw*cmath.sqrt(2))", order={"QED": 1}
)

GC_78 = Coupling(
    name="GC_78", value="(CKM3x3*ee*complex(0,1))/(sw*cmath.sqrt(2))", order={"QED": 1}
)

GC_79 = Coupling(name="GC_79", value="-(cw*ee*complex(0,1))/(2.*sw)", order={"QED": 1})

GC_80 = Coupling(name="GC_80", value="(cw*ee*complex(0,1))/(2.*sw)", order={"QED": 1})

GC_81 = Coupling(name="GC_81", value="-((cw*ee*complex(0,1))/sw)", order={"QED": 1})

GC_82 = Coupling(name="GC_82", value="(cw*ee*complex(0,1))/sw", order={"QED": 1})

GC_83 = Coupling(name="GC_83", value="-ee**2/(2.*sw)", order={"QED": 2})

GC_84 = Coupling(name="GC_84", value="-(ee**2*complex(0,1))/(2.*sw)", order={"QED": 2})

GC_85 = Coupling(name="GC_85", value="ee**2/(2.*sw)", order={"QED": 2})

GC_86 = Coupling(name="GC_86", value="(-2*cw*ee**2*complex(0,1))/sw", order={"QED": 2})

GC_87 = Coupling(name="GC_87", value="-(ee*complex(0,1)*sw)/(6.*cw)", order={"QED": 1})

GC_88 = Coupling(name="GC_88", value="(ee*complex(0,1)*sw)/(2.*cw)", order={"QED": 1})

GC_89 = Coupling(
    name="GC_89", value="(-2*ee*complex(0,1)*sw)/(3.*cw)", order={"QED": 1}
)

GC_90 = Coupling(
    name="GC_90", value="(8*ee**2*complex(0,1)*sw)/(9.*cw)", order={"QED": 2}
)

GC_91 = Coupling(
    name="GC_91", value="(4*ee*complex(0,1)*G*sw)/(3.*cw)", order={"QCD": 1, "QED": 1}
)

GC_92 = Coupling(
    name="GC_92", value="(2*ee*complex(0,1)*kappaUtilde*sw)/(3.*cw)", order={"QED": 1}
)

GC_93 = Coupling(
    name="GC_93", value="(4*ee**2*complex(0,1)*sw**2)/(9.*cw**2)", order={"QED": 2}
)

GC_94 = Coupling(
    name="GC_94", value="-(cw*ee)/(2.*sw) - (ee*sw)/(2.*cw)", order={"QED": 1}
)

GC_95 = Coupling(
    name="GC_95",
    value="-(cw*ee*complex(0,1))/(2.*sw) + (ee*complex(0,1)*sw)/(2.*cw)",
    order={"QED": 1},
)

GC_96 = Coupling(
    name="GC_96",
    value="(cw*ee*complex(0,1))/(2.*sw) + (ee*complex(0,1)*sw)/(2.*cw)",
    order={"QED": 1},
)

GC_97 = Coupling(
    name="GC_97",
    value="(cw*ee**2*complex(0,1))/sw - (ee**2*complex(0,1)*sw)/cw",
    order={"QED": 2},
)

GC_98 = Coupling(
    name="GC_98",
    value="-(ee**2*complex(0,1)) + (cw**2*ee**2*complex(0,1))/(2.*sw**2) + (ee**2*complex(0,1)*sw**2)/(2.*cw**2)",
    order={"QED": 2},
)

GC_99 = Coupling(
    name="GC_99",
    value="ee**2*complex(0,1) + (cw**2*ee**2*complex(0,1))/(2.*sw**2) + (ee**2*complex(0,1)*sw**2)/(2.*cw**2)",
    order={"QED": 2},
)

GC_100 = Coupling(name="GC_100", value="-(ee**2*vev)/(2.*cw)", order={"QED": 1})

GC_101 = Coupling(name="GC_101", value="(ee**2*vev)/(2.*cw)", order={"QED": 1})

GC_102 = Coupling(name="GC_102", value="-2*complex(0,1)*lam*vev", order={"QED": 1})

GC_103 = Coupling(name="GC_103", value="-6*complex(0,1)*lam*vev", order={"QED": 1})

GC_104 = Coupling(name="GC_104", value="-(ee**2*vev)/(4.*sw**2)", order={"QED": 1})

GC_105 = Coupling(
    name="GC_105", value="-(ee**2*complex(0,1)*vev)/(4.*sw**2)", order={"QED": 1}
)

GC_106 = Coupling(
    name="GC_106", value="(ee**2*complex(0,1)*vev)/(2.*sw**2)", order={"QED": 1}
)

GC_107 = Coupling(name="GC_107", value="(ee**2*vev)/(4.*sw**2)", order={"QED": 1})

GC_108 = Coupling(name="GC_108", value="-(ee**2*vev)/(2.*sw)", order={"QED": 1})

GC_109 = Coupling(name="GC_109", value="(ee**2*vev)/(2.*sw)", order={"QED": 1})

GC_110 = Coupling(
    name="GC_110",
    value="-(ee**2*vev)/(4.*cw) - (cw*ee**2*vev)/(4.*sw**2)",
    order={"QED": 1},
)

GC_111 = Coupling(
    name="GC_111",
    value="(ee**2*vev)/(4.*cw) - (cw*ee**2*vev)/(4.*sw**2)",
    order={"QED": 1},
)

GC_112 = Coupling(
    name="GC_112",
    value="-(ee**2*vev)/(4.*cw) + (cw*ee**2*vev)/(4.*sw**2)",
    order={"QED": 1},
)

GC_113 = Coupling(
    name="GC_113",
    value="(ee**2*vev)/(4.*cw) + (cw*ee**2*vev)/(4.*sw**2)",
    order={"QED": 1},
)

GC_114 = Coupling(
    name="GC_114",
    value="-(ee**2*complex(0,1)*vev)/2. - (cw**2*ee**2*complex(0,1)*vev)/(4.*sw**2) - (ee**2*complex(0,1)*sw**2*vev)/(4.*cw**2)",
    order={"QED": 1},
)

GC_115 = Coupling(
    name="GC_115",
    value="ee**2*complex(0,1)*vev + (cw**2*ee**2*complex(0,1)*vev)/(2.*sw**2) + (ee**2*complex(0,1)*sw**2*vev)/(2.*cw**2)",
    order={"QED": 1},
)

GC_116 = Coupling(
    name="GC_116", value="-((complex(0,1)*yt)/cmath.sqrt(2))", order={"QED": 1}
)

GC_117 = Coupling(name="GC_117", value="yt/cmath.sqrt(2)", order={"QED": 1})

GC_118 = Coupling(
    name="GC_118",
    value="-(complex(0,1)*gZp*zetal2x2*cmath.sqrt(1.5))/2.",
    order={"NP": 1},
)

GC_119 = Coupling(
    name="GC_119",
    value="-(complex(0,1)*gZp*zetal2x3*cmath.sqrt(1.5))/2.",
    order={"NP": 1},
)

GC_120 = Coupling(
    name="GC_120",
    value="-(complex(0,1)*gZp*zetal3x2*cmath.sqrt(1.5))/2.",
    order={"NP": 1},
)

GC_121 = Coupling(
    name="GC_121",
    value="-(complex(0,1)*gZp*zetal3x3*cmath.sqrt(1.5))/2.",
    order={"NP": 1},
)

GC_122 = Coupling(
    name="GC_122",
    value="(complex(0,1)*gZp*zetaq1x1)/(2.*cmath.sqrt(6))",
    order={"NP": 1},
)

GC_123 = Coupling(
    name="GC_123",
    value="(complex(0,1)*gZp*zetaq2x2)/(2.*cmath.sqrt(6))",
    order={"NP": 1},
)

GC_124 = Coupling(
    name="GC_124",
    value="(complex(0,1)*gZp*zetaq3x3)/(2.*cmath.sqrt(6))",
    order={"NP": 1},
)

GC_125 = Coupling(
    name="GC_125",
    value="(complex(0,1)*gZp*zetaRd1x1)/(2.*cmath.sqrt(6))",
    order={"NP": 1},
)

GC_126 = Coupling(
    name="GC_126",
    value="(complex(0,1)*gZp*zetaRd2x2)/(2.*cmath.sqrt(6))",
    order={"NP": 1},
)

GC_127 = Coupling(
    name="GC_127",
    value="(complex(0,1)*gZp*zetaRd3x3)/(2.*cmath.sqrt(6))",
    order={"NP": 1},
)

GC_128 = Coupling(
    name="GC_128",
    value="-(complex(0,1)*gZp*zetaRe2x2*cmath.sqrt(1.5))/2.",
    order={"NP": 1},
)

GC_129 = Coupling(
    name="GC_129",
    value="-(complex(0,1)*gZp*zetaRe3x3*cmath.sqrt(1.5))/2.",
    order={"NP": 1},
)

GC_130 = Coupling(
    name="GC_130",
    value="(complex(0,1)*gZp*zetaRu1x1)/(2.*cmath.sqrt(6))",
    order={"NP": 1},
)

GC_131 = Coupling(
    name="GC_131",
    value="(complex(0,1)*gZp*zetaRu2x2)/(2.*cmath.sqrt(6))",
    order={"NP": 1},
)

GC_132 = Coupling(
    name="GC_132",
    value="(complex(0,1)*gZp*zetaRu3x3)/(2.*cmath.sqrt(6))",
    order={"NP": 1},
)

GC_133 = Coupling(
    name="GC_133",
    value="(ee*complex(0,1)*complexconjugate(CKM1x1))/(sw*cmath.sqrt(2))",
    order={"QED": 1},
)

GC_134 = Coupling(
    name="GC_134",
    value="(ee*complex(0,1)*complexconjugate(CKM1x2))/(sw*cmath.sqrt(2))",
    order={"QED": 1},
)

GC_135 = Coupling(
    name="GC_135",
    value="(ee*complex(0,1)*complexconjugate(CKM1x3))/(sw*cmath.sqrt(2))",
    order={"QED": 1},
)

GC_136 = Coupling(
    name="GC_136",
    value="(ee*complex(0,1)*complexconjugate(CKM2x1))/(sw*cmath.sqrt(2))",
    order={"QED": 1},
)

GC_137 = Coupling(
    name="GC_137",
    value="(ee*complex(0,1)*complexconjugate(CKM2x2))/(sw*cmath.sqrt(2))",
    order={"QED": 1},
)

GC_138 = Coupling(
    name="GC_138",
    value="(ee*complex(0,1)*complexconjugate(CKM2x3))/(sw*cmath.sqrt(2))",
    order={"QED": 1},
)

GC_139 = Coupling(
    name="GC_139",
    value="(ee*complex(0,1)*complexconjugate(CKM3x1))/(sw*cmath.sqrt(2))",
    order={"QED": 1},
)

GC_140 = Coupling(
    name="GC_140",
    value="(ee*complex(0,1)*complexconjugate(CKM3x2))/(sw*cmath.sqrt(2))",
    order={"QED": 1},
)

GC_141 = Coupling(
    name="GC_141",
    value="(ee*complex(0,1)*complexconjugate(CKM3x3))/(sw*cmath.sqrt(2))",
    order={"QED": 1},
)

GC_142 = Coupling(
    name="GC_142",
    value="(betaL3x3*complex(0,1)*gU*complexconjugate(newCKM3x3))/cmath.sqrt(2)",
    order={"NP": 1},
)
