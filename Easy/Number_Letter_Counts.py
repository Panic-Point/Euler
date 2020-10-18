ones = ['', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
teens = ['Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
tens = ['Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
units = ['Hundred', 'Thousand', 'Million', 'Billion']


def num_to_letter(n):
    ls = list(str(n))
    sp = ''
    if len(ls) == 1:
        sp += ones[int(ls[0])]
    else:
        unit_idx = len(ls) - 3
        i = 0
        while unit_idx >= 0:
            if ones[int(ls[i])] != '':
                sp += ones[int(ls[i])] + units[unit_idx] + 'and'
            unit_idx -= 1
            i += 1

        if int(ls[i]) >= 2:
            sp += tens[int(ls[i])-2] + ones[int(ls[i+1])]
        elif int(ls[i]) >= 1:
            sp += teens[int(ls[i+1])]
        else:
            sp += ones[int(ls[i+1])]

    if sp[-3:] == 'and':
        sp = sp[:len(sp)-3]

    return len(sp)


count = 0
for n in range(1, 1001):
    count += num_to_letter(n)

print(count)

