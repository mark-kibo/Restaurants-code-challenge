class Customer:
    customers=[]
    def __init__(self, fname, lname, family_name):
        self.fname=fname
        self.lname=lname
        self.family_name=family_name
        Customer.customers.append({
            "first name" : self.fname,
            "last_name": self.lname,
            "family_name":self.family_name
        })

    def given_name(self, fname=None, lname=None):
        if fname:
            self.fname=fname
        if lname:
            self.lname=lname
        return self.fname + " " +self.lname
    

    def family_name(self, family_name=None):
        if family_name:
            self.family_name=family_name
        return self.family_name
    

    def full_name(self):
        return f"{self.fname} {self.lname} {self.given_name}" 
    

    @classmethod
    def all(cls):
        return cls.customers
    
    def restaurants(self):
        customer_restaurants=set()
        for review in Review.reviews:
            if review["customer"].given_name().split(" ")[0] == self.fname:
                customer_restaurants.add(review["restaurant"].name())

        return customer_restaurants
    
    def add_review(self, restaurant, rating):
       new_review=Review(self, restaurant, rating)
       return f"The following review was created {new_review}"

    def num_reviews(self):
        number_of_reviews=0
        for review in Review.reviews:
            if review["customer"].given_name().split(" ")[0] == self.fname:
                number_of_reviews += 1
        return number_of_reviews
    
    def find_by_name(self, name):
        for review in Review.reviews:
            if review["customer"].given_name() == name:
                return review["customer"].full_name() 

    def find_all_by_name(self, name):
        all_customers = []
        for review in Review.reviews:
            if review["customer"].given_name().__contains__(name):
                all_customers.append(review["customer"].full_name())

        return all_customers
    




    

class Restaurant:
    def __init__(self, name):
        if type(name) is not str:
            print("Name should be a string")
        else:
            self._name = name

    
    def name(self):
        return self._name
    
    def reviews(self):
        reviews=[]
        for review in Review.reviews:
            print(review["restaurant"].name()
             )
            if review["restaurant"].name() == self._name:
                reviews.append(review)
        return reviews
    
    def customers(self):
        restaurant_customers=set()
        for review in Review.reviews:
            if review["restaurant"].name() == self._name:
                restaurant_customers.add(review["customer"].given_name())

        return restaurant_customers
    
    def average_star_rating(self):
        rating_count=0
        rating_sum=0
        for review in Review.reviews:
            if review["restaurant"].name() == self._name:
               rating_count += 1
               rating_sum += int(review["rating"])
        

        return (rating_sum/rating_count)


class Review:
    reviews=[]
    def __init__(self, customer=None, restaurant=None, rating=None):
        if not isinstance(rating, int):
            print("Rating should be a number")
            self.rating = None  # Assign a default value (or handle it as needed)
        else:
            self.customer = customer
            self.restaurant = restaurant
            self.rating = rating
            Review.reviews.append({
                "customer": self.customer,
                "restaurant": self.restaurant,
                "rating": self.rating
            })


    def rating(self):
        return f"{self.restaurant} is rated {self.rating}"
    

    @classmethod
    def all(cls):
        return cls.reviews

    def customer(self):
        return self.customer
    
    def restaurant(self):
        return self.restaurant
    
# Create Customer objects
customer1 = Customer("John", "Doe", "Doe Family")
customer2 = Customer("Alice", "Smith", "Smith Family")
customer3 = Customer("Bob", "Johnson", "Johnson Family")
customer4 = Customer("Eva", "Williams", "Williams Family")
customer5 = Customer("Michael", "Brown", "Brown Family")

# Create Restaurant objects
restaurant1 = Restaurant("Restaurant A")
restaurant2 = Restaurant("Restaurant B")



# Create Review objects for each customer and restaurant
review1 = Review(customer1, restaurant1, 4)
review2 = Review(customer1, restaurant2, 5)
review3 = Review(customer2, restaurant1, 3)
review4 = Review(customer2, restaurant2, 4)
review5 = Review(customer3, restaurant1, 5)
review6 = Review(customer3, restaurant2, 3)
review7 = Review(customer4, restaurant1, 4)
review8 = Review(customer4, restaurant2, 2)
review9 = Review(customer5, restaurant1, 5)
review10 = Review(customer5, restaurant2, 1)

print("rest, ", restaurant1.reviews())

print("rest, ", customer1.restaurants())
print("rest, ", customer3.add_review(restaurant1, 5))
print("rest, ", customer1.num_reviews())
print("rest", customer2.find_by_name("Alice Smith"))
print('rest', customer1.find_all_by_name("John"))
# Call the all() function to retrieve customers and reviews
all_customers = Customer.all()
all_reviews = Review.all()


# Print the lists of customers and reviews
print(type(3))
for customer in all_customers:
    print(customer["first name"], customer["last_name"], customer["family_name"])

print("\nReviews:")
for review in all_reviews:
    print(review["customer"].given_name(), "reviewed", review["restaurant"].name(), "with a rating of", review["rating"])

