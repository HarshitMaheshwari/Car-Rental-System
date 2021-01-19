
Steps to run the Code:

1.	 Before running the code, it is important understand the following points:
a.	Install all the necessary libraries used in this program. Libraries used are: datetime, random and unittest.
b.	I have used Pycharm community version as the IDE to write and test the program.
c.	Python 3.8 is used for the whole program.
d.	All the configuration files are added with the program.
2.	 Run the main.py file.
3.	 You will get a Welcome message and the count for the total number of cars available in the system.
4.	 After the welcome message, there will be a prompt to ask the user if they want to rent a car or return a previously rented car.
5.	 If the user chooses to rent a car, then a prompt will ask for the category of car that they are interested in.
6.	 After selecting an appropriate category, A list of all the available cars in that category will be displayed with all the details of the cars like price, carID, name. And a prompt will ask the ID of the car that you want to rent.
7.	 After entering the car ID, it will ask to enter the customer ID. There are two customer IDs available. 
•	Customer ID for General customer: 100
•	Customer ID for VIP customer: 101
8.	 A message will be displayed. After which the system will ask for the booking start date in a specified.
9.	 After entering the booking start date, it will ask for the booking end date.
10.	 A booking confirmation prompt will ask for the confirmation for the selected dates.
11.	 After confirming the dates, a final booking confirmation prompt will appear.
12.	 Confirming this prints the confirmation message.


To return a previously rented car:


13. It will ask for the customer ID. There are two customer IDs available. Customer ID for General customer: 100; Customer ID for VIP customer: 101.
14. After confirming the customer ID, Bill gets displayed. 
15. A prompt asks for the final payment. And after payment, the system starts from the start. While displaying the total number of cars available.



Limitations of the system:

1. There is no database used for this application. So if you want to test the car return part, then first rent a car and then without terminating the program, return the car. 
2. You can rent multiple cars but the return can only be done if the program is not terminated after renting.
3. At the final return, program asks for the payment of the rented car. That does not have any real payment method involved.
4. There are only two customers involved. One as a VIP customer, that is, gets some extra benefits as they have company loyalty card and the other as a General customer because they do not get extra benefits as they do not have a card.
