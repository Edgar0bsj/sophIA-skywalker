from src.module.log.logging_config import logging
from pathlib import Path

import keyboard

from src.module.quadro_curricular_auto.model import AutoParam, GradeCurricularSetting
from src.module.quadro_curricular_auto.service import Service
from src.module.util.clear_terminal import clear_terminal

from rich import print


class QuadroCurricularController:
    def __init__(
        self,
        file_path: str,
        *,
        col_turma: str = "TURMA",
        col_disc: str = "DISCIPLINA",
        col_prof: str = "PROF_DISC",
    ):
        base_dir = Path().cwd()

        self.service = Service()

        self._gc = None

        self.file_path = base_dir / file_path
        self.col_turma = col_turma
        self.col_disc = col_disc
        self.col_prof = col_prof

    def grade_curricular_setting(
        self,
        *,
        input_prof_1: AutoParam,
        input_prof_2: AutoParam,
        btn_proximo: AutoParam,
        aba_dados_gerais: AutoParam,
        a_quadro: AutoParam,
        q_semana: AutoParam,
        warning: AutoParam,
        ok_warning: AutoParam,
    ):
        self._gc = GradeCurricularSetting(
            input_prof_1=input_prof_1,
            input_prof_2=input_prof_2,
            btn_proximo=btn_proximo,
            aba_dados_gerais=aba_dados_gerais,
            a_quadro=a_quadro,
            q_semana=q_semana,
            warning=warning,
            ok_warning=ok_warning,
        )

    def run(self):
        list_turma = self.service.carregar_objetos_do_xlsx(
            self.file_path,
            col_disc=self.col_disc,
            col_turma=self.col_turma,
            col_prof=self.col_prof,
        )

        cont = 0
        for i in list_turma:
            self.service.painel_info(qtd_total=len(list_turma), qtd_atual=cont)
            cont += 1
            logging.info(f"{i.nome} | Pronto para Preenchimento, aguardando comando")
            print(
                f"[bold green]{len(i.disciplina)} disciplinas carregadas[/bold green]"
            )
            print(f"Aguardando comando my nobre...")
            keyboard.wait("f8")

            logging.info(f"{i.nome} | Digitando na tela de Turmas")
            keyboard.write(i.nome, delay=0.04)
            #
            logging.info(f"{i.nome} | Entrando no Quadro curricular ")
            #
            logging.info(f"{i.nome} | Indo para aba responsavel pelas disciplinas")
            #
            logging.info(f"{i.nome} | Iniciando processo de preenchimento")
            # self.service.clicar_no_campo_professor()
            # self.service.ir_para_proxima_disciplina()
            # self.service.tratar_warning()
            #
            logging.info(f"{i.nome} | Salvando")
            #
            logging.info(f"{i.nome} | Preenchido com sucesso")
            clear_terminal()
            input("enter")
