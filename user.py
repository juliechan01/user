class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member  = False #rewards membership is False on default
        self.gold_card_points = 0
    
    def display_info(self):
        print("Name: ", self.first_name, self.last_name)
        print("Email: ", self.email)
        print("Age:", self.age)
        print("Rewards member?: ", self.is_rewards_member)
        print("Gold card points: ", self.gold_card_points)

    def enroll(self): #enroll in membership
        q = input('Would you like to enroll? Y or N\n')
        if q == "y":
            self.is_rewards_member = True
            self.gold_card_points = 200
            User.display_info(self)
        else:
            self.is_rewards_member = False
            self.gold_card_points = 0
            print("Are you sure? You're missing out on amazing deals and rewards!")
            User.display_info(self)

    def spend_points(self): #spending rewards points
        if self.is_rewards_member == True:
            r = input('How many points would you like to spend today?\n')
            r = int(r)
            if r <= self.gold_card_points:
                self.gold_card_points = self.gold_card_points - r
                print(f"You have {self.gold_card_points} points left.")
            else:
                r = input("Sorry but it looks like you don't have enough points! Please try again.\n")
                r= int(r)
                self.gold_card_points = self.gold_card_points - r
                print(f"You have {self.gold_card_points} points left.")
        else:
            print("Sorry, but it looks like you're not a member yet!")


user_julie = User("Julie", "Chan", "juliechan03@gmail.com", 24)
User.display_info(user_julie)
User.enroll(user_julie)
User.spend_points(user_julie)

user_andrew = User("Andrew", "Fowler", "drewtotha@outlook.com", 29)
User.display_info(user_andrew)
User.enroll(user_andrew)
User.spend_points(user_andrew)

user_leah = User("Leah", "Truong", "leahtruong@gmail.com", 24)
User.display_info(user_leah)
User.enroll(user_leah)
User.spend_points(user_leah)

print("••••••••••••••••••••••••")
User.display_info(user_julie)
User.display_info(user_andrew)
User.display_info(user_leah)