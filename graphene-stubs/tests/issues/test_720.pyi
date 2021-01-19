import graphene
from typing import Any, Optional

class MyInputClass(graphene.InputObjectType):
    @classmethod
    def __init_subclass_with_meta__(
        cls,
        container: Optional[Any] = ...,
        _meta: Optional[Any] = ...,
        fields: Optional[Any] = ...,
        **options: Any
    ) -> None: ...

class MyInput(MyInputClass):
    class Meta:
        fields: Any = ...

class Query(graphene.ObjectType):
    myField: Any = ...
    def resolve_myField(parent: Any, info: Any, input: Any) -> Any: ...

def test_issue() -> None: ...
