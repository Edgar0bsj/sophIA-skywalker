from src.module.log.logging_config import logger
import pyautogui as gui
from src.module.quadro_curricular_auto.model import AutoParam
from src.module.quadro_curricular_auto.controller import QuadroCurricularController


def main():
    qcc = QuadroCurricularController("textoAutoFill.xlsx")
    qcc.grade_curricular_setting(
        turma_stado=AutoParam(x=66, y=349, cor=(255, 201, 14)),  # <-
        stado_dados_turma=AutoParam(x=1056, y=90, cor=(128, 128, 128)),
        aba_quadro_curricular=AutoParam(x=260, y=159, cor=(96, 0, 54)),
        input_prof_1=AutoParam(x=1345, y=299, cor=(0, 0, 0)),
        input_prof_2=AutoParam(x=1314, y=297, cor=(0, 120, 215)),
        btn_proximo=AutoParam(x=119, y=235, cor=(0, 0, 0)),
        aba_dados_gerais=AutoParam(x=1019, y=182, cor=(240, 240, 240)),
        a_quadro=AutoParam(x=1123, y=240, cor=(255, 255, 255)),
        q_semana=AutoParam(x=1287, y=240, cor=(255, 255, 255)),
        warning=AutoParam(x=524, y=381, cor=(234, 169, 0)),
        ok_warning=AutoParam(x=824, y=432, cor=(240, 240, 240)),
        campo_list_turmas=AutoParam(x=1233, y=354, cor=(255, 255, 255)),
        salvar_dados_turma=AutoParam(x=80, y=50, cor=(77, 193, 55)),
        fechar_dados_turma=AutoParam(x=1342, y=7, cor=(211, 98, 87)),
        fechar_dados_turma_confirm1=AutoParam(x=834, y=486, cor=(133, 203, 236)),
        fechar_dados_turma_confirm2=AutoParam(x=839, y=435, cor=(240, 240, 171)),
    )
    qcc.run()


if "__main__" == __name__:
    logger()
    main()
    # gui.mouseInfo()
