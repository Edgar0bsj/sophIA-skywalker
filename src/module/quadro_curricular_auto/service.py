from pathlib import Path
import pandas as pd
import keyboard
import pyautogui as pag
from src.module.quadro_curricular_auto.model import (
    GradeCurricularSetting,
    Disciplina,
    Professor,
    Turma,
)
from rich import print
from rich.panel import Panel


class Service:

    # ================================================
    # clicar_no_campo_professor
    # ================================================
    def clicar_no_campo_professor(
        self,
        gc: GradeCurricularSetting,
        prof_name: str,
        sleep_time: float = 2,
        write_delay: float = 0.04,
        matche_color_tolerance: int = 10,
    ):

        if pag.pixelMatchesColor(
            gc.input_prof_1.x,
            gc.input_prof_1.y,
            gc.input_prof_1.cor,
            tolerance=matche_color_tolerance,
        ) or pag.pixelMatchesColor(
            gc.input_prof_2.x,
            gc.input_prof_2.y,
            gc.input_prof_2.cor,
            tolerance=matche_color_tolerance,
        ):
            pag.doubleClick(x=gc.input_prof_1.x, y=gc.input_prof_1.y)
            pag.sleep(sleep_time)
            keyboard.write(prof_name, delay=write_delay)
            pag.sleep(sleep_time)
        else:
            print(">>>>>>>>  ERROR  <<<<<<<<<<<")
            input("")
            raise Exception(">>>>>>>>  ERROR  <<<<<<<<<<<")

    # ================================================
    # ir_para_proxima_disciplina
    # ================================================
    def ir_para_proxima_disciplina(
        self,
        gc: GradeCurricularSetting,
        matche_color_tolerance: int = 10,
        sleep_time: float = 2,
    ):

        if pag.pixelMatchesColor(
            gc.btn_proximo.x,
            gc.btn_proximo.y,
            gc.btn_proximo.cor,
            tolerance=matche_color_tolerance,
        ):
            pag.click(x=gc.btn_proximo.x, y=gc.btn_proximo.y)
            pag.sleep(sleep_time)
        else:
            print(">>>>>>>>  ERROR  <<<<<<<<<<<")
            input("")
            raise Exception(">>>>>>>>  ERROR  <<<<<<<<<<<")

    # ================================================
    # tratar_warning
    # ================================================
    def tratar_warning(
        self,
        gc: GradeCurricularSetting,
        sleep_time: float = 2,
        write_delay: float = 0.04,
        matche_color_tolerance: int = 10,
    ):

        if pag.pixelMatchesColor(
            gc.warning.x,
            gc.warning.y,
            gc.warning.cor,
            tolerance=matche_color_tolerance,
        ):
            pag.sleep(sleep_time)
            pag.click(x=gc.ok_warning.x, y=gc.ok_warning.y)

            if pag.pixelMatchesColor(
                gc.a_quadro.x,
                gc.a_quadro.y,
                gc.a_quadro.cor,
                tolerance=matche_color_tolerance,
            ):
                pag.sleep(sleep_time)
                pag.doubleClick(x=gc.a_quadro.x, y=gc.a_quadro.y)

                pag.sleep(sleep_time)
                keyboard.write("0", delay=write_delay)

                pag.sleep(sleep_time)
                pag.doubleClick(x=gc.q_semana.x, y=gc.q_semana.y)

                pag.sleep(sleep_time)
                keyboard.write("0", delay=write_delay)

                pag.sleep(sleep_time)
                pag.click(x=gc.aba_dados_gerais.x, y=gc.aba_dados_gerais.y)

                pag.sleep(sleep_time)
                pag.click(x=gc.btn_proximo.x, y=gc.btn_proximo.y)
            else:
                print(">>>>>>>>  ERROR  <<<<<<<<<<<")
                input("")
                raise Exception(">>>>>>>>  ERROR  <<<<<<<<<<<")

    # ================================================
    # carregar_objetos_do_xlsx
    # ================================================
    def carregar_objetos_do_xlsx(
        self,
        file_path: Path,
        *,
        col_turma: str = "TURMA",
        col_disc: str = "DISCIPLINA",
        col_prof: str = "PROF_DISC",
    ) -> list[Turma]:
        df = pd.read_excel(file_path)

        box: dict[str, Turma] = {}

        for _, value in df.iterrows():
            turma = str(value[col_turma])
            prof = Professor(nome=value[col_prof])
            disc = Disciplina(nome=value[col_disc], prof=prof)

            if not turma in box:
                box[turma] = Turma(nome=turma, disciplina=[])

            box[turma].disciplina.append(disc)

        return list(box.values())

    # ================================================
    # carregar_objetos_do_xlsx
    # ================================================
    def painel_info(self, qtd_total: int, qtd_atual: int):
        percentual = (qtd_atual / qtd_total) * 100
        info = (
            f"[bold white]Turmas Restante:[/bold white] [bold green]{qtd_total-qtd_atual}[/bold green]\n"
            f"[bold white]Turmas concluidas:[/bold white] [bold green]{qtd_atual}[/bold green]\n"
            f"[bold white]Concluido:[/bold white] [bold green]{round(percentual)}%[/bold green]\n"
        )
        print(Panel(info, title="[bold cyan]Informações[/bold cyan]", expand=False))

    # ================================================
    # stado_turmas_filtrar_curso
    # ================================================
    def stado_turmas_filtrar_curso(
        self,
        turma: str,
        gc: GradeCurricularSetting,
        sleep_time: float = 2,
        write_delay: float = 0.04,
        matche_color_tolerance: int = 10,
    ):

        if pag.pixelMatchesColor(
            gc.turma_stado.x,
            gc.turma_stado.y,
            gc.turma_stado.cor,
            tolerance=matche_color_tolerance,
        ):
            pag.sleep(sleep_time)
            pag.click(x=gc.campo_list_turmas.x, y=gc.campo_list_turmas.y)
            pag.sleep(sleep_time)
            keyboard.write(turma, delay=write_delay)
            pag.sleep(sleep_time)
            pag.press("enter")
            pag.sleep(5)
            pag.hotkey("win", "up")
            pag.sleep(sleep_time)
        else:
            print(">>>>>>>>  ERROR  <<<<<<<<<<<")
            input("")
            raise Exception(">>>>>>>>  ERROR  <<<<<<<<<<<")

    # ================================================
    # stado_dados_turmas_ir_para_quadro_curricular
    # ================================================
    def stado_dados_turmas_ir_para_quadro_curricular(
        self,
        gc: GradeCurricularSetting,
        sleep_time: float = 3,
        matche_color_tolerance: int = 10,
    ):

        if pag.pixelMatchesColor(
            gc.stado_dados_turma.x,
            gc.stado_dados_turma.y,
            gc.stado_dados_turma.cor,
            tolerance=matche_color_tolerance,
        ):
            pag.sleep(sleep_time)
            pag.click(x=gc.aba_quadro_curricular.x, y=gc.aba_quadro_curricular.y)
            pag.sleep(sleep_time)
        else:
            print(">>>>>>>>  ERROR  <<<<<<<<<<<")
            input("")
            raise Exception(">>>>>>>>  ERROR  <<<<<<<<<<<")

    # ================================================
    # salvar_dados_da_turma
    # ================================================
    def salvar_dados_da_turma(
        self,
        gc: GradeCurricularSetting,
        size_turma: int,
        sleep_time: float = 3,
        matche_color_tolerance: int = 10,
    ):

        if pag.pixelMatchesColor(
            gc.salvar_dados_turma.x,
            gc.salvar_dados_turma.y,
            gc.salvar_dados_turma.cor,
            tolerance=matche_color_tolerance,
        ):
            pag.sleep(sleep_time)
            pag.click(x=gc.salvar_dados_turma.x, y=gc.salvar_dados_turma.y)
            pag.sleep(sleep_time)
            pag.click(x=gc.fechar_dados_turma.x, y=gc.fechar_dados_turma.y)
            pag.sleep(sleep_time)
            if pag.pixelMatchesColor(
                gc.fechar_dados_turma_confirm1.x,
                gc.fechar_dados_turma_confirm1.y,
                gc.fechar_dados_turma_confirm1.cor,
                tolerance=matche_color_tolerance,
            ):
                pag.click(
                    x=gc.fechar_dados_turma_confirm1.x,
                    y=gc.fechar_dados_turma_confirm1.y,
                )
                pag.sleep(sleep_time)
                pag.click(
                    x=gc.fechar_dados_turma_confirm2.x,
                    y=gc.fechar_dados_turma_confirm2.y,
                )
                pag.sleep(sleep_time)
                pag.click(
                    x=gc.campo_list_turmas.x,
                    y=gc.campo_list_turmas.y,
                )
                pag.sleep(sleep_time)
                pag.press("backspace", presses=size_turma, interval=0.1)

        else:
            print(">>>>>>>>  ERROR  <<<<<<<<<<<")
            input("")
            raise Exception(">>>>>>>>  ERROR  <<<<<<<<<<<")
