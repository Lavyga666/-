import doctest
class OxygenConcentration:
    """
    Абстрактный класс, описывающий объект концентрации кислорода в комнате.
    """
    def __init__(self, oxygen_level: float, carbon_dioxide_level: float):
        """
        Создание и подготовка к работе объекта концентрации кислорода в комнате.

        :param oxygen_level: Количество кислорода в воздухе.
        :param carbon_dioxide_level: Количество углекислого газа в воздухе.

        Пример:
        >>> air_quality = OxygenConcentration(21.5, 0.03)
        """
        if not isinstance(oxygen_level, (int, float)) or oxygen_level < 0:
            raise ValueError("Количество кислорода должно быть положительным числом")
        self.oxygen_level: float = oxygen_level

        if not isinstance(carbon_dioxide_level, (int, float)) or carbon_dioxide_level < 0:
            raise ValueError("Количество углекислого газа должно быть положительным числом")
        self.carbon_dioxide_level: float = carbon_dioxide_level
    def add_plant(self, oxygen_production_rate: float) -> None:
        """
        Метод описывающий добавление нового растения для повышения концентрации кислорода.

        :param oxygen_production_rate: Скорость производства кислорода новым растением.

        Пример:
        >>> air_quality.add_plant(0.5)
        """
        ...
    def add_person(self, carbon_dioxide_production_rate: float) -> None:
        """
        Метод описывающий добавление нового человека для повышения концентрации углекислого газа.

        :param carbon_dioxide_production_rate: Скорость производства углекислого газа новым человеком.

        Пример:
        >>> air_quality.add_person(0.02)
        """
        ...
if __name__ == "__main__":
    doctest.testmod()

