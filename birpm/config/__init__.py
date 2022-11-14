import hashlib
import typing

import pydantic


class Config(pydantic.BaseSettings):
    """
    Base configuration for birpm.
    """

    hash_algorithms: typing.List[str] = ["sha256", "sha224"]

    @pydantic.validator("hash_algorithms")
    def validate_settings_hash_algorithms(
        cls, value: typing.List[str]
    ) -> typing.List[str]:
        if not value:
            raise ValueError("hash_algorithms must not be empty.")
        for hash_algorithm in value:
            if hash_algorithm not in hashlib.algorithms_guaranteed:
                raise ValueError(f"{hash_algorithm} not avalible on this platform.")
        return value
