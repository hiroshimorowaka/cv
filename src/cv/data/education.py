from datetime import date

from cv.models import Education

EDUCATION = (
    Education(
        institution="UNINTER - Centro Universitário Internacional",
        degree="Bacharelado",
        field="Ciência da Computação",
        start=date(2026, 1, 1),
        end=date(2029, 12, 1),
    ),
)
