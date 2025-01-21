
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout,  QLabel, QListWidget, QMessageBox

class Exercise_suggestions(QWidget):  
    def __init__(self):  
        super().__init__()  
        # Create layout for the main window  
        self.layout = QVBoxLayout()  
        # create the exercise lists  
        self.create_exercise_sections() 
        #-------------------------- 

        self.setLayout(self.layout)  

    def create_exercise_sections(self):  
        # Create a QWidget for exercises  
        exercise_widget = QWidget()  
        exercise_layout = QHBoxLayout()  

        # High Budget Exercises  
        high_budget_exercises = [("Exercise #1", "Explanation for Exercise #1."),  
                                  ("Exercise #2", "Explanation for Exercise #2."),  
                                  ("Exercise #3", "Explanation for Exercise #3."),  
                                  ("Exercise #4", "Explanation for Exercise #4.")]  
        
        low_budget_exercises = [("Exercise #5", "Explanation for Exercise #5."),  
                                ("Exercise #6", "Explanation for Exercise #6."),  
                                ("Exercise #7", "Explanation for Exercise #7."),  
                                ("Exercise #8", "Explanation for Exercise #8.")]  

        # Create sections for each budget category  
        self.create_exercise_section(exercise_layout, "High Budget", high_budget_exercises)  
        self.create_exercise_section(exercise_layout, "Low Budget", low_budget_exercises)  

        exercise_widget.setLayout(exercise_layout)  
        self.layout.addWidget(exercise_widget)  

    def create_exercise_section(self, layout, title, exercises):  
        v_box = QVBoxLayout()  
        title_label = QLabel(title)  
        title_label.setStyleSheet("font-weight: bold; font-size: 18px;")  

        list_widget = QListWidget()  
        for exercise in exercises:  
            list_widget.addItem(exercise[0])  
        
        explanation_label = QLabel("")  
        list_widget.itemClicked.connect(lambda item: self.update_explanation(item.text(), exercises, explanation_label))  

        v_box.addWidget(title_label)  
        v_box.addWidget(list_widget)  
        v_box.addWidget(explanation_label)  
        
        layout.addLayout(v_box)  

    def update_explanation(self, exercise_name, exercises, explanation_label):  
        for exercise in exercises:  
            if exercise[0] == exercise_name:  
                explanation_label.setText(exercise[1])  
                break  
