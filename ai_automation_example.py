"""
X API AI Automation Example
==========================

Simple example for searching recent posts and generating a summary using AI (placeholder).
Uses official XDK (pip install xdk).

Requirements:
- Set BEARER_TOKEN environment variable (app-only auth for search).
- For posting, use OAuth 2.0 PKCE with CLIENT_ID / CLIENT_SECRET.

Follow X Automation Rules: https://help.x.com/en/rules-and-policies/x-automation
- Use official API
- No spam, no mass unsolicited replies
- Original content at human pace
"""

import os
import json
from xdk import Client

def search_recent_posts(query: str, max_results: int = 10):
    """Search recent posts (last 7 days) using Bearer Token."""
    bearer_token = os.environ.get("BEARER_TOKEN")
    if not bearer_token:
        raise ValueError("BEARER_TOKEN environment variable is required")
    
    client = Client(bearer_token=bearer_token)
    
    results = []
    for page in client.posts.search_recent(query=query, max_results=max_results):
        if page.data:
            for post in page.data:
                results.append({
                    "id": post.id,
                    "text": post.text,
                    "author_id": getattr(post, "author_id", None),
                    "created_at": getattr(post, "created_at", None),
                })
        break  # Limit to first page for example
    return results

def generate_ai_summary(posts):
    """Placeholder for AI summary generation.
    Integrate with Grok, OpenAI, Claude, etc."""
    if not posts:
        return "No posts found."
    texts = [p["text"] for p in posts[:5]]
    summary = "Recent posts summary (AI placeholder):\n" + "\n".join(f"- {t[:100]}..." for t in texts)
    return summary

def main():
    query = "AI automation OR X API"
    print(f"Searching for: {query}")
    posts = search_recent_posts(query, max_results=5)
    print(f"Found {len(posts)} posts")
    print(json.dumps(posts, indent=2, ensure_ascii=False))
    
    summary = generate_ai_summary(posts)
    print("\n" + summary)

if __name__ == "__main__":
    main()
