class EvilDatabase:
    cookies = []
    keyStrokes = ""
    locations = []

    def getCookies(self):
        return self.cookies

    def addCookie(self, post):
        self.cookies.append(post)

    def getKeystrokes(self):
        return self.keyStrokes

    def addKeystroke(self, keystroke):
        self.keyStrokes = self.keyStrokes + keystroke

    def addLocation(self, lat, long):
        self.locations = {lat, long}