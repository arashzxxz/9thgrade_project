import sys  
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QProgressBar  ,QComboBox
from PyQt5.QtSql import QSqlQuery  
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas  
import matplotlib.pyplot as plt  
from users import current_user  
from calculations.calculations import calculate_ideal_weight, calculate_bmi  
class CircleChartWidget(QWidget):  
    def __init__(self):  
        super().__init__()  
        self.layout = QVBoxLayout()  
        self.figure, self.ax = plt.subplots(figsize=(5, 5))  
        self.canvas = FigureCanvas(self.figure)  
        self.layout.addWidget(self.canvas)  
        self.setLayout(self.layout)  

    def plot_circle(self, date, carb_value, protein_value, fat_value):  
        self.ax.clear()  
        self.ax.plot(date, carb_value, 'o', markersize=10, color='orange', label='Carbs')  
        self.ax.plot(date, protein_value, 'o', markersize=10, color='red', label='Protein')  
        self.ax.plot(date, fat_value, 'o', markersize=10, color='purple', label='Fat')  
        
        self.ax.set_title('Selected Nutritional Data Point')  
        self.ax.set_xlabel('Date')  
        self.ax.set_ylabel('Grams')  
        self.ax.legend(loc="upper right")  
        self.ax.grid()  
        self.canvas.draw()  
class Chart_Widget(QWidget):  
    def __init__(self, database):  
        super().__init__()  
        
        self.database = database  
        self.cw = CircleChartWidget()
        self.weights = []  
        self.ideal_weights = []  
        self.dates = []  
        self.numbers = []  
        self.carbohydrates = []  
        self.protein = []  
        self.fat = []  
        self.date_selector = QComboBox(self)

        layout = QVBoxLayout()  

        self.figure, self.ax = plt.subplots(2, 1, figsize=(10, 10))  
        self.canvas = FigureCanvas(self.figure)  
        layout.addWidget(self.canvas)  
        layout.addWidget(self.date_selector) 
        layout.addWidget(self.cw) 
        self.wbar = QProgressBar(self)  
        #layout.addWidget(self.wbar)  

        self.setLayout(layout)  

    def create_bar(self):  
        self.wbar.setRange(0, 100)  
        weight = int(current_user.logged_in_user.weight)  
        ideal_weight = calculate_ideal_weight(  
            current_user.logged_in_user.age,  
            current_user.logged_in_user.gender,  
            current_user.logged_in_user.height,  
            calculate_bmi(current_user.logged_in_user.height, current_user.logged_in_user.weight)  
        )  

        if ideal_weight > 0:  
            progress_percentage = (weight / ideal_weight) * 100  
            self.wbar.setValue(min(progress_percentage, 100))  
        else:  
            self.wbar.setValue(0)  

    def create_the_chart(self):  
        data_id = current_user.logged_in_user.data_id   
        self.fetch_data(data_id)   
        self.plot_weights()   
        self.plot_nutrition() 
        self.populate_date_selector()
        self.highlight_data_point() 
        #self.cw.plot_circle(self.date_selector.currentText,self.carbohydrates[self.date_selector.currentIndex()],self.protein[self.date_selector.currentIndex()],self.fat[self.date_selector.currentIndex()])

    def fetch_data(self, data_id):  
        query_data = QSqlQuery()  
        query_data.prepare("SELECT * FROM Data WHERE id = ? ORDER BY number")  
        query_data.addBindValue(data_id)  
        query_data.exec_()  
    
        while query_data.next():  
            self.weights.append(query_data.value(1))  
            self.ideal_weights.append(query_data.value(14))  
            self.dates.append(query_data.value(6))  
            self.numbers.append(query_data.value(9))  
            self.carbohydrates.append(query_data.value(16))  
            self.protein.append(query_data.value(17))  
            self.fat.append(query_data.value(18))  

    def plot_weights(self):  
        self.ax[0].clear()  
        self.ax[0].plot(self.dates, self.weights, label="Weight Progress", marker='o', color="blue")  
        self.ax[0].plot(self.dates, self.ideal_weights, label="Ideal Weights", linestyle='--', marker='x', color="green")  
        self.ax[0].set_title('Weight Progress vs Ideal Weights')  
        self.ax[0].set_xlabel('Dates')  
        self.ax[0].set_ylabel('Weight (kg)')  
        self.ax[0].legend(loc="upper right")  
        self.ax[0].grid()  

    def plot_nutrition(self):  
        self.ax[1].clear()  
        self.ax[1].plot(self.dates, self.carbohydrates, label="Carbohydrates", marker='o', color="orange")  
        self.ax[1].plot(self.dates, self.protein, label="Protein", marker='o', color="red")  
        self.ax[1].plot(self.dates, self.fat, label="Fat", marker='o', color="purple")  
        self.ax[1].set_title('Nutritional Intake Over Time')  
        self.ax[1].set_xlabel('Dates')  
        self.ax[1].set_ylabel('Grams')  
        self.ax[1].legend(loc="upper right")  
        self.ax[1].grid()  
        self.canvas.draw()  
    def populate_date_selector(self):  
        self.date_selector.clear()  
        self.date_selector.addItems(self.dates)  

    def highlight_data_point(self):  
        selected_index = self.date_selector.currentIndex()  
        self.plot_nutrition()  # Replot nutrition to refresh existing plots  

        # Highlight the selected data point  
        if selected_index >= 0:  
            carb_value = self.carbohydrates[selected_index]  
            protein_value = self.protein[selected_index]  
            fat_value = self.fat[selected_index]  
            date = self.dates[selected_index]  

            # Plot a circle marker at the selected index for carbohydrates, protein, and fat  
            self.ax[1].plot(date, carb_value, 'o', markersize=10, color='orange', label='Selected Carbs')  
            self.ax[1].plot(date, protein_value, 'o', markersize=10, color='red', label='Selected Protein')  
            self.ax[1].plot(date, fat_value, 'o', markersize=10, color='purple', label='Selected Fat')  

            # Draw this point on top of existing lines  
            self.ax[1].legend(loc="upper right")  

        self.canvas.draw()  