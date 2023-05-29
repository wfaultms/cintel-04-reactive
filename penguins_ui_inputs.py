"""
Purpose: Provide user interaction options for the Penguins dataset.

Checkboxes should be independent of each other.

Radio buttons should be mutually exclusive.

IDs must be unique. They are capitalized in this app for clarity (not typical).
The IDs are case-sensitive and must match the server code exactly.

We prefaced IDs with the dataset name to avoid naming conflicts.

"""

from shiny import ui


def get_penguins_sidebar():
    return ui.panel_sidebar(
        ui.h2("Penguins Interaction"),
        ui.tags.hr(),
        ui.input_slider(
            "PENGUIN_BODY_MASS_RANGE",
            "Body Mass (g)",
            min=2700,
            max=6300,
            value=[2700, 6300],
        ),
        ui.input_numeric("PENGUIN_MAX_BILL", "Max Bill Length (mm):", value=60.0),
        ui.input_checkbox("PENGUIN_SPECIES_Adelie", "Adelie", value=True),
        ui.input_checkbox("PENGUIN_SPECIES_Chinstrap", "Chinstrap", value=True),
        ui.input_checkbox("PENGUIN_SPECIES_Gentoo", "Gentoo", value=True),
        ui.input_radio_buttons(
            "PENGUIN_GENDER",
            "Select Genders",
            {"a": "All (includes missing values)", "f": "Female", "m": "Male"},
            selected="a",
        ),
        ui.tags.hr(),
        ui.p("Please be patient. The charts may take a few seconds to load."),
        ui.tags.hr(),
    )
