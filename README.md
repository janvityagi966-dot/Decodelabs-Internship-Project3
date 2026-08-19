# 🔐 Random Password Generator

A simple, secure command-line password generator written in Python. It uses the `secrets` module (not `random`) to ensure passwords are cryptographically strong and suitable for real-world use.

## Features

- Generates passwords with a mix of lowercase, uppercase, digits, and symbols
- Guarantees at least one character from each enabled category
- Uses `secrets.choice()` for cryptographically secure randomness
- Customizable password length
- Lightweight — no external dependencies

## Requirements

- Python 3.6+

## Usage

Run the script:

```bash
python password_generator.py
```

You'll be prompted to enter the desired password length:

```
Enter desired password length (min 4): 16
Generated password: xY7#kLp9$Qz2!bN4
```

## Why `secrets` instead of `random`?

Python's built-in `random` module is not cryptographically secure — it's predictable enough to be unsuitable for generating passwords, tokens, or anything security-sensitive. The `secrets` module is specifically designed for this purpose.

## License

This project is licensed under the MIT License.

## Contributing

Contributions, issues, and feature requests are welcome. Feel free to open a pull request or an issue.
