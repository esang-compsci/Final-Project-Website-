from drafter import *
from dataclasses import dataclass

set_website_title("Prosthetic Limb Finder")

set_site_information(
    author="Elena Sangemino",
    description="Explore prosthetic limb options based on your activity level, interests, and desired features.",
    sources="Prosthetic product information from manufacturers including Ottobock, Össur, Fillauer, and College Park. Created with the help of Drafter documentation.",
    planning=["https://github.com/esang-compsci/Final-Project-Website-/blob/main/CS1FinalProject0_PickaProblemElenaSangemino.pdf", "https://github.com/esang-compsci/Final-Project-Website-/blob/main/CS1FinalProject1_Design.pdf"],
    links=["https://github.com/esang-compsci/Final-Project-Website-"]
)

hide_debug_information()
set_website_framed(False)

@dataclass
class Prosthetic:
    """Represent one prosthetic product and the activities/features it supports."""
    name: str
    limb_type: str
    activity: str
    activity_level: str
    features: list[str]
    description: str


@dataclass
class State:
    """Store user selections and prosthetic data shared between website pages."""
    limb_type: str
    activity: str
    activity_level: str
    desired_features: list[str]
    extra_notes: str
    prosthetic_catalog: list[Prosthetic]
    prosthetic_options: list[Prosthetic]


def make_starting_state():
    """Create the initial website state and populate the prosthetic catalog."""
    catalog = [

        # LEG PROSTHETICS

        Prosthetic(
            "Ottobock 1E90 Sprinter",
            "Leg", "Running", "High",
            ["Lightweight", "Energy return"],
            "A running prosthetic foot designed for athletic movement."
        ),

        Prosthetic(
            "Ottobock 1E91 Runner",
            "Leg", "Running", "High",
            ["Lightweight", "Energy return", "Comfort"],
            "A prosthetic running foot designed for active users."
        ),

        Prosthetic(
            "Ossur Cheetah Xceed",
            "Leg", "Running", "High",
            ["Lightweight", "Energy return"],
            "A running blade designed for athletic performance."
        ),

        Prosthetic(
            "Fillauer Obsidian Sprint",
            "Leg", "Running", "High",
            ["Lightweight", "Energy return"],
            "A running prosthetic foot designed for sports and running."
        ),

        Prosthetic(
            "Fillauer Obsidian Running DM",
            "Leg", "Running", "High",
            ["Lightweight", "Energy return", "Comfort"],
            "A dynamic prosthetic foot designed for running."
        ),

        Prosthetic(
            "Ottobock 1E95 Challenger",
            "Leg", "Sports", "High",
            ["Stability and control", "Energy return", "Comfort"],
            "A prosthetic foot designed for active sports and movement."
        ),

        Prosthetic(
            "Ottobock Taleo",
            "Leg", "Everyday Activities", "Moderate",
            ["Comfort", "Lightweight"],
            "A prosthetic foot designed for everyday walking."
        ),

        Prosthetic(
            "Ottobock Trias",
            "Leg", "Everyday Activities", "Moderate",
            ["Stability and control", "Comfort"],
            "A prosthetic foot designed to support everyday movement."
        ),

        Prosthetic(
            "Ottobock Triton",
            "Leg", "Everyday Activities", "High",
            ["Stability and control", "Energy return"],
            "A prosthetic foot designed for more active users."
        ),

        Prosthetic(
            "College Park Celsus",
            "Leg", "Everyday Activities", "Low",
            ["Stability and control", "Comfort"],
            "A prosthetic foot designed for everyday mobility."
        ),

        Prosthetic(
            "Fillauer AllPro",
            "Leg", "Sports", "High",
            ["Stability and control", "Energy return"],
            "A prosthetic foot designed for dynamic movement and activity."
        ),

        Prosthetic(
            "College Park Soleus Tactical",
            "Leg", "Sports", "Moderate",
            ["Stability and control", "Energy return"],
            "A prosthetic foot designed for active movement and varied activities."
        ),

        Prosthetic(
            "College Park Trustep",
            "Leg", "Everyday Activities", "Moderate",
            ["Comfort", "Stability and control"],
            "A prosthetic foot designed to support everyday mobility."
        ),

        Prosthetic(
            "Fillauer Aeris Performance LP",
            "Leg", "Sports", "High",
            ["Energy return", "Stability and control"],
            "A prosthetic foot designed for dynamic movement."
        ),

        Prosthetic(
            "Freedom Innovations Agilix",
            "Leg", "Everyday Activities", "Moderate",
            ["Lightweight", "Comfort", "Stability and control"],
            "A prosthetic foot designed for everyday movement and varied terrain."
        ),


        # ARM PROSTHETICS

        Prosthetic(
            "Ossur i-Limb Quantum",
            "Arm", "Everyday Activities", "Any",
            ["Stability and control", "Comfort"],
            "A multi-articulating prosthetic hand designed for different grips."
        ),

        Prosthetic(
            "Ottobock bebionic Hand",
            "Arm", "Everyday Activities", "Any",
            ["Stability and control", "Comfort"],
            "A prosthetic hand designed to perform different everyday tasks."
        ),

        Prosthetic(
            "Ottobock Michelangelo Hand",
            "Arm", "Everyday Activities", "Any",
            ["Stability and control", "Comfort"],
            "A prosthetic hand designed to provide different grip functions."
        ),

        Prosthetic(
            "TASKA HandGen2",
            "Arm", "Everyday Activities", "Any",
            ["Stability and control", "Comfort"],
            "A prosthetic hand designed for everyday activities."
        ),

        Prosthetic(
            "TRS Grip 5 Evolution Prehensor",
            "Arm", "Everyday Activities", "Any",
            ["Stability and control", "Lightweight"],
            "A prosthetic attachment designed to help users grip objects."
        ),

        Prosthetic(
            "TRS Helix",
            "Arm", "Sports", "Any",
            ["Stability and control"],
            "A prosthetic sports attachment for active users."
        ),

        Prosthetic(
            "Ossur i-Digits Quantum",
            "Arm", "Everyday Activities", "Any",
            ["Stability and control", "Comfort"],
            "A partial-hand prosthetic designed to support different grip patterns."
        ),

        Prosthetic(
            "Ossur i-Digits Access",
            "Arm", "Everyday Activities", "Any",
            ["Stability and control", "Comfort"],
            "A partial-hand prosthetic designed for practical everyday gripping."
        ),

        Prosthetic(
            "Ottobock Speedhand",
            "Arm", "Everyday Activities", "Any",
            ["Lightweight", "Stability and control"],
            "A prosthetic hand designed for grip and everyday performance."
        ),

        Prosthetic(
            "TRS Hi-Fly Fielder",
            "Arm", "Sports", "Any",
            ["Stability and control"],
            "A sports attachment designed for baseball fielding activities."
        ),

        Prosthetic(
            "TRS Cobra Baseball and Softball Attachment",
            "Arm", "Sports", "Any",
            ["Stability and control"],
            "A prosthetic attachment designed for baseball and softball activities."
        )
    ]

    return State(
        "Leg",
        "Running",
        "High",
        [],
        "",
        catalog,
        []
    )


# HOME PAGE

@route
def index(state: State):
    """Show the home page, where users can start or learn about the website."""
    return Page(state, [
        Header("Prosthetic Limb Finder"),
        "Welcome! This website helps you explore prosthetic options based on your activities and preferences.",
        Button("Get Started", "limb_type"),
        Button("Learn About This Website", "about")
    ])


# LIMB TYPE PAGE

@route
def limb_type(state: State):
    """Ask the user to choose an arm or leg prosthetic."""
    return Page(state, [
        Header("Choose Your Prosthetic Type"),
        "What type of prosthetic are you looking for?",
        SelectBox("selected_limb_type", ["Leg", "Arm"]),
        Button("Continue", "save_limb_type"),
        Button("Back Home", "index")
    ])


@route
def save_limb_type(state: State, selected_limb_type: str):
    """Save the limb type selected by the user and open the preferences page."""
    state.limb_type = selected_limb_type
    return preferences(state)


# PREFERENCES PAGE

@route
def preferences(state: State):
    """Display questions about activities, activity level, and desired features."""
    return Page(state, [
        Header("Your Activity Preferences"),

        "What activity are you most interested in?",
        SelectBox(
            "selected_activity",
            ["Running", "Sports", "Everyday Activities"]
        ),

        "What is your activity level?",
        SelectBox(
            "selected_level",
            ["Low", "Moderate", "High"]
        ),

        "Which features are important to you? Select any that apply.",
        CheckBox("lightweight", "Lightweight" in state.desired_features),
        "Lightweight",

        CheckBox("stability", "Stability and control" in state.desired_features),
        "Stability and control",

        CheckBox("energy_return", "Energy return" in state.desired_features),
        "Energy return",

        CheckBox("comfort", "Comfort" in state.desired_features),
        "Comfort",

        "Any additional information you would like to include?",
        TextArea("extra_notes", state.extra_notes),

        Button("Review My Answers", "review"),
        Button("Back", "limb_type")
    ])


# REVIEW PAGE

@route
def review(
    state: State,
    selected_activity: str,
    selected_level: str,
    lightweight: bool,
    stability: bool,
    energy_return: bool,
    comfort: bool,
    extra_notes: str
):
    """Save the user's answers and display them for review.

    The checkbox values are converted into a list of selected feature names
    for the recommendation page to compare with the catalog.
    """
    # Save the activity, activity level, and additional notes in the state.
    state.activity = selected_activity
    state.activity_level = selected_level
    state.extra_notes = extra_notes

    state.desired_features = []

    if lightweight:
        state.desired_features.append("Lightweight")

    if stability:
        state.desired_features.append("Stability and control")

    if energy_return:
        state.desired_features.append("Energy return")

    if comfort:
        state.desired_features.append("Comfort")

    return Page(state, [
        Header("Review Your Answers"),

        "Limb type: " + state.limb_type,
        "Activity: " + state.activity,
        "Activity level: " + state.activity_level,

        "Desired features: " + str(state.desired_features),
        "Additional notes: " + state.extra_notes,

        Button("Find My Prosthetic Options", "recommendations"),
        Button("Change My Preferences", "preferences")
    ])


# RECOMMENDATIONS PAGE

@route
def recommendations(state: State):
    """Filter the catalog using the user's selections and display matching items."""
    # Build a list of catalog entries that meet the user's selections.
    matching_options = []

    for prosthetic in state.prosthetic_catalog:
        # Assume the item matches unless one of the checks rules it out.
        matches = True

        # The prosthetic must be designed for the selected limb type.
        if prosthetic.limb_type != state.limb_type:
            matches = False

        # The intended activity must match the user's selected activity.
        if prosthetic.activity != state.activity:
            matches = False

        # "Any" means the catalog item is not limited to one activity level.
        if (prosthetic.activity_level != "Any"
                and prosthetic.activity_level != state.activity_level):
            matches = False

        # If the user selected features, require at least one feature to match.
        if len(state.desired_features) > 0:
            feature_match = False

            # Compare each selected feature with this prosthetic's features.
            for feature in state.desired_features:
                if feature in prosthetic.features:
                    feature_match = True

            if not feature_match:
                matches = False

        # Add the item only if it passed all required checks.
        if matches:
            matching_options.append(prosthetic)

    # Save the matching items so they can be displayed on the page.
    state.prosthetic_options = matching_options

    # If nothing matched, send the user to the no-matches page.
    if len(state.prosthetic_options) == 0:
        return no_matches(state)

    page_content = [
        Header("Your Prosthetic Options"),
        "Here are the options that match your selections:"
    ]

    # Display the details for each prosthetic that matched.
    for prosthetic in state.prosthetic_options:
        page_content.append(Header(prosthetic.name))
        page_content.append(prosthetic.description)
        page_content.append("Limb type: " + prosthetic.limb_type)
        page_content.append("Activity: " + prosthetic.activity)
        page_content.append("Activity level: " + prosthetic.activity_level)
        page_content.append("Features: " + str(prosthetic.features))

    page_content.append(Button("Change Preferences", "preferences"))
    page_content.append(Button("Start Over", "index"))

    return Page(state, page_content)


# NO MATCHES PAGE

@route
def no_matches(state: State):
    """Show a message when no prosthetics match and offer a way to try again."""
    return Page(state, [
        Header("No Matching Options Found"),
        "We could not find prosthetic options that match all of your selections.",
        "Try changing your activity, activity level, or desired features.",
        Button("Change Preferences", "preferences"),
        Button("Start Over", "index")
    ])


# ABOUT PAGE

@route
def about(state: State):
    """Explain the website's purpose and clarify that it is not medical advice."""
    return Page(state, [
        Header("About This Website"),
        "The Prosthetic Limb Finder is an educational project designed to help users explore different prosthetic products.",
        "The website compares user preferences with a catalog of prosthetic options.",
        "The recommendations are for educational purposes only. They are not medical advice and should not replace guidance from a qualified prosthetist or healthcare professional.",
        Button("Back Home", "index"),
        Button("Get Started", "limb_type")
    ])


# Start the website with its initial state and prosthetic catalog.
start_server(make_starting_state())
