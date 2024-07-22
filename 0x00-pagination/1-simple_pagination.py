#!/usr/bin/env python3
""" Python Module for paginating a database of popular baby names. """

import csv
from typing import Tuple, List


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Calculate the start and end index for a given page and page size.

    Args:
        page (int): The page number (1-based index).
        page_size (int): The number of items per page.

    Returns:
        Tuple[int, int]: A tuple containing the start and end indices.
    """
    start = (page - 1) * page_size
    end = page * page_size

    return start, end


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Load and cache the dataset from the CSV file if not already done.

        Returns:
            List[List]: The loaded dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            # Cache the dataset, skipping the header row
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Get a page of data from the dataset.

        Args:
            page (int): The page number (1-based index). Defaults to 1.
            page_size (int): The number of items per page. Defaults to 10.

        Returns:
            List[List]: A list of rows representing the page of data.
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        self.dataset()

        if self.__dataset is None:
            return []

        # Calculate the start and end indices for the given page
        idx_range = index_range(page, page_size)
        # Slice the dataset to get the data for the current page
        data = self.__dataset[idx_range[0]:idx_range[1]]
        return data
