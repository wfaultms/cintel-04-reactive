"""
Purpose: Use Python to create a continuous intelligence and 
interactive analytics dashboard using Shiny for Python and 
interactive charts from Holoviews Bokeh and Plotly Express.

"""
from shiny import *
import shinyswatch

from flights_server import get_flights_server_functions
from flights_ui_inputs import get_flights_sidebar
from flights_ui_outputs import get_flights_main

from mtcars_server import get_mtcars_server_functions
from mtcars_ui_inputs import get_mtcars_sidebar
from mtcars_ui_outputs import get_mtcars_main

from penguins_server import get_penguins_server_functions
from penguins_ui_inputs import get_penguins_sidebar
from penguins_ui_outputs import get_penguins_main

from relationships_server import get_relationships_server_functions
from relationships_ui_inputs import get_relationships_sidebar
from relationships_ui_outputs import get_relationships_main

from util_logger import setup_logger

logger, logname = setup_logger(__name__)

app_ui = ui.page_navbar(
    shinyswatch.theme.minty(),
    ui.nav(
        "Flights",
        ui.layout_sidebar(
            get_flights_sidebar(),
            get_flights_main(),
        ),
    ),
    ui.nav(
        "MT_Cars",
        ui.layout_sidebar(
            get_mtcars_sidebar(),
            get_mtcars_main(),
        ),
    ),
    ui.nav(
        "Penguins",
        ui.layout_sidebar(
            get_penguins_sidebar(),
            get_penguins_main(),
        ),
    ),
    ui.nav(
        "Relationships",
        ui.layout_sidebar(
            get_relationships_sidebar(),
            get_relationships_main(),
        ),
    ),

    ui.nav(ui.a("About", href="https://github.com/denisecase")),
    ui.nav(ui.a("GitHub", href="https://github.com/denisecase/cintel-04-reactive")),
    ui.nav(ui.a("App", href="https://denisecase.github.io/cintel-04-reactive/")),
    ui.nav(ui.a("Examples", href="https://shinylive.io/py/examples/")),
    ui.nav(ui.a("shinywidgets", href="https://shiny.rstudio.com/py/docs/ipywidgets.html")),
    title=ui.h1("Case Dashboard"),
)


def server(input, output, session):
    logger.info("Starting server...")
    flights_server_functions = get_flights_server_functions(input, output, session)
    mtcars_server_functions = get_mtcars_server_functions(input, output, session)
    penguins_server_functions = get_penguins_server_functions(input, output, session)
    relationships_server_functions = get_relationships_server_functions(input, output, session) 

#app = App(app_ui, server, debug=True)
app = App(app_ui, server)
