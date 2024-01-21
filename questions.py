# dictionaries of questions with 4 answers each (the correct one is always the first)
kt_questions = {
    "Ist der Entdecker des Neutrinos Fan eines Hamburger Fußball-Zweitligisten, dann unterstützt der ...": ("Wolfgang Pauli", "Enrico Fermi", "Richard Feynman", "Peter Higgs"),
    "Nukleone und Nuklide: Was zeichnet ein Isotop aus?": ("gleiche Protonenzahl Z", "gleiche Massezahl A", "gleiche Neutronenzahl N", "gleicher Bizepsumfang"),
    "Nukleone und Nuklide: Was zeichnet ein Isoton aus?": ("gleiche Neutronenzahl N", "gleiche Protonenzahl Z", "gleiche Massezahl A", "gleicher Bizepsumfang"),
    "Nukleone und Nuklide: Was zeichnet ein Isobar aus?": ("gleiche Massezahl A", "gleiche Protonenzahl Z", "gleiche Neutronenzahl N", "gleicher Bizepsumfang"),
    "Tröpfchenmodell: Bei welcher Energie hat die Bindungsenergie pro Nukleon laut Bethe-Weizsäcker-Massenformel ihr Maximum?": ("8,7 MeV", "8,7 GeV", "93 GeV", "7,8 GeV"),
    "Tröpfchenmodell: Bei welcher atomaren Massezahl A hat die Bindungsenergie pro Nukleon laut Bethe-Weizsäcker-Massenformel ihr Maximum?": ("A = 60", "A = 40", "A = 80", "A = 20"),
    "Tröpfchenmodell: Wie lautet der Beitrag des Volumentermsterms E_V zur Bindungsenergie?": ("E_V = a_V * A", "E_V = -a_V * A", "E_V = a_V * Z^2 * A^(-1/3)", "E_V = a_V * Z^2 * A^(-1/3)"),
    "Tröpfchenmodell: Wie lautet der Beitrag des Oberflächenterms E_S zur Bindungsenergie?": ("E_S = -a_S * A^(2/3)", "E_S = -a_S * A^(-2/3)", "E_S = -a_S * A^(1/3)", "E_S = -a_S * A^(-1/3)"),
    "Tröpfchenmodell: Wie lautet der Beitrag des Coulombterms E_C zur Bindungsenergie?": ("E_C -a_C * Z^2 * A^(-1/3)", "E_C -a_C * Z^2 * A^(-2/3)", "E_C -a_C * Z^2 * A^(1/3)", "E_C -a_C * Z^2 * A^(2/3)"),
    "Tröpfchenmodell: Wie lautet der Beitrag des Symmetrieterms E_sym zur Bindungsenergie?": ("E_S = -a_S * (N-Z)^2 / A", "E_S = -a_S * (N-Z)^2 * A^(-1/2)", "E_S = -a_S * (A-Z)^2 * A^(-1/2)", "E_S = -a_S * (A-N)^2 / A^2"),
    "Tröpfchenmodell: Wie lautet der Beitrag des Paarungsterms E_P zur Bindungsenergie mit delta = (+/-) 1?": ("E_P = a_P * delta * A^(-1/2)", "E_P = a_P * delta * A^(1/2)", "E_P = a_P * delta * A", "E_P = a_P * delta * A"),
    "Tröpfchenmodell: Was tritt für Atome mit niedrigerer atomaren Massezahl A als der des Maximums der Bindungsenergie bevorzugt auf?": ("Fusionen", "beta- Zerfälle", "beta+ Zerfälle", "Zerfälle"),
    "Tröpfchenmodell: Was tritt für Atome mit größerer atomaren Massezahl A als der des Maximums der Bindungsenergie bevorzugt auf?": ("Zerfälle", "Fusionen", "beta- Zerfälle", "beta+ Zerfälle"),
    "Tröpfchenmodell: Was tritt für Isobare mit niedrigerer Ladungszahl als dem leichtesten Isobar bevorzugt auf?": ("beta- Zerfälle", "beta+ Zerfälle", "Fusionen", "Zerfälle"),
    "Tröpfchenmodell: Was tritt für Isobare mit größerer Ladungszahl als dem leichtesten Isobar bevorzugt auf?": ("beta+ Zerfälle", "beta- Zerfälle", "Fusionen", "Zerfälle"),
    "Tröpfchenmodell: Bei welcher Ladungszahl Z existiert für Massezahl A = 100 das leichteste und damit stabilste Isobar für gg oder uu Kerne?": ("Z = 42 und Z = 44", "Z = 44 (Ruthenium)", "Isobare sind immer gleich schwer", "für gerade Massezahlen A existiert ein schwerstes Isobar"),
    "Tröpfchenmodell: Bei welcher Ladungszahl Z existiert für Massezahl A = 101 das leichteste und damit stabilste Isobar für gu oder ug Kerne?": ("Z = 44 (Ruthenium)", "Z = 42 und Z = 44", "Isobare sind immer gleich schwer", "für ungerade Massezahlen A existiert ein schwerstes Isobar"),
    "Tröpfchenmodell: Welche Masse besitzt ein typisches (A = 100) leichtestes Isobar laut Bethe-Weizsäcker-Massenformel?": ("93 GeV", "8,7 MeV", "8,7 GeV", "7.8 GeV"),
    "Radioaktive Zerfälle: Was gilt für den Zusammenhang zwischen Halbwertszeit t_(1/2) und Zerfallskonstante lambda?": ("t_(1/2) = ln(2) / lambda", "t_(1/2) = -ln(2) / lambda", "t_(1/2) = lambda / ln(2)", "t_(1/2) = -lambda / ln(2)"),
    "Radioaktive Zerfälle: Was gilt für den Zusammenhang zwischen Halbwertszeit t_(1/2) und mittlerer Lebensdauer <t>?": ("t_(1/2) = ln(2) * <t>", "t_(1/2) = ln(2) / <t>", "t_(1/2) = 1 / <t>", "t_(1/2) = -ln(2) / <t>"),
    "Radioaktive Zerfälle: Was gilt für die mittlerer Lebensdauer <t> mit Zerfallskonstante lambda und Halbwertszeit t_(1/2)?": ("<t> = 1 / lambda", "<t> = t_(1/2)", "<t> = t_(1/2) / lambda", "<t> = t_(1/2) * ln(2)"),
    "Radioaktive Zerfälle: Was gilt für die mittlerer Lebensdauer <t> mit Zerfallskonstante lambda und Halbwertszeit t_(1/2)?": ("<t> = t_(1/2) / ln(2)", "<t> = t_(1/2) / lambda", "<t> = t_(1/2) * ln(2)", "<t> = t_(1/2)"),
    "Multimoden-Zerfälle: Was gilt für die Gesamt-Zerfallskonstante lambda_tot für die Zerfallskonstanten lambda_A und lambda_B?": ("lambda_tot = lambda_A + lambda_B", "lambda_tot = 1 / (lambda_A + lambda_B)", "lambda_tot = lambda_A * lambda_B", "lambda_tot = lambda_A / lambda_B"),
    "Multimoden-Zerfälle: Welcher Zusammenhang gilt zwischen Zerfallskonstante lambda_A und Zerfallswahrscheinlichkeint P_A mit Gesamt-Zerfallskonstante lambda_tot?": ("lambda_A = P_A * lambda_tot", "lambda_A = P_A / lambda_tot", "lambda_A = lambda_tot / P_A", "lambda_A = P_A"),
    "Mehrstufige radioaktive Zerfälle: Wie lautet die Differentialgleichung für N_B für den 2-stufigen Zerfall 'A -lambda_1 -> B - lambda_2 -> C'?": ("dN_B/dt = lambda_1*N_A - lambda_2*N_B", "dN_B/dt = lambda_1*N_B - lambda_2*N_A", "dN_B/dt = lambda_1*N_B - lambda_2*N_C", "dN_B/dt = lambda_1*N_C - lambda_2*N_B"),
    "Kernspaltung und Kettenreaktionen: Welches Uran wird in Kernreaktoren benötigt?": ("U-235", "U-238", "U-232", "jedes Uranisotop ist leicht spaltbar und kann verwendet werden"),
    "Kernspaltung und Kettenreaktionen: Wie groß ist der Anteil des Uranisotops U-238 in natürlichem Uran?": ("99,3 %", "93 %", "97 %", "3 %"),
    "Kernspaltung und Kettenreaktionen: Wie groß ist typischerweise der Anteil des Uranisotops U-235 in dem angereichertem Uran in Kernreaktoren?": ("3 %", "15 %", "50 %", "97 %"),
}


fk_questions = {
    "Ein Festkörper ist ...": ("fest", "weich", "flüssig", "gasförmig"),
}