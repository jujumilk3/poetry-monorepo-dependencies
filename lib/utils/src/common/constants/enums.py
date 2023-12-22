from enum import Enum


class StringEnumMixin(str, Enum):
    def __str__(self):
        return str(self.value)


class OrderType(StringEnumMixin):
    ASC = "asc"
    DESC = "desc"
