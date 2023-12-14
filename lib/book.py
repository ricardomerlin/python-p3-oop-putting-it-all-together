#!/usr/bin/env python3
from shoe import Shoe
class Book:
    def __init__(self, title, page_count):
        self.title = title
        self.page_count = page_count
    
    @property
    def page_count(self):
        return self._page_count
    
    @page_count.setter
    def page_count(self, page_count):
        if not isinstance(page_count, int):
            print('page_count must be an integer')
        else:
            self._page_count = page_count
            self.turn_page()

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")