
# 🛍️ Gestor de Produtos com Tkinter e SQLite

![Python](https://img.shields.io/badge/Python-3.7+-blue?logo=python\&logoColor=white)
![License](https://img.shields.io/badge/Licença-MIT-green)
![Status](https://img.shields.io/badge/Status-Em%20Desenvolvimento-yellow)

Aplicação desktop simples para **gestão de produtos**, desenvolvida em **Python**, com interface gráfica usando **Tkinter** e banco de dados **SQLite**. Permite **registrar**, **editar** e **excluir produtos**, com nome e preço.

---

![image](https://github.com/user-attachments/assets/11601d3b-ad94-4192-a11b-ed5e881b12e6)


---

## ⚙️ Funcionalidades

* ✅ **Cadastrar** novos produtos
* 📝 **Editar** produtos existentes
* ❌ **Excluir** produtos
* 🔎 Visualizar todos os produtos em uma tabela
* 💾 Armazenamento local com SQLite
* 🖥️ Interface gráfica simples e funcional com Tkinter

---

## 📦 Requisitos

* 🐍 Python 3.7 ou superior
* Nenhuma biblioteca externa necessária (Tkinter e SQLite são nativos)

---

## ▶️ Como Executar

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/gestor-produtos-tkinter.git
cd gestor-produtos-tkinter
```

2. *(Opcional)* Crie um ambiente virtual:

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

3. Execute o app:

```bash
python app.py
```

---

## 📁 Estrutura do Projeto

```
gestor-produtos-tkinter/
├── app.py                  # Código principal
├── database/
│   └── produtos.db         # Criado automaticamente
├── recursos/
│   └── icon.ico            # Ícone da janela (opcional)
└── README.md
```

---

## 🛠️ Tecnologias Utilizadas

| Tecnologia  | Descrição                          |
| ----------- | ---------------------------------- |
| 🐍 Python   | Linguagem de programação principal |
| 🖼️ Tkinter | Interface gráfica                  |
| 💾 SQLite   | Banco de dados leve e local        |

---

## 📌 Observações

* O banco de dados é criado automaticamente na primeira execução.
* Se desejar personalizar o ícone da janela, basta substituir `recursos/icon.ico`.

---
