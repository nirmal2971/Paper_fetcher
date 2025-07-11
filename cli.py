import typer
from pubmed_paper_fetcher.fetch import fetch_papers
from pubmed_paper_fetcher.utils import save_to_csv

app = typer.Typer()

@app.command()
def fetch(query: str, file: str = "", debug: bool = False):
    """Fetch PubMed papers with non-academic authors."""
    if debug:
        print(f"Query: {query}")
    results = fetch_papers(query, debug=debug)
    if not results:
        print("No results found.")
        return
    if file:
        save_to_csv(results, file)
        print(f"Results saved to: {file}")
    else:
        for item in results:
            print(item)

def main():
    app()

if __name__ == "__main__":
    main()
