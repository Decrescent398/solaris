import reflex as rx

class State(rx.State):

    count: int = 0

    @rx.event
    def increment(self):
        self.count += 1

    @rx.event
    def decrement(self):
        self.count -= 1

def index():

    return rx.box(

    rx.hstack(

        rx.button("Increment", color_scheme="grass", on_click=State.increment),
        rx.heading(State.count),
        rx.button("Decrement", color_scheme="ruby", on_click=State.decrement)
    ),

    rx.progress(value=State.count)

    )

app = rx.App()
app.add_page(index)