from src.constants import *


def input_error(func):
    """
    Декоратор для обробки помилок введення користувача.

    Args:
        func (callable): Функція, що обробляє команди користувача

    Returns:
        callable: Функція-обгортка, що обробляє помилки

    Raises:
        ValueError: Якщо введені неповні або неправильні дані
        KeyError: Якщо контакт не знайдено у словнику контактів
        IndexError: Якщо не вказано ім'я контакту при виконанні команди
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
