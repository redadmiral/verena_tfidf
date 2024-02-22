from src.index import Article

article = Article(text="Das ist ein ein Test.", title="Test-Titel", source="https://example.com")

def test_article():

    assert isinstance(article, Article)
    assert article.text == "Das ist ein Test."
    assert article.title == "Test-Titel"
    assert article.source == "https://example.com"

def test_termfrequency():
    terms = ["Test.", "ein"]
    results = [1, 2]

    for i, t in enumerate(terms):
        assert article.termfrequency(t, normalize=False) == results[i]
        assert article.termfrequency(t) == results[i]/len(article.text)

