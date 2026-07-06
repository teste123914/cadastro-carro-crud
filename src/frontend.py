import tkinter as tk
from tkinter import ttk, messagebox

from marca import criar_marca, listar_marcas, atualizar_marca, excluir_marca
from modelo import criar_modelo, listar_modelos, atualizar_modelo, excluir_modelo
from carro import criar_carro, listar_carros, atualizar_carro, excluir_carro


class SistemaConcessionariaGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Concessionária")
        self.root.geometry("950x620")
        self.root.minsize(850, 560)

        titulo = ttk.Label(
            root,
            text="Sistema de Cadastro de Veículos",
            font=("Arial", 18, "bold")
        )
        titulo.pack(pady=12)

        self.abas = ttk.Notebook(root)
        self.abas.pack(fill="both", expand=True, padx=12, pady=8)

        self.criar_aba_marcas()
        self.criar_aba_modelos()
        self.criar_aba_carros()

    def campo(self, frame, texto, linha, coluna=0, largura=28):
        ttk.Label(frame, text=texto).grid(row=linha, column=coluna, padx=6, pady=6, sticky="w")
        entrada = ttk.Entry(frame, width=largura)
        entrada.grid(row=linha, column=coluna + 1, padx=6, pady=6, sticky="w")
        return entrada

    def limpar_campos(self, *campos):
        for campo in campos:
            campo.delete(0, tk.END)

    # =========================
    # ABA MARCAS
    # =========================
    def criar_aba_marcas(self):
        aba = ttk.Frame(self.abas)
        self.abas.add(aba, text="Marcas")

        form = ttk.LabelFrame(aba, text="Dados da marca")
        form.pack(fill="x", padx=10, pady=10)

        self.marca_id = self.campo(form, "ID:", 0)
        self.marca_nome = self.campo(form, "Nome da marca:", 1)

        botoes = ttk.Frame(aba)
        botoes.pack(fill="x", padx=10, pady=5)

        ttk.Button(botoes, text="Cadastrar", command=self.gui_cadastrar_marca).pack(side="left", padx=4)
        ttk.Button(botoes, text="Listar", command=self.gui_listar_marcas).pack(side="left", padx=4)
        ttk.Button(botoes, text="Atualizar", command=self.gui_atualizar_marca).pack(side="left", padx=4)
        ttk.Button(botoes, text="Excluir", command=self.gui_excluir_marca).pack(side="left", padx=4)
        ttk.Button(botoes, text="Limpar", command=lambda: self.limpar_campos(self.marca_id, self.marca_nome)).pack(side="left", padx=4)

        self.tabela_marcas = ttk.Treeview(aba, columns=("id", "nome"), show="headings")
        self.tabela_marcas.heading("id", text="ID")
        self.tabela_marcas.heading("nome", text="Nome")
        self.tabela_marcas.column("id", width=80, anchor="center")
        self.tabela_marcas.column("nome", width=400)
        self.tabela_marcas.pack(fill="both", expand=True, padx=10, pady=10)
        self.tabela_marcas.bind("<<TreeviewSelect>>", self.selecionar_marca)

    def gui_cadastrar_marca(self):
        try:
            criar_marca(self.marca_nome.get())
            messagebox.showinfo("Sucesso", "Marca cadastrada com sucesso!")
            self.gui_listar_marcas()
        except Exception as erro:
            messagebox.showerror("Erro", str(erro))

    def gui_listar_marcas(self):
        try:
            self.tabela_marcas.delete(*self.tabela_marcas.get_children())
            for item in listar_marcas():
                self.tabela_marcas.insert("", tk.END, values=item)
        except Exception as erro:
            messagebox.showerror("Erro", str(erro))

    def gui_atualizar_marca(self):
        try:
            atualizar_marca(int(self.marca_id.get()), self.marca_nome.get())
            messagebox.showinfo("Sucesso", "Marca atualizada com sucesso!")
            self.gui_listar_marcas()
        except Exception as erro:
            messagebox.showerror("Erro", str(erro))

    def gui_excluir_marca(self):
        try:
            excluir_marca(int(self.marca_id.get()))
            messagebox.showinfo("Sucesso", "Marca excluída com sucesso!")
            self.gui_listar_marcas()
        except Exception as erro:
            messagebox.showerror("Erro", str(erro))

    def selecionar_marca(self, event):
        selecionado = self.tabela_marcas.focus()
        if selecionado:
            valores = self.tabela_marcas.item(selecionado, "values")
            self.limpar_campos(self.marca_id, self.marca_nome)
            self.marca_id.insert(0, valores[0])
            self.marca_nome.insert(0, valores[1])

    # =========================
    # ABA MODELOS
    # =========================
    def criar_aba_modelos(self):
        aba = ttk.Frame(self.abas)
        self.abas.add(aba, text="Modelos")

        form = ttk.LabelFrame(aba, text="Dados do modelo")
        form.pack(fill="x", padx=10, pady=10)

        self.modelo_id = self.campo(form, "ID:", 0)
        self.modelo_nome = self.campo(form, "Nome do modelo:", 1)
        self.modelo_id_marca = self.campo(form, "ID da marca:", 2)

        dica = ttk.Label(form, text="Dica: consulte a aba Marcas para localizar o ID da marca.")
        dica.grid(row=3, column=0, columnspan=2, padx=6, pady=4, sticky="w")

        botoes = ttk.Frame(aba)
        botoes.pack(fill="x", padx=10, pady=5)

        ttk.Button(botoes, text="Cadastrar", command=self.gui_cadastrar_modelo).pack(side="left", padx=4)
        ttk.Button(botoes, text="Listar", command=self.gui_listar_modelos).pack(side="left", padx=4)
        ttk.Button(botoes, text="Atualizar", command=self.gui_atualizar_modelo).pack(side="left", padx=4)
        ttk.Button(botoes, text="Excluir", command=self.gui_excluir_modelo).pack(side="left", padx=4)
        ttk.Button(botoes, text="Limpar", command=lambda: self.limpar_campos(self.modelo_id, self.modelo_nome, self.modelo_id_marca)).pack(side="left", padx=4)

        self.tabela_modelos = ttk.Treeview(aba, columns=("id", "modelo", "marca"), show="headings")
        self.tabela_modelos.heading("id", text="ID")
        self.tabela_modelos.heading("modelo", text="Modelo")
        self.tabela_modelos.heading("marca", text="Marca")
        self.tabela_modelos.column("id", width=80, anchor="center")
        self.tabela_modelos.column("modelo", width=280)
        self.tabela_modelos.column("marca", width=280)
        self.tabela_modelos.pack(fill="both", expand=True, padx=10, pady=10)
        self.tabela_modelos.bind("<<TreeviewSelect>>", self.selecionar_modelo)

    def gui_cadastrar_modelo(self):
        try:
            criar_modelo(self.modelo_nome.get(), int(self.modelo_id_marca.get()))
            messagebox.showinfo("Sucesso", "Modelo cadastrado com sucesso!")
            self.gui_listar_modelos()
        except Exception as erro:
            messagebox.showerror("Erro", str(erro))

    def gui_listar_modelos(self):
        try:
            self.tabela_modelos.delete(*self.tabela_modelos.get_children())
            for item in listar_modelos():
                self.tabela_modelos.insert("", tk.END, values=item)
        except Exception as erro:
            messagebox.showerror("Erro", str(erro))

    def gui_atualizar_modelo(self):
        try:
            atualizar_modelo(int(self.modelo_id.get()), self.modelo_nome.get(), int(self.modelo_id_marca.get()))
            messagebox.showinfo("Sucesso", "Modelo atualizado com sucesso!")
            self.gui_listar_modelos()
        except Exception as erro:
            messagebox.showerror("Erro", str(erro))

    def gui_excluir_modelo(self):
        try:
            excluir_modelo(int(self.modelo_id.get()))
            messagebox.showinfo("Sucesso", "Modelo excluído com sucesso!")
            self.gui_listar_modelos()
        except Exception as erro:
            messagebox.showerror("Erro", str(erro))

    def selecionar_modelo(self, event):
        selecionado = self.tabela_modelos.focus()
        if selecionado:
            valores = self.tabela_modelos.item(selecionado, "values")
            self.limpar_campos(self.modelo_id, self.modelo_nome)
            self.modelo_id.insert(0, valores[0])
            self.modelo_nome.insert(0, valores[1])

    # =========================
    # ABA CARROS
    # =========================
    def criar_aba_carros(self):
        aba = ttk.Frame(self.abas)
        self.abas.add(aba, text="Carros")

        form = ttk.LabelFrame(aba, text="Dados do carro")
        form.pack(fill="x", padx=10, pady=10)

        self.carro_id = self.campo(form, "ID:", 0, 0)
        self.carro_id_modelo = self.campo(form, "ID do modelo:", 1, 0)
        self.carro_nome = self.campo(form, "Nome do carro:", 2, 0)
        self.carro_renavam = self.campo(form, "Renavam:", 0, 2)
        self.carro_placa = self.campo(form, "Placa:", 1, 2)
        self.carro_valor = self.campo(form, "Valor:", 2, 2)
        self.carro_ano = self.campo(form, "Ano:", 3, 2)

        dica = ttk.Label(form, text="Dica: consulte a aba Modelos para localizar o ID do modelo.")
        dica.grid(row=4, column=0, columnspan=4, padx=6, pady=4, sticky="w")

        botoes = ttk.Frame(aba)
        botoes.pack(fill="x", padx=10, pady=5)

        ttk.Button(botoes, text="Cadastrar", command=self.gui_cadastrar_carro).pack(side="left", padx=4)
        ttk.Button(botoes, text="Listar", command=self.gui_listar_carros).pack(side="left", padx=4)
        ttk.Button(botoes, text="Atualizar", command=self.gui_atualizar_carro).pack(side="left", padx=4)
        ttk.Button(botoes, text="Excluir", command=self.gui_excluir_carro).pack(side="left", padx=4)
        ttk.Button(botoes, text="Limpar", command=self.limpar_campos_carro).pack(side="left", padx=4)

        self.tabela_carros = ttk.Treeview(
            aba,
            columns=("id", "nome", "modelo", "placa", "valor", "ano"),
            show="headings"
        )
        for coluna, titulo, largura in [
            ("id", "ID", 60),
            ("nome", "Carro", 180),
            ("modelo", "Modelo", 180),
            ("placa", "Placa", 100),
            ("valor", "Valor", 120),
            ("ano", "Ano", 80),
        ]:
            self.tabela_carros.heading(coluna, text=titulo)
            self.tabela_carros.column(coluna, width=largura)

        self.tabela_carros.pack(fill="both", expand=True, padx=10, pady=10)
        self.tabela_carros.bind("<<TreeviewSelect>>", self.selecionar_carro)

    def limpar_campos_carro(self):
        self.limpar_campos(
            self.carro_id,
            self.carro_id_modelo,
            self.carro_nome,
            self.carro_renavam,
            self.carro_placa,
            self.carro_valor,
            self.carro_ano,
        )

    def gui_cadastrar_carro(self):
        try:
            criar_carro(
                int(self.carro_id_modelo.get()),
                self.carro_nome.get(),
                int(self.carro_renavam.get()),
                self.carro_placa.get(),
                float(self.carro_valor.get()),
                int(self.carro_ano.get())
            )
            messagebox.showinfo("Sucesso", "Carro cadastrado com sucesso!")
            self.gui_listar_carros()
        except Exception as erro:
            messagebox.showerror("Erro", str(erro))

    def gui_listar_carros(self):
        try:
            self.tabela_carros.delete(*self.tabela_carros.get_children())
            for item in listar_carros():
                self.tabela_carros.insert("", tk.END, values=item)
        except Exception as erro:
            messagebox.showerror("Erro", str(erro))

    def gui_atualizar_carro(self):
        try:
            atualizar_carro(
                int(self.carro_id.get()),
                int(self.carro_id_modelo.get()),
                self.carro_nome.get(),
                int(self.carro_renavam.get()),
                self.carro_placa.get(),
                float(self.carro_valor.get()),
                int(self.carro_ano.get())
            )
            messagebox.showinfo("Sucesso", "Carro atualizado com sucesso!")
            self.gui_listar_carros()
        except Exception as erro:
            messagebox.showerror("Erro", str(erro))

    def gui_excluir_carro(self):
        try:
            excluir_carro(int(self.carro_id.get()))
            messagebox.showinfo("Sucesso", "Carro excluído com sucesso!")
            self.gui_listar_carros()
        except Exception as erro:
            messagebox.showerror("Erro", str(erro))

    def selecionar_carro(self, event):
        selecionado = self.tabela_carros.focus()
        if selecionado:
            valores = self.tabela_carros.item(selecionado, "values")
            self.limpar_campos_carro()
            self.carro_id.insert(0, valores[0])
            self.carro_nome.insert(0, valores[1])
            self.carro_placa.insert(0, valores[3])
            self.carro_valor.insert(0, valores[4])
            self.carro_ano.insert(0, valores[5])


if __name__ == "__main__":
    janela = tk.Tk()
    app = SistemaConcessionariaGUI(janela)
    janela.mainloop()
