#Logan H's Initials Finder
#
def get_initials(full_name):
    name_parts = full_name.split()
    initials = " ".join(part[0].upper() + '.' for part in name_parts)
    return initials

full_name = input("Enter your full name (First Middle Last): ")
print("Initials:", get_initials(full_name))
