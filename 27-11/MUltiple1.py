
class Camera:
    def take_photo(self):
        print("Photo taken!")

class Phone:
    def make_call(self):
        print("Calling...")

class SmartPhone(Camera, Phone):
    def browse_internet(self):
        print("Browsing the internet...")

# Usage
sp = SmartPhone()
sp.take_photo()      # From Camera
sp.make_call()       # From Phone
sp.browse_internet() # From SmartPhone
