# 1. Prevod na Pig Latin
def pig_latin(slovo: str) -> str:
    return slovo[1::] + slovo[0] + "ay"

# 2. Palindrome checker
def je_palindrom(slovo: str) -> bool:
    return slovo == slovo[::-1]

# 3. Pocet samohlasek
def pocet_samohlasek(s: str) -> int:
    samohlasky = "aáeéěiíoóuůúyýAÁEÉĚIÍOÓUŮÚYÝ"
    return sum(map(lambda c: s.count(c), samohlasky))

# 4. Generator akronymu
def generator_akronym(s: str) -> str:
    return "".join(map(lambda x: x[0].upper(), s.split()))

# 5. Caesarova šifra
def caesarova_sifra(s: str, posun: int, zasifrovat: bool = True) -> str:
    abeceda = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return "".join(map(lambda c: abeceda[(abeceda.find(c) + (posun if zasifrovat else -posun )) % (len(abeceda))], list(s)))

# 6. Pocet slov
def pocet_slov(s: str) -> int:
    return len(s.split())

# 7. Nejdelsi slovo
def nejdelsi_slovo(s: str) -> str:
    return sorted(s.split(), key=len, reverse=True)[0]

# 8. Reverzni slova ve vete
def reverzni_slova(s: str) -> str:
    return " ".join(s.split()[::-1])
