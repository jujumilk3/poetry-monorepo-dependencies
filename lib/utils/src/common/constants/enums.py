from enum import Enum, unique


class StringEnumMixin(str, Enum):
    def __str__(self):
        return str(self.value)


class OrderType(StringEnumMixin):
    ASC = "asc"
    DESC = "desc"
    