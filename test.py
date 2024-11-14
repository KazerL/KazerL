def greet(name: str) -> str:
    """Return a greeting message for the given name."""
    return f"Hello, {name}!"


def main() -> None:
    """Main function to run the greeting."""
    name = "World"
    print(greet(name))


if __name__ == "__main__":
    main()
