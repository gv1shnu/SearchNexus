import os
from tinydb import TinyDB, Query
from src.scrape import Scrape


class DBHandler:
    def __init__(self):
        """
        Initializes the DBHandler object.

        Checks if the 'db' directory exists, and if not, creates it.
        Creates or opens the TinyDB instance for the search results database.
        """
        if not os.path.exists('db'):
            os.mkdir('db')
        self.db = TinyDB('db/search_results_db.json')

    def insert(self, req):
        """
        Inserts a new entry into the search results database.

        Takes a request as input and performs web scraping to obtain the search results.
        Inserts the query and results into the database.
        Returns the results.
        """
        if req:
            scrape = Scrape(req)
            results = scrape.get_results()
            self.db.insert({'query': req, 'results': results})
            return results
        print("\033[95m Null request")

    def query(self, req):
        """
        Queries the search results database for a specific request.

        Searches the database for an entry matching the given request.
        If a match is found, returns the results.
        If no match is found, returns None.
        """
        query_result = self.db.search(Query().query == req)
        if query_result:
            print("Entry exists")
            return query_result[0]['results']
        return None
