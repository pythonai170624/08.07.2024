
card_id: int = int(input("Enter a card number (2-14):"))
# 2..10, 11=J, 12=Q, 13=K, 14=A, 15=JOKER

# 3 --> 3
# 11 --> J
# 12 --> Q
# 13 --> K
# 14 --> A
# 15 --> JOKER

if card_id >= 2 and card_id <= 10:
    print(card_id)
else:
    match card_id:
        case 11:
            print("J");
        case 12:
            print("Q");
        case 13:
            print("K");
        case 14:
            print("A");
        case 15:
            print("JOKER");

match card_id:
    case 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10:
        print(card_id);
    case 11:
        print("J");
    case 12:
        print("Q");
    case 13:
        print("K");
    case 14:
        print("A");
    case 15:
        print("JOKER");
    case _: #else
        print("Invalid card");


