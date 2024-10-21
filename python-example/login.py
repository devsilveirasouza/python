import customtkinter
# Configurando o tema
customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"

# Criando a janela
janela = customtkinter.CTk()
janela.geometry("250x300")
# Desabilitar o redimensionamento da janela
janela.resizable(False, False)

# Função para o botão 
def clique():
    print("Fazer login!")

# Criando o título da janela
janela.title("Login")

# Criando o título
customtkinter.CTkLabel(janela, text="Entre com as suas credenciais!").pack(padx=10, pady=10)

# Criando o campo de entrada
entrada = customtkinter.CTkEntry(janela, placeholder_text="Username")
entrada.pack(padx=10, pady=20)

# Criando o campo de senha
senha = customtkinter.CTkEntry(janela, placeholder_text="Password", show="*")
senha.pack(padx=10, pady=10)

# Criando o checkbox
checkbox = customtkinter.CTkCheckBox(janela, text="Remember me")
checkbox.pack(padx=10, pady=10)
    
# Criando o botão    
botao = customtkinter.CTkButton(janela, text="Logar", command=clique)
botao.pack(padx=10, pady=20)

# Executando a janela
janela.mainloop()