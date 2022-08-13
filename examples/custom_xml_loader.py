from pyi18n.loaders import PyI18nBaseLoader
from pyi18n import PyI18n
from xmltodict import parse

from os.path import exists

class PyI18nXMLLoader(PyI18nBaseLoader):

    _type: str = "xml"
    
    def load(self, locales: tuple) -> dict:
        """ Load translations from xml files

        Args:
            locales (tuple): list of available locales
        Returns:
            dict: loaded translations

        """
        
        loaded: dict = {}
        for locale in locales:
            
            file_path: str = f"{self.load_path}{locale}.xml"
            if not exists(file_path):
                # raise FileNotFoundError(f"locale file not found: {file_path}")
                continue
            
            with open(file_path, "r") as f:
                loaded[locale] = parse(f.read())[locale]
            
        return loaded


if __name__ == "__main__":
    loader: PyI18nXMLLoader = PyI18nXMLLoader("locales/")
    i18n: PyI18n = PyI18n(('en', 'pl'), loader=loader)
    print(i18n.gettext("en", "hello.world"))
    print(i18n.gettext("pl", "hello.world"))
    # >> Hello world!
    # >> Witaj świecie!
