#module_characters_jap.py
#This module lists all japanese characteres in a dictionary (romaji and hiragana and katakana).

from typing import NamedTuple

class Syll(NamedTuple) :
    roma: str #"str"
    hira: int #chr(int)
    kata: int #chr(int)

def printSyll(a):
    print(f""" {a.roma} -> Hira = {a.hira} Kata = {a.kata}""")


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


#creation of all simple kanas
#i = (0, 4)
a = Syll("a", chr(12354), chr(12450))
i = Syll("i", chr(12356), chr(12452))
u = Syll("u", chr(12358), chr(12454))
e = Syll("e", chr(12360), chr(12456))
o = Syll("o", chr(12362), chr(12458))
#printSyll(a), printSyll(i), printSyll(u), printSyll(e), printSyll(o)

#i = (5, 14)
ka = Syll("ka", chr(12363), chr(12459))
ki = Syll("ki", chr(12365), chr(12461))
ku = Syll("ku", chr(12367), chr(12463))
ke = Syll("ke", chr(12369), chr(12465))
ko = Syll("ko", chr(12371), chr(12467))
ga = Syll("ga", chr(12364), chr(12460))
gi = Syll("gi", chr(12366), chr(12462))
gu = Syll("gu", chr(12368), chr(12464))
ge = Syll("ge", chr(12370), chr(12466))
go = Syll("go", chr(12372), chr(12468))
#printSyll(ka), printSyll(ki), printSyll(ku), printSyll(ke), printSyll(ko)
#printSyll(ga), printSyll(gi), printSyll(gu), printSyll(ge), printSyll(go)

#i = (15, 24)
sa = Syll("sa", chr(12373), chr(12469))
shi = Syll("shi", chr(12375), chr(12471))
su = Syll("su", chr(12377), chr(12473))
se = Syll("se", chr(12379), chr(12475))
so = Syll("so", chr(12381), chr(12477))
za = Syll("za", chr(12374), chr(12470))
jiS = Syll("ji", chr(12376), chr(12472))
zuS = Syll("zu", chr(12378), chr(12474))
ze = Syll("ze", chr(12380), chr(12476))
zo = Syll("zo", chr(12382), chr(12478))
#printSyll(sa), printSyll(shi), printSyll(su), printSyll(se), printSyll(so)
#printSyll(za), printSyll(jiS), printSyll(zuS), printSyll(ze), printSyll(zo)

#i = (25, 34)
ta = Syll("ta", chr(12383), chr(12479))
chi = Syll("chi", chr(12385), chr(12481))
tsu = Syll("tsu", chr(12388), chr(12484))
te = Syll("te", chr(12390), chr(12486))
to = Syll("to", chr(12392), chr(12488))
da = Syll("da", chr(12384), chr(12480))
jiD = Syll("ji", chr(12386), chr(12482))
zuD = Syll("zu", chr(12389), chr(12485))
de = Syll("de", chr(12391), chr(12487))
do = Syll("do", chr(12393), chr(12489))
#printSyll(ta), printSyll(chi), printSyll(tsu), printSyll(te), printSyll(to)
#printSyll(da), printSyll(jiD), printSyll(zuD), printSyll(de), printSyll(do)

#i = (35, 39)
na = Syll("na", chr(12394), chr(12490))
ni = Syll("ni", chr(12395), chr(12491))
nu = Syll("nu", chr(12396), chr(12492))
ne = Syll("ne", chr(12397), chr(12493))
no = Syll("no", chr(12398), chr(12494))
#printSyll(na), printSyll(ni), printSyll(nu), printSyll(ne), printSyll(no)

#i = (40, 54)
ha = Syll("ha", chr(12399), chr(12495))
hi = Syll("hi", chr(12402), chr(12498))
fu = Syll("fu", chr(12405), chr(12501))
he = Syll("he", chr(12408), chr(12504))
ho = Syll("ho", chr(12411), chr(12507))
ba = Syll("ba", chr(12400), chr(12496))
bi = Syll("bi", chr(12403), chr(12499))
bu = Syll("bu", chr(12406), chr(12502))
be = Syll("be", chr(12409), chr(12505))
bo = Syll("bo", chr(12412), chr(12508))
pa = Syll("pa", chr(12401), chr(12497))
pi = Syll("pi", chr(12404), chr(12500))
pu = Syll("pu", chr(12407), chr(12503))
pe = Syll("pe", chr(12410), chr(12506))
po = Syll("po", chr(12413), chr(12509))
#printSyll(ha), printSyll(hi), printSyll(fu), printSyll(he), printSyll(ho)
#printSyll(ba), printSyll(bi), printSyll(bu), printSyll(be), printSyll(bo)
#printSyll(pa), printSyll(pi), printSyll(pu), printSyll(pe), printSyll(po)

#i = (55, 59)
ma = Syll("ma", chr(12414), chr(12510))
mi = Syll("mi", chr(12415), chr(12511))
mu = Syll("mu", chr(12416), chr(12512))
me = Syll("me", chr(12417), chr(12513))
mo = Syll("mo", chr(12418), chr(12514))
#printSyll(ma), printSyll(mi), printSyll(mu), printSyll(me), printSyll(mo)

#i = (60, 62)
ya = Syll("ya", chr(12420), chr(12516))
yu = Syll("yu", chr(12422), chr(12518))
yo = Syll("yo", chr(12424), chr(12520))
#printSyll(ya), printSyll(yu), printSyll(yo)

#i = (63, 67)
ra = Syll("ra", chr(12425), chr(12521))
ri = Syll("ri", chr(12426), chr(12522))
ru = Syll("ru", chr(12427), chr(12523))
re = Syll("re", chr(12428), chr(12524))
ro = Syll("ro", chr(12429), chr(12525))
#printSyll(ra), printSyll(ri), printSyll(ru), printSyll(re), printSyll(ro)

#i = (68, 70)
wa = Syll("wa", chr(12431), chr(12527))
wo = Syll("wo", chr(12434), chr(12530))
n = Syll("n", chr(12435), chr(12531))
#printSyll(wa), printSyll(wo), printSyll(n)
 

longVowel = Syll("", 0, chr(12540))
#printSyll(longVowel)



#special kanas
yaSmall = Syll("", chr(12419), chr(12515))
yuSmall = Syll("", chr(12421), chr(12517))
yoSmall = Syll("", chr(12423), chr(12519))
tsuSmall = Syll("", chr(12387), chr(12483))
aSmall = Syll("", chr(12353), chr(12449))
iSmall = Syll("", chr(12355), chr(12451))
uSmall = Syll("", chr(12357), chr(12453))
eSmall = Syll("", chr(12359), chr(12455))
oSmall = Syll("", chr(12361), chr(12457))
#printSyll(yaSmall), printSyll(yuSmall), printSyll(yoSmall), printSyll(aSmall), printSyll(iSmall), printSyll(uSmall), printSyll(eSmall), printSyll(oSmall)


kya = Syll("kya", ki.hira + yaSmall.hira, ki.kata + yaSmall.kata)
kyu = Syll("kyu", ki.hira + yuSmall.hira, ki.kata + yuSmall.kata)
kyo = Syll("kyo", ki.hira + yoSmall.hira, ki.kata + yoSmall.kata)
#printSyll(kya), printSyll(kyu), printSyll(kyo)

gya = Syll("gya", gi.hira + yaSmall.hira, gi.kata + yaSmall.kata)
gyu = Syll("gyu", gi.hira + yuSmall.hira, gi.kata + yuSmall.kata)
gyo = Syll("gyo", gi.hira + yoSmall.hira, gi.kata + yoSmall.kata)
#printSyll(gya), printSyll(gyu), printSyll(gyo)

sha = Syll("sha", shi.hira + yaSmall.hira, shi.kata + yaSmall.kata)
shu = Syll("shu", shi.hira + yuSmall.hira, shi.kata + yuSmall.kata)
sho = Syll("sho", shi.hira + yoSmall.hira, shi.kata + yoSmall.kata)
#printSyll(sha), printSyll(shu), printSyll(sho)

cha = Syll("cha", chi.hira + yaSmall.hira, chi.kata + yaSmall.kata)
chu = Syll("chu", chi.hira + yuSmall.hira, chi.kata + yuSmall.kata)
cho = Syll("cho", chi.hira + yoSmall.hira, chi.kata + yoSmall.kata)
#printSyll(cha), printSyll(chu), printSyll(cho)

ja = Syll("ja", jiS.hira + yaSmall.hira, jiS.kata + yaSmall.kata)
ju = Syll("ju", jiS.hira + yuSmall.hira, jiS.kata + yuSmall.kata)
jo = Syll("jo", jiS.hira + yoSmall.hira, jiS.kata + yoSmall.kata)
#printSyll(ja), printSyll(ju), printSyll(jo)

nya = Syll("nya", ni.hira + yaSmall.hira, ni.kata + yaSmall.kata)
nyu = Syll("nyu", ni.hira + yuSmall.hira, ni.kata + yuSmall.kata)
nyo = Syll("nyo", ni.hira + yoSmall.hira, ni.kata + yoSmall.kata)
#printSyll(nya), printSyll(nyu), printSyll(nyo)

hya = Syll("hya", hi.hira + yaSmall.hira, hi.kata + yaSmall.kata)
hyu = Syll("hyu", hi.hira + yuSmall.hira, hi.kata + yuSmall.kata)
hyo = Syll("hyo", hi.hira + yoSmall.hira, hi.kata + yoSmall.kata)
#printSyll(hya), printSyll(hyu), printSyll(hyo)

bya = Syll("bya", bi.hira + yaSmall.hira, bi.kata + yaSmall.kata)
byu = Syll("byu", bi.hira + yuSmall.hira, bi.kata + yuSmall.kata)
byo = Syll("byo", bi.hira + yoSmall.hira, bi.kata + yoSmall.kata)
#printSyll(bya), printSyll(byu), printSyll(byo)

pya = Syll("pya", pi.hira + yaSmall.hira, pi.kata + yaSmall.kata)
pyu = Syll("pyu", pi.hira + yuSmall.hira, pi.kata + yuSmall.kata)
pyo = Syll("pyo", pi.hira + yoSmall.hira, pi.kata + yoSmall.kata)
#printSyll(pya), printSyll(pyu), printSyll(pyo)

mya = Syll("mya", mi.hira + yaSmall.hira, mi.kata + yaSmall.kata)
myu = Syll("myu", mi.hira + yuSmall.hira, mi.kata + yuSmall.kata)
myo = Syll("myo", mi.hira + yoSmall.hira, mi.kata + yoSmall.kata)
#printSyll(mya), printSyll(myu), printSyll(myo)

rya = Syll("rya", ri.hira + yaSmall.hira, ri.kata + yaSmall.kata)
ryu = Syll("ryu", ri.hira + yuSmall.hira, ri.kata + yuSmall.kata)
ryo = Syll("ryo", ri.hira + yoSmall.hira, ri.kata + yoSmall.kata)
#printSyll(rya), printSyll(ryu), printSyll(ryo)


vu = Syll("vu", chr(12436), chr(12532))
va = Syll("va", vu.hira + aSmall.hira, vu.kata + aSmall.kata)
vi = Syll("vi", vu.hira + iSmall.hira, vu.kata + iSmall.kata)
ve = Syll("ve", vu.hira + eSmall.hira, vu.kata + eSmall.kata)
vo = Syll("vo", vu.hira + oSmall.hira, vu.kata + oSmall.kata)
#printSyll(va), printSyll(vi), printSyll(vu), printSyll(ve), printSyll(vo)


fa = Syll("fa", fu.hira + aSmall.hira, fu.kata + aSmall.kata)
fi = Syll("fi", fu.hira + iSmall.hira, fu.kata + iSmall.kata)
fe = Syll("fe", fu.hira + eSmall.hira, fu.kata + eSmall.kata)
fo = Syll("fo", fu.hira + oSmall.hira, fu.kata + oSmall.kata)
#printSyll(fa), printSyll(fi), printSyll(fe), printSyll(fo)


wi = Syll("", u.hira + iSmall.hira, u.kata + iSmall.kata)
we = Syll("", u.hira + eSmall.hira, u.kata + eSmall.kata)
#"wo" writed "u + oSmall" exists, but i cannot implement it (because "wo" already exists)
#printSyll(wi), printSyll(we)



she = Syll("she", shi.hira + eSmall.hira, shi.kata + eSmall.kata)
je = Syll("je", jiS.hira + eSmall.hira, jiS.kata + eSmall.kata)
che = Syll("che", chi.hira + eSmall.hira, chi.kata + eSmall.kata)
ti = Syll("ti", te.hira + iSmall.hira, te.kata + iSmall.kata)
di = Syll("di", de.hira + iSmall.hira, de.kata + iSmall.kata)
tu = Syll("tu", to.hira + uSmall.hira, to.kata + uSmall.kata)
du = Syll("du", do.hira + uSmall.hira, do.kata + uSmall.kata)
#printSyll(she), printSyll(je), printSyll(che), printSyll(ti), printSyll(di), printSyll(tu), printSyll(du)


tsa = Syll("tsa", tsu.hira + aSmall.hira, tsu.kata + aSmall.kata)
tsi = Syll("tsi", tsu.hira + iSmall.hira, tsu.kata + iSmall.kata)
tse = Syll("tse", tsu.hira + eSmall.hira, tsu.kata + eSmall.kata)
tso = Syll("tso", tsu.hira + oSmall.hira, tsu.kata + oSmall.kata)
#printSyll(tsa), printSyll(tsi), printSyll(tse), printSyll(tso)


si = Syll("si", su.hira + iSmall.hira, su.kata + iSmall.kata)
zi = Syll("zi", zuS.hira + iSmall.hira, zuS.kata + iSmall.kata)
dyu = Syll("dyu", de.hira + yuSmall.hira, de.kata + yuSmall.kata)
tyu = Syll("tyu", te.hira + yuSmall.hira, te.kata + yuSmall.kata)
kwo = Syll("kwo", ku.hira + oSmall.hira, ku.kata + oSmall.kata)
#printSyll(si), printSyll(zi), printSyll(dyu), printSyll(tyu), printSyll(kwo)



char = {
    'all' : [], 
    'vowel' : [a, i, u, e, o],
    'k' : [ka, ki, ku, ke, ko, ga, gi, gu, ge, go], 
    's' : [sa, shi, su, se, so, za, jiS, zuS, ze, zo], 
    't' : [ta, chi, tsu, te, to, da, jiD, zuD, de, do], 
    'n' : [na, ni, nu, ne, no], 
    'h' : [ha, hi, fu, he, ho, ba, bi, bu, be, bo, pa, pi, pu, pe, po], 
    'm' : [ma, mi, mu, me, mo], 
    'y' : [ya, yu, yo], 
    'r' : [ra, ri, ru, re, ro], 
    'w' : [wa, wo], 
    'nOnly' : [n], 
    'sp' : [kya, kyu, kyo, gya, gyu, gyo, 
            sha, shu, sho, 
            ja, ju, jo, 
            cha, chu, cho, 
            nya, nyu, nyo, 
            hya, hyu, hyo, bya, byu, byo, pya, pyu, pyo], 
    'sp+' : [fa, fi, fe, fo, 
             mya, myu, myo, 
             rya, ryu, ryo, 
             va, vi, vu, ve, vo, 
             wi, we, 
             she, je, che, 
             ti, di, tu, du, 
             tsa, tsi, tse, tso, 
             si, zi, dyu, tyu, kwo]}




#['all']
for n in char['vowel']:
    char['all'].append(n)
for n in char['k']:
    char['all'].append(n)
for n in char['s']:
    char['all'].append(n)
for n in char['t']:
    char['all'].append(n)
for n in char['n']:
    char['all'].append(n)
for n in char['h']:
    char['all'].append(n)
for n in char['m']:
    char['all'].append(n)
for n in char['y']:
    char['all'].append(n)
for n in char['r']:
    char['all'].append(n)
for n in char['w']:
    char['all'].append(n)
for n in char['nOnly']:
    char['all'].append(n)



#pour verifier que tout les characteres correspondent en romaji et hiragana et katakana

'''
for n in char['sp']:
    char['all'].append(n)
for n in char['sp+']:
    char['all'].append(n)

n = len(char['all'])
print(f"""Taille de la liste [all] = {n}\n""")

for i in range(0, n):
    print(f"""{i} {char['all'][i]}""")
'''
