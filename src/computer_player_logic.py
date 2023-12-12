lst = []

class Cookie:


    def __init__(self):
        self.count = 0

    def create(self):
        self.count += 1
        return(f"cookie {self.count}")


cookie = Cookie()

for elem in range(1, 100 + 1):
    lst.append(cookie.create())

print(lst)