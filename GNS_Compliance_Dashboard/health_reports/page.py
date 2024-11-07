import reflex as rx
from ..ui.base import base_page

from . import state

def health_reports_page() ->rx.Component:
    return base_page(
        rx.vstack(
            rx.hstack(
                rx.heading(
                    "Health Reports Page",
                ),        
            ),
            spacing="5",
            align = "center",
            min_height="85vh",
        ),
    )