import frontmatter

post = frontmatter.load("about.md")

print("YAML Metadata:")
print(post.metadata)

print("YAML Metadata title:")
print(post["title"])

print("\nMarkdown İçeriği:")
print(post.content)
