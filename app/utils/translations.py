import os
import csv
import re

_current_locale = "en"
_translations = {}


def load_csv_translations(locale):
    """
    Carga el archivo CSV de traducciones para el idioma indicado.
    Se espera que el archivo tenga dos columnas: clave y traducción.
    """
    base_dir = os.path.join(os.path.dirname(__file__), "../i18n")
    file_path = os.path.join(base_dir, f"{locale}.csv")
    translations = {}
    try:
        with open(file_path, encoding="utf-8") as f:
            reader = csv.reader(f)
            for row in reader:
                if not row or row[0].startswith("#"):
                    continue
                if len(row) >= 2:
                    key = row[0].strip()
                    value = row[1].strip()
                    translations[key] = value
    except FileNotFoundError:
        translations = {}
    return translations


def set_locale(locale):
    """
    Establece el locale actual y carga las traducciones correspondientes.

    :param locale: Código del idioma, e.g., "en" o "es".
    """
    global _current_locale, _translations
    if locale not in ["en", "es"]:
        locale = "en"
    _current_locale = locale
    _translations = load_csv_translations(locale)


def translate(key):
    """
    Traduce una clave usando las traducciones cargadas.

    :param key: La clave a traducir.
    :return: La traducción correspondiente o la propia clave si no se encuentra.
    """
    return _translations.get(key, key)


def translate_template(template, locale=None):
    """
    Recibe una plantilla (string) y reemplaza las claves de traducción que estén
    marcadas en el formato {clave} por su valor traducido.

    :param template: La cadena de la plantilla a traducir.
    :param locale: (Opcional) Código del idioma. Si se proporciona, se carga ese locale.
    :return: La plantilla con las claves traducidas.
    """
    if locale:
        set_locale(locale)
    pattern = re.compile(r"\{(\w+)\}")

    def repl(match):
        key = match.group(1)
        return translate(key)

    return pattern.sub(repl, template)


set_locale("en")
