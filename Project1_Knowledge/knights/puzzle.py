from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
A0_dict = And(AKnight, AKnave)
knowledge0 = And(
    Or(And(AKnight,(Not(AKnave))), And(Not(AKnight), AKnave)), #exclusive or
    Biconditional(A0_dict, AKnight) #if A0_dict is true, that implies A is a knight

)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
A1_dict = And(AKnave, BKnave)
B1_dict = Symbol('')
knowledge1 = And(
    Or(And(AKnight,(Not(AKnave))), And(Not(AKnight), AKnave)), #exclusive or for A1
    Or(And(BKnight,(Not(BKnave))), And(Not(BKnight), BKnave)), #exclusive ot for B1
    Biconditional(A1_dict, AKnight),                           #If what A1 says is true, then A1 is knight
    Biconditional(B1_dict, BKnight)

)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
A2_dict = Or(And(AKnight, BKnight), And(AKnave, BKnave))
B2_dict = Or(And(AKnight, BKnave), And(AKnave, BKnight))
knowledge2 = And(
    Or(And(AKnight, (Not(AKnave))), And(Not(AKnight), AKnave)),  # exclusive or for A2
    Or(And(BKnight, (Not(BKnave))), And(Not(BKnight), BKnave)),  # exclusive ot for B2
    Biconditional(A2_dict, AKnight),  # If what A2 says is true, then A2 is knight
    Biconditional(B2_dict, BKnight)   # If what B2 says is true, then B2 is knight
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
A3_dict = Or(AKnight, AKnave)
B3_dict = And(Symbol(A3_dict == AKnave), CKnave)
C3_dict = AKnight
knowledge3 = And(
    Or(And(AKnight, (Not(AKnave))), And(Not(AKnight), AKnave)),  # exclusive or for A3
    Or(And(BKnight, (Not(BKnave))), And(Not(BKnight), BKnave)),  # exclusive ot for B3
    Or(And(CKnight, (Not(CKnave))), And(Not(CKnight), CKnave)),  # exclusive ot for C3
    Biconditional(A3_dict, AKnight),  # If what A3 says is true, then A3 is knight
    Biconditional(B3_dict, BKnight),   # If what B3 says is true, then B3 is knight
    Biconditional(C3_dict, CKnight)   # If what C3 says is true, then C3 is knight
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
