from typing import List, Dict


class Article:
    """
    This class represents a single article. It holds basic information like title, text and the url.
    """
    def __init__(self, title: str, text: str, source: str):
        self.title: str = title
        self.text: str = text
        self.source: str = source

    def termfrequency(self, term: str, normalize: bool = True):
        """
        Returns the frequency of a given term in the document.
        :param term: The term to get the frequency
        :param normalize: If true, normalize the frequency in a range between 0 and 1.
        :return:
        """
        pass

class Index:
    """
    This class represents a very basic implementation of an index.
    In this first version the index consists only of a list of articles.
    """
    def __init__(self):
        self.articles: List[Article] = []

    def add(self, article: Article) -> None:
        """
        Add an article to the list.
        :param article:
        :return:
        """
        pass

    def idf(self, term, normalize: bool = True):
        """
        Returns the inverse document frequency of a given term.
        :param term: The term to get the inverse document frequency
        :param normalize: If true, the inverse document is normalized in a range between 0 and 1
        :return:
        """
        pass

    def search(self, query, limit) -> List[Dict]:
        """
        Create the tf/idf score for every article in the index and return the articles sorted by highest tf/idf.
        :param query: The search query.
        :param limit: How many articles shall be returned
        :return: A list of dictionaries consisting of the articles and the search score.
        """
        pass
