class Generator:
    def __init__(self):
        self.active = {}    # username -> set of used numbers
        self.free = {}      # username -> list of freed numbers
        self.counter = {}   # username -> next new number to assign
        

    def create(self, username):
        # Initialize structures if new user
        if username not in self.active:
            self.active[username] = set()
            self.free[username] = []
            self.counter[username] = 1

        # If there are freed numbers, reuse the smallest one
        if self.free[username]:
            num = min(self.free[username])
            self.free[username].remove(num)
        else:
            num = self.counter[username]
            self.counter[username] += 1

        self.active[username].add(num)
        print(self.active, self.free, self.counter)
        return f"{username}{num}"

    def delete(self, username):
        if username in self.active and self.active[username]:
            # remove the smallest active number
            num = min(self.active[username])
            self.active[username].remove(num)
            self.free[username].append(num)
            print(self.active, self.free, self.counter)
            return f"{username}{num}"
        return None


# Example usage
generator = Generator()
result = []

queries=['create alex','create alex','delete alex','create alex','create john']

for query in queries:
    action=query.split(' ')[0]
    name=query.split(' ')[1]
    if action == 'create':
        result.append(generator.create(name))   

    if action == 'delete':
        generator.delete(name)                

print(result)  # ['alex1', 'alex2', 'alex1', 'john1']

# result:
# {'alex': {1, 2}} {'alex': []} {'alex': 3}
# {'alex': {2}} {'alex': [1]} {'alex': 3}
# {'alex': {1, 2}} {'alex': []} {'alex': 3}
# {'alex': {1, 2}, 'john': {1}} {'alex': [], 'john': []} {'alex': 3, 'john': 2}
# ['alex1', 'alex2', 'alex1', 'john1']