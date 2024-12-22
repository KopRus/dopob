# TODO Написать 3 класса с документацией и аннотацией типов
from abc import ABC, abstractmethod

class Table(ABC):
    """
    Класс, описывающий стол.
    """
    def __init__(self, material: str, height: float):
        self.material = material
        self.height = height

    @abstractmethod
    def get_material(self) -> str:
        """
        Возвращает материал стола.
        >>> table = WoodenTable('wood', 1.5)
        >>> table.get_material()
        'wood'
        """
        pass

    @abstractmethod
    def get_height(self) -> float:
        """
        Возвращает высоту стола.
        >>> table = WoodenTable('wood', 1.5)
        >>> table.get_height()
        1.5
        """
        pass

class WoodenTable(Table):
    def get_material(self) -> str:
        return self.material

    def get_height(self) -> float:
        return self.height

class Tree(ABC):
    """
    Класс, описывающий дерево.
    """
    def __init__(self, species: str, height: float):
        self.species = species
        self.height = height

    @abstractmethod
    def get_species(self) -> str:
        """
        Возвращает вид дерева.
        >>> tree = OakTree('oak', 20)
        >>> tree.get_species()
        'oak'
        """
        pass

    @abstractmethod
    def get_height(self) -> float:
        """
        Возвращает высоту дерева.
        >>> tree = OakTree('oak', 20)
        >>> tree.get_height()
        20
        """
        pass

class OakTree(Tree):
    def get_species(self) -> str:
        return self.species

    def get_height(self) -> float:
        return self.height

class Facebook(ABC):
    """
    Класс, описывающий Facebook.
    """
    def __init__(self, users: int, posts: int):
        self.users = users
        self.posts = posts

    @abstractmethod
    def get_users(self) -> int:
        """
        Возвращает количество пользователей Facebook.
        >>> facebook = FacebookInstance(2000000000, 1000000000)
        >>> facebook.get_users()
        2000000000
        """
        pass

    @abstractmethod
    def get_posts(self) -> int:
        """
        Возвращает количество постов в Facebook.
        >>> facebook = FacebookInstance(2000000000, 1000000000)
        >>> facebook.get_posts()
        1000000000
        """
        pass

class FacebookInstance(Facebook):
    def get_users(self) -> int:
        return self.users

    def get_posts(self) -> int:
        return self.posts


if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    import doctest
    doctest.testmod()
