from src.module.log.logging_config import logger

from src.module.quadro_curricular_auto.controller import QuadroCurricularController


def main():
    qcc = QuadroCurricularController("textoAutoFill.xlsx")
    qcc.run()


if "__main__" == __name__:
    logger()
    main()
