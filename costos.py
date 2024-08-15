#Pracitca de pograma para calcular costos,  ingresos etc.
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

hours: int = 13
clients_hora: int = 2
copy: float= 200.0
impression_Color: float= 400.0
impression_BN: float = 300.0
scanner:  float = 300.0
day: int = 24
internet: float  = 63000.00
paper: float = 17000.00


class Balance:

    def __init__(self):
        pass

    def income_diaries_services(self):
        self.quanity_copies = int(input("Ingrese la cantidad de copias: "))
        self.quanity_impression_color = int(input("Ingrese la cantidad de impresiones a color: "))
        self.quanity_impression_BN  = int(input("Ingrese la cantidad de impresiones a B/N: "))
        self.quanity_scanners = int(input("Ingrese la cantidad de scanners\n: "))

        self.copies = self.quanity_copies
        self.impression_color = self.quanity_impression_color
        self.impression_bn = self.quanity_impression_BN
        self.scanners = self.quanity_scanners

        self.income_diaries_service = ((self.copies * copy) + (self.impression_color * impression_Color) + (self.impression_bn * impression_BN) + (self.scanners * scanner)) 

        print(f"Los ingresos diarios de servicios son {self.income_diaries_service} pesos\n ") 


    def total_income_month(self):

        self.total_incomes_month = self.income_diaries_service *day

        print(f"Total de ingresos mensuales  es {self.total_incomes_month} pesos\n.")

    def total_expenses_month(self):

        self.total_expen_month = paper + internet
        
        print(f"Total de egresos mensuales es {self.total_expen_month} pesos\n")

    def gross_total(self):

        self.total_gross__month = self.total_incomes_month + self.total_expen_month

        print(f"Total bruto es igual a {self.total_gross__month} pesos\n")

    def net_total(self):

        self.net_total_ = self.total_incomes_month - self.total_expen_month

        print(f"Total neto es igual a {self.net_total_}")

    def graphisc(self):
        self.ejex = ["Total ingresos", "Total egresos", "Total bruto", "Total neto"]
        self.ejey = [self.total_incomes_month, self.total_expen_month, self.total_gross__month, self.net_total_]

        fig, ax = plt.subplots()
        ax.set_ylabel("Balance")
        ax.set_title("Total ingresos y egresos")

        plt.bar(self.ejex, self.ejey)
        plt.savefig("grafico.png")
        plt.show()

local = Balance()
local.income_diaries_services()
local.total_income_month()
local.total_expenses_month()
local.gross_total()
local.net_total()
#local.graphisc()