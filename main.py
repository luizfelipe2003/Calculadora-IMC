import customtkinter as ctk

# Cores
cor0 = "#2C3E50"  # Azul Escuro para texto e rótulos (profissional e moderno)
cor1 = "#ECF0F1"  # Cinza Claro para fundo e texto (limpo e legível)
cor2 = "#3498DB"  # Azul para botões (calmo e moderno)
cor3 = "#E5E8E8"  # Cinza Claro para fundo da janela
cor4 = "#16A085"  # Verde Água para detalhes (fresco e estiloso)
cor5 = "#95A5A6"  # Cinza para texto secundário

# Função para calcular o IMC
def calcular_imc():
    try:
        peso = float(entry_peso.get())
        altura = float(entry_altura.get())
        imc = peso / (altura ** 2)
        resultado_label.configure(text=f"Seu IMC: {imc:.2f}")

        if imc < 18.5:
            classificacao_label.configure(text="Classificação: Abaixo do peso", fg_color=cor2)
        elif 18.5 <= imc < 24.9:
            classificacao_label.configure(text="Classificação: Peso normal", fg_color=cor4)
        elif 25 <= imc < 29.9:
            classificacao_label.configure(text="Classificação: Sobrepeso", fg_color=cor5)
        else:
            classificacao_label.configure(text="Classificação: Obesidade", fg_color="#E74C3C")
    except ValueError:
        resultado_label.configure(text="Entrada inválida! Use números.")
        classificacao_label.configure(text="")

# Configuração da janela
janela = ctk.CTk()
janela.title("Calculadora de IMC")
janela.geometry('440x520')
janela.configure(bg=cor3)

# Título
titulo_label = ctk.CTkLabel(janela, text="Calculadora de IMC", font=("Arial", 20, "bold"), text_color=cor0, bg_color=cor3)
titulo_label.pack(pady=20)

# Entrada de Peso
entry_peso = ctk.CTkEntry(janela, placeholder_text="Peso (kg)", font=("Arial", 14), fg_color=cor1, text_color=cor0)
entry_peso.pack(pady=10)

# Entrada de Altura
entry_altura = ctk.CTkEntry(janela, placeholder_text="Altura (m)", font=("Arial", 14), fg_color=cor1, text_color=cor0)
entry_altura.pack(pady=10)

# Botão Calcular
botao_calcular = ctk.CTkButton(janela, text="Calcular", font=("Arial", 14, "bold"), fg_color=cor2, command=calcular_imc)
botao_calcular.pack(pady=20)

# Resultado
resultado_label = ctk.CTkLabel(janela, text="", font=("Arial", 16, "bold"), text_color=cor0, bg_color=cor3)
resultado_label.pack(pady=10)

# Classificação
classificacao_label = ctk.CTkLabel(janela, text="", font=("Arial", 16, "bold"), text_color=cor0, bg_color=cor3)
classificacao_label.pack(pady=10)

janela.mainloop()
