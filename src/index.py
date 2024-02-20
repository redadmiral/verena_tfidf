from typing import List, Dict
import json
import math
import numpy as np
PATH = "./data/cleaned.jsonl"


class Article:
    """
    This class represents a single article. It holds basic information like title, text and the url.
    """
    def __init__(self, title: str, text: str, source: str):
        self.title: str = title
        self.text: str = text
        self.source: str = source


    def termfrequency(self, term: str, normalize: bool = True) -> float | int:
        """
        Returns the frequency of a given term in the document.
        :param term: The term to get the frequency
        :param normalize: If true, normalize the frequency in a range between 0 and 1.
        :return: the frequency of the term as float value if normalize = True, else an integer
        """
        # tf(t, d) = count of t in d / number of words in d
        if normalize:
            term_frequency = self.text.count(term) / len(self.text)
        else:
            term_frequency = self.text.count(term)

        return term_frequency


class Index:
    """
    This class represents a very basic implementation of an index.
    In this first version the index consists only of a list of articles.
    """
    def __init__(self):
        self.articles: List[Article] = []

    def add(self, article: Article) -> None: #ohne return-statement, weil nichts returned wird?
        """
        Add an article to the list.
        :param article:
        :return:
        """
        return self.articles.append(article)

    def idf(self, term, normalize: bool = True) -> float:
        """
        Returns the inverse document frequency of a given term.
        :param term: The term to get the inverse document frequency
        :param normalize: If true, the inverse document is normalized in a range between 0 and 1
        :return:
        """
        df = 0
        for article in self.articles:
            if term in article:
                df += 1
        if normalize:
            idf = (np.log(len(self.articles)/(df+1))) / len(self.articles)
        else:
            idf = np.log(len(self.articles)/(df+1))

        return idf


    def search(self, query: str, limit: int) -> List[Dict]:
        """
        Create the tf/idf score for every article in the index and return the articles sorted by highest tf/idf.
        :param query: The search query.
        :param limit: How many articles shall be returned
        :return: A list of dictionaries consisting of the articles and the search score.
        """
        #tf-idf(t, D) = (tf(t, D) x idf(t))
        tfidf_list = []
        for article in self.articles:
            tfidf = Article.termfrequency(query) * self.idf(query)
            tfidf_dict = {article.title: tfidf}
            tfidf_list.append(tfidf_dict)

        return tfidf_list.sort(key=lambda x: x['tfidf'])[:limit]

