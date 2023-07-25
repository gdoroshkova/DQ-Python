import datetime

# create Publication class
class Publication:
    # constructor, publication_type is required - it's news, advertising or motivation
    # text and publication_date are initialized as empty string
    def __init__(self, publication_type):
        self.publication_type = publication_type
        self.text = ""
        self.publication_date = ""

    # publish() method will be overriden by subclasses
    def publish(self):
        # method's implementation is empty
        pass

# Create News class that inherits from Publication class
class News(Publication):
    # Constructor initializes publication_type variable
    def __init__(self):
        super().__init__("News")
        # initialize city
        self.city = ""


    # news_data() method takes text, city as parameters
    def news_data(self, text, city):
        # set test, city, publication_date attributes
        self.text = text
        self.city = city
        # datetime.datetime.now() takes current date and strftime() formats it
        self.publication_date = datetime.datetime.now().strftime("%m/%d/%Y %H.%M")

    # publish() method publishes news by returning formatted string with certain parameters
    def publish(self):
        return f"{self.publication_type} --------------------\n{self.text}\n{self.city}, {self.publication_date}"

# Create Advertising class that inherits Publication class
class Advertising(Publication):
    # Constructor initializes publication_type attribute by calling the Constructor of parent class
    def __init__(self):
        super().__init__("Private Ad")
        # Initialize expiration_date as an empty string
        self.expiration_date = ""

    # adv_data() method takes text and expiration_date_input as parameters
    def adv_data(self, text, expiration_date_input):
        self.text = text
        # Convert expiration_date_input to datetime object and set it as the expiration_date
        self.expiration_date = datetime.datetime.strptime(expiration_date_input, "%m/%d/%Y")
        # Calculate the number of days left until the expiration_date and save it in days_left
        days_left = (self.expiration_date - datetime.datetime.now()).days
        # set publication_date attribute
        self.publication_date = expiration_date_input
        # set days_left attribute
        self.days_left = days_left

    # publish() method publishes advertising by returning formatted string with certain parameters
    def publish(self):
        return f"{self.publication_type} --------------\n{self.text}\nActual until: {self.publication_date}, {self.days_left} days left"


# Create Motivator class that inherits Publication class
class Motivator(Publication):
    # Constructor initializes publication_type attribute by calling the Constructor of parent class
    def __init__(self):
        super().__init__("Motivation")
        # Initialize audience
        self.audience = 'all'

    # motivation_data() method takes text and audience as parameters
    def motivation_data(self, text, audience):
        self.text = text
        self.audience = audience
        # set publication_date
        # datetime.datetime.now() takes current date and strftime() formats it
        self.publication_date = datetime.datetime.now().strftime("%m/%d/%Y")

    # publish() method publishes motivation by returning formatted string with certain parameters
    def publish(self):
        return f"{self.publication_type} --------------------\n{self.text}\nEspecially for {self.audience}, {self.publication_date}"

# Create class UserInteraction that provides tool for user interaction to add different type of publications
class UserInteraction:
    # Constructor initializes publications as an empty list for saving publications
    def __init__(self):
        self.publications = []

    # add_news() method allows to add news
    def add_news(self):
        # create object of News class
        news = News()
        # prompt the user to enter news text and city
        text = input("Enter news text: ")
        city = input("Enter city: ")
        # call news_data() to set news data
        news.news_data(text, city)
        # publish news by calling publish_record() method from UserInteraction class
        self.publish_record(news)

    # add_advertising() method allows to add advertising
    def add_advertising(self):
        # create Advertising object
        ad = Advertising()
        # prompt the user to enter advertising text and expiration_date_input
        text = input("Enter advertising text: ")
        expiration_date_input = input("Enter expiration date (mm/dd/YYYY): ")
        # call adv_data() to set advertising data
        ad.adv_data(text, expiration_date_input)
        # publish advertising by calling publish_record() method from UserInteraction class
        self.publish_record(ad)

    # add_motivator() method allows to add motivation
    def add_motivator(self):
        # create Motivator object
        motivation = Motivator()
        # prompt the user to enter motivation text and audience
        text = input("Enter motivation: ")
        audience = input("Enter goal audience: ")
        # call motivation_data() to set motivation data
        motivation.motivation_data(text, audience)
        # publish motivation by calling publish_record() method from UserInteraction class
        self.publish_record(motivation)

    # publish_record() method publishes records
    # record parameter is a publication
    def publish_record(self, record):
        # record.publish() - call publish() method that returns publication of each publication object
        # publications.append() - add publication to the list of publications
        self.publications.append(record.publish())
        print("Record published successfully!")


    # save_publication() method saves the publications to a file named "publication.txt"
    def save_publication(self):
        # Write each publication record from the list of publications to the file
        # Open "publication.txt" file in write mode and associated it with the file object named 'file'
        # The with statement is used to ensure that the file is properly closed after its suite is executed
        with open("publication.txt", "w") as file:
            # run through each record in the publication list
            for record in self.publications:
                file.write(record + "\n")
        print("Records saved to file successfully!")

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
    menu_point = input("Select publication type (1|2|3), Save Publication (4) or Exit (5): ")
    # Based on the user's input use if-elif-else statements to call the corresponding methods of the UserInteraction class
    if menu_point == '1':
        user_interaction.add_news()
    elif menu_point == '2':
        user_interaction.add_advertising()
    elif menu_point == '3':
        user_interaction.add_motivator()
    elif menu_point == '4':
        user_interaction.save_publication()
    elif menu_point == '5':
        break
    else:
        print("The entered data is incorrect. Please try again!")


