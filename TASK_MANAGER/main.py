import customtkinter as custom 

aba1 = custom.CTk() #criando a aba
#config da aba
aba1._set_appearance_mode("dark")
aba1.title("Task Manager")
aba1.geometry("400x700")
aba1.maxsize(width=450, height=800)
aba1.minsize(width=300, height=500)
#aba1.overrideredirect(True)

##############################################################################################################################

def caixa_tarefa(destino, texto_da_tarefa):#função que vai chamar as tarefas pra dentro do scrollableframe
    frame_tarefa = custom.CTkFrame(destino)#frame de tarefa
    frame_tarefa.pack(fill="x", padx=2, pady=2)

    botao_apagar = custom.CTkButton(frame_tarefa, text="Apagar", width=20, height=10, command=frame_tarefa.destroy)#botão de excluir tarefa
    botao_apagar.pack(padx=5, pady=5, side="right")

    checkbox = custom.CTkCheckBox(frame_tarefa, text="", width=24)#checkbox
    checkbox.pack(padx=5, pady=5, side="right")
    
    texto_frame = custom.CTkLabel(frame_tarefa, text=texto_da_tarefa, wraplength=200, anchor="w", justify="left")#texto que ficará dentro do frame
    texto_frame.pack(padx=5, pady=5, side="left", fill="both", expand=True)

def nova_aba():
    global aba_criar
    aba_criar = custom.CTkToplevel(aba1)
    aba_criar.title("")
    aba_criar.geometry("400x100")
    aba_criar.attributes("-topmost", True)

    campo_texto = custom.CTkEntry(aba_criar, placeholder_text="Digite sua tarefa.....")
    campo_texto.pack(expand=True, fill="x", padx=10)

    selecao = custom.CTkComboBox(aba_criar, values=["DIA", "SEMANA", "MÊS"], width=60, height=20)
    selecao.pack(pady=5)

    def salvar_tarefa():
        texto_digitado = campo_texto.get()
        categoria = selecao.get()
        if categoria == "DIA":
            caixa_tarefa(lista_dia, texto_digitado)
        elif categoria == "SEMANA":
            caixa_tarefa(lista_sem, texto_digitado)
        else:
            caixa_tarefa(lista_mes, texto_digitado)

        aba_criar.destroy()

    botao_salvar = custom.CTkButton(aba_criar, text="Salvar", command=salvar_tarefa)
    botao_salvar.pack(pady=5)



##############################################################################################################################
cabecalho = custom.CTkFrame(aba1, fg_color="transparent")
cabecalho.pack(pady=5, padx=10, fill="x")
texto_cabecalho = custom.CTkLabel(cabecalho, text="TAREFAS")
texto_cabecalho.pack(side="left")
modo_foco = custom.CTkSwitch(cabecalho, text="MODO FOCO")
modo_foco.pack(side="right")


tarefas = custom.CTkTabview(aba1)
tarefas.pack(side="top", fill="both", expand=True, padx=10)
tarefas.add("Diárias")
tarefas.add("Semanais")
tarefas.add("Mensais")

lista_dia = custom.CTkScrollableFrame(tarefas.tab("Diárias"))
lista_dia.pack(side="top", fill="both", expand=True)

lista_sem = custom.CTkScrollableFrame(tarefas.tab("Semanais"))
lista_sem.pack(side="top", fill="both", expand=True,)

lista_mes = custom.CTkScrollableFrame(tarefas.tab("Mensais"))
lista_mes.pack(side="top", fill="both", expand=True,)

btn_criar = custom.CTkButton(aba1, text="Criar Tarefa", command=nova_aba)
btn_criar.pack(pady=10)

btn_fechar = custom.CTkButton(aba1, text="Fechar", command=aba1.destroy)
btn_fechar.pack(pady=10)

##############################################################################################################################

aba1.mainloop() #um "loop" que faz a janela abrir 




