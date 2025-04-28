
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout,QPushButton, QHBoxLayout,  QLabel, QListWidget, QMessageBox
import api
class Food_suggestions(QWidget):  
    def __init__(self):  
        super().__init__()  
        # Create layout for the main window  
        self.layout = QVBoxLayout()  
        self.buttons_layout=QHBoxLayout()
        # create the exercise lists  
        self.create_foods_sections() 
        #-------------------------- 

        self.setLayout(self.layout)  

    def connect_buttons(self,tabs):
        self.backbutton.clicked.connect(lambda : tabs.setCurrentIndex(0))

    def create_foods_sections(self,high_budget_foods,low_budget_foods):  
        # Create a QWidget for exercises  
        foods_widget = QWidget()  
        foods_layout = QHBoxLayout()  

         

        # Create sections for each budget category  
        self.create_exercise_section(foods_layout, "High Budget", high_budget_foods)  
        self.create_exercise_section(foods_layout, "Low Budget", low_budget_foods)  
        self.backbutton=QPushButton("",self)
        self.backbutton.setStyleSheet("background-color: transparent; border-radius: 0px; image: url(C:/Users/r/Contacts/Desktop/9thgrade_project/assets/back.png)")
        foods_widget.setLayout(foods_layout)  
        self.buttons_layout.addWidget(self.backbutton,1)
        self.buttons_layout.addWidget(QLabel(""),4)
        self.layout.addLayout(self.buttons_layout)
        self.layout.addWidget(foods_widget)  

    def create_exercise_section(self, layout, title, foods):  
        v_box = QVBoxLayout()  
        title_label = QLabel(title)  
        title_label.setStyleSheet("font-weight: bold; font-size: 18px;")  

        list_widget = QListWidget()  
        for food in foods:  
            list_widget.addItem(food[0])  
        
        explanation_label = QLabel("")  
        list_widget.itemClicked.connect(lambda item: self.update_explanation(item.text(), foods, explanation_label))  

        v_box.addWidget(title_label)  
        v_box.addWidget(list_widget)  
        v_box.addWidget(explanation_label)  
        
        layout.addLayout(v_box)  

    def update_explanation(self, food_name, foods, explanation_label):  
        for food in foods:  
            if food[0] == food_name:  
                explanation_label.setText(food[1])  
                break  
    def change_suggestions(self,p,c,f):
        low, high = api.get_food_suggestions(protein=p,fat=f,carbohydrates=c)
        h_t = self.dict_to_food_list(high)
        l_t = self.dict_to_food_list(low)
        self.create_foods_sections(self,h_t,l_t)
    def dict_to_food_list(self,food_dict):
        return [(food, explanation) for food, explanation in food_dict.items()]
