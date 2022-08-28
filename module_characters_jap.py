#module_characters_jap.py
#This module list all japanese characteres in a dictionary (romaji and hiragana and katakana).


#japanese code
'''
#hiragana
print("\n--------HIRAGANA")
for i in range(0x3041, 0x30a0):
    print(i, end=' ')
    print(chr(i))
#katakana
print("\n--------KATAKANA")
for i in range(0x30a1, 0x30ff):
    print(i, end=' ')
    print(chr(i))
'''



#creation of all simple hiraganas
hira_a, hira_i, hira_u, hira_e, hira_o = chr(12354), chr(12356), chr(12358), chr(12360), chr(12362)
#print(a, i, u, e, o) #i(0, 4)
hira_ka, hira_ki ,hira_ku, hira_ke, hira_ko = chr(12363), chr(12365), chr(12367), chr(12369), chr(12371)
hira_ga, hira_gi, hira_gu, hira_ge, hira_go = chr(12364), chr(12366), chr(12368), chr(12370), chr(12372)
#print(ka, ki, ku, ke, ko, ga, gi, gu, ge, go) #i(5, 14)
hira_sa, hira_shi, hira_su, hira_se, hira_so = chr(12373), chr(12375), chr(12377), chr(12379), chr(12381)
hira_za, hira_ji_s, hira_zu_s, hira_ze, hira_zo = chr(12374), chr(12376), chr(12378), chr(12380), chr(12382)
#print(sa, shi, su, se, so, za, ji, zu, ze, zo) #i(15, 24)
hira_ta, hira_chi, hira_tsu, hira_te, hira_to = chr(12383), chr(12385), chr(12388), chr(12390), chr(12392)
hira_da, hira_ji_d, hira_zu_d, hira_de, hira_do = chr(12384), chr(12386), chr(12389), chr(12391), chr(12393)
#print(ta, chi, tsu, te, to, da, di, zu, de, do) #i(25, 34)
hira_na, hira_ni, hira_nu, hira_ne, hira_no = chr(12394), chr(12395), chr(12396), chr(12397), chr(12398)
#print(na, ni, nu, ne, no) #i(35, 39)
hira_ha, hira_hi, hira_fu, hira_he, hira_ho = chr(12399), chr(12402), chr(12405), chr(12408), chr(12411)
hira_ba, hira_bi, hira_bu, hira_be, hira_bo = chr(12400), chr(12403), chr(12406), chr(12409), chr(12412)
hira_pa, hira_pi, hira_pu, hira_pe, hira_po = chr(12401), chr(12404), chr(12407), chr(12410), chr(12413)
#print(ha, hi, fu, he, ho, ba, bi, bu, be, bo, pa, pi, pu, pe, po) #i(40, 54)
hira_ma, hira_mi, hira_mu, hira_me, hira_mo = chr(12414), chr(12415), chr(12416), chr(12417), chr(12418)
#print(ma, mi, mu, me, mo) #i(55, 59)
hira_ya, hira_yu, hira_yo = chr(12420), chr(12422), chr(12424)
#print(ya, yu, yo) #i(60, 62)
hira_ra, hira_ri, hira_ru, hira_re, hira_ro = chr(12425), chr(12426), chr(12427), chr(12428), chr(12429)
#print(ra, ri, ru, re, ro) #i(63, 67)
hira_wa, hira_wo, hira_n = chr(12431), chr(12434), chr(12435)
#print(wa, wo, n) #i(68, 70)


#...special hiraganas
hira_small_ya, hira_small_yu, hira_small_yo = chr(12419), chr(12421), chr(12423)
hira_small_tsu = chr(12387)
hira_small_a, hira_small_i, hira_small_u, hira_small_e, hira_small_o = chr(12353), chr(12355), chr(12357), chr(12359), chr(12361)
hira_vu = chr(12436)
hira_va, hira_vi, hira_ve, hira_vo = hira_vu + hira_small_a, hira_vu + hira_small_i, hira_vu + hira_small_e, hira_vu + hira_small_o


hira_kya, hira_kyu, hira_kyo = hira_ki + hira_small_ya, hira_ki + hira_small_yu , hira_ki + hira_small_yo
hira_gya, hira_gyu, hira_gyo = hira_gi + hira_small_ya, hira_gi + hira_small_yu, hira_gi + hira_small_yo
hira_sha, hira_shu, hira_sho = hira_shi + hira_small_ya, hira_shi + hira_small_yu, hira_shi + hira_small_yo
hira_cha, hira_chu, hira_cho = hira_chi + hira_small_ya, hira_chi + hira_small_yu, hira_chi + hira_small_yo
hira_ja, hira_ju, hira_jo = hira_ji_s + hira_small_ya, hira_ji_s + hira_small_yu, hira_ji_s + hira_small_yo
hira_nya, hira_nyu, hira_nyo = hira_ni + hira_small_ya, hira_ni + hira_small_yu, hira_ni + hira_small_yo
hira_hya, hira_hyu, hira_hyo = hira_hi + hira_small_ya, hira_hi + hira_small_yu, hira_hi + hira_small_yo
hira_bya, hira_byu, hira_byo = hira_bi + hira_small_ya, hira_bi + hira_small_yu, hira_bi + hira_small_yo
hira_pya, hira_pyu, hira_pyo = hira_pi + hira_small_ya, hira_pi + hira_small_yu, hira_pi + hira_small_yo
hira_mya, hira_myu, hira_myo = hira_mi + hira_small_ya, hira_mi + hira_small_yu, hira_mi + hira_small_yo
hira_rya, hira_ryu, hira_ryo = hira_ri + hira_small_ya, hira_ri + hira_small_yu, hira_ri + hira_small_yo

#i know those kana doesn't exist (in hiragana)
hira_fa, hira_fi, hira_fe, hira_fo = hira_fu + hira_small_a, hira_fu + hira_small_i, hira_fu + hira_small_e, hira_fu + hira_small_o

hira_wi, hira_we = hira_u + hira_small_i, hira_u + hira_small_e

hira_she = hira_shi + hira_small_e
hira_je = hira_ji_s + hira_small_e
hira_che = hira_chi + hira_small_e
hira_ti = hira_te + hira_small_i
hira_di = hira_de + hira_small_i
hira_tu = hira_to + hira_small_u
hira_du = hira_do + hira_small_u
hira_tsa, hira_tsi, hira_tse, hira_tso = hira_tsu + hira_small_a, hira_tsu + hira_small_i, hira_tsu + hira_small_e, hira_tsu + hira_small_o

hira_si = hira_su + hira_small_i
hira_zi = hira_zu_s + hira_small_i
hira_dyu = hira_de + hira_small_yu
hira_tyu = hira_te + hira_small_yu
hira_kwo = hira_ku + hira_small_o





#creation of all simple katakanas
kata_a, kata_i, kata_u, kata_e, kata_o = chr(12450), chr(12452), chr(12454), chr(12456), chr(12458)
#print(a, i, u, e, o) #i(0, 4)
kata_ka, kata_ki ,kata_ku, kata_ke, kata_ko = chr(12459), chr(12461), chr(12463), chr(12465), chr(12467)
kata_ga, kata_gi, kata_gu, kata_ge, kata_go = chr(12460), chr(12462), chr(12464), chr(12466), chr(12468)
#print(ka, ki, ku, ke, ko, ga, gi, gu, ge, go) #i(5, 14)
kata_sa, kata_shi, kata_su, kata_se, kata_so = chr(12469), chr(12471), chr(12473), chr(12475), chr(12477)
kata_za, kata_ji_s, kata_zu_s, kata_ze, kata_zo = chr(12470), chr(12472), chr(12474), chr(12476), chr(12478)
#print(sa, shi, su, se, so, za, ji, zu, ze, zo) #i(15, 24)
kata_ta, kata_chi, kata_tsu, kata_te, kata_to = chr(12479), chr(12481), chr(12484), chr(12486), chr(12488)
kata_da, kata_ji_d, kata_zu_d, kata_de, kata_do = chr(12480), chr(12482), chr(12485), chr(12487), chr(12489)
#print(ta, chi, tsu, te, to, da, di, zu, de, do) #i(25, 34)
kata_na, kata_ni, kata_nu, kata_ne, kata_no = chr(12490), chr(12491), chr(12492), chr(12493), chr(12494)
#print(na, ni, nu, ne, no) #i(35, 39)
kata_ha, kata_hi, kata_fu, kata_he, kata_ho = chr(12495), chr(12498), chr(12501), chr(12504), chr(12507)
kata_ba, kata_bi, kata_bu, kata_be, kata_bo = chr(12496), chr(12499), chr(12502), chr(12505), chr(12508)
kata_pa, kata_pi, kata_pu, kata_pe, kata_po = chr(12497), chr(12500), chr(12503), chr(12506), chr(12509)
#print(ha, hi, fu, he, ho, ba, bi, bu, be, bo, pa, pi, pu, pe, po) #i(40, 54)
kata_ma, kata_mi, kata_mu, kata_me, kata_mo = chr(12510), chr(12511), chr(12512), chr(12513), chr(12514)
#print(ma, mi, mu, me, mo) #i(55, 59)
kata_ya, kata_yu, kata_yo = chr(12516), chr(12518), chr(12520)
#print(ya, yu, yo) #i(60, 62)
kata_ra, kata_ri, kata_ru, kata_re, kata_ro = chr(12521), chr(12522), chr(12523), chr(12524), chr(12525)
#print(ra, ri, ru, re, ro) #i(63, 67)
kata_wa, kata_wo, kata_n = chr(12527), chr(12530), chr(12531)
#print(wa, wo, n) #i(68, 70)


#...special katakanas
kata_small_ya, kata_small_yu, kata_small_yo = chr(12515), chr(12517), chr(12519)
kata_small_tsu = chr(12483)
kata_small_a, kata_small_i, kata_small_u, kata_small_e, kata_small_o = chr(12449), chr(12451), chr(12453), chr(12455), chr(12457)
kata_vu = chr(12532)
kata_va, kata_vi, kata_ve, kata_vo = kata_vu + kata_small_a, kata_vu + kata_small_i, kata_vu + kata_small_e, kata_vu + kata_small_o

kata_kya, kata_kyu, kata_kyo = kata_ki + kata_small_ya, kata_ki + kata_small_yu , kata_ki + kata_small_yo
kata_gya, kata_gyu, kata_gyo = kata_gi + kata_small_ya, kata_gi + kata_small_yu, kata_gi + kata_small_yo
kata_sha, kata_shu, kata_sho = kata_shi + kata_small_ya, kata_shi + kata_small_yu, kata_shi + kata_small_yo
kata_cha, kata_chu, kata_cho = kata_chi + kata_small_ya, kata_chi + kata_small_yu, kata_chi + kata_small_yo
kata_ja, kata_ju, kata_jo = kata_ji_s + kata_small_ya, kata_ji_s + kata_small_yu, kata_ji_s + kata_small_yo
kata_nya, kata_nyu, kata_nyo = kata_ni + kata_small_ya, kata_ni + kata_small_yu, kata_ni + kata_small_yo
kata_hya, kata_hyu, kata_hyo = kata_hi + kata_small_ya, kata_hi + kata_small_yu, kata_hi + kata_small_yo
kata_bya, kata_byu, kata_byo = kata_bi + kata_small_ya, kata_bi + kata_small_yu, kata_bi + kata_small_yo
kata_pya, kata_pyu, kata_pyo = kata_pi + kata_small_ya, kata_pi + kata_small_yu, kata_pi + kata_small_yo
kata_mya, kata_myu, kata_myo = kata_mi + kata_small_ya, kata_mi + kata_small_yu, kata_mi + kata_small_yo
kata_rya, kata_ryu, kata_ryo = kata_ri + kata_small_ya, kata_ri + kata_small_yu, kata_ri + kata_small_yo

kata_long_vowel = chr(12540)

kata_fa, kata_fi, kata_fe, kata_fo = kata_fu + kata_small_a, kata_fu + kata_small_i, kata_fu + kata_small_e, kata_fu + kata_small_o

kata_wi, kata_we = kata_u + kata_small_i, kata_u + kata_small_e
#"wo" writed "u + small_o" exist, but i cannot implement it (because "wo already exist")

kata_she = kata_shi + kata_small_e
kata_je = kata_ji_s + kata_small_e
kata_che = kata_chi + kata_small_e
kata_ti = kata_te + kata_small_i
kata_di = kata_de + kata_small_i
kata_tu = kata_to + kata_small_u
kata_du = kata_do + kata_small_u
kata_tsa, kata_tsi, kata_tse, kata_tso = kata_tsu + kata_small_a, kata_tsu + kata_small_i, kata_tsu + kata_small_e, kata_tsu + kata_small_o

kata_si = kata_su + kata_small_i
kata_zi = kata_zu_s + kata_small_i
kata_dyu = kata_de + kata_small_yu
kata_tyu = kata_te + kata_small_yu
kata_kwo = kata_ku + kata_small_o





char = {
    'romaji' : {'all' : [],
                'vowel' : ["a", "i", "u", "e", "o"],
                'k' : ["ka", "ki", "ku", "ke", "ko", "ga", "gi", "gu", "ge", "go"],
                's' : ["sa", "shi", "su", "se", "so", "za", "ji", "zu", "ze", "zo"],
                't' : ["ta", "chi", "tsu", "te", "to", "da", "ji", "zu", "de", "do"],
                'n' : ["na", "ni", "nu", "ne", "no"],
                'h' : ["ha", "hi", "fu", "he", "ho", "ba", "bi", "bu", "be", "bo", "pa", "pi", "pu", "pe", "po"],
                'm' : ["ma", "mi", "mu", "me", "mo"],
                'y' : ["ya", "yu", "yo"],
                'r' : ["ra", "ri", "ru", "re", "ro"],
                'w' : ["wa", "wo"],
                'only_n' : ["n"],
                'sp' : ["kya", "kyu", "kyo", "gya", "gyu", "gyo",
                        "sha", "shu", "sho",
                        "ja", "ju", "jo",
                        "cha", "chu", "cho",
                        "nya", "nyu", "nyo",
                        "hya", "hyu", "hyo", "bya", "byu", "byo", "pya", "pyu", "pyo"],
                'sp+' : ["fa", "fi", "fe", "fo",
                         "mya", "myu", "myo",
                         "rya", "ryu", "ryo",
                         "va", "vi", "vu", "ve", "vo",
                         "wi", "we",
                         "she", "je", "che",
                         "ti", "di", "tu", "du",
                         "tsa", "tsi", "tse", "tso",
                         "si", "zi", "dyu", "tyu", "kwo"]},
    'hira' : {'all' : [],
                  'vowel' : [hira_a, hira_i, hira_u, hira_e, hira_o],
                  'k' : [hira_ka, hira_ki, hira_ku, hira_ke, hira_ko, hira_ga, hira_gi, hira_gu, hira_ge, hira_go],
                  's' : [hira_sa, hira_shi, hira_su, hira_se, hira_so, hira_za, hira_ji_s, hira_zu_s, hira_ze, hira_zo],
                  't' : [hira_ta, hira_chi, hira_tsu, hira_te, hira_to, hira_da, hira_ji_d, hira_zu_d, hira_de, hira_do],
                  'n' : [hira_na, hira_ni, hira_nu, hira_ne, hira_no],
                  'h' : [hira_ha, hira_hi, hira_fu, hira_he, hira_ho, hira_ba, hira_bi, hira_bu, hira_be, hira_bo, hira_pa, hira_pi, hira_pu, hira_pe, hira_po],
                  'm' : [hira_ma, hira_mi, hira_mu, hira_me, hira_mo],
                  'y' : [hira_ya, hira_yu, hira_yo],
                  'r' : [hira_ra, hira_ri, hira_ru, hira_re, hira_ro],
                  'w' : [hira_wa, hira_wo],
                  'only_n' : [hira_n],
                  'sp' : [hira_kya, hira_kyu, hira_kyo, hira_gya, hira_gyu, hira_gyo,
                          hira_sha, hira_shu, hira_sho,
                          hira_ja, hira_ju, hira_jo,
                          hira_cha, hira_chu, hira_cho,
                          hira_nya, hira_nyu, hira_nyo,
                          hira_hya, hira_hyu, hira_hyo, hira_bya, hira_byu, hira_byo, hira_pya, hira_pyu, hira_pyo],
                  'sp+' : [hira_fa, hira_fi, hira_fe, hira_fo,
                           hira_mya, hira_myu, hira_myo,
                           hira_rya, hira_ryu, hira_ryo,
                           hira_va, hira_vi, hira_vu, hira_ve, hira_vo,
                           hira_wi, hira_we,
                           hira_she, hira_je, hira_che,
                           hira_ti, hira_di, hira_tu, hira_du,
                           hira_tsa, hira_tsi, hira_tse, hira_tso,
                           hira_si, hira_zi, hira_dyu, hira_tyu, hira_kwo]},
    'kata' : {'all' : [],
                  'vowel' : [kata_a, kata_i, kata_u, kata_e, kata_o],
                  'k' : [kata_ka, kata_ki, kata_ku, kata_ke, kata_ko, kata_ga, kata_gi, kata_gu, kata_ge, kata_go],
                  's' : [kata_sa, kata_shi, kata_su, kata_se, kata_so, kata_za, kata_ji_s, kata_zu_s, kata_ze, kata_zo],
                  't' : [kata_ta, kata_chi, kata_tsu, kata_te, kata_to, kata_da, kata_ji_d, kata_zu_d, kata_de, kata_do],
                  'n' : [kata_na, kata_ni, kata_nu, kata_ne, kata_no],
                  'h' : [kata_ha, kata_hi, kata_fu, kata_he, kata_ho, kata_ba, kata_bi, kata_bu, kata_be, kata_bo, kata_pa, kata_pi, kata_pu, kata_pe, kata_po],
                  'm' : [kata_ma, kata_mi, kata_mu, kata_me, kata_mo],
                  'y' : [kata_ya, kata_yu, kata_yo],
                  'r' : [kata_ra, kata_ri, kata_ru, kata_re, kata_ro],
                  'w' : [kata_wa, kata_wo],
                  'only_n' : [kata_n],
                  'sp' : [kata_kya, kata_kyu, kata_kyo, kata_gya, kata_gyu, kata_gyo,
                          kata_sha, kata_shu, kata_sho,
                          kata_ja, kata_ju, kata_jo,
                          kata_cha, kata_chu, kata_cho,
                          kata_nya, kata_nyu, kata_nyo,
                          kata_hya, kata_hyu, kata_hyo, kata_bya, kata_byu, kata_byo, kata_pya, kata_pyu, kata_pyo],
                  'sp+' : [kata_fa, kata_fi, kata_fe, kata_fo,
                           kata_mya, kata_myu, kata_myo,
                           kata_rya, kata_ryu, kata_ryo,
                           kata_va, kata_vi, kata_vu, kata_ve, kata_vo,
                           kata_wi, kata_we,
                           kata_she, kata_je, kata_che,
                           kata_ti, kata_di, kata_tu, kata_du,
                           kata_tsa, kata_tsi, kata_tse, kata_tso,
                           kata_si, kata_zi, kata_dyu, kata_tyu, kata_kwo]}
    }

#['romaji']['all']
for n in char['romaji']['vowel']:
    char['romaji']['all'].append(n)
for n in char['romaji']['k']:
    char['romaji']['all'].append(n)
for n in char['romaji']['s']:
    char['romaji']['all'].append(n)
for n in char['romaji']['t']:
    char['romaji']['all'].append(n)
for n in char['romaji']['n']:
    char['romaji']['all'].append(n)
for n in char['romaji']['h']:
    char['romaji']['all'].append(n)
for n in char['romaji']['m']:
    char['romaji']['all'].append(n)
for n in char['romaji']['y']:
    char['romaji']['all'].append(n)
for n in char['romaji']['r']:
    char['romaji']['all'].append(n)
for n in char['romaji']['w']:
    char['romaji']['all'].append(n)
for n in char['romaji']['only_n']:
    char['romaji']['all'].append(n)

#['hira']['all']
for n in char['hira']['vowel']:
    char['hira']['all'].append(n)
for n in char['hira']['k']:
    char['hira']['all'].append(n)
for n in char['hira']['s']:
    char['hira']['all'].append(n)
for n in char['hira']['t']:
    char['hira']['all'].append(n)
for n in char['hira']['n']:
    char['hira']['all'].append(n)
for n in char['hira']['h']:
    char['hira']['all'].append(n)
for n in char['hira']['m']:
    char['hira']['all'].append(n)
for n in char['hira']['y']:
    char['hira']['all'].append(n)
for n in char['hira']['r']:
    char['hira']['all'].append(n)
for n in char['hira']['w']:
    char['hira']['all'].append(n)
for n in char['hira']['only_n']:
    char['hira']['all'].append(n)

#['kata']['all']
for n in char['kata']['vowel']:
    char['kata']['all'].append(n)
for n in char['kata']['k']:
    char['kata']['all'].append(n)
for n in char['kata']['s']:
    char['kata']['all'].append(n)
for n in char['kata']['t']:
    char['kata']['all'].append(n)
for n in char['kata']['n']:
    char['kata']['all'].append(n)
for n in char['kata']['h']:
    char['kata']['all'].append(n)
for n in char['kata']['m']:
    char['kata']['all'].append(n)
for n in char['kata']['y']:
    char['kata']['all'].append(n)
for n in char['kata']['r']:
    char['kata']['all'].append(n)
for n in char['kata']['w']:
    char['kata']['all'].append(n)
for n in char['kata']['only_n']:
    char['kata']['all'].append(n)



#pour verifier que tout les characteres correspondent en romaji et hiragana et katakana

'''
for n in char['romaji']['sp']:
    char['romaji']['all'].append(n)
for n in char['romaji']['sp+']:
    char['romaji']['all'].append(n)
for n in char['hira']['sp']:
    char['hira']['all'].append(n)
for n in char['hira']['sp+']:
    char['hira']['all'].append(n)
for n in char['kata']['sp']:
    char['kata']['all'].append(n)
for n in char['kata']['sp+']:
    char['kata']['all'].append(n)

n = len(char['romaji']['all'])
print(n)

for i in range(0, n):
    print(char['romaji']['all'][i], char['hira']['all'][i], char['kata']['all'][i])
'''
