class Employee:
    raise_amt = 1.05
    def __init__(self, first, last, title, salary, email):
        self.first = first
        self.last = last
        self.title = title
        self.salary = salary
        self.email = email
        
    def get_raise(self):
        self.salary = int(self.salary * 1.05)
        print(f"Congratulations, you received a raise, and your salary is now {self.salary}!")
        
emp1 = Employee('Michael', 'Wormley', 'Engineer', 100000, 'mworm@compan.y')
emp1.get_raise()

class Sales(Employee):
    def __init__(self, first, last, title, salary, email, phone):
        super().__init__(first, last, title, salary, email)
        self.phone = phone
                         
    def send(self):
        print(f"Dear customer, Thank you for your interest in our product. Please let me know if you have any questions. My email is {self.email} or my phone number is {self.phone}. Thanks, {first} {last}")
    
emp2 = Sales('John', 'Jacob', 'Sales Manager', 150000, 'email@smail.com', 81555555)
