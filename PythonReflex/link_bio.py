import reflex as rx

class State(rx.state):
  pass

  def index() -> rx.Component:
    return rx.text("Hola Reflex!")