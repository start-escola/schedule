import pandas as pd
import plotly.figure_factory as ff
import plotly.io as pio
from datetime import datetime, timedelta

# Configurar data de início do projeto
data_inicio = datetime(2025, 1, 1)

# Criar função para calcular datas
def calcular_data(mes, semana, duracao_semanas=1):
    data_inicio_atividade = data_inicio + timedelta(days=(mes-1)*30 + (semana-1)*7)
    data_fim_atividade = data_inicio_atividade + timedelta(days=duracao_semanas*7 - 1)
    return data_inicio_atividade, data_fim_atividade

# Criar dados para o gráfico de Gantt
df = []

# Fase 1: PLANEJAMENTO INICIAL
df.append(dict(Task="1. PLANEJAMENTO INICIAL", Start='2025-01-01', Finish='2025-01-28', Resource='Fase'))
df.append(dict(Task="Mobilização inicial", Start='2025-01-01', Finish='2025-01-07', Resource='Planejamento'))
df.append(dict(Task="Formação do Comitê Técnico-Científico", Start='2025-01-08', Finish='2025-01-14', Resource='Planejamento'))
df.append(dict(Task="Mapeamento das 70 escolas", Start='2025-01-15', Finish='2025-01-28', Resource='Planejamento'))

# Fase 2: DIAGNÓSTICO E FORMAÇÃO
df.append(dict(Task="2. DIAGNÓSTICO E FORMAÇÃO", Start='2025-02-01', Finish='2025-03-07', Resource='Fase'))
df.append(dict(Task="Diagnóstico cognitivo e socioemocional", Start='2025-02-01', Finish='2025-02-14', Resource='Diagnóstico'))
df.append(dict(Task="Formação presencial de professores", Start='2025-02-15', Finish='2025-02-28', Resource='Formação'))
df.append(dict(Task="Devolutiva do diagnóstico", Start='2025-03-01', Finish='2025-03-07', Resource='Diagnóstico'))

# Fase 3: TRILHAS FORMATIVAS
df.append(dict(Task="3. TRILHAS FORMATIVAS", Start='2025-03-08', Finish='2025-08-31', Resource='Fase'))
df.append(dict(Task="Lançamento das trilhas online", Start='2025-03-08', Finish='2025-03-14', Resource='Trilhas'))
df.append(dict(Task="Encontros semanais online", Start='2025-03-15', Finish='2025-08-31', Resource='Trilhas'))
df.append(dict(Task="Aplicação do conteúdo presencial", Start='2025-03-15', Finish='2025-08-31', Resource='Trilhas'))
df.append(dict(Task="Workshops de comunicação e liderança", Start='2025-04-15', Finish='2025-06-15', Resource='Trilhas'))

# Fase 4: DESENVOLVIMENTO DE PROJETOS
df.append(dict(Task="4. DESENVOLVIMENTO DE PROJETOS", Start='2025-03-08', Finish='2025-09-07', Resource='Fase'))
df.append(dict(Task="Mentorias semanais para professores", Start='2025-03-08', Finish='2025-08-31', Resource='Desenvolvimento'))
df.append(dict(Task="Mentoria dos professores para alunos", Start='2025-03-15', Finish='2025-08-31', Resource='Desenvolvimento'))
df.append(dict(Task="Desenvolvimento dos desafios semanais", Start='2025-04-01', Finish='2025-07-31', Resource='Desenvolvimento'))
df.append(dict(Task="Desenvolvimento do projeto macro", Start='2025-05-01', Finish='2025-08-31', Resource='Desenvolvimento'))
df.append(dict(Task="Monitoramento via dashboard", Start='2025-03-08', Finish='2025-09-07', Resource='Desenvolvimento'))

# Fase 5: EVENTOS E COMPETIÇÕES
df.append(dict(Task="5. EVENTOS E COMPETIÇÕES", Start='2025-05-08', Finish='2025-08-21', Resource='Fase'))
df.append(dict(Task="Primeira feira escolar (orientação)", Start='2025-05-08', Finish='2025-05-09', Resource='Eventos'))
df.append(dict(Task="Desafio gamificado intercolegial", Start='2025-06-15', Finish='2025-06-22', Resource='Eventos'))
df.append(dict(Task="Segunda feira escolar - Hackathon", Start='2025-08-01', Finish='2025-08-02', Resource='Eventos'))
df.append(dict(Task="Segunda feira escolar - Banca", Start='2025-08-08', Finish='2025-08-09', Resource='Eventos'))
df.append(dict(Task="Seleção dos 20 projetos finalistas", Start='2025-08-15', Finish='2025-08-21', Resource='Eventos'))

# Fase 6: AVALIAÇÃO E ENCERRAMENTO
df.append(dict(Task="6. AVALIAÇÃO E ENCERRAMENTO", Start='2025-08-22', Finish='2026-03-31', Resource='Fase'))
df.append(dict(Task="Aplicação do questionário final", Start='2025-08-22', Finish='2025-08-28', Resource='Avaliação'))
df.append(dict(Task="Análise comparativa com diagnóstico", Start='2025-09-01', Finish='2025-09-07', Resource='Avaliação'))
df.append(dict(Task="Evento de formatura e premiação", Start='2025-09-08', Finish='2025-09-09', Resource='Avaliação'))
df.append(dict(Task="Anúncio dos 5 projetos selecionados", Start='2025-09-08', Finish='2025-09-09', Resource='Avaliação'))
df.append(dict(Task="Mentoria estendida", Start='2025-09-15', Finish='2026-03-15', Resource='Avaliação'))
df.append(dict(Task="Entrega do portfólio final", Start='2026-03-22', Finish='2026-03-31', Resource='Avaliação'))

# Criar o gráfico de Gantt
colors = {'Fase': 'rgb(220, 220, 220)', 
          'Planejamento': 'rgb(46, 137, 205)',
          'Diagnóstico': 'rgb(114, 44, 121)', 
          'Formação': 'rgb(198, 47, 105)',
          'Trilhas': 'rgb(58, 149, 136)', 
          'Desenvolvimento': 'rgb(214, 123, 14)',
          'Eventos': 'rgb(33, 102, 172)', 
          'Avaliação': 'rgb(169, 34, 98)'}

fig = ff.create_gantt(df, colors=colors, index_col='Resource', show_colorbar=True,
                     showgrid_x=True, showgrid_y=True, group_tasks=True, title='Cronograma do Projeto "Empreender para Transformar"')

# Ajustar layout
fig.update_layout(
    autosize=False,
    width=1200,
    height=800,
    margin=dict(l=50, r=50, b=100, t=100, pad=4),
    font=dict(family="Arial", size=12),
    title_font=dict(size=20),
    legend=dict(
        orientation="h",
        yanchor="bottom",
        y=-0.2,
        xanchor="center",
        x=0.5
    )
)

# Salvar como HTML e PNG
pio.write_html(fig, file='/home/ubuntu/projeto/cronograma_visual/cronograma_gantt.html', auto_open=False)
pio.write_image(fig, file='/home/ubuntu/projeto/cronograma_visual/cronograma_gantt.png', width=1200, height=800, scale=2)

print("Cronograma visual criado com sucesso!")
