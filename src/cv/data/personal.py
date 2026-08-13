from pydantic import HttpUrl

from cv.models import Personal

PERSONAL = Personal(
    name="Guilherme Cabral",
    title="Desenvolvedor de Software | Android & Backend | Kotlin · Java · TypeScript",
    location="Brasil",
    email="guilhermecabral1204@gmail.com",
    github=HttpUrl("https://github.com/hiroshimorowaka"),
    linkedin=HttpUrl("https://www.linkedin.com/in/guilherme-cabral-130689254/"),
    summary="""
Desenvolvedor de software com experiência no desenvolvimento de aplicações Android, APIs backend e integrações entre sistemas.
Tenho experiências recentes com Kotlin, Java e TypeScript, criando soluções escaláveis, confiáveis e distribuídas para ambientes que exigem alto nível de estabilidade, envolvendo processamento de transações financeiras, persistência de dados e comunicação entre diferentes plataformas e dispositivos.
Curiosidade é o meu ponto forte, adoro aprender novas tecnologias, investigar problemas complexos e entregar soluções limpas e bem documentadas.
""",
)
