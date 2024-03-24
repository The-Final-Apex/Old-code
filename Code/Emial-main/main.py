import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
import smtplib

file = open("username.txt", "r")
usrnam = file.read()
file.close()

file = open("username.txt", "w")
file.write("u dumb")
file.close()


file = open("psswd.txt", "r")
psswd = file.read()
file.close()

file = open("psswd.txt", "w")
file.write("why r u even doing this bro.")
file.close()

class Compose_Email(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        header_label = Label(text='Enter Email content', size_hint=(1, 0.1))
        layout.add_widget(header_label)

        to = TextInput(hint_text='To',  size_hint=(1, 0.1))
        layout.add_widget(to)

        sub = TextInput(hint_text='Subject',  size_hint=(1, 0.1))
        layout.add_widget(sub)

        bod = TextInput(hint_text='Body', size_hint=(2, 0.5))
        layout.add_widget(bod)
        return layout

    def send(self):
        try:
            username = usrnam.get()
            password = psswd.get()

            subject = self.sub
            body = self.bod
            if username == "" or password == "" or self.to == "" or subject == "" or body == "":
                print("All fields req")
                return
            else:
                finalMessage = 'Subject: {}\n\n{}'.format(subject, body)
                server = smtplib.SMTP('smtp.outlook.com', 587)
                server.starttls()
                server.login(username, password)
                server.sendmail(username, self.to, finalMessage)
                print("sent")
        except:
            print("Failure")


class EmailClient(App):
    def build(self):
        # Create the main layout
        layout = BoxLayout(orientation='vertical')

        # Create the header label
        header_label = Label(text='Welcome to the Email Client', size_hint=(1, 0.1))
        layout.add_widget(header_label)

        # Create the email input field
        email_input = TextInput(hint_text='Enter your email', size_hint=(1, 0.1))
        layout.add_widget(email_input)

        # Create the password input field
        password_input = TextInput(hint_text='Enter your password', password=True, size_hint=(1, 0.1))
        layout.add_widget(password_input)

        # Create the login button
        login_button = Button(text='Login', size_hint=(1, 0.1))
        layout.add_widget(login_button)

        # Create the email list
        email_list = BoxLayout(orientation='vertical', size_hint=(1, 0.6))
        layout.add_widget(email_list)

        # Create the compose button
        compose_button = Button(text='Compose', size_hint=(1, 0.1))
        compose_button.bind(on_press=self.comp)
        layout.add_widget(compose_button)

        # Create the footer label
        footer_label = Label(text='© 2022 Email Client. All rights reserved.', size_hint=(1, 0.1))
        layout.add_widget(footer_label)

        return layout

    def comp(self, instance):
        self.stop()
        Compose_Email().run()


if __name__ == '__main__':
    EmailClient().run()

