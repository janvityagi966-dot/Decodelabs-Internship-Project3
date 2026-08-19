import secrets
import string


def generate_password(length=12, use_upper=True, use_digits=True, use_symbols=True):
    """Generate a cryptographically secure random password."""
    if length < 4:
        raise ValueError("Password length should be at least 4 for good security.")

    # Build the pool of allowed characters
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase if use_upper else ""
    digits = string.digits if use_digits else ""
    symbols = string.punctuation if use_symbols else ""

    all_chars = lower + upper + digits + symbols
    if not all_chars:
        raise ValueError("At least one character set must be enabled.")

    # Guarantee at least one character from each selected category
    password_chars = [secrets.choice(lower)]
    if use_upper:
        password_chars.append(secrets.choice(upper))
    if use_digits:
        password_chars.append(secrets.choice(digits))
    if use_symbols:
        password_chars.append(secrets.choice(symbols))

    # Fill the rest randomly
    remaining_length = length - len(password_chars)
    password_chars += [secrets.choice(all_chars) for _ in range(remaining_length)]

    # Shuffle so guaranteed characters aren't predictable in position
    secrets.SystemRandom().shuffle(password_chars)

    return "".join(password_chars)


if __name__ == "__main__":
    length = int(input("Enter desired password length (min 4): "))
    password = generate_password(length)
    print(f"Generated password: {password}")
