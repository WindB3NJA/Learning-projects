num = 1994
num = list(str(num))
rome_number = []

for i in range(len(num)):
    num_actual_range = "".join(num[i]+"0"*(len(num)-i-1))
    num_range = []
    for n in range(len(num) - i):
        num_range.append(num[n + i])

    if len(num_actual_range) == 4:
        times = int(int(num_actual_range) / 1000)
        if times != 0:
            rome_number.append("M"*times)

    elif len(num_actual_range) == 3:
        times = int(int(num_actual_range) / 100)
        if times != 0:
            if times < 4:
                rome_number.append("C"*times)
            elif times == 4:
                rome_number.append("CD")
            elif 9 >= times >= 5:
                if 9 == times:
                    rome_number.append("CM")
                else:
                    times = times % 5
                    rome_number.append("D"+("C"*times))

    elif len(num_actual_range) == 2:
        times = int(int(num_actual_range) / 10)
        if times != 0:
            if times < 4:
                rome_number.append("X" * times)
            elif times == 4:
                rome_number.append("XL")
            elif 9 >= times >= 5:
                if 9 == times:
                    rome_number.append("XC")
                else:
                    times = times % 5
                    rome_number.append("L"+("X" * times))

    elif len(num_actual_range) == 1:
        times = int(int(num_actual_range) / 1)
        if times != 0:
            if times < 4:
                rome_number.append("I" * times)
            elif times == 4:
                rome_number.append("IV")
            elif 9 >= times >= 5:
                if 9 == times:
                    rome_number.append("IX")
                else:
                    times = times % 5
                    rome_number.append("V"+"I" * times)

rome_number = "".join(rome_number)


