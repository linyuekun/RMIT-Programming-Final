# SUKHUM BOONDECHARAK (S3940976)
# The Highest Part Attempted: HD LEVEL

# # PROBLEMS:

# 1. Not sure what requirement 2 (Adjusting the rate) in HD level would be like
# I was able to set the new rate, but once I was done setting it, it's the end of the program
# If I re-enter the command line again, it reset the program
# So, I'm quite sure I was wrong on this, but really had no clue what to do about it

# 2. I feel like the class design could be better than what I've done
# But since I kept doing step by step, from PASS to CREDIT, CREDIT to DI, and DI to HD
# Modifying the entire code is quite scary for me, so I kept going with what I had
# I ended up getting quite a long messy chunk of code, which is practically not prefer by me
# If I, as a beginner, still dislike it, most programmers probably don't like it, either

# # COURSE SUGGESTIONS
# 1. Fibonacci formular was a too-complicated example to start with loop for a student with no background
# 2. Would be nice to see how the code should be like after the assignment
# 3. Mini assignment (no mark) would also be a good idea to familiarise the actual assignments

# # PERSONAL MESSAGE
# I was wrong earlier thinking that coding was not a very creative activity
# Only to found out that I really had to use lots of imaginations
# I've tried, but unfortunately, this is my best effort at this point in time

# Not sure if there's an extended amount of time because I wrote on the last submission
# But thank you for extending the time
# It meant a lot to me

# And even if it's a headache for me, sometimes, I still found coding fun, much fun
# At least compared to any other courses I've been thorough this semester
# This is my favourite course so far

# Have a nice summer!

####################################################################################################################
####################################################################################################################

# import sys to be used with sys.argv later for command line arguments
import sys


# EXCEPTIONS
class NoRecord(Exception):
    pass

class InvalidUsage(Exception):
    pass

class InvalidPrice(Exception):
    pass

class InvalidServiceIDR(Exception):
    pass

class InvalidServiceIDS(Exception):
    pass


# RECORDS
# Class that consists of lists
# Also contains methods to read specific formatted files
# Also contains methods to display information of the lists
class Records:

    def __init__(self):
        self.list_of_username = []
        self.list_of_users = []
        self.list_of_sid = []
        self.list_of_services = []
        self.users_usage = {}

    # A method to read record file with a specific format
    def read_records(self, file_name):

        file = open(file_name, "r")
        line = file.readline()

        # Declare a variable to check for an empty file
        empty_file = True

        while line:

            # If line is not None, it enters the loop
            # change the boolean for this available to the opposite
            empty_file = False
            # Because username and usages are in the same line
            # Extract the first index as a username
            # Then add it to list of usernames
            field_from_line = line.strip().split(",")
            username = field_from_line[0].strip()
            if username not in self.list_of_username:
                self.list_of_username.append(username)

            # Declare a dictionary for this specific username
            # This will then be another layer of dictionary in users_usage
            self.users_usage[username] = {}

            # Start counting from index 1 onward for a pair of service ID and usage
            # SID will be the first count
            # Usage will be the count next to the current SID
            # Add the specific service ID into list of service IDs
            # Also add usage to the list declared earlier
            # At the end, skip 2 index for another pair os service ID and usage
            i = 1
            while i < len(field_from_line):
                sid = field_from_line[i].strip()

                # Check if service ID is in a valid format
                if sid[0] != "S" or not sid[1:].isnumeric():
                    raise InvalidServiceIDR("\nWrong format for service ID detected in your records file!\n"
                                            "Service ID must begin with \"S\" and the rest should be numbers.\n"
                                            "Please check your records file and try again.\n")

                if sid not in self.list_of_sid:
                    self.list_of_sid.append(sid)

                usage = field_from_line[i + 1]

                # Check if the usage value is valid
                if float(usage) < 0:
                    raise InvalidUsage("\nNegative number(s) detected in the usage!\n"
                                       "Please check your records file and try again.\n")

                self.users_usage[username][sid] = float(usage)
                i += 2

            line = file.readline()
        # The file is empty if not entering the loop, then raise an exception
        if empty_file:
            raise NoRecord("\nNo records are available!\n")

    # A method to display information from record file
    def display_records(self):

        # Declare a number of users, services, and total services used by every user
        # These numbers will be count as they're being printed
        total_users = 0
        total_services = 0
        used_services = 0

        print("\nRECORDS")
        print("-" * 111)
        print("{:<20}".format("Usernames"), end="")

        # Loop and print every item in the list
        # Also count the number of services as it's being printed
        for sid in self.list_of_sid:
            print("{:>15}".format(sid), end="")
            total_services += 1
        print("")
        print("-" * 111)

        # Loop and print every item in the list
        # Also count the number of users as it's being printed
        # end="" is applied to avoid entering a new line
        for username in self.users_usage:
            print("{:<20}".format(username), end="")
            total_users += 1

            # Loop and print every usage in the dictionary according to each user with corresponding SID
            # Also count the number of total used times as it's being printed
            # The services not used by each user will be printed as "--"
            for sid in self.list_of_sid:
                if sid in self.users_usage[username]:
                    print("{:>15.1f}".format(self.users_usage[username][sid]), end="")
                    used_services += 1
                else:
                    print("{:>15}".format("--"), end="")
            print("")
        print("\nRECORDS SUMMARY")

        # Compute a usage percentage from the counts
        usage_percentage = (used_services / (total_users * total_services)) * 100

        print("There are {} users and {} services.".format(total_users, total_services))
        print("The usage percentage is {:.2f}%\n".format(usage_percentage))

    # A method to export records information to a file
    def print_records(self):

        # Declare a number of users, services, and total services used by every user
        # These numbers will be count as they're being printed
        total_users = 0
        total_services = 0
        used_services = 0

        # Declare a file to be written on
        # And print as in display_records() but onto the file
        with open("reports.txt", "w") as report:
            print("\nRECORDS", file=report)
            print("-" * 111, file=report)
            print("{:<20}".format("Usernames"), end="", file=report)

            # Loop and print every item in the list
            # Also count the number of services as it's being printed
            for sid in self.list_of_sid:
                print("{:>15}".format(sid), end="", file=report)
                total_services += 1
            print("", file=report)
            print("-" * 111, file=report)

            # Loop and print every item in the list
            # Also count the number of users as it's being printed
            # end="" is applied to avoid entering a new line
            for username in self.users_usage:
                print("{:<20}".format(username), end="", file=report)
                total_users += 1

                # Loop and print every usage in the dictionary according to each user with corresponding SID
                # Also count the number of total used times as it's being printed
                # The services not used by each user will be printed as "--"
                for sid in self.list_of_sid:
                    if sid in self.users_usage[username]:
                        print("{:>15.1f}".format(self.users_usage[username][sid]), end="", file=report)
                        used_services += 1
                    else:
                        print("{:>15}".format("--"), end="", file=report)
                print("", file=report)
            print("\nRECORDS SUMMARY", file=report)

            # Compute a usage percentage from the counts
            usage_percentage = (used_services / (total_users * total_services)) * 100

            print("There are {} users and {} services.".format(total_users, total_services), file=report)
            print("The usage percentage is {:.2f}%\n".format(usage_percentage), file=report)

    # A method to read service file with a specific format
    def read_services(self, file_name):
        file = open(file_name, "r")
        line = file.readline()
        while line:

            # Each line is split and assigned to a variable
            field_from_line = line.strip().split(",")
            service_id = field_from_line[0].strip()

            # Check if service ID is in a valid format
            if service_id[0] != "S" or not service_id[1:].isnumeric():
                raise InvalidServiceIDS("\nWrong format for service ID detected in your services file!\n"
                                        "Service ID must begin with \"S\" and the rest should be numbers.\n"
                                        "Please check your services file and try again.\n")

            service_name = field_from_line[1].strip()
            service_type = field_from_line[2].strip()
            service_price = field_from_line[3].strip()

            # Check if the service_price value is valid
            if float(service_price) < 0:
                raise InvalidPrice("\nNegative number(s) detected in the price!\n"
                                   "Please check your services file and try again.\n")

            # Declare a new variable and make it an object according to service type
            new_service = None
            if service_type == "Standard":
                new_service = StandardService(SID=service_id,
                                              name=service_name,
                                              price=float(service_price))

            elif service_type == "Premium":
                new_service = PremiumService(SID=service_id,
                                             name=service_name,
                                             price=float(service_price))

            # Loop into users_usage to check usage for each user
            # Count the number of user according to each service
            # Also count the usage according to each service
            for username in self.users_usage:
                user_usage = self.users_usage[username]
                for sid in user_usage:
                    if new_service.SID == sid:
                        new_service.no_users += 1
                        new_service.total_usages += user_usage[sid]

            # Add the object to the list of services
            self.list_of_services.append(new_service)
            line = file.readline()

    # A method to display information from service file
    def display_services(self):

        print("\nSERVICE INFORMATION")
        print("-" * 96)
        print("{:<15} {:<15} {:<15} {:>15} {:>15} {:>15}".format("ServiceID",
                                                                 "Name",
                                                                 "Type",
                                                                 "Price",
                                                                 "Nuser",
                                                                 "Usage"))
        print("-" * 96)

        # Sort the object in the list according to total_usage from high to low
        # Then print each service according to their format
        for service in sorted(self.list_of_services, key=lambda service: service.total_usages, reverse=True):
            service.display_info()

        print("\nSERVICE SUMMARY")

        # Compute the most popular service by comparing the number of users using the service
        most_pop = self.list_of_services[0]
        for target in self.list_of_services:
            if target.no_users > most_pop.no_users:
                most_pop = target

        # Print SID and name of the service from the calculation above
        print("The most popular service is {} ({}).".format(most_pop.SID,
                                                            most_pop.name))

        # Compute the most expensive service by comparing the price of each service
        most_expensive = self.list_of_services[0]
        for target in self.list_of_services:
            if target.price > most_expensive.price:
                most_expensive = target

        # Print SID and name of the service from the calculation above
        print("The most expensive service (per unit) is {} ({}).\n".format(most_expensive.SID,
                                                                           most_expensive.name))

    # A method to export services information to a file
    def print_services(self):

        # Declare a file to be written on
        # And print as in display_services() but onto the file
        with open("reports.txt", "a") as report:
            print("\nSERVICE INFORMATION", file=report)
            print("-" * 96, file=report)
            print("{:<15} {:<15} {:<15} {:>15} {:>15} {:>15}".format("ServiceID",
                                                                     "Name",
                                                                     "Type",
                                                                     "Price",
                                                                     "Nuser",
                                                                     "Usage"), file=report)
            print("-" * 96, file=report)

            # Sort the object in the list according to total_usage from high to low
            # Then print each service according to their format
            for service in sorted(self.list_of_services, key=lambda service: service.total_usages, reverse=True):
                if service.type == "Standard":
                    print("{:<15} {:<15} {:<15} {:>15.2f} {:>15} {:>15.1f}".format(service.SID,
                                                                                   service.name,
                                                                                   service.type,
                                                                                   service.price,
                                                                                   service.no_users,
                                                                                   service.total_usages), file=report)
                elif service.type == "Premium":
                    print("{:<15} {:<15} {:<15} {:<7.2f}/{:>7.2f} {:>15} {:>15.1f}".format(service.SID,
                                                                                           service.name,
                                                                                           service.type,
                                                                                           service.price,
                                                                                           service.second_price,
                                                                                           service.no_users,
                                                                                           service.total_usages), file=report)

            print("\nSERVICE SUMMARY", file=report)

            # Compute the most popular service by comparing the number of users using the service
            most_pop = self.list_of_services[0]
            for target in self.list_of_services:
                if target.no_users > most_pop.no_users:
                    most_pop = target

            # Print SID and name of the service from the calculation above
            print("The most popular service is {} ({}).".format(most_pop.SID,
                                                                most_pop.name), file=report)

            # Compute the most expensive service by comparing the price of each service
            most_expensive = self.list_of_services[0]
            for target in self.list_of_services:
                if target.price > most_expensive.price:
                    most_expensive = target

            # Print SID and name of the service from the calculation above
            print("The most expensive service (per unit) is {} ({}).\n".format(most_expensive.SID,
                                                                               most_expensive.name), file=report)

    # A method to read user file with a specific format
    def read_users(self, file_name):
        file = open(file_name, "r")
        line = file.readline()
        while line:

            # Each line is split and assigned to a variable
            field_from_line = line.strip().split(",")
            user_username = field_from_line[0].strip()
            user_firstname = field_from_line[1].strip()
            user_lastname = field_from_line[2].strip()
            user_type = (field_from_line[3].strip())

            # Declare a new variable and make it an object according to user type
            new_user = None
            if user_type == "Free":
                new_user = FreeUser(username=user_username,
                                    firstname=user_firstname,
                                    lastname=user_lastname)

            elif user_type == "Personal":
                new_user = PersonalUser(username=user_username,
                                        firstname=user_firstname,
                                        lastname=user_lastname)

            elif user_type == "Corporate":
                new_user = CorporateUser(username=user_username,
                                         firstname=user_firstname,
                                         lastname=user_lastname)

            # Add the object to the list of users
            self.list_of_users.append(new_user)
            line = file.readline()

        # Loop into the list of users to list all the users
        for user in self.list_of_users:
            if user.username in self.users_usage:
                username = user.username

                # Loop into the users_usage to list all the usages according to each user
                for sid in self.users_usage[username]:
                    usage = self.users_usage[username][sid]

                    # Loop into the list of services to calculate cost according to user type and service price
                    for service in self.list_of_services:
                        if service.SID == sid:

                            # 3 types of user and 2 types of service, the variation is 6 in total
                            # for each scenario, compute the cost according to user type
                            # Add the computed cost to spending for each user
                            # Also count the number of service for each type of service being computed
                            if user.type == "Free" and service.type == "Standard":
                                service_cost = usage * service.price
                                user.spending += service_cost
                                user.s_service += 1
                            elif user.type == "Free" and service.type == "Premium":
                                service_cost = usage * service.price
                                user.spending += service_cost
                                user.p_service += 1
                            elif user.type == "Personal" and service.type == "Standard":
                                service_cost = usage * 0
                                user.spending += service_cost
                                user.s_service += 1
                            elif user.type == "Personal" and service.type == "Premium":
                                service_cost = usage * service.price
                                user.spending += service_cost
                                user.p_service += 1
                            elif user.type == "Corporate" and service.type == "Standard":
                                service_cost = usage * 0
                                user.spending += service_cost
                                user.s_service += 1
                            elif user.type == "Corporate" and service.type == "Premium":
                                service_cost = usage * service.second_price
                                user.spending += service_cost
                                user.p_service += 1

    # A method to display information from user file
    def display_users(self):

        print("\nUSER INFORMATION")
        print("-" * 91)
        print("{:<20} {:<15} {:<15} {:<10} {:>10} {:>15}".format("Username",
                                                                 "First name",
                                                                 "Last name",
                                                                 "Type",
                                                                 "Spent",
                                                                 "Nservice"))
        print("-" * 91)

        # Sort the object in the list according to spending from high to low
        # Then print each user according to their format
        for user in sorted(self.list_of_users, key=lambda user: user.spending, reverse=True):
            user.display_info()

        print("\nUSER SUMMARY")

        # Compute the most valuable user by comparing the spending
        most_valuable = self.list_of_users[0]
        for target in self.list_of_users:
            if target.spending > most_valuable.spending:
                most_valuable = target

        # Print username of the user from the calculation above
        print("The most valuable user is {}.".format(most_valuable.username))

        # Compute the service being used the most by comparing the sums of numbers of each type
        most_service_used = self.list_of_users[0]
        for target in self.list_of_users:
            if target.s_service + target.p_service > most_service_used.s_service + most_service_used.p_service:
                most_service_used = target

        # Print username of the user from the calculation above
        print("The user used the most services is {}.\n".format(most_service_used.username))

    # A method to export users information to a file
    def print_users(self):

        # Declare a file to be written on
        # And print as in display_users() but onto the file
        with open("reports.txt", "a") as report:
            print("\nUSER INFORMATION", file=report)
            print("-" * 91, file=report)
            print("{:<20} {:<15} {:<15} {:<10} {:>10} {:>15}".format("Username",
                                                                     "First name",
                                                                     "Last name",
                                                                     "Type",
                                                                     "Spent",
                                                                     "Nservice"), file=report)
            print("-" * 91, file=report)

            # Sort the object in the list according to spending from high to low
            # Then print each user according to their format
            for user in sorted(self.list_of_users, key=lambda user: user.spending, reverse=True):
                if user.type == "Free":
                    print("{:<20} {:<15} {:<15} {:<10} {:>10.2f} {:>9}{:>} +{:>2}{}".format(user.username,
                                                                                            user.firstname,
                                                                                            user.lastname,
                                                                                            user.type,
                                                                                            user.spending,
                                                                                            user.s_service,
                                                                                            "S",
                                                                                            user.p_service,
                                                                                            "P"), file=report)
                elif user.type == "Personal":
                    print("{:<20} {:<15} {:<15} {:<10} {:>10.2f} {:>9}{:>} +{:>2}{}".format(user.username,
                                                                                            user.firstname,
                                                                                            user.lastname,
                                                                                            user.type,
                                                                                            user.spending,
                                                                                            user.s_service,
                                                                                            "S",
                                                                                            user.p_service,
                                                                                            "P"), file=report)
                elif user.type == "Corporate":
                    print("{:<20} {:<15} {:<15} {:<10} {:>10.2f} {:>9}{:>} +{:>2}{}".format(user.username,
                                                                                            user.firstname,
                                                                                            user.lastname,
                                                                                            user.type,
                                                                                            user.spending,
                                                                                            user.s_service,
                                                                                            "S",
                                                                                            user.p_service,
                                                                                            "P"), file=report)

            print("\nUSER SUMMARY", file=report)

            # Compute the most valuable user by comparing the spending
            most_valuable = self.list_of_users[0]
            for target in self.list_of_users:
                if target.spending > most_valuable.spending:
                    most_valuable = target

            # Print username of the user from the calculation above
            print("The most valuable user is {}.".format(most_valuable.username), file=report)

            # Compute the service being used the most by comparing the sums of numbers of each type
            most_service_used = self.list_of_users[0]
            for target in self.list_of_users:
                if target.s_service + target.p_service > most_service_used.s_service + most_service_used.p_service:
                    most_service_used = target

            # Print username of the user from the calculation above
            print("The user used the most services is {}.\n".format(most_service_used.username), file=report)


# USERS
# Contains spending and each type of service count
# Has 3 child classes
class User:

    def __init__(self, username):
        self.__username = username
        self.spending = 0.0
        self.s_service = 0
        self.p_service = 0

    @property
    def username(self):
        return self.__username


# User class as a parent class
# Inherit attributes from the parent
# Contains firstname, lastname, and type
# Also contain a method to display object attributes
class FreeUser(User):
    def __init__(self, username, firstname, lastname):
        super().__init__(username)
        self.__firstname = firstname
        self.__lastname = lastname
        self.__type = "Free"

    @property
    def firstname(self):
        return self.__firstname

    @property
    def lastname(self):
        return self.__lastname

    @property
    def type(self):
        return self.__type

    # A method to display object attributes for FreeUser class
    def display_info(self):
        print("{:<20} {:<15} {:<15} {:<10} {:>10.2f} {:>9}{:>} +{:>2}{}".format(self.username,
                                                                                self.firstname,
                                                                                self.lastname,
                                                                                self.type,
                                                                                self.spending,
                                                                                self.s_service,
                                                                                "S",
                                                                                self.p_service,
                                                                                "P"))


# User class as a parent class
# Inherit attributes from the parent
# Contains firstname, lastname, and type
# Also contain a method to display object attributes
class PersonalUser(User):
    def __init__(self, username, firstname, lastname):
        super().__init__(username)
        self.__firstname = firstname
        self.__lastname = lastname
        self.__type = "Personal"

    @property
    def firstname(self):
        return self.__firstname

    @property
    def lastname(self):
        return self.__lastname

    @property
    def type(self):
        return self.__type

    # A method to display object attributes for PersonalUser class
    def display_info(self):
        print("{:<20} {:<15} {:<15} {:<10} {:>10.2f} {:>9}{:>} +{:>2}{}".format(self.username,
                                                                                self.firstname,
                                                                                self.lastname,
                                                                                self.type,
                                                                                self.spending,
                                                                                self.s_service,
                                                                                "S",
                                                                                self.p_service,
                                                                                "P"))


# User class as a parent class
# Inherit attributes from the parent
# Contains firstname, lastname, and type
# Also contain a method to display object attributes
class CorporateUser(User):
    def __init__(self, username, firstname, lastname):
        super().__init__(username)
        self.__firstname = firstname
        self.__lastname = lastname
        self.__type = "Corporate"

    @property
    def firstname(self):
        return self.__firstname

    @property
    def lastname(self):
        return self.__lastname

    @property
    def type(self):
        return self.__type

    # A method to display object attributes for CorporateUser class
    def display_info(self):
        print("{:<20} {:<15} {:<15} {:<10} {:>10.2f} {:>9}{:>} +{:>2}{}".format(self.username,
                                                                                self.firstname,
                                                                                self.lastname,
                                                                                self.type,
                                                                                self.spending,
                                                                                self.s_service,
                                                                                "S",
                                                                                self.p_service,
                                                                                "P"))


# SERVICES
# Contains number of users and total usages
# Has 2 child classes
class Service:
    def __init__(self, SID):
        self.__SID = SID
        self.no_users = 0
        self.total_usages = 0.0

    @property
    def SID(self):
        return self.__SID


# Service class as a parent class
# Inherit attributes from the parent
# Contains name, price, and type
# Also contain a method to display object attributes
class StandardService(Service):
    def __init__(self, SID, name, price):
        super().__init__(SID)
        self.__name = name
        self.__price = price
        self.__type = "Standard"

    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price

    @property
    def type(self):
        return self.__type

    # A method to display object attributes for StandardService class
    def display_info(self):
        print("{:<15} {:<15} {:<15} {:>15.2f} {:>15} {:>15.1f}".format(self.SID,
                                                                       self.name,
                                                                       self.type,
                                                                       self.price,
                                                                       self.no_users,
                                                                       self.total_usages))


# Service class as a parent class
# Inherit attributes from the parent
# Contains name, price, second_price, and type
# Contains rate as a class attribute with the default value
# Second_price is calculated using this rate
# Also contain a method to display object attributes
class PremiumService(Service):
    rate = 0.8

    def __init__(self, SID, name, price):
        super().__init__(SID)
        self.__name = name
        self.__price = price
        self.__second_price = self.__price * self.rate
        self.__type = "Premium"

    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price

    @property
    def second_price(self):
        return self.__second_price

    @property
    def type(self):
        return self.__type

    @staticmethod
    def set_rate(rate):
        PremiumService.rate = rate

    # A method to display object attributes for PremiumService class
    # Prices printing from this class will consist of 2 prices, separated by "/"
    def display_info(self):
        print("{:<15} {:<15} {:<15} {:<7.2f}/{:>7.2f} {:>15} {:>15.1f}".format(self.SID,
                                                                               self.name,
                                                                               self.type,
                                                                               self.price,
                                                                               self.second_price,
                                                                               self.no_users,
                                                                               self.total_usages))


# MAIN
# The main operation for the program
# Contains an object with Records class
# Also contain a method to run a program
class Main:
    def __init__(self):
        self.record = Records()

    def run(self):

        # Count the number of command line arguments
        count_argv = len(sys.argv)

        # Apply the execution according to the number
        # The count is 1, missing every file
        # no_file method is executed, throwing an error message
        if count_argv == 1:
            self.no_file()

        # The count is 2, missing service and user file
        # Read the record file and provide options for the user to choose
        # If 1 is chosen, display_records method is executed, showing the records
        # If 0 is chosen, exit method is executed, exiting the program with a farewell message
        elif count_argv == 2:
            record_file = sys.argv[1]

            # If the file exists and is not empty
            try:
                self.record.read_records(record_file)

            # If records file is empty, display a message that no records are available
            # Return None to exit the program right away
            except NoRecord as e:
                print(e)
                return None

            # If no records file matched, let the user know and quit
            except FileNotFoundError:
                print("\nNo records file named \"" + record_file + "\" in your directory.\n"
                                                                   "Please try again.\n")
                return None

            # If a usage value is invalid, let the user know and quit
            except InvalidUsage as iu:
                print(iu)
                return None

            # If service ID is in a wrong format, let the user know and quit
            except InvalidServiceIDR as isir:
                print(isir)
                return None

            # If try is successful, continue
            self.pattern_one()
            option = input("Choose one option:\n")
            if option == "1":
                self.record.display_records()
            if option == "0":
                self.exit()
            if option == "x":
                self.record.print_records()
                print("\nYour report has been exported!\n")

        # The count is 3, missing user file
        # Read the record and service file, and provide options for the user to choose
        # If 1 is chosen, display_records method is executed, showing the records
        # If 2 is chosen, display_services method is executed, showing the service information
        # If 0 is chosen, exit method is executed, exiting the program with a farewell message
        elif count_argv == 3:
            record_file = sys.argv[1]

            # If the file exists and is not empty
            try:
                self.record.read_records(record_file)

            # If records file is empty, display a message that no records are available
            # Return None to exit the program right away
            except NoRecord as e:
                print(e)
                return None

            # If no records file matched, let the user know and quit
            except FileNotFoundError:
                print("\nNo records file named \"" + record_file + "\" in your directory.\n"
                                                                   "Please try again.\n")
                return None

            # If a usage value is invalid, let the user know and quit
            except InvalidUsage as iu:
                print(iu)
                return None

            # If service ID is in a wrong format, let the user know and quit
            except InvalidServiceIDR as isir:
                print(isir)
                return None

            # If try is successful, continue
            service_file = sys.argv[2]

            # If the file exists
            try:
                self.record.read_services(service_file)

            # If no services file matched, let the user know and quit
            except FileNotFoundError:
                print("\nNo services file named \"" + service_file + "\" in your directory.\n"
                                                                     "Please try again.\n")
                return None

            # If a service_price value is invalid, let the user know and quit
            except InvalidPrice as ip:
                print(ip)
                return None

            # If service ID is in a wrong format, let the user know and quit
            except InvalidServiceIDS as isis:
                print(isis)
                return None

            # If try is successful, continue
            self.pattern_two()
            option = input("Choose one option:\n")
            if option == "1":
                self.record.display_records()
            if option == "2":
                self.record.display_services()
            if option == "0":
                self.exit()
            if option == "x":
                print("\nYour report has been exported!\n")
                self.record.print_records()
                self.record.print_services()
            if option == "y":

                # Declare a variable to check if the input is in a valid format
                valid_input = False
                while not valid_input:
                    try:
                        new_rate = input("\nPlease enter a new rate:\n")
                        if float(new_rate) <= 0:
                            print("\nRate cannot be zero or negative!")
                        else:

                            PremiumService.set_rate(new_rate)

                            # Only when the input is valid, exit the loop
                            valid_input = True
                            print("\nNew rate has been applied!\n")

                    # This is to cover when the input is non-numeric
                    except ValueError:
                        print("\nRate should only be in numeric format!")

        # The count is 4, no file missing
        # Read the record, service, and user file, and provide options for the user to choose
        # If 1 is chosen, display_records method is executed, showing the records
        # If 2 is chosen, display_services method is executed, showing the service information
        # If 3 is chosen, display_users method is executed, showing the user information
        # If 0 is chosen, exit method is executed, exiting the program with a farewell message
        elif count_argv == 4:
            record_file = sys.argv[1]

            # If the file exists and is not empty
            try:
                self.record.read_records(record_file)

            # If records file is empty, display a message that no records are available
            # Return None to exit the program right away
            except NoRecord as e:
                print(e)
                return None

            # If no records file matched, let the user know and quit
            except FileNotFoundError:
                print("\nNo records file named \"" + record_file + "\" in your directory.\n"
                                                                   "Please try again.\n")
                return None

            # If a usage value is invalid, let the user know and quit
            except InvalidUsage as iu:
                print(iu)
                return None

            # If service ID is in a wrong format, let the user know and quit
            except InvalidServiceIDR as isir:
                print(isir)
                return None

            # If try is successful, continue
            service_file = sys.argv[2]

            # If the file exists
            try:
                self.record.read_services(service_file)

            # If no services file matched, let the user know and quit
            except FileNotFoundError:
                print("\nNo services file named \"" + service_file + "\" in your directory.\n"
                                                                     "Please try again.\n")
                return None

            # If a service_price value is invalid, let the user know and quit
            except InvalidPrice as ip:
                print(ip)
                return None

            # If service ID is in a wrong format, let the user know and quit
            except InvalidServiceIDS as isis:
                print(isis)
                return None

            # If try is successful, continue
            user_file = sys.argv[3]

            # If the file exists
            try:
                self.record.read_users(user_file)

            # If no users file matched, let the user know and quit
            except FileNotFoundError:
                print("\nNo services file named \"" + user_file + "\" in your directory.\n"
                                                                  "Please try again.\n")
                return None

            self.pattern_three()
            option = input("Choose one option:\n")
            if option == "1":
                self.record.display_records()
            if option == "2":
                self.record.display_services()
            if option == "3":
                self.record.display_users()
            if option == "0":
                self.exit()
            if option == "x":
                print("\nYour report has been exported!\n")
                self.record.print_records()
                self.record.print_services()
                self.record.print_users()
            if option == "y":

                # Declare a variable to check if the input is in a valid format
                valid_input = False
                while not valid_input:
                    try:
                        new_rate = input("\nPlease enter a new rate:\n")
                        if float(new_rate) <= 0:
                            print("\nRate cannot be zero or negative!")
                        else:

                            PremiumService.set_rate(new_rate)

                            # Only when the input is valid, exit the loop
                            valid_input = True
                            print("\nNew rate has been applied!\n")

                    # This is to cover when the input is non-numeric
                    except ValueError:
                        print("\nRate should only be in numeric format!")

    # Header option for scenario 1 if not all files are missing
    @staticmethod
    def pattern_one():
        print("\nWelcome to the RMIT Service Provider Dashboard!")
        print("#" * 47)
        print("You can choose from the following options:")
        print("1: Display records")
        print("0: Exit the program")
        print("x: Export data to file")
        print("#" * 47)

    # Header option for scenario 2 if not all files are missing
    @staticmethod
    def pattern_two():
        print("\nWelcome to the RMIT Service Provider Dashboard!")
        print("#" * 47)
        print("You can choose from the following options:")
        print("1: Display records")
        print("2: Display services")
        print("0: Exit the program")
        print("x: Export data to file")
        print("y: Adjust the premium service price rate")
        print("#" * 47)

    # Header option for scenario 3 if not all files are missing
    @staticmethod
    def pattern_three():
        print("\nWelcome to the RMIT Service Provider Dashboard!")
        print("#" * 47)
        print("You can choose from the following options:")
        print("1: Display records")
        print("2: Display services")
        print("3: Display users")
        print("0: Exit the program")
        print("x: Export data to file")
        print("y: Adjust the premium service price rate")
        print("#" * 47)

    # An error message when all files are missing
    @staticmethod
    def no_file():
        print("\n[Usage:] python my_record.py <records file>\n")

    # A farewell message before exiting the program
    @staticmethod
    def exit():
        print("\nGood bye! Have a good day!\n")


test = Main()
test.run()
