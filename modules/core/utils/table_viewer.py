from colorama import Fore, Style, Back


class TableViewer:
    """
    Class for displaying data in formatted table view with colored layout
    Клас для відображення даних у форматованому табличному вигляді з кольоровим оформленням
    """

    def __init__(self, columns=None):
        """
        Initialize table viewer with column settings
        Ініціалізація переглядача таблиць з налаштуваннями стовпців

        Args:
            columns (list, optional): List of column names in desired order
                                    Список назв стовпців у бажаному порядку
        """
        self.column_widths = {}
        self.columns = columns or []

    def _calculate_column_widths(self, data, headers):
        """
        Calculate the optimal width for each column based on content
        Розрахунок оптимальної ширини для кожного стовпця на основі вмісту
        """
        self.column_widths = {header: len(str(header)) for header in headers}

        for row in data:
            for header in headers:
                value = row.get(header, "")
                width = len(str(value)) if value is not None else 0
                self.column_widths[header] = max(self.column_widths[header], width)

    def _create_separator(self, headers):
        """
        Create a separator line for the table with blue color
        Створення роздільної лінії для таблиці синього кольору
        """
        parts = []
        for header in headers:
            parts.append("-" * (self.column_widths[header] + 2))
        return f"{Fore.BLUE}+{'+'.join(parts)}+"

    def _format_row(self, row_dict, headers, is_header=False, row_number=None):
        """
        Format a single row of data with colors
        Форматування одного рядка даних з кольорами

        Args:
            row_dict (dict): Row data dictionary / Словник даних рядка
            headers (list): List of headers / Список заголовків
            is_header (bool): Is this a header row / Чи це рядок заголовку
            row_number (int): Row number for alternating colors / Номер рядка для чергування кольорів
        """
        row_parts = []

        # Set colors based on row type / Встановлюємо кольори в залежності від типу рядка
        if is_header:
            # Dark green text on white background for / Темнозелений текст на білому фоні для заголовків
            text_color = Fore.GREEN + Style.BRIGHT
            bg_color = Back.WHITE
        else:
            # Black text with alternating background colors for data / Чорний текст з кольором фону що чергується для даних
            text_color = Fore.BLACK
            bg_color = Back.LIGHTYELLOW_EX if row_number % 2 == 0 else Back.LIGHTBLUE_EX

        for header in headers:
            value = row_dict.get(header, "")
            width = self.column_widths[header]
            row_parts.append(f" {str(value):<{width}} ")

        return f"{Fore.BLUE}|{bg_color}{text_color}{'|'.join(row_parts)}{Style.RESET_ALL}{Fore.BLUE}|"

    def display_table(self, data, title=None):
        """
        Display data in a formatted table with colors
        Відображення даних у форматованій таблиці з кольорами

        Args:
            data (list): List of dictionaries containing the data
                        Список словників з даними
            title (str, optional): Table title
                                 Заголовок таблиці
        """
        if not data:
            print(f"{Fore.YELLOW}No data to display")
            return

        # Get headers in specified order /  Отримуємо заголовки у вказаному порядку
        headers = self.columns if self.columns else sorted(data[0].keys())

        # Calculate widths / Розрахунок ширини
        self._calculate_column_widths(data, headers)

        # Create separator / Створення роздільника
        separator = self._create_separator(headers)

        # Display title / Відображення заголовку
        if title:
            print(f"\n{Fore.CYAN}{title}")
        print(f"{separator}")

        # Display headers with dark green text on white background / Відображення заголовків темнозеленим текстом на білому фоні
        header_row = {header: header for header in headers}
        print(f"{self._format_row(header_row, headers, is_header=True)}")
        print(f"{separator}")

        # Display data rows with alternating background colors / Відображення рядків даних з чергуванням кольорів фону
        for i, row in enumerate(data):
            print(f"{self._format_row(row, headers, is_header=False, row_number=i)}")

        print(f"{separator}\n")
        print(Style.RESET_ALL, end="")
