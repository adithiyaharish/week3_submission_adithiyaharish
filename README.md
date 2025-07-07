# week3_submission_adithiyaharish
Week 3 submissions for Project Kratos - Electronics subsystem

# Question 1
Python node files for question 1:
  1. q1_publisher_node.py
  2. q1_subscriber_node.py

q1_publisher_node.py writes "Hello World !" to the topic /new at a rate of 15 Hz.
q2_subscriber_node.py displays the data published by the publisher node in the terminal.

# Question 2
Python node files for question 2:
  1. q2_s1_node.py
  2. q2_s2_node.py

q2_s1_node.py publishes "green" and "red" alternatively every 10 seconds to the terminal and prints it.
q2_s2_node.py publishes "red" and "green" alternatively evert 10 seconds to the terminal and prints it.

It is done alternatively by using a comparison operator and if else statements between both the topics.

# Question 4
Python node files for question 4:
q4_clock.py

q4_clock.py uses the std_msgs package to print the time in HH:MM:SS format published on the /clock topic

<img width="806" alt="Screenshot 2025-07-07 at 11 12 51 PM" src="https://github.com/user-attachments/assets/ac4ad44f-ae28-4bdc-b9c5-fa6347dbe878" />
