import random

# База стилей и шаблонов
STYLES = {
    "агрессивный": [
        "Rage{}",
        "Killer{}",
        "Bloody{}",
        "Mad{}",
        "Fury{}",
        "Toxic{}",
        "Savage{}",
        "Brutal{}",
        "Venom{}",
        "Reaper{}"
    ],

    "аниме": [
        "Akira{}",
        "Kira{}",
        "Sakura{}",
        "Yami{}",
        "Hikari{}",
        "Rin{}",
        "Zero{}",
        "Shiro{}",
        "Kuro{}",
        "Aoi{}"
    ],

    "pubg": [
        "PUBG{}",
        "Sniper{}",
        "Headshot{}",
        "Zone{}",
        "Clutch{}",
        "Spray{}",
        "Winner{}",
        "Chicken{}",
        "Loot{}",
        "Drop{}"
    ],

    "минимализм": [
        "{}X",
        "X{}",
        "{}_",
        "_{}",
        "{}01",
        "{}99",
        "{}VX",
        "VX{}",
        "{}PRO",
        "PRO{}"
    ],

    "арабский": [
        "الملك{}",
        "صقر{}",
        "نمر{}",
        "قائد{}",
        "أسد{}",
        "ظل{}",
        "نسر{}",
        "عقاب{}",
        "سيف{}",
        "رعد{}"
    ],

    "киберспорт": [
        "Pro{}",
        "Ace{}",
        "Clutch{}",
        "Sharp{}",
        "Neo{}",
        "Flash{}",
        "Storm{}",
        "Pixel{}",
        "Cyber{}",
        "Volt{}"
    ]
}


# Символы для украшения
DECOR = [
    "", "_", ".", "X", "V", "Z", "Q", "7", "9", "RX", "FX", "GG", "OP"
]


def generate_nicknames(style: str):
    """
    Генерирует 10 никнеймов в указанном стиле.
    """

    style = style.lower().strip()

    # Если стиль есть в базе — используем его
    if style in STYLES:
        templates = STYLES[style]
    else:
        # Если стиль неизвестен — создаём универсальные ники
        templates = [
            "{}X",
            "X{}",
            "{}Pro",
            "{}King",
            "{}God",
            "{}Zone",
            "{}Fire",
            "{}Storm",
            "{}Wolf",
            "{}Shadow"
        ]

    nicknames = []

    for _ in range(10):
        template = random.choice(templates)
        decor = random.choice(DECOR)
        word = random.choice(["", "Pro", "King", "Wolf", "Zero", "Nova", "RX", "FX"])

        # Генерация ника
        nickname = template.format(word + decor)

        # Убираем двойные пробелы
        nickname = nickname.replace("  ", " ").strip()

        nicknames.append(nickname)

    return nicknames

