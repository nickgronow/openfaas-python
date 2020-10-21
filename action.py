import sentry


def input(body: dict, key: str) -> str:
    """
    Retrieve a value from the body, returning None if key does not exist.
    """
    return body.get("input", {}).get(key)


def hasura(body: dict, key: str) -> str:
    """
    Retrieves a value from the hasura session variables.
    Returns None if key does not exist.
    """
    key = f"x-hasura-{key}"
    return body.get("session_variables", {}).get(key)


def configure_sentry(body: dict, **tags) -> None:
    """
    Configure sentry, setting the action name
    """
    tags["app.action"] = body.get("action", {}).get("name")
    sentry.configure(body, **tags)


def error(message: str, code: int = 400) -> dict:
    """
    Generate an error response dict
    """
    return {
        "body": {"message": message},
        "headers": {"content-type": "application/json"},
        "code": code,
    }
