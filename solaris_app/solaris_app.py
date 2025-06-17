import reflex as rx
from collections import Counter

class User(rx.Base):
    name: str
    email: str
    gender: str

class State(rx.State):
    users: list[User] = [

        User(
            name = "Danilo Sousa",
            email = "danilo@example.com",
            gender = "Male"
        ),

        User(
            name = "Zahram Ambessa",
            email = "zahra@example.com",
            gender = "Female"
        )

    ]

    def add_user(self, form_data: dict):
        self.users.append(User(**form_data))

def show_user(user: User):
    return rx.table.row(
        rx.table.cell(user.name),
        rx.table.cell(user.email),
        rx.table.cell(user.gender)
    )

def form():
    return rx.form(

        rx.vstack(
            rx.input(
                placeholder="User Name",
                name = "name",
                required = True
            ),

            rx.input(
                placeholder = "user@example.com",
                name = "email",
                required = True
            ),

            rx.select(
                ["Male", "Female", "Other"],
                placeholder = "Select your gender",
                name = "gender"
            ),
            rx.button("Submit", type="submit"),
        ),
        on_submit=State.add_user,
        reset_on_submit = True,
    )

def index() -> rx.Component:
    return rx.vstack(
form(),
rx.table.root(
        rx.table.header(
            rx.table.row(
                rx.table.column_header_cell("Name"),
                rx.table.column_header_cell("Email"),
                rx.table.column_header_cell("Gender"),
            )
        ),
        rx.table.body(
            rx.foreach(State.users, show_user)
        ),
        variant = "surface",
        size = "3"
    ))

app = rx.App()
app.add_page(index)