import tkinter as tk
import nltk
from textblob import TextBlob
from newspaper import Article

# Ensure necessary NLTK data is downloaded
# nltk.download('punkt')

def summarize():
    article_url = url_text.get("1.0", "end").strip()
    article = Article(article_url)
    article.download()
    article.parse()
    article.nlp()

    # Enable text widgets to update their content
    title_text.config(state="normal")
    author_text.config(state="normal")
    published_text.config(state="normal")
    summary_text.config(state="normal")
    sentiment_text.config(state="normal")
    keywords_text.config(state="normal")

    title_text.delete("1.0", "end")
    title_text.insert("1.0", article.title)
    
    author_text.delete("1.0", "end")
    author_text.insert("1.0", article.authors)

    published_text.delete("1.0", "end")
    published_text.insert("1.0", (article.publish_date).strftime("%B %d, %Y"))

    keywords_text.delete("1.0", "end")
    keywords_text.insert("1.0", str(article.keywords))

    summary_text.delete("1.0", "end")
    summary_text.insert("1.0", article.summary)

    analysis = TextBlob(article.text)

    sentiment_text.delete("1.0", "end")
    sentiment_text.insert("1.0", f'Polarity: {analysis.polarity} Sentiment: {"Positive" if analysis.polarity > 0 else "Negative"}')
    

    # Disable text widgets
    keywords_text.config(state="disabled")
    title_text.config(state="disabled")
    author_text.config(state="disabled")
    published_text.config(state="disabled")
    summary_text.config(state="disabled")
    sentiment_text.config(state="disabled")

root = tk.Tk()
root.title("Article Summarizer")
root.geometry("1280x720")

# Article Title
title_label = tk.Label(root, text="Article Title")
title_label.pack()
title_text = tk.Text(root, height=1, width=128)
title_text.config(state="disabled", bg="light grey")
title_text.pack()

# Article Author
author_label = tk.Label(root, text="Article Author")
author_label.pack()
author_text = tk.Text(root, height=1, width=128)
author_text.config(state="disabled", bg="light grey")
author_text.pack()

# Article Published Date
published_label = tk.Label(root, text="Article Published Date")
published_label.pack()
published_text = tk.Text(root, height=1, width=128)
published_text.config(state="disabled", bg="light grey")
published_text.pack()

#keywords
keywords_label = tk.Label(root, text="Keywords")
keywords_label.pack()
keywords_text = tk.Text(root, height=3, width=128)
keywords_text.config(state="disabled", bg="light grey")
keywords_text.pack()

# Article Summary
summary_label = tk.Label(root, text="Article Summary")
summary_label.pack()
summary_text = tk.Text(root, height=20, width=128)
summary_text.config(state="disabled", bg="light grey")
summary_text.pack()

# Article Sentiment Analysis
sentiment_label = tk.Label(root, text="Article Sentiment Analysis")
sentiment_label.pack()
sentiment_text = tk.Text(root, height=1, width=128)
sentiment_text.config(state="disabled", bg="light grey")
sentiment_text.pack()



# Article URL
url_label = tk.Label(root, text="Article URL")
url_label.pack()
url_text = tk.Text(root, height=1, width=128)
url_text.pack()

# Summarize Button
btn = tk.Button(root, text="Summarize", command=summarize)
btn.pack()

root.mainloop()
