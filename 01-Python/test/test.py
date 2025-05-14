def wave(people):
    result = []
    for i, p in enumerate(people):
        if p.isalpha():
            wave = people[:i] + p.upper() + people[i+1:]
            result.append(wave)

    result = [people[:i] + people[i].upper() + people[i+1:] for i in range(len(people)) if i.isalpha() ]

    return result

print(wave('   gap  '))
# wave("hello") => ["Hello", "hEllo", "heLlo", "helLo", "hellO"]
