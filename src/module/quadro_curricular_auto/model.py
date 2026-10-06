from typing import Any

from pydantic import BaseModel, field_validator


class Professor(BaseModel):
    nome: str

    @field_validator("nome")
    @classmethod
    def normalizar_nome(cls, value: Any) -> str:
        return str(value).strip()


class Disciplina(BaseModel):
    nome: str
    prof: Professor

    @field_validator("nome")
    @classmethod
    def normalizar_nome(cls, value: Any) -> str:
        return str(value).strip()

    @field_validator("prof")
    @classmethod
    def normalizar_prof(cls, value: str) -> str:
        if value == "nan":
            value = ""

        return value


class Turma(BaseModel):
    nome: str
    disciplina: list[Disciplina]


class AutoParam(BaseModel):
    x: int
    y: int
    cor: tuple | None = None


class GradeCurricularSetting(BaseModel):

    # QUADRO CURRICULAR
    stado_dados_turma: AutoParam
    aba_quadro_curricular: AutoParam
    input_prof_1: AutoParam
    input_prof_2: AutoParam
    btn_proximo: AutoParam
    aba_dados_gerais: AutoParam
    a_quadro: AutoParam
    q_semana: AutoParam
    warning: AutoParam
    ok_warning: AutoParam
    # FILTRO
    turma_stado: AutoParam
    campo_list_turmas: AutoParam
    # SALVAR DADOS DA TURMA
    salvar_dados_turma: AutoParam
    fechar_dados_turma: AutoParam
    fechar_dados_turma_confirm1: AutoParam
    fechar_dados_turma_confirm2: AutoParam
