import pprint

from pyi18n import PyI18n
from typing import Optional
from pyi18n.loaders import PyI18nYamlLoader
from discord.app_commands import Translator, Command
from discord.app_commands.translator import TranslationContextTypes, locale_str, TranslationContextLocation
from discord.enums import Locale


from karin.const import LOCALS_FILE_PATH, SUPPORTED_LANGUAGES

# i18n support
loader: PyI18nYamlLoader = PyI18nYamlLoader(LOCALS_FILE_PATH, namespaced=True)
i18n = PyI18n(tuple(SUPPORTED_LANGUAGES), loader=loader)
_: callable = i18n.gettext

class MyTranslator(Translator):
    async def translate(
            self,
            string: locale_str,
            locale: Locale,
            context: TranslationContextTypes
    ) -> str:
        message = str(string)
        print("-" * 100)
        pprint.pprint(
            {
                string,
                locale.value,
                context.location,
                context.data,
            }
        )
        if locale.value in SUPPORTED_LANGUAGES and TranslationContextLocation.command_description == context.location:
            print(_(locale.value, message))
            return _(locale.value, message)
        return message
