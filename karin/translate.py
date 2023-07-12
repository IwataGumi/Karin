from pyi18n import PyI18n
from pyi18n.loaders import PyI18nYamlLoader


from karin.const import LOCALS_FILE_PATH, SUPPORTED_LANGUAGES

# i18n support
loader: PyI18nYamlLoader = PyI18nYamlLoader(LOCALS_FILE_PATH, namespaced=True)
i18n = PyI18n(tuple(SUPPORTED_LANGUAGES), loader=loader)
_t: callable = i18n.gettext
# TODO: Create Translator