from pyscript import document, when

club_members = [
    "thirdy sumugat",
    "pia serdena",
    "johann geneveo",
    "alessi bugayong",
    "thirdy agaceta"
]

@when("click", "#check_button")
def candidate_checker(event):
    first_name = document.getElementById("first_name").value.strip()
    last_name = document.getElementById("last_name").value.strip()

    candidate = " ".join(
        (first_name + " " + last_name).lower().split()
    )

    member_checker = candidate in club_members

    messages = [
        f"Sorry, {candidate.title()}, your name is not on the list.",
        f"Congratulations, {candidate.title()}! You are now part of the COCC!"
    ]

    document.getElementById("result").innerText = messages[int(member_checker)]