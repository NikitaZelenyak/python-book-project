import json
from pathlib import Path


def load_from_file(file_path):
    """
    Loads data from JSON file
    Завантажує дані з JSON файлу
    Args:
        file_path (str): Path to file / Шлях до файлу
    Returns:
        dict or None: Loaded data / Завантажені дані
    """
    try:
        with open(file_path, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return None


def save_to_file(file_path, data):
    """
    Saves data to JSON file
    Зберігає дані у JSON файл
    Args:
        file_path (str): Path to file / Шлях до файлу
        data: Data to save / Дані для збереження
    """
    Path(file_path).parent.mkdir(exist_ok=True)
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)
