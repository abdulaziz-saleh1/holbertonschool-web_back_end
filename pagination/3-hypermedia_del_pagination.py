#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""
import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset (skip header)."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by position, starting at 0."""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {i: dataset[i] for i in range(len(dataset))}
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Return a deletion-resilient page starting at `index`.

        Response keys:
        - index: start index requested
        - next_index: index to request for the next page
        - page_size: number of items actually returned
        - data: list of rows
        """
        assert isinstance(index, int) and index >= 0
        assert isinstance(page_size, int) and page_size > 0

        indexed = self.indexed_dataset()
        max_index = max(indexed.keys()) if indexed else -1
        # index must be within possible range (<= max existing index)
        assert index <= max_index

        data: List[List] = []
        current = index

        # Collect up to page_size existing rows, skipping deleted indices
        while len(data) < page_size and current <= max_index:
            if current in indexed:
                data.append(indexed[current])
            current += 1

        return {
            "index": index,
            "data": data,
            "page_size": len(data),
            "next_index": current,
        }
