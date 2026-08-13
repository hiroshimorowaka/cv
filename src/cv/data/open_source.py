from cv.models import OpenSourceProject

# Author-time fields only. Stars / language / pushed date come from
# `cv refresh-metrics` (cached at data/_oss_metrics.json).
#
# Definition order below is irrelevant; the renderer sorts by `order` ascending.
# Lower `order` = appears first. Default is 100 ("no preference").
# Use small numbers (10, 20, 30, ...) to promote, larger to demote.

OPEN_SOURCE_PROJECTS = (
    OpenSourceProject(
        name="esp32-snake-game",
        repo="hiroshimorowaka/esp32-snake-game",
        tagline="Snake Game para ESP32 escrito em Rust bare-metal (no_std).",
        description="""
    Implementação do clássico Snake Game rodando diretamente no microcontrolador ESP32-WROOM-32,
    desenvolvida em Rust no modo no_std. Utiliza display OLED
    SSD1306 via I2C e quatro botões físicos para controle. Projeto de estudo em
    sistemas embarcados com Rust, usando o ecossistema esp-rs (esp-hal, espflash,
    espup).
    """,
        keywords=("Rust", "ESP32", "Embarcado", "Embedded", "no_std", "esp-rs"),
    ),
    OpenSourceProject(
        name="esp32-pong-game",
        repo="hiroshimorowaka/esp32-pong-game",
        tagline="Pong Game para ESP32 escrito em Rust bare-metal (no_std).",
        description="""
    Implementação do clássico Pong Game rodando diretamente no microcontrolador ESP32-WROOM-32,
        desenvolvida em Rust no modo no_std. Utiliza display OLED
        SSD1306 via I2C e quatro botões físicos para controle. Projeto de estudo em
        sistemas embarcados com Rust, usando o ecossistema esp-rs (esp-hal, espflash,
        espup)
    """,
        keywords=("Rust", "ESP32", "Embarcado", "Embedded", "no_std", "esp-rs"),
    ),
)
