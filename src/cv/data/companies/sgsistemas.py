from datetime import date

from cv.models import Company, Position

SG_SISTEMAS = Company(
    name="SG Sistemas",
    one_liner="Empresa especializada em soluções para automação comercial e meios de pagamento.",
    positions=(
        Position(
            title="Desenvolvedor Android e Backend",
            start=date(2024, 12, 1),
            end=date(2025, 12, 1),
            location="Brasil",
            remote=False,
            description="""
Atuei em uma plataforma completa de pagamentos, desenvolvendo desde aplicações Android e bibliotecas de integração até APIs backend e ferramentas administrativas.

- Desenvolvi bibliotecas Android para integração com Smart POS e PinPads (USB e Bluetooth), criando uma arquitetura reutilizável com suporte aos provedores SiTef, Scope e Rede.

- Desenvolvi a aplicação principal de transações utilizando Kotlin e Jetpack Compose, responsável pelo processamento de pagamentos, integração com bibliotecas internas e comunicação com sistemas PDV.

- Desenvolvi a arquitetura e a API Java responsável pela comunicação entre ERPs, caixas de supermercado e dispositivos Smart POS, permitindo processamento de transações em tempo real.

- Implementei mecanismos de persistência local, sincronização automática e melhorias de desempenho no backend para garantir maior confiabilidade e eficiência operacional.

- Desenvolvi integrações com dispositivos externos e um dashboard administrativo em Next.js para gerenciamento de clientes, dispositivos e histórico de transações.
""",
            keywords=(
                "Kotlin",
                "Java",
                "Jetpack Compose",
                "Android SDK",
                "TypeScript",
                "Next.js",
                "REST APIs",
                "PostgreSQL",
                "Docker",
                "Git",
                "SQLite",
            ),
        ),
    ),
)
