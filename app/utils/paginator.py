import math
from typing import Tuple

class Paginator:
    def __init__(self, total_items: int, page: int = 1, per_page: int = 5):
        self.total_items = max(0, total_items)
        self.per_page = max(1, per_page)
        self.total_pages = max(1, math.ceil(self.total_items / self.per_page))
        self.page = max(1, min(page, self.total_pages))

    @property
    def offset(self) -> int:
        return (self.page - 1) * self.per_page

    @property
    def has_prev(self) -> bool:
        return self.page > 1

    @property
    def has_next(self) -> bool:
        return self.page < self.total_pages

    @property
    def prev_page(self) -> int:
        return self.page - 1 if self.has_prev else 1

    @property
    def next_page(self) -> int:
        return self.page + 1 if self.has_next else self.total_pages
