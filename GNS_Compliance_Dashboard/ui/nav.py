import reflex as rx 


from .. import navigation



def navbar_link(text: str, url: str) -> rx.Component:
    return rx.link(
        rx.text(text, size="4", weight="medium"), href=url
    )


def navbar() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.hstack(
                rx.hstack(
                    rx.image( 
                        src="/logo_2.png",
                        width="2.25em",
                        height="auto",
                        border_radius="75%",
                    ),
                    rx.heading(
                        "GNE Dashboard", size="5", weight="bold"
                    ),
                    align_items="center",
                ),
                rx.hstack(
                    navbar_link("Home", navigation.routes.HOME_ROUTE),
                    navbar_link("Compliance", navigation.routes.COMPLIANCE_ROUTE),
                    navbar_link("Onboarding", navigation.routes.ON_BOARDING_ROUTE),
                    navbar_link("End of Life", navigation.routes.END_OF_LIFE_ROUTE),
                    navbar_link("New Devices", navigation.routes.NEW_DEVICES_ROUTE),
                    navbar_link("Health Status", navigation.routes.HEALTH_STATUS_ROUTE),
                    navbar_link("Health Reports", navigation.routes.HEALTH_REPORTS_ROUTE),
                    spacing="5",
                ),
                rx.hstack(
                    rx.color_mode.button(),
                ),
                justify="between",
                id="inner_hstack"
            ),
            id="outter_hstack"
        ),
        rx.mobile_and_tablet(
            rx.hstack(
                rx.hstack(
                    rx.image(
                        src="/logo_2.png",
                        width="2.25em",
                        height="auto",
                        border_radius="75%",
                    ),
                    rx.heading(
                        "Reflex", size="6", weight="bold"
                    ),
                    align_items="center",
                ),
                rx.color_mode.button(position="center"),
                rx.menu.root(
                    rx.menu.trigger(
                        rx.icon("menu", size=30)
                    ),
                    rx.menu.content(
                        rx.menu.item("Home", on_click=navigation.NavState.to_home),
                        rx.menu.item("Compliance", on_click=navigation.NavState.to_compliance),
                        rx.menu.item("On Boarding", on_click=navigation.NavState.to_on_boarding),
                        rx.menu.item("End of Life", on_click=navigation.NavState.to_end_of_life),
                        rx.menu.item("New Devices", on_click=navigation.NavState.to_new_devices),
                        rx.menu.item("Health Status", on_click=navigation.NavState.to_health_status),
                        rx.menu.item("Health Reports", on_click=navigation.NavState.to_health_reports),

                    ),
                    justify="end",
                ),
                justify="between",
                align_items="center",
            ),
        ),
        bg=rx.color("accent", 3),
        padding="1em",
        # position="fixed",
        # top="0px",
        # z_index="5",
        width="100%",
    )