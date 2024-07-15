import reflex as rx

class State(rx.State):
pass

def index() -> rx. Component:
  return rx.hstack(
    rx.text(
      "ACabrera",
      height="40px",
            ),
      position="sticky",
  )


app = rx. App()
app. add_page(index)
app. compile()