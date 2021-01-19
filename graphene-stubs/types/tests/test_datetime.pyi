from ..datetime import Date as Date, DateTime as DateTime, Time as Time
from ..objecttype import ObjectType as ObjectType
from ..schema import Schema as Schema
from typing import Any, Optional

class Query(ObjectType):
    datetime: Any = ...
    date: Any = ...
    time: Any = ...
    def resolve_datetime(self, info: Any, _in: Optional[Any] = ...) -> Any: ...
    def resolve_date(self, info: Any, _in: Optional[Any] = ...) -> Any: ...
    def resolve_time(self, info: Any, _at: Optional[Any] = ...) -> Any: ...

schema: Any

def sample_datetime() -> Any: ...
def sample_time(sample_datetime: Any) -> Any: ...
def sample_date(sample_datetime: Any) -> Any: ...
def test_datetime_query(sample_datetime: Any) -> None: ...
def test_date_query(sample_date: Any) -> None: ...
def test_time_query(sample_time: Any) -> None: ...
def test_bad_datetime_query() -> None: ...
def test_bad_date_query() -> None: ...
def test_bad_time_query() -> None: ...
def test_datetime_query_variable(sample_datetime: Any) -> None: ...
def test_date_query_variable(sample_date: Any) -> None: ...
def test_time_query_variable(sample_time: Any) -> None: ...
def test_bad_variables(
    sample_date: Any, sample_datetime: Any, sample_time: Any
) -> None: ...
