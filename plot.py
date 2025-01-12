import matplotlib.pyplot as plt

def plot_monthly_balance(balance: dict):
    months = sorted(balance.keys())
    values = [balance[month] for month in months]
    plt.figure(figsize=(10, 5))
    plt.bar(months, values, color='blue')
    plt.xlabel('Mês')
    plt.ylabel('Saldo Líquido (Receita - Despesa)')
    plt.title('Saldo Financeiro Mensal')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.show()

def plot_spends_by_category(spends_by_category: dict):
    categories = list(spends_by_category.keys())
    values = list(spends_by_category.values())
    plt.figure(figsize=(10, 5))
    plt.bar(categories, values, color='red')
    plt.xlabel('Categoria')
    plt.ylabel('Despesa total')
    plt.title('Total de gastos por categoria')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.show()


def plot_revenue_by_category(revenue_by_category: dict):
    categories = list(revenue_by_category.keys())
    values = list(revenue_by_category.values())
    plt.figure(figsize=(10, 5))
    plt.bar(categories, values, color='red')
    plt.xlabel('Categoria')
    plt.ylabel('Receita total')
    plt.title('Receita total por categoria')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.show()