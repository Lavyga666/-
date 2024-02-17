if __name__ == "__main__":
    class Tutor:
        """ Базовый класс для репетитора.

        Атрибуты:
            name (str): Имя репетитора.
            subject (str): Предмет, который репетитор ведет.
            hourly_rate (float): Почасовая ставка репетитора.

        Методы:
            __init__(self, name: str, subject: str, hourly_rate: float) -> None:
                Конструктор класса Tutor.

            __str__(self) -> str:
                Возвращает строковое представление репетитора.

            __repr__(self) -> str:
                Возвращает представление репетитора для использования в REPL.
        """

        def __init__(self, name: str, subject: str, hourly_rate: float) -> None:
            """
            Класс Tutor.

            Аргументы:
                name (str): Имя репетитора.
                subject (str): Предмет, который репетитор ведет.
                hourly_rate (float): Почасовая ставка репетитора.
            """
            self.name = name
            self.subject = subject
            self.hourly_rate = hourly_rate

        def __str__(self) -> str:
            """
            Возвращает строковое представление репетитора.Возвращает str: Строковое представление репетитора.
            """
            return f"{self.name} - {self.subject} - ${self.hourly_rate}/hour"


    class OnlineTutor(Tutor):
        """
        Дочерний класс - онлайн-репетитор.

        Атрибуты:
            online_platform (str): Платформа, на которой ведет занятия репетитор.

        Методы:
            __init__(self, name: str, subject: str, hourly_rate: float, online_platform: str) -> None:
                Конструктор класса OnlineTutor.

            __str__(self) -> str:
                Возвращает строковое представление онлайн-репетитора.

            introduce(self) -> str:
                Представляет репетитора и описывает его специфику работы.

            _setup_online_session(self) -> str:
                Внутренний метод для настройки онлайн-сессии.

            teach_online(self) -> str:
                Перегруженный метод для проведения онлайн-занятия.
        """

        def __init__(self, name: str, subject: str, hourly_rate: float, online_platform: str) -> None:
            """
            Конструктор класса OnlineTutor.

            Аргументы:
                name (str): Имя репетитора.
                subject (str): Предмет, который репетитор ведет.
                hourly_rate (float): Почасовая ставка репетитора.
                online_platform (str): Платформа, на которой ведет занятия репетитор.
            """
            super().__init__(name, subject, hourly_rate)
            self.online_platform = online_platform

        def __str__(self) -> str:
            """
            Возвращает строковое представление онлайн-репетитора.

            """
            return f"{super().__str__()} - Online platform: {self.online_platform}"

        def introduce(self) -> str:
            """
            Представляет репетитора и описывает его условия  работы.

            Возвращает str: Информация о репетиторе и его условиях  работы.
            """
            # Реализация представления репетитора
            pass

        def _setup_online_session(self) -> str:
            """
            Внутренний метод для настройки онлайн-сессии.

            Возвращает str: Сообщение о выполненной настройке сессии.
            """
            # Реализация настройки онлайн-сессии
            pass

        def teach_online(self) -> str:
            """
            Перегруженный метод для проведения онлайн-занятия.

            Возвращает str: Сообщение о проведенном онлайн-занятии.
            """
    pass
