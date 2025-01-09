from modules.core.constants.messages import (
    MISSING_ARGS_MESSAGE,
    CONTACT_NOT_FOUND_MESSAGE,
    MISSING_NAME_MESSAGE,
)


def input_error(func):
    """
    Decorator for handling user input errors
    Декоратор для обробки помилок введення користувача
    Args:
        func (callable): Function that handles user commands
    Returns:
        callable: Wrapper function that handles errors
    """

    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return MISSING_ARGS_MESSAGE
        except KeyError:
            return CONTACT_NOT_FOUND_MESSAGE
        except IndexError:
            return MISSING_NAME_MESSAGE

    return inner
