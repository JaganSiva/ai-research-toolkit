
def analyze_abstract(abstract):
    """Return basic statistics for a research abstract."""
    words = abstract.split()
    sentences = [
        part.strip()
        for part in abstract.replace("!", ".").replace("?", ".").split(".")
        if part.strip()
    ]

    return {
        "word_count": len(words),
        "character_count": len(abstract),
        "sentence_count": len(sentences),
    }


def parse_keywords(keywords):
    """Return non-empty keywords after trimming whitespace."""
    return [keyword.strip() for keyword in keywords.split(",")
            if keyword.strip()]


def main():
    title = input("Enter paper title: ")
    authors = input("Enter authors: ")
    year = input("Enter publication year: ")
    abstract = input("Enter paper abstract: ")
    keywords = input("Enter keywords (comma separated): ")

    stats = analyze_abstract(abstract)
    keyword_list = parse_keywords(keywords)

    print("\n" + "=" * 60)
    print("RESEARCH PAPER ANALYSIS")
    print("=" * 60)
    print(f"Title           : {title}")
    print(f"Authors         : {authors}")
    print(f"Year            : {year}")
    print(f"Word Count      : {stats['word_count']}")
    print(f"Character Count : {stats['character_count']}")
    print(f"Sentence Count  : {stats['sentence_count']}")
    print(f"Keyword Count   : {len(keyword_list)}")
    print(f"Keywords        : {', '.join(keyword_list)}")
    print("=" * 60)
    print("Analysis completed successfully!")
    print("AI Research Toolkit")


if __name__ == "__main__":
    main()
