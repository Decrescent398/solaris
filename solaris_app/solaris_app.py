import reflex as rx

class State(rx.State):

    count: int = 0
    log: bool = False
    head: str = ""
    decider: bool = True
    items: list[str] = ["Apple", "Banana", "Cherry"]

    @rx.event
    def increment(self):
        self.count += 1

    @rx.event
    def decrement(self):
        self.count -= 1

    @rx.event
    def get_head(self, new_head):
        self.head = new_head

    @rx.event
    def is_even(self):
        if self.count % 2 == 0:
            self.decider = True
        else:
            self.decider = False
        
    @rx.event
    def toggle(self):
        self.log = not self.log
        State.is_even()

def render_item(item: rx.Var[str]):
    return rx.list.item(item)

def index():

    return rx.box(

    rx.hstack(

        rx.button("Increment", color_scheme="grass", on_click=State.increment),
        rx.heading(State.count),
        rx.button("Decrement", color_scheme="ruby", on_click=State.decrement)
    ),

    rx.progress(value=State.count),
    rx.input(default_value=State.head, on_blur=State.get_head),

    rx.vstack(

        rx.button(f"Toggle {State.head}", on_click=State.toggle),
        rx.cond(State.decider, rx.heading(State.head), rx.heading(f"{State.head} not")),
        rx.heading(State.head),
        rx.foreach(State.items, render_item)

    )

    )

app = rx.App()
app.add_page(index)