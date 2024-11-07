import reflex as rx
from . import routes

class NavState(rx.State):
    
    def to_home(self):
        return rx.redirect(routes.HOME_ROUTE)
    
    def to_compliance(self):
        return rx.redirect(routes.COMPLIANCE_ROUTE)
    
    def to_on_boarding(self):
        return rx.redirect(routes.ON_BOARDING_ROUTE)
    
    def to_end_of_life(self):
        return rx.redirect(routes.END_OF_LIFE_ROUTE)
    
    def to_new_devices(self):
        return rx.redirect(routes.NEW_DEVICES_ROUTE)
    
    def to_health_status(self):
        return rx.redirect(routes.HEALTH_STATUS_ROUTE)
    
    def to_health_reports(self):
        return rx.redirect(routes.HEALTH_REPORTS_ROUTE)
    