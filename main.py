from cli import parser_cli, get_interactive_input
from fetcher import fetch_articles
from storage import save_to_json
import textwrap

def main():
    args = parser_cli()

    if not args.query:
        args = get_interactive_input()

    print(f"\n🔍 Searching for '{args.query}' - (Limit - {args.limit})")

    articles = fetch_articles(
        query=args.query,
        limit=args.limit,
        open_access=args.open_access
    )

    if not articles:
        print("❌ No relevant article found!")
        return

    print(f"\nFound {len(articles)} articles:\n")
    print("=" * 80)
    for i, article in enumerate(articles, start=1):
        print(f"\n[{i}] {article['title']}")
        print(f"    Authors : {article['author']}")
        print(f"    Year    : {article['pub_year']} | DOI: {article['doi']} | ID: {article['id']}")
        
        abstract = article['abstract']
        if len(abstract) > 250:
            abstract = abstract[:250].rsplit(' ', 1)[0] + "..."
            
        wrapped_abstract = textwrap.fill(abstract, width=75, initial_indent="    Abstract: ", subsequent_indent="              ")
        print(wrapped_abstract)
        print("\n" + "-" * 80)

    if args.output:
        save_to_json(articles, args.output)

if __name__ == "__main__":
    main()