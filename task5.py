import datetime


# create Publication class
class Publication:
    # constructor
    def __init__(self, publication_type, text):
        self.publication_type = publication_type
        self.text = text

    # formatting() method will be overriden by subclasses
    def formatting(self):
        # method's implementation is empty
        pass


# Create News class that inherits from Publication class
class News(Publication):
    # Constructor
    def __init__(self, text, city):
        super().__init__("News", text)
        # initialize city
        self.city = city
        # datetime.datetime.now() takes current date and strftime() formats it
        self.publication_date = datetime.datetime.now().strftime("%m/%d/%Y %H.%M")

    # formatting() method publishes news by returning formatted string with certain parameters
    def formatting(self):
        return f"{self.publication_type} --------------------\n{self.text}\n{self.city}, {self.publication_date}"


# Create Advertising class that inherits Publication class
class Advertising(Publication):
    # Constructor
    def __init__(self, text, expiration_date):
        super().__init__("Advertising", text)
        self.expiration_date = datetime.datetime.strptime(expiration_date, "%m/%d/%Y")
        # Calculate the number of days left until the expiration_date and save it in days_left
        days_left = (self.expiration_date - datetime.datetime.now()).days
        # set days_left attribute
        self.days_left = days_left

    def formatting(self):
        return f"{self.publication_type} --------------\n{self.text}\nActual until: {self.expiration_date}, {self.days_left} days left"


# Create Motivator class that inherits Publication class
class Motivator(Publication):
    # Constructor
    def __init__(self, text, audience):
        super().__init__("Motivation", text)
        self.text = text
        self.audience = audience
        # datetime.datetime.now() takes current date and strftime() formats it
        self.publication_date = datetime.datetime.now().strftime("%m/%d/%Y")

    def formatting(self):
        return f"{self.publication_type} --------------------\n{self.text}\nEspecially for {self.audience}, " \
               f"{self.publication_date}"


# Create class UserInteraction that provides tool for user interaction to add different type of publications
class UserInteraction:
    # Constructor
    def __init__(self):
        self.publications = []

    def add_publication(self, publication_type, text, city=None, expiration_date=None, audience=None):
        publication = None
        if publication_type == "News":
            publication = News(text, city)
        elif publication_type == "Advertising":
            publication = Advertising(text, expiration_date)
        elif publication_type == "Motivation":
            publication = Motivator(text, audience)
        if publication:
            self.publish_record(publication)

    # add_news() method allows to add news
    def add_news(self):
        # prompt the user to enter news text and city
        text = input("Enter news text: ")
        city = input("Enter city: ")
        self.add_publication("News", text=text, city=city)

    # add_advertising() method allows to add advertising
    def add_advertising(self):
        # prompt the user to enter advertising text and expiration_date_input
        text = input("Enter advertising text: ")
        expiration_date = input("Enter expiration date (mm/dd/YYYY): ")
        self.add_publication("Advertising", text=text, expiration_date=expiration_date)

    # add_motivator() method allows to add motivation
    def add_motivator(self):
        # prompt the user to enter motivation text and audience
        text = input("Enter motivation: ")
        audience = input("Enter goal audience: ")
        self.add_publication("Motivation", text=text, audience=audience)

    # publish_record() method publishes records
    # record parameter is a publication
    def publish_record(self, record):
        # publications.append() - add publication to the list of publications
        self.publications.append(record)
        print("Record published successfully!")

    # save_publication() method saves the publications to a file named "publication.txt"
    def save_publication(self):
        # Write each publication record from the list of publications to the file
        # Open "publication.txt" file in write mode and associated it with the file object named 'file'
        # The with statement is used to ensure that the file is properly closed after its suite is executed
        with open("publication.txt", "a") as file:
            # run through each record in the publication list
            for record in self.publications:
                file.write(record.formatting() + "\n")
        self.publications = []
        print("Records saved to file successfully!")

    # save_to_db() method saves the publications entered by user to DB


if __name__ == '__main__':
    # Create object of UserInteraction class to interact with the UserInteraction methods and manage publications
    user_interaction = UserInteraction()

    # Display the menu options repeatedly until the user selects to exit by selecting option '5'
    while True:
        # Display the menu options to the user
        print("1. Add News")
        print("2. Add Advertising")
        print("3. Add Motivator")
        print("4. Save Publication to File")
        print("5. Exit")
        # Prompt the user to enter choice
        menu_point = input("Select publication type (1|2|3), Save Publication to file (4) or Exit (5): ")
        # Based on the user's input use if-elif-else statements to call
        # the corresponding methods of the UserInteraction class
        if menu_point == '1':
            publication_type = 'News'
            user_interaction.add_news()
        elif menu_point == '2':
            publication_type = 'Advertising'
            user_interaction.add_advertising()
        elif menu_point == '3':
            publication_type = 'Motivation'
            user_interaction.add_motivator()
        elif menu_point == '4':
            user_interaction.save_publication()
        elif menu_point == '5':
            break
        else:
            print("The entered data is incorrect. Please try again!")
