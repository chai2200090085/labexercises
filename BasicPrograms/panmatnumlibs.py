#example1

#example2
# import matplotlib.pyplot as plt
# import numpy as np
# y=np.array([35,25,25,15])
# mylabels=["DBMS","PYTHON","OS","MP"]
# plt.pie(y,labels=mylabels,startangle=90)
# plt.show()

#example3
# import matplotlib.pyplot as plt
# import numpy as np
# y=np.array([35,25,25,15])
# mylabels=["DBMS","PYTHON","OS","MP"]
# plt.pie(y,labels=mylabels,startangle=90)
# plt.show()

#Example 4
# import numpy as np
# # Creating a NumPy array
# arr1 = np.array([1, 2, 3, 4, 5])
# arr2 = np.array([[1, 2, 3], [4, 5, 6]])
#
# # Basic operations on arrays
# sum_arr1 = np.sum(arr1)
# mean_arr2 = np.mean(arr2)
#
# print("Sum of 1D Array:", sum_arr1)
# print("Mean of 2D Array:", mean_arr2)
# # Element-wise operations
# squared_arr1 = np.square(arr1)
# sqrt_arr2 = np.sqrt(arr2)
#
# print("Squared elements of arr1:", squared_arr1)
# print("Square root of arr2:", sqrt_arr2)

#Example 5
# import matplotlib.pyplot as plt
# import numpy as np
# regnum = ['101', '102', '103']
# categories = ["DBMS", "Python", "OS", "MP"]
# values = np.array([
#     [35, 25, 25, 15],  # Values for category "DBMS"
#     [20, 30, 15, 35],  # Values for category "Python"
#     [10, 40, 20, 30],  # Values for category "OS"
# ])
# colors = ['blue', 'green', 'orange', 'red']
# # Plot area for each registration number and category
# for i, reg in enumerate(regnum):
#     plt.fill_between(categories, 0, values[i], label=f'Registration {reg}', color=colors[i], alpha=0.7)
# # Add labels and title
# plt.xlabel("Categories")
# plt.ylabel("Values")
# plt.title("Area Plot with Different Colors")
# plt.legend()
# plt.show()

import pandas as pd
import matplotlib.pyplot as plt
def read_csv_file(file_path):
    df = pd.read_csv(file_path)
    return df
def generate_graph(data_frame):
    x_values = data_frame['REGNUM']
    y_columns = data_frame.columns[1:]
    colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']
    for i,column in enumerate(y_columns):
        y_values = data_frame[column]
        plt.plot(x_values, y_values, marker='o', linestyle='-', label=column, color = colors[i])
    # plt.plot(x_values, y_values, marker='o', linestyle='-', color=colors)
    plt.xlabel('X-axis Label')
    plt.ylabel('Y-axis Label')
    plt.title('CSV Data Plot')
    plt.grid(True)
    plt.legend()
    plt.savefig("a1.png")
    plt.show()

if __name__ == "__main__":
    file_path = "data.csv"
    data_frame = read_csv_file(file_path)
    generate_graph(data_frame)









































# class Student:
#     def init(self, student_id, student_name):
#         self.student_id = student_id
#         self.student_name = student_name
#
#     def add_student_class(self, student_class):
#         self.student_class = student_class
#
#     def display_attributes(self):
#         print("Student ID:", self.student_id)
#         print("Student Name:", self.student_name)
#         print("Student Class:", self.student_class)
#
#     def remove_student_name(self):
#         del self.student_name
#
# # Creating an instance of the Student class
# student_instance = Student(student_id=1, student_name="John Doe")
#
# # Displaying attributes before adding student_class
# print("Before adding student_class:")
# student_instance.display_attributes()
#
# # Adding the student_class attribute
# student_instance.add_student_class(student_class="Class 10A")
#
# # Displaying attributes after adding student_class
# print("\nAfter adding student_class:")
# student_instance.display_attributes()
#
# # Removing the student_name attribute
# student_instance.remove_student_name()
#
# # Displaying attributes after removing student_name
# print("\nAfter removing student_name:")
# student_instance.display_attributes()