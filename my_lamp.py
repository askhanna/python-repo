class Lamp:

    def plug_in(self):
        self.is_on = False

    def toggle(self):
        if self.is_on == False:
            self.is_on = True
        else:
            self.is_on = False
