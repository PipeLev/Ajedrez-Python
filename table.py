table = dict(
    letras = ("A ", "B ", "C ", "D ", "E ", "F ", "G ", "H "),
    ONE = ["T1", "C1", "A1", "R ", "K ", "A2", "C2", "T2"],
    TWO = ["P1","P2","P3","P4","P5","P6","P7","P8"],
    THRE = ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
    FOUR = ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
    FIVE = ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
    SIX = ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
    SEVEN = ["P1","P2","P3","P4","P5","P6","P7","P8"],
    EIGHT = ["T1", "C1", "A1", "R ", "K ", "A2", "C2", "T2"]
)

tipos = ("letras","ONE", "TWO", "THRE", "FOUR", "FIVE", "SIX","SEVEN", "EIGHT")

def tablero(ta, ti):
    for i in range (len(ta)):
        t = ti[i]
        print(f"{i} |{"|".join(ta[t])}|")

tablero(table, tipos)

