def passwordmanager():
    def addpassword():
        app = input("whats the name of your app: ")
        user = input("whats your username: ")
        password = input("whats the password of app: ")
        more = input("would you like to add more y/n: ")
        f = open((app), "x")
        f = open((app), "w")
        if more == "y":
            plus = input("what would you like to add: ")
            f.write((user) + " and " + (password) + " you added " + plus)
        else:
            f.write((user) + " and " + (password))
        f.close

    addpassword()


passwordmanager()
