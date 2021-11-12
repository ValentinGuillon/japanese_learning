#This module list all japanese characteres in a dictionary (romaji and hiragana). Katagana can easily get added.
"""
#all hiragana code
for i in range(0x3040, 0x30a0):
    print(i, end=' ')
    print(chr(i))
"""
#creation of all hiraganas
a, i, u, e, o = chr(12354), chr(12356), chr(12358), chr(12360), chr(12362)
#print(a, i, u, e, o) #i(0, 4)
ka, ki ,ku, ke, ko = chr(12363), chr(12365), chr(12367), chr(12369), chr(12371)
ga, gi, gu, ge, go = chr(12364), chr(12366), chr(12368), chr(12370), chr(12372)
#print(ka, ki, ku, ke, ko, ga, gi, gu, ge, go) #i(5, 14)
sa, shi, su, se, so = chr(12373), chr(12375), chr(12377), chr(12379), chr(12381)
za, ji_s, zu_s, ze, zo = chr(12374), chr(12376), chr(12378), chr(12380), chr(12382)
#print(sa, shi, su, se, so, za, ji, zu, ze, zo) #i(15, 24)
ta, chi, tsu, te, to = chr(12383), chr(12385), chr(12388), chr(12390), chr(12392)
da, ji_d, zu_d, de, do = chr(12384), chr(12386), chr(12389), chr(12391), chr(12393)
#print(ta, chi, tsu, te, to, da, di, zu, de, do) #i(25, 34)
na, ni, nu, ne, no = chr(12394), chr(12395), chr(12396), chr(12397), chr(12398)
#print(na, ni, nu, ne, no) #i(35, 39)
ha, hi, fu, he, ho = chr(12399), chr(12402), chr(12405), chr(12408), chr(12411)
ba, bi, bu, be, bo = chr(12400), chr(12403), chr(12406), chr(12409), chr(12412)
pa, pi, pu, pe, po = chr(12401), chr(12404), chr(12407), chr(12410), chr(12413)
#print(ha, hi, fu, he, ho, ba, bi, bu, be, bo, pa, pi, pu, pe, po) #i(40, 54)
ma, mi, mu, me, mo = chr(12414), chr(12415), chr(12416), chr(12417), chr(12418)
#print(ma, mi, mu, me, mo) #i(55, 59)
ya, yu, yo = chr(12420), chr(12422), chr(12424)
#print(ya, yu, yo) #i(60, 62)
ra, ri, ru, re, ro = chr(12425), chr(12426), chr(12427), chr(12428), chr(12429)
#print(ra, ri, ru, re, ro) #i(63, 67)
wa, wo, n = chr(12431), chr(12434), chr(12435)
#print(wa, wo, n) #i(68, 70)


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
                'only_n' : ["n"]},
    'hiragana' : {'all' : [],
                  'vowel' : [a, i, u, e, o],
                  'k' : [ka, ki, ku, ke, ko, ga, gi, gu, ge, go],
                  's' : [sa, shi, su, se, so, za, ji_s, zu_s, ze, zo],
                  't' : [ta, chi, tsu, te, to, da, ji_d, zu_d, de, do],
                  'n' : [na, ni, nu, ne, no],
                  'h' : [ha, hi, fu, he, ho, ba, bi, bu, be, bo, pa, pi, pu, pe, po],
                  'm' : [ma, mi, mu, me, mo],
                  'y' : [ya, yu, yo],
                  'r' : [ra, ri, ru, re, ro],
                  'w' : [wa, wo],
                  'only_n' : [n]}
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

#['hiragana']['all']
for n in char['hiragana']['vowel']:
    char['hiragana']['all'].append(n)
for n in char['hiragana']['k']:
    char['hiragana']['all'].append(n)
for n in char['hiragana']['s']:
    char['hiragana']['all'].append(n)
for n in char['hiragana']['t']:
    char['hiragana']['all'].append(n)
for n in char['hiragana']['n']:
    char['hiragana']['all'].append(n)
for n in char['hiragana']['h']:
    char['hiragana']['all'].append(n)
for n in char['hiragana']['m']:
    char['hiragana']['all'].append(n)
for n in char['hiragana']['y']:
    char['hiragana']['all'].append(n)
for n in char['hiragana']['r']:
    char['hiragana']['all'].append(n)
for n in char['hiragana']['w']:
    char['hiragana']['all'].append(n)
for n in char['hiragana']['only_n']:
    char['hiragana']['all'].append(n)


"""
#pour verifier que tout les characteres correspondes en romaji et hiragana
i = len(char['hiragana']['all'])
print(i)
i = len(char['romaji']['all'])
print(i)

for n in range(0, i):
    print(f"{char['romaji']['all'][n]} {char['hiragana']['all'][n]}")
"""

