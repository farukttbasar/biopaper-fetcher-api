import argparse

#ARGPARSE

def parser_cli():
    parser = argparse.ArgumentParser(
        description="-- BioPaper Fetcher CLI --" \
        "A CLI tools retrieves biomedical articles' information via Europe PMC"
    )

    parser.add_argument(
        "-q",
        "--query",
        type=str,
        help="Enter the main topic (e.g malaria, cancer, CRISPR)",
    )

    parser.add_argument(
        "-l",
        "--limit",
        type=int,
        default=5,
        help="Number of articles to retrieve (default: 5)",
    )

    parser.add_argument(
        "--open-access",
        action="store_true",
        help="Lists only Open-Accessible articles",
    )

    return parser.parse_args()

# INTERACTIVE INPUT

def get_input(prompt, targetted_type, error_message, default=None, validator=None):
    while True:
        first_val = input(prompt).strip()

        if not first_val and default is not None:
            return default
        
        try:
            val = targetted_type(first_val)
            if validator and not validator(val):
                raise ValueError
            return val
        except ValueError:
            print(error_message)

def get_interactive_input():
    print("=" * 35)
    print("  -- BioPaper Interactive Menu --")
    print("=" * 35)

    query = get_input(
        "Search keyword > ",
        str,
        "Search keyword cannot be empty!",
        validator=lambda x: len(x) > 0
    ).lower()

    limit = get_input(
        "Number of articles to retrieve > ",
        int,
        "Please enter a positive integer!",
        validator=lambda x: x > 0
    )

    open_access_input = get_input(
        "Open the filter for open access articles? (Y/n, default: n) > ",
        str,
        "Please enter 'Y' or 'n'!",
        default="n",
        validator=lambda x: x.lower() in ["y", "n"]
    ).lower()

    open_access = open_access_input == "y"

    return argparse.Namespace(
        query=query, limit=limit, open_access=open_access
    )
