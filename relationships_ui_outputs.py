"""
Purpose: Display ouput for the relationships dataset.
"""
from shiny import ui
from shinywidgets import output_widget


def get_relationships_main():
    return ui.panel_main(
        ui.h2("Main Panel with Reactive Output"),
        ui.tags.hr(),
        ui.tags.section(
            ui.h3("Relationships: Charts"),
            output_widget("relationships_output_widget1"),
            ui.tags.hr(),
        ),
    )
