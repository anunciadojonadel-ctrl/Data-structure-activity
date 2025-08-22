def to_binary(n):
    return bin(n)[2:]  # convert to binary string without '0b'

def main():
    print("=== Bitwise Operations Demo ===")
    print("1. AND (&)")
    print("2. OR (|)")
    print("3. XOR (^)")
    print("4. NOT (~)")
    print("5. Left Shift (<<)")
    print("6. Right Shift (>>)")
    
    choice = int(input("Choose an operation (1-6): "))
    a = int(input("Enter first number: "))

    if choice in [1, 2, 3, 5, 6]:
        b = int(input("Enter second number: "))

    if choice == 1:
        result = a & b
        op = "&"
    elif choice == 2:
        result = a | b
        op = "|"
    elif choice == 3:
        result = a ^ b
        op = "^"
    elif choice == 4:
        result = ~a
        op = "~"
    elif choice == 5:
        result = a << b
        op = "<<"
    elif choice == 6:
        result = a >> b
        op = ">>"
    else:
        print("Invalid choice!")
        return

    print("\n=== Result ===")
    if choice == 4:  # NOT has only one input
        print(f"{op}{a} = {result}")
        print(f"Binary: {op}{to_binary(a)} = {to_binary(result)}")
    else:
        print(f"{a} {op} {b} = {result}")
        print(f"Binary: {to_binary(a)} {op} {to_binary(b)} = {to_binary(result)}")

if __name__ == "__main__":
    main()