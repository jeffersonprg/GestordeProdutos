from tkinter import ttk, messagebox
from tkinter import *
import sqlite3
import os

class ProdutoApp:
    db = 'database/produtos.db'

    def __init__(self, root):
        self.janela = root
        self.janela.title("Gestor de Produtos")
        self.janela.resizable(1, 1)

        if os.path.exists('recursos/icon.ico'):
            self.janela.wm_iconbitmap('recursos/icon.ico')

        # Garante que a pasta database existe
        os.makedirs('database', exist_ok=True)

        # Criar a base de dados se necessário
        self.criar_tabela()

        # Frame principal
        frame = LabelFrame(self.janela, text="Registar um novo Produto")
        frame.grid(row=0, column=0, columnspan=3, pady=20)

        # Nome
        Label(frame, text="Nome: ").grid(row=1, column=0)
        self.nome = Entry(frame)
        self.nome.focus()
        self.nome.grid(row=1, column=1)

        # Preço
        Label(frame, text="Preço: ").grid(row=2, column=0)
        self.preco = Entry(frame)
        self.preco.grid(row=2, column=1)

        # Botão para salvar produto
        self.botao_adicionar = ttk.Button(frame, text="Guardar Produto", command=self.add_produto)
        self.botao_adicionar.grid(row=3, columnspan=2, sticky=W+E)

        # Tabela
        style = ttk.Style()
        style.configure("mystyle.Treeview", highlightthickness=0, bd=0, font=('Calibri', 11))
        style.configure("mystyle.Treeview.Heading", font=('Calibri', 13, 'bold'))
        style.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})])
        # Botões de Eliminar e Editar
        botao_eliminar = ttk.Button(text='ELIMINAR', command = self.del_produto)
        botao_eliminar.grid(row=5, column=0, sticky=W + E)
        botao_editar = ttk.Button(text='EDITAR', command = self.edit_produto)
        botao_editar.grid(row=5, column=1, sticky=W + E)

        self.tabela = ttk.Treeview(height=10, columns=2, style="mystyle.Treeview")
        self.tabela.grid(row=4, column=0, columnspan=2)
        self.tabela.heading("#0", text="Nome", anchor=CENTER)
        self.tabela.heading("#1", text="Preço", anchor=CENTER)

        # Mensagem de feedback
        self.mensagem = Label(self.janela, text="", fg="red")
        self.mensagem.grid(row=4, column=0, columnspan=2, sticky=W + E)

        # Janela nova (editar produto)
        self.janela_editar = Toplevel()  # Criar uma janela à frente da principal
        self.janela_editar.title = "Editar Produto"  # Título da janela
        self.janela_editar.resizable(1, 1)  # Ativar o redimensionamento da janela.Para desativá - la: (0, 0)
        self.janela_editar.wm_iconbitmap('recursos/icon.ico')  # Ícone da janela
        titulo = Label(self.janela_editar, text='Edição de Produtos', font=('Calibri', 50, 'bold'))
        titulo.grid(column=0, row=0)
        # Criação do recipiente Frame da janela de Editar Produto
        frame_ep = LabelFrame(self.janela_editar, text="Editar o seguinte Produto") # frame_ep: Frame Editar Produto
        frame_ep.grid(row=1, column=0, columnspan=20, pady=20)

        self.get_produtos()

    def db_consulta(self, consulta, parametros=()):
        with sqlite3.connect(self.db) as con:
            cursor = con.cursor()
            resultado = cursor.execute(consulta, parametros)
            con.commit()
        return resultado

    def criar_tabela(self):
        sql = '''
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            preco REAL NOT NULL
        )
        '''
        self.db_consulta(sql)

    def get_produtos(self):
        # Limpa tabela
        registos_tabela = self.tabela.get_children()
        for linha in registos_tabela:
            self.tabela.delete(linha)
        # Busca e insere
        query = 'SELECT * FROM produtos ORDER BY nome DESC'
        registos_db = self.db_consulta(query)
        for linha in registos_db:
            self.tabela.insert('', 0, text=linha[1], values=(linha[2],))

    def validacao_nome(self):
        nome_introduzido_por_utilizador = self.nome.get()
        return len(nome_introduzido_por_utilizador) > 0
    def validacao_preco(self):
        preco_introduzido_por_utilizador = self.preco.get()
        return len(preco_introduzido_por_utilizador)

        if not preco:
            return False
        try:
            float(preco)
            return True
        except ValueError:
            return False

    def add_produto(self):
        nome = self.nome.get().strip()
        preco = self.preco.get().strip()

        if not self.validacao_nome() and not self.validacao_preco():
            messagebox.showerror("Erro", "O nome e o preço são obrigatórios.")
            return
        if not self.validacao_nome():
            messagebox.showerror("Erro", "O nome é obrigatório.")
            return
        if not self.validacao_preco():
            messagebox.showerror("Erro", "O preço é obrigatório e deve ser um número.")
            return

        try:
            preco_float = float(preco)
            query = 'INSERT INTO produtos (nome, preco) VALUES (?, ?)'
            self.db_consulta(query, (nome, preco_float))
            self.nome.delete(0, END)
            self.preco.delete(0, END)
            self.get_produtos()
            messagebox.showinfo("Sucesso", "Produto adicionado com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao adicionar produto: {e}")
            self.get_produtos()
    def del_produto(self):
        # Debug
        #print(self.tabela.item(self.tabela.selection()))
        #print(self.tabela.item(self.tabela.selection())['text'])
        #print(self.tabela.item(self.tabela.selection())['values'])
        #print(self.tabela.item(self.tabela.selection())['values'][0])

        self.mensagem['text'] = ''
        try:
            self.tabela.item(self.tabela.selection())['text'][0]
        except IndexError as e:
            self.mensagem['text'] = 'Selecione um produto para eliminar.'
            return

        self.mensagem['text'] = ''
        nome = self.tabela.item(self.tabela.selection())['text']
        query = 'DELETE FROM produtos WHERE nome = ?' #consulta SQL
        self.db_consulta(query, (nome,)) #executa a consulta
        self.mensagem['text'] = 'Produto {} eliminado com sucesso.' .format(nome)
        self.get_produtos()

    def edit_produto(self):
        self.mensagem['text'] = ''  # Mensagem inicialmente vazia
        try:
            self.tabela.item(self.tabela.selection())['text'][0]
        except IndexError as e:
            self.mensagem['text'] = 'Por favor, selecione um produto'
            return
        nome = self.tabela.item(self.tabela.selection())['text']
        old_preco = self.tabela.item(self.tabela.selection())['values'][0]  # O preço encontra - se dentro de uma lista
        # Cria uma nova janela para editar o produto
        self.janela_editar = Toplevel()  # Criar uma janela à frente da principal
        self.janela_editar.title = "Editar Produto"  # Titulo da janela
        self.janela_editar.resizable(1, 1)  # Ativar a redimensão da janela. Para desativá - la: (0, 0)
        self.janela_editar.wm_iconbitmap('recursos/icon.ico')  # Ícone da janela

if __name__ == '__main__':
    root = Tk()
    app = ProdutoApp(root)
    root.mainloop()
