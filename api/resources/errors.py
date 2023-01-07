class BadRequestError(Exception):
    pass


class UnauthorizedError(Exception):
    pass


class InvalidLicenceError(Exception):
    pass


class ExpiredLicenceError(Exception):
    pass


class PermissionError(Exception):
    pass


class AlreadyExistsError(Exception):
    pass


class DoesNotExistError(Exception):
    pass


class ReachLimitError(Exception):
    pass


class InvalidTokenError(Exception):
    pass


class TokenRequiredError(Exception):
    pass


class InternalServerError(Exception):
    pass


errors = {
    "BadRequestError": {
        "message": "The request cannot be processed",
        "status": 400,
    },
    "UnauthorizedError": {
        "message": "Access denied",
        "status": 401,
    },
    "InvalidLicenceError": {
        "message": "Invalid licence",
        "status": 401,
    },
    "ExpiredLicenceError": {
        "message": "Expired licence",
        "status": 402,
    },
    "PermissionError": {
        "message": "Permission denied",
        "status": 403,
    },
    "AlreadyExistsError": {
        "message": "Already exists",
        "status": 403,
    },
    "DoesNotExistError": {
        "message": "Not found",
        "status": 404,
    },
    "ReachLimitError": {
        "message": "Reached the limit",
        "status": 429,
    },
    "InvalidTokenError": {
        "message": "Revoked, expired or invalid token",
        "status": 498,
    },
    "TokenRequiredError": {
        "message": "Token is required",
        "status": 499,
    },
    "InternalServerError": {
        "message": "Something went wrong",
        "status": 500,
    },
}
