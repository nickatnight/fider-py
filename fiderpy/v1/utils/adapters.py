from fiderpy.v1.utils.domain import FiderError
from fiderpy.v1.utils.interfaces import IAdapter
from fiderpy.v1.utils.types import FiderAPIResponseType


class FiderErrorAdapter(IAdapter[FiderAPIResponseType, list[FiderError]]):
    @staticmethod
    def to_domain(obj: FiderAPIResponseType) -> list[FiderError]:
        errors = []

        for error in obj.get("errors", []):
            data = {"message": error["message"]}

            if "field" in error:
                data["field"] = error["field"]

            errors.append(FiderError(**data))

        return errors
