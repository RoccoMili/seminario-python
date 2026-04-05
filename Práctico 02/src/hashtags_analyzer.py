def analyze(posts):
    tags = {}
    for post in posts:
        words = post.split()
        hashtags = [word for word in words if word.strip().startswith("#")]
        for hashtag in hashtags:
            tags[hashtag] = tags.get(hashtag, 0) + 1
    filtered = {tag: count for tag, count in tags.items() if count > 1}
    trending = dict(sorted(filtered.items(), key=lambda x: x[1], reverse=True))
    return trending, len(tags)