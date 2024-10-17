import matplotlib.pyplot as plt

class Investment:
    def __init__(self, principal, rate, time):
        self.principal = principal
        self.rate = rate  
        self.time = time

    def calculate_compound_investment(self):
    
        return self.principal * (1 + self.rate) ** self.time


class Portfolio:
    def __init__(self):
        self.investments = []

    def add_investment(self, investment):
        self.investments.append(investment)

    def total_value(self):
        total = 0
        for investment in self.investments:
            total += investment.calculate_compound_investment()
        return total

    def simulate_investment(self, investment, years):
        values = []
        for year in range(1, years + 1):
            value = investment.principal * (1 + investment.rate) ** year
            values.append(value)
        return values

    def plot_investment_growth(self, values):
        plt.plot(values)
        plt.title('Crescimento do Investimento')
        plt.xlabel('Ano')
        plt.ylabel('Valor (R$)')
        plt.show()


def get_user_input():
    principal = float(input("Valor inicial: "))
    rate = float(input("Taxa de retorno anual (em decimal): "))
    time = int(input("Número de anos: "))
    return principal, rate, time

if __name__ == "__main__":
    principal, rate, time = get_user_input()
    investment = Investment(principal, rate, time)

    portfolio = Portfolio()
    portfolio.add_investment(investment)

    print(f"Valor total após {time} anos: R$ {portfolio.total_value():,.2f}")

  
    values = portfolio.simulate_investment(investment, time)
    portfolio.plot_investment_growth(values)
