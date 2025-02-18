import sys  
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout  
from PyQt5.QtSql import QSqlQuery  
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas  
import matplotlib.pyplot as plt  
from users import current_user

class Chart_Widget(QWidget):  
    def __init__(self,database):  
        super().__init__()  
        self.weights = []  
        self.ideal_weights = []  
        self.dates = []  
        self.numbers = []
        self.database=database

        layout = QVBoxLayout()  
        self.figure, self.ax = plt.subplots()  
        self.canvas = FigureCanvas(self.figure)  
        layout.addWidget(self.canvas)  
        self.setLayout(layout) 
    def create_the_chart(self):
        data_id = current_user.logged_in_user.data_id   
        self.fetch_data(data_id) 
        self.plot_weights()   

    def fetch_data(self, data_id):  
        query_data = QSqlQuery()  
        query_data.prepare("""SELECT * FROM Data WHERE id = ? ORDER BY number""")  
        query_data.addBindValue(data_id)  
        query_data.exec_()  
    
        while query_data.next():  
            self.weights.append(query_data.value(1))
            self.ideal_weights.append(query_data.value(14))
            self.dates.append(query_data.value(6))
            self.numbers.append(query_data.value(9))
  

    def plot_weights(self):  
        self.ax.clear()  
        self.ax.plot(self.dates, self.weights, label="Weight Progress", marker='o' , color="Blue")  
        self.ax.plot(self.dates, self.ideal_weights, label="Ideal Weights", linestyle='--', marker='x' , color="Green")  
        self.ax.set_title('Weight Progress vs Ideal Weights')  
        self.ax.set_xlabel('Dates')  
        self.ax.set_ylabel('Weight (kg)')  
        self.ax.legend(loc="lower center")  

        self.ax.grid()  

        self.canvas.draw()
