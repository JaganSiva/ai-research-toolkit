# AI Research Toolkit
# Research Paper Statistics Generator

title = input("Enter paper title: ")
authors = input("Enter authors: ")
year = input("Enter publication year: ")
abstract = input("Enter paper abstract: ")
keywords = input("Enter keywords (comma separated): ")

# Calculate statistics
word_count = len(abstract.split())
character_count = len(abstract)
sentence_count = abstract.count(".") + abstract.count("!") + abstract.count("?")

keyword_list = [k.strip() for k in keywords.split(",") if k.strip()]

# Display results
print("\n" + "=" * 60)
print("RESEARCH PAPER ANALYSIS")
print("=" * 60)

print(f"Title          : {title}")
print(f"Authors        : {authors}")
print(f"Year           : {year}")
print(f"Word Count     : {word_count}")
print(f"Character Count: {character_count}")
print(f"Sentence Count : {sentence_count}")
print(f"Keyword Count  : {len(keyword_list)}")
print(f"Keywords       : {', '.join(keyword_list)}")

print("=" * 60)
print("Analysis completed successfully!")
print("AI Research Toolkit")   