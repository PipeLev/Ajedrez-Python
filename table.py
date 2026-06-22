tab = dict(
    letras = (" A ", " B ", " C ", " D ", " E ", " F ", " G ", " H "),
    ONE = ["NT1", "NC1", "NA1", "NR ", "NK ", "NA2", "NC2", "NT2"],
    TWO = ["NP1","NP2","NP3","NP4","NP5","NP6","NP7","NP8"],
    THRE = ["   ", "   ", "   ", "   ", "   ", "   ", "   ", "   "],
    FOUR = ["   ", "   ", "   ", "   ", "   ", "   ", "   ", "   "],
    FIVE = ["   ", "   ", "   ", "   ", "   ", "   ", "   ", "   "],
    SIX = ["   ", "   ", "   ", "   ", "   ", "   ", "   ", "   "],
    SEVEN = ["BP1","BP2","BP3","BP4","BP5","BP6","BP7","BP8"],
    EIGHT = ["BT1", "BC1", "BA1", "BR ", "BK ", "BA2", "BC2", "BT2"]
)
tipos = ("letras","ONE", "TWO", "THRE", "FOUR", "FIVE", "SIX","SEVEN", "EIGHT")

def tablero(ta, ti):
    for i in range (len(ta)):
        t = ti[i]
        print(f"{i} |{"|".join(ta[t])}|")

tablero(tab, tipos)