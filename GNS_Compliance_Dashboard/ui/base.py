
import reflex as rx

from .nav import navbar


def base_layout_component(child:rx.Component, *args, **kwargs)->rx.Component:
    return rx.fragment(
        navbar(),
        rx.box(
            child,
            padding="1em",
            width="100%"
        ),
        rx.logo()
    )

def base_page(child:rx.Component, *args, **kwargs) -> rx.Component:
    #print([type(x) for x in args])
    is_logged_in = True
    
    if not isinstance(child,rx.Component):
        child= rx.heading("this is not a valid child elemnt")
        
    return rx.cond(
        is_logged_in,
        base_layout_component(child,*args, kwargs),
    )
