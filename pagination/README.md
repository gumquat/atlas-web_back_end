# 0 - Simple helper function 
### Write a function named index_range that takes two integer arguments page and page_size.
The function should return a tuple of size two containing a start index and an end index corresponding to the range of indexes to return in a list for those particular pagination parameters.
Page numbers are 1-indexed, i.e. the first page is page 1.
* This function calculates the start index by subtracting 1 from the page number (since page numbers are 1-indexed) and then multiplying by the page_size. 
* The end index is simply the page number multiplied by the page_size. The function returns a tuple containing the start and end indexes.

# 1 - Simple Pagination
### Copy index_range from the previous task and the following class into your code
```
import csv
import math
from typing import List


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
            pass
```