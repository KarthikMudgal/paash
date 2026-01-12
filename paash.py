# WORDLIST GENERATOR (CLI + OPTIONAL COUNT LIMIT)

import argparse
import random

DEFAULT_SPECIALS = "!@#$%^&*_+-=."

words = []
common_words = []

# ---------------- CLI ---------------- #

parser = argparse.ArgumentParser(
    description="Password Wordlist Generator - Limit total password count"
)

parser.add_argument(
    "--max",
    type=int,
    default=None,
    help="Maximum number of passwords to generate (optional)"
)

args = parser.parse_args()


# ---------------- INPUT ---------------- #

def ask_questions():
    return {
        "first_name": input("Victim's first name: ").strip(),
        "last_name": input("Victim's last name: ").strip(),
        "birth_input": input(
            "Possible birth dates (DDMMYYYY or DDMMYY, comma-separated): "
        ).strip(),
        "nicknames": input("Nicknames (comma-separated): ").strip(),
        "favourites": input("Favourite things (movies, hobbies): ").strip(),
        "pets": input("Pet names (comma-separated): ").strip(),
        "family": input("Family member names (comma-separated): ").strip(),
        "special_chars": input(
            "Special characters (press Enter for default): "
        ).strip(),
    }


# ---------------- HELPERS ---------------- #

def add_item(text, is_common=False):
    if not text:
        return
    for item in text.split(","):
        clean = item.strip()
        if clean:
            words.append(clean)
            if is_common:
                common_words.append(clean)


def expand_birthdate(birthdate):
    variations = set()
    birthdate = birthdate.strip()

    if not birthdate.isdigit():
        return variations

    if len(birthdate) == 8:  # DDMMYYYY
        dd, mm, yyyy = birthdate[:2], birthdate[2:4], birthdate[4:]
        yy = yyyy[-2:]
    elif len(birthdate) == 6:  # DDMMYY
        dd, mm, yy = birthdate[:2], birthdate[2:4], birthdate[4:]
        yyyy = "19" + yy if int(yy) > 25 else "20" + yy
    else:
        return variations

    variations.update({
        dd + mm + yy,
        dd + mm + yyyy,
        mm + dd + yy,
        mm + dd + yyyy,
        yyyy,
        yy,
        mm + yyyy,
        yyyy + mm + dd,
        dd + mm,
    })

    return variations


def limit_passwords(passwords, max_count):
    """
    Limit the total number of passwords generated.
    If max_count is None or greater than total passwords, return all.
    """
    if max_count is None or max_count >= len(passwords):
        return list(passwords)

    # Convert to list and select top N
    password_list = list(passwords)

    # Try to get diverse passwords (not just first N)
    if len(password_list) > max_count * 2:
        # If we have many passwords, sample randomly for diversity
        return random.sample(password_list, max_count)
    else:
        # Otherwise take first N (which are often the most basic/common)
        return password_list[:max_count]


# ---------------- GENERATION ---------------- #

def generate_combinations(words, birth_numbers, special_chars):
    final = set()

    # Base words
    for w in words:
        final.add(w)
        if w in common_words:
            final.update([w.lower(), w.capitalize()])

    # Word + number
    for w in common_words:
        for n in birth_numbers:
            final.update({
                w + n,
                w.capitalize() + n,
                w + "_" + n,
                w + "." + n,
            })

    # Word + special + number
    for w in common_words:
        for n in birth_numbers[:3]:
            for s in special_chars[:5]:
                final.add(w + s + n)
                final.add(w.capitalize() + s + n)
                final.add(w + s + n[-2:])

    # Number + word
    for n in birth_numbers:
        for w in common_words:
            final.add(n + w)
            final.add(n + w.capitalize())

    # Two-word combos
    for i in range(min(5, len(common_words))):
        for j in range(min(5, len(common_words))):
            if i != j:
                w1, w2 = common_words[i], common_words[j]
                final.update({
                    w1 + w2,
                    w1.capitalize() + w2.capitalize(),
                    w1 + "_" + w2,
                    w1 + "." + w2,
                })

    # Leetspeak (limited)
    leet_map = {'a': '@', 'e': '3', 'i': '1', 'o': '0', 's': '$', 't': '7'}
    for w in common_words[:3]:
        leet = w.lower()
        for k, v in leet_map.items():
            leet = leet.replace(k, v)
        final.add(leet)
        for n in birth_numbers[:2]:
            final.add(leet + n)

    # Symbols at start/end
    for w in common_words:
        for s in special_chars[:3]:
            final.update({s + w, w + s, s + w + s})

    # Birth numbers alone
    final.update(birth_numbers)

    return final


# ---------------- MAIN ---------------- #

data = ask_questions()

special_chars = data["special_chars"] or DEFAULT_SPECIALS

add_item(data["first_name"], True)
add_item(data["last_name"], True)
add_item(data["nicknames"], True)
add_item(data["favourites"])
add_item(data["pets"], True)
add_item(data["family"], True)

birth_numbers = set()
if data["birth_input"]:
    for b in data["birth_input"].split(","):
        birth_numbers.update(expand_birthdate(b))

birth_numbers = list(birth_numbers)

# Generate passwords
all_passwords = generate_combinations(
    words,
    birth_numbers,
    special_chars
)

# Limit number of passwords if --max is provided
if args.max and args.max > 0:
    limited_passwords = limit_passwords(all_passwords, args.max)
    print(f"\n⚠️  Limiting output to {args.max} passwords (from {len(all_passwords)} total)")
else:
    limited_passwords = list(all_passwords)

print(f"\nGenerated {len(limited_passwords)} passwords")
print("Sample (showing all):")
for i, p in enumerate(limited_passwords, 1):
    print(f"  {i:3d}. {p}")

with open("wordlist.txt", "w") as f:
    for p in limited_passwords:
        f.write(p + "\n")

print(f"\n[*] Saved {len(limited_passwords)} passwords to wordlist.txt")

# Show statistics
if args.max and args.max > 0:
    print(f"[*] Total generated: {len(all_passwords)}")
    print(f"[*] Limited to: {args.max}")

    # Show password length distribution of limited set
    lengths = [len(p) for p in limited_passwords]
    print(f"\n[*] Password lengths in limited set:")
    print(f"[*] Shortest: {min(lengths)} chars")
    print(f"[*] Longest: {max(lengths)} chars")
    print(f"[*] Average: {sum(lengths) / len(lengths):.1f} chars")
