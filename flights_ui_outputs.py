'''
Purpose: Display ouput for the Flights dataset.
'''

from shiny import ui
from shinywidgets import output_widget

def get_flights_main():
    return ui.panel_main(
        ui.h2("Main Panel with Reactive Output"),
        ui.tags.hr(),
        ui.tags.section(
            ui.h3("Filtered Flights: Charts"),
            output_widget("flights_output_widget1"),
            output_widget("flights_output_widget2"),
            ui.tags.hr(),
            ui.h3("Filtered Flights Table"),
            ui.output_text("flights_record_count_string"),
            ui.output_table("flights_filtered_table"),
            ui.tags.hr(),
        )
    )
