#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""
import csv
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
        """Dataset indexed by sorting position, starting at 0.

        IMPORTANT: per spec, only index the first 1000 rows.
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: truncated_dataset[i] for i in range(len(truncated_dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Return a deletion-resilient page starting at `index`.

        Response keys:
          - index: start index requested (after defaulting None->0)
          - next_index: first index after the last returned item
          - page_size: number of items actually returned
          - data: list of rows
        """
        # Default behavior: if index is None, start at 0
        if index is None:
            index = 0

        assert isinstance(index, int) and index >= 0
        assert isinstance(page_size, int) and page_size > 0

        indexed = self.indexed_dataset()
        # Validate index within possible range of current indexed dataset
        max_index = max(indexed.keys()) if indexed else -1
        assert index <= max_index

        data: List[List] = []
        cursor = index

        # Collect up to page_size existing rows, skipping deleted indices
        while len(data) < page_size and cursor <= max_index:
            if cursor in indexed:
                data.append(indexed[cursor])
            cursor += 1

        return {
            "index": index,
            "data": data,
            "page_size": len(data),
            "next_index": cursor,
        }
