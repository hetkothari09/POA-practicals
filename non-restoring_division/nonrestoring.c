def twos_complement(num):
    ones_comp = ''.join(['1' if bit == '0' else '0' for bit in num])
    decimal = int(ones_comp, 2) + 1
    return bin(decimal)[2:]

def main():
    num1 = int(input("Enter 1st number: "))
    num2 = int(input("Enter 2nd number: "))

    bin_num1 = bin(abs(num1))[2:]
    bin_num2 = bin(abs(num2))[2:]

    maxlen = max(len(bin_num1), len(bin_num2))

    bin_comp_num2 = twos_complement(bin_num2)
    formatted_bin_comp_num2 = bin_comp_num2.rjust(maxlen, '0')

    count = maxlen
    a = '0' * (maxlen + 1)
    q = bin_num1
    m = bin_num2
    left_shift = ''

    print("Step\tA\t\t\tQ\t\t\tQ1\tOperation")

    while count > 0:
        merged = a + q
        left_shift = merged[1:]
        a = left_shift[:maxlen + 1]

        operation = ''
        if a[0] == '1':
            sum_ = int(a, 2) + int(m, 2)
            a = bin(sum_)[2:].rjust(maxlen + 1, '0')
            if len(a) > maxlen + 1:
                a = a[1:]
            operation = "A = A + M"
        else:
            sum_ = int(a, 2) + int(formatted_bin_comp_num2, 2)
            a = bin(sum_)[2:].rjust(maxlen + 1, '0')
            if len(a) > maxlen + 1:
                a = a[1:]
            operation = "A = A - M"

        left_shift = a + q[1:]

        if a[0] == '1':
            left_shift += '0'
        else:
            left_shift += '1'

        a = left_shift[:maxlen + 1]
        q = left_shift[maxlen + 1:]

        print(f"{maxlen - count + 1}\t{a}\t{q}\t{q[0]}\t{operation}")

        count -= 1

    if a[0] == '1':
        sum_ = int(a, 2) + int(m, 2)
        a = bin(sum_)[2:].rjust(maxlen + 1, '0')
        if len(a) > maxlen + 1:
            a = a[1:]

    print("Final Result:")
    print("A:", int(a, 2))
    print("Q:", int(q, 2))

if __name__ == "__main__":
    main()
