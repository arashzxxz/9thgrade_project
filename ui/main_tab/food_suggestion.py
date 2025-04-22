
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout,QPushButton, QHBoxLayout,  QLabel, QListWidget, QMessageBox

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

    def create_foods_sections(self):  
        # Create a QWidget for exercises  
        foods_widget = QWidget()  
        foods_layout = QHBoxLayout()  

        # High Budget foods  
        high_budget_foods = [("food #1", "Explanation for food #1."),  
                                  ("food #2", "Explanation for food #2."),  
                                  ("food #3", "Explanation for food #3."),  
                                  ("food #4", "Explanation for food #4.")]  
        
        low_budget_foods = [("food #5", "Explanation for food #5."),  
                                ("food #6", "Explanation for food #6."),  
                                ("food #7", "Explanation for food #7."),  
                                ("food #8", "Explanation for food #8.")]  

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
