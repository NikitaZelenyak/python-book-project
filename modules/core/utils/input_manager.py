from modules.core.constants.messages import INVALID_NAME, CANCELED_MESSAGE


def input_with_validation(prompt, validator, error_message, allow_empty=True):
    """
    Helper function for input with validation
    Допоміжна функція для введення з валідацією
    Args:
        prompt (str): Input prompt / Запрошення до введення
        validator (callable): Validation function / Функція валідації
        error_message (str): Error message / Повідомлення про помилку
        allow_empty (bool): Allow empty input / Дозволити пусте введення
    Returns:
        str or None: Validated input or None / Перевірене введення або None
    """
    while True:
        value = input(prompt).strip()
        if not value:
            if allow_empty:
                return None
            print(INVALID_NAME)
            continue
        if validator(value):
            return value
        print(error_message)


def confirm_action(prompt):
    """
    Asks user to confirm action
    Запитує користувача про підтвердження дії
    Args:
        prompt (str): Confirmation prompt / Запит підтвердження
    Returns:
        bool: True if confirmed, False if not
    """
    response = input(prompt).lower().strip()
    return response == "y"


def parse_input(user_input):
    """
    Parses user input into command and arguments
    Розбирає введення користувача на команду та аргументи
    Args:
        user_input (str): Raw user input / Введення користувача
    Returns:
        tuple: Command and its arguments / Команда та її аргументи
    """
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args
