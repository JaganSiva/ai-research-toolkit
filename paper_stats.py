
# AI Research Toolkit
# Paper Statistics Generator

title = input("Enter paper title: ")
authors = input("Enter authors: ")
year = input("Enter publication year: ")
keywords = input("Enter keywords (comma separated): ")

keyword_list = [k.strip() for k in keywords.split(",") if k.strip()]

print("\n" + "=" * 50)
print("RESEARCH PAPER SUMMARY")
print("=" * 50)

print(f"Title    : {title}")
print(f"Authors  : {authors}")
print(f"Year     : {year}")
print(f"Keywords : {', '.join(keyword_list)}")
print(f"Keyword Count: {len(keyword_list)}")

print("=" * 50)
print("Summary generated successfully!")



print("Thank you for using AI Research Toolkit!")    