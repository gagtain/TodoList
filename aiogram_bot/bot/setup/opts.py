from dataclasses import dataclass

from aiogram import Bot
from fluentogram import TranslatorRunner

from config.settings import Settings


@dataclass(frozen=True)
class SetupOpts:
    bot: Bot
    settings: Settings
    l10n: TranslatorRunner