## Curso de Engenharia de Software - UniEVANGÉLICA
## Disciplina de Programação Web
## Dev: Lucas Alberto Pereira Davi
##

import tkinter as tk
from tkinter import ttk, messagebox
from dataclasses import dataclass
from typing import List

# Modelos de dados usando dataclasses
@dataclass
class User:
    username: str
    password: str

@dataclass
class Product:
    name: str
    price: float

@dataclass
class ServiceOrder:
    description: str
    user: User
    product: Product

# Armazenamento em memória para usuários, produtos e ordens de serviço
users: List[User] = []
products: List[Product] = []
service_orders: List[ServiceOrder] = []

# Função para adicionar um usuário
def add_user(username: str, password: str):
    """Adiciona um novo usuário à lista de usuários."""
    users.append(User(username, password))

# Função para adicionar um produto
def add_product(name: str, price: float):
    """Adiciona um novo produto à lista de produtos."""
    products.append(Product(name, price))

# Função para adicionar uma ordem de serviço
def add_service_order(description: str, user: User, product: Product):
    """Adiciona uma nova ordem de serviço à lista de ordens de serviço."""
    service_orders.append(ServiceOrder(description, user, product))

# Função para obter um usuário pelo nome de usuário
def get_user(username: str) -> User:
    """Retorna um usuário pelo nome de usuário."""
    for user in users:
        if user.username == username:
            return user
    return None

# Função para obter um produto pelo nome
def get_product(name: str) -> Product:
    """Retorna um produto pelo nome."""
    for product in products:
        if product.name == name:
            return product
    return None

# Aplicação Tkinter
class App(tk.Tk):
    def __init__(self):
        """Inicializa a aplicação e cria as abas."""
        super().__init__()

        self.title("Gerenciamento de Entidades")
        self.geometry("600x400")

        # Controle de abas
        tab_control = ttk.Notebook(self)
        self.tab_users = ttk.Frame(tab_control)
        self.tab_products = ttk.Frame(tab_control)
        self.tab_service_orders = ttk.Frame(tab_control)

        tab_control.add(self.tab_users, text="Usuários")
        tab_control.add(self.tab_products, text="Produtos")
        tab_control.add(self.tab_service_orders, text="Ordens de Serviço")
        tab_control.pack(expand=1, fill="both")

        # Configuração das abas
        self.setup_users_tab()
        self.setup_products_tab()
        self.setup_service_orders_tab()

    def setup_users_tab(self):
        """Configura a aba de usuários."""
        frame = ttk.Frame(self.tab_users)
        frame.pack(padx=10, pady=10, fill='x')

        tk.Label(frame, text="Usuário:").grid(row=0, column=0, sticky='e')
        self.entry_user_username = ttk.Entry(frame)
        self.entry_user_username.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(frame, text="Senha:").grid(row=1, column=0, sticky='e')
        self.entry_user_password = ttk.Entry(frame, show='*')
        self.entry_user_password.grid(row=1, column=1, padx=5, pady=5)

        self.btn_add_user = ttk.Button(frame, text="Adicionar Usuário", command=self.add_user)
        self.btn_add_user.grid(row=2, columnspan=2, pady=10)

        self.users_list = tk.Listbox(self.tab_users)
        self.users_list.pack(padx=10, pady=10, fill='both', expand=True)

    def add_user(self):
        """Adiciona um usuário ao clicar no botão."""
        username = self.entry_user_username.get()
        password = self.entry_user_password.get()
        if username and password:
            add_user(username, password)
            self.users_list.insert(tk.END, username)
            self.entry_user_username.delete(0, tk.END)
            self.entry_user_password.delete(0, tk.END)
        else:
            messagebox.showerror("Erro", "Nome de usuário e senha são obrigatórios!")

    def setup_products_tab(self):
        """Configura a aba de produtos."""
        frame = ttk.Frame(self.tab_products)
        frame.pack(padx=10, pady=10, fill='x')

        tk.Label(frame, text="Nome do Produto:").grid(row=0, column=0, sticky='e')
        self.entry_product_name = ttk.Entry(frame)
        self.entry_product_name.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(frame, text="Preço:").grid(row=1, column=0, sticky='e')
        self.entry_product_price = ttk.Entry(frame)
        self.entry_product_price.grid(row=1, column=1, padx=5, pady=5)

        self.btn_add_product = ttk.Button(frame, text="Adicionar Produto", command=self.add_product)
        self.btn_add_product.grid(row=2, columnspan=2, pady=10)

        self.products_list = tk.Listbox(self.tab_products)
        self.products_list.pack(padx=10, pady=10, fill='both', expand=True)

    def add_product(self):
        """Adiciona um produto ao clicar no botão."""
        name = self.entry_product_name.get()
        price = self.entry_product_price.get()
        try:
            price = float(price)
            if name:
                add_product(name, price)
                self.products_list.insert(tk.END, name)
                self.entry_product_name.delete(0, tk.END)
                self.entry_product_price.delete(0, tk.END)
            else:
                messagebox.showerror("Erro", "Nome do produto é obrigatório!")
        except ValueError:
            messagebox.showerror("Erro", "Preço deve ser um número!")

    def setup_service_orders_tab(self):
        """Configura a aba de ordens de serviço."""
        frame = ttk.Frame(self.tab_service_orders)
        frame.pack(padx=10, pady=10, fill='x')

        tk.Label(frame, text="Descrição:").grid(row=0, column=0, sticky='e')
        self.entry_service_description = ttk.Entry(frame)
        self.entry_service_description.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(frame, text="Usuário:").grid(row=1, column=0, sticky='e')
        self.entry_service_user = ttk.Entry(frame)
        self.entry_service_user.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(frame, text="Produto:").grid(row=2, column=0, sticky='e')
        self.entry_service_product = ttk.Entry(frame)
        self.entry_service_product.grid(row=2, column=1, padx=5, pady=5)

        self.btn_add_service_order = ttk.Button(frame, text="Adicionar Ordem de Serviço", command=self.add_service_order)
        self.btn_add_service_order.grid(row=3, columnspan=2, pady=10)

        self.service_orders_list = tk.Listbox(self.tab_service_orders)
        self.service_orders_list.pack(padx=10, pady=10, fill='both', expand=True)

    def add_service_order(self):
        """Adiciona uma ordem de serviço ao clicar no botão."""
        description = self.entry_service_description.get()
        username = self.entry_service_user.get()
        product_name = self.entry_service_product.get()
        
        user = get_user(username)
        product = get_product(product_name)
        
        if description and user and product:
            add_service_order(description, user, product)
            self.service_orders_list.insert(tk.END, description)
            self.entry_service_description.delete(0, tk.END)
            self.entry_service_user.delete(0, tk.END)
            self.entry_service_product.delete(0, tk.END)
        else:
            messagebox.showerror("Erro", "Todos os campos são obrigatórios e devem corresponder a usuários e produtos existentes!")

if __name__ == "__main__":
    app = App()
    app.mainloop()
