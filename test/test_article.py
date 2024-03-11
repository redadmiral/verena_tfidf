git from src.index import Article, Index
import pytest
import numpy as np


@pytest.fixture
def article():
    return Article(text="Das ist ein ein Test.", title="Test-Titel", source="https://example.com")


@pytest.fixture
def article_2():
    return Article(title="test two", text="text text two", source="https://exampletwo.com")


index = Index()

def test_article(article):

    assert isinstance(article, Article)
    assert article.text == "Das ist ein ein Test."
    assert article.title == "Test-Titel"
    assert article.source == "https://example.com"


def test_termfrequency(article):
    terms = ["Test.", "ein"]
    results = [1, 2]

    for i, t in enumerate(terms):
        assert article.termfrequency(t, normalize=False) == results[i]
        assert article.termfrequency(t) == results[i]/len(article.text)

def test_index(article):
    assert isinstance(index, Index)
    assert len(index.articles) == 0


def test_add(article, article_2):
    index.add(article)
    index.add(article_2)
    assert len(index.articles) == 2


def test_idf(article, article_2):
    article_3 = Article(title="Test drei", text="ein dritter Test", source="https://examplethree.com")
    article_4 = Article(title="Test vier", text="der vierte Test", source="https:examplefour.com")
    term = "ein"
    index.add(article) #enthät term
    index.add(article_2) #enthält term nicht
    index.add(article_3) #enthält term
    index.add(article_4) #enthält term nicht
    assert len(index.articles) == 4
    assert term in article.text
    assert index.idf("ein", normalize=False) == np.log(4/2)
    assert index.idf("ein") == np.log(4/2)/4



def test_search(article, article_2):
    index.add(article)
    index.add(article_2)
    article_3 = Article(title="Test drei", text="ein dritter Test", source="https://examplethree.com")
    article_4 = Article(title="Test vier", text="der vierte Test", source="https:examplefour.com")
    index.add(article_3)
    index.add(article_4)
    results = index.search("ein", limit=2)
    assert len(results) == 2
    #assert results[0].get("title") == "Test-Titel"
    #assert results[1].get("title") == "test two"
    assert results[0].get("score") == 2/5 * np.log(4/2)/4
