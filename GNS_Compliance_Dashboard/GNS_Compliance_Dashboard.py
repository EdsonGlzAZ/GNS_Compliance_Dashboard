"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config

from .ui.base import base_page

from . import navigation

############## Pages Import #####################
from .compliance import compliance_page
from .EOL import eol_page
from .onboarding import onboarding_page
from .new_devices import new_devices_page
from .health_reports import health_reports_page
from .health_status import health_status_page
#################################################



def index() -> rx.Component:
    # Welcome Page (Index)
    my_child = rx.vstack(
            rx.image( 
                src="/logo.png",
                width="175px",
                height="auto",
                border_radius="25%",
            ),
            rx.heading("Weclome to the NRE Dashboard", size="9"),
            spacing="5",
            justify="center",
            text_align="center",
            align = "center",
            min_height="75vh",
        )
    return base_page(my_child)


app = rx.App()
app.add_page(index)
app.add_page(
    compliance_page,
    route=navigation.routes.COMPLIANCE_ROUTE,
)
app.add_page(
    eol_page,
    route=navigation.routes.END_OF_LIFE_ROUTE,
)
app.add_page(
    onboarding_page,
    route=navigation.routes.ON_BOARDING_ROUTE,
)
app.add_page(
    new_devices_page,
    route=navigation.routes.NEW_DEVICES_ROUTE,
)
app.add_page(
    health_status_page,
    route=navigation.routes.HEALTH_STATUS_ROUTE,
)
app.add_page(
    health_reports_page,
    route=navigation.routes.HEALTH_REPORTS_ROUTE,
)

