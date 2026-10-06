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
        # Dados da turma
        stado_dados_turma: AutoParam,
        aba_quadro_curricular: AutoParam,
        input_prof_1: AutoParam,
        input_prof_2: AutoParam,
        btn_proximo: AutoParam,
        aba_dados_gerais: AutoParam,
        a_quadro: AutoParam,
        q_semana: AutoParam,
        warning: AutoParam,
        ok_warning: AutoParam,
        # Filtro
        turma_stado: AutoParam,
        campo_list_turmas: AutoParam,
        # Fechar dados da turma
        salvar_dados_turma: AutoParam,
        fechar_dados_turma: AutoParam,
        fechar_dados_turma_confirm1: AutoParam,
        fechar_dados_turma_confirm2: AutoParam,
    ):
        self._gc = GradeCurricularSetting(
            stado_dados_turma=stado_dados_turma,
            aba_quadro_curricular=aba_quadro_curricular,
            input_prof_1=input_prof_1,
            input_prof_2=input_prof_2,
            btn_proximo=btn_proximo,
            aba_dados_gerais=aba_dados_gerais,
            a_quadro=a_quadro,
            q_semana=q_semana,
            warning=warning,
            ok_warning=ok_warning,
            turma_stado=turma_stado,
            campo_list_turmas=campo_list_turmas,
            salvar_dados_turma=salvar_dados_turma,
            fechar_dados_turma=fechar_dados_turma,
            fechar_dados_turma_confirm1=fechar_dados_turma_confirm1,
            fechar_dados_turma_confirm2=fechar_dados_turma_confirm2,
        )

    def run(self):
        list_turma = self.service.carregar_objetos_do_xlsx(
            self.file_path,
            col_disc=self.col_disc,
            col_turma=self.col_turma,
            col_prof=self.col_prof,
        )

        print(f"Aguardando comando my nobre...")
        keyboard.wait("f8")
        cont = 0
        for turma in list_turma:
            self.service.painel_info(qtd_total=len(list_turma), qtd_atual=cont)
            cont += 1
            logging.info(f"Turma:{turma.nome} | Iniciando Preenchimento")
            print(f"[bold cyan]{turma.nome}[/bold cyan]")
            print(
                f"[bold green]{len(turma.disciplina)} disciplinas carregadas[/bold green]"
            )
            self.service.stado_turmas_filtrar_curso(turma.nome, self._gc)
            self.service.stado_dados_turmas_ir_para_quadro_curricular(self._gc)

            for disciplina in turma.disciplina:
                logging.info(f"Disciplina:{disciplina.nome} | Iniciando Preenchimento")
                logging.info(
                    f"Professor:{disciplina.prof.nome} | Iniciando Preenchimento"
                )
                print(f"========================================")
                print(f"DISCIPLINA: {disciplina.nome}")
                print(f"PROFESSOR: {disciplina.prof.nome}")
                self.service.clicar_no_campo_professor(
                    prof_name=disciplina.prof.nome, gc=self._gc
                )
                self.service.ir_para_proxima_disciplina(gc=self._gc)
                self.service.tratar_warning(gc=self._gc)
                logging.info(
                    f"Disciplina:{disciplina.nome} | Preenchimento feito com sucesso!"
                )
                logging.info(
                    f"Professor:{disciplina.prof.nome} | Preenchimento feito com sucesso!"
                )

            self.service.salvar_dados_da_turma(gc=self._gc, size_turma=len(turma.nome))
            logging.info(f"Turma:{turma.disciplina} | Preenchimento feito com sucesso!")
            clear_terminal()
