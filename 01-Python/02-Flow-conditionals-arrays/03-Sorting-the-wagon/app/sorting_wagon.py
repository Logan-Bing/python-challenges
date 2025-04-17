
def wagon_sort(students: list[str]) -> list[str]:
    return sorted(students, key=lambda s: s.lower())

print(wagon_sort(["Julia", "logan", "rudy", "albert"]))
