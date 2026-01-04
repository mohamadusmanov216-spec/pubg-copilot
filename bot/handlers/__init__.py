from .start import register_start_handlers
from .menu import register_menu_handlers
from .advice import register_advice_handlers
from .weapons import register_weapon_handlers
from .maps import register_map_handlers
from .ai_chat import register_ai_handlers
from .matchmaking import register_matchmaking_handlers
from .nicknames import register_nickname_handlers

__all__ = [
    "register_start_handlers",
    "register_menu_handlers",
    "register_advice_handlers",
    "register_weapon_handlers",
    "register_map_handlers",
    "register_ai_handlers",
    "register_matchmaking_handlers",
    "register_nickname_handlers",
]
