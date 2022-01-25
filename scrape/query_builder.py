from typing import Union

QueryParameter = Union[list, int, str]


class QueryBuilder:
    def __init__(self, base_url: str):
        self.base_url = base_url if base_url.endswith("/") else base_url + "/"
        self._queries = dict()

    def upsert_query(self, query: str, parameter: QueryParameter) -> None:
        if not isinstance(query, str):
            raise TypeError("Query parameter must be a string")
        if isinstance(parameter, list):
            parameter = ",".join([str(o) for o in parameter])
        self._queries[query] = parameter
        return self

    def build(self) -> str:
        query_string = ""
        for i, pair in enumerate(self._queries.items()):
            name, value = pair
            query_string += f"{name}={value}"

            if i < len(self._queries) - 1:
                query_string += "&"

        return self.base_url + "?" + query_string
