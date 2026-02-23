from pyscript import display, document

def intramquali(e):
    document.getElementById("output").innerHTML = " "

    section = document.getElementById("section").value
    grade = int(document.getElementById("grade").value)

    registration = document.querySelector('input[name="reg"]:checked')
    medical = document.querySelector('input[name="med"]:checked')

    if registration is None or medical is None or section == "":
        display("Complete the forum", target="output")

    elif registration.value != "yes":
        display("Register to join.", target="output")

    elif medical.value != "cleared":
        display("Get a medical clearance.", target="output")



    elif grade < 7 or grade > 10:
        display("Required Grades 7-10", target="output")
    elif grade == 7 and section == "Sapphire":
        display("You're in Green Hornets", target="output")
    elif grade == 7 and section == "Ruby":
        display("You're in Blue Bears", target="output")
    elif grade == 7 and section == "Topaz":
        display("You're in Red Bull Dogs", target="output")
    elif grade == 7 and section == "Emerald":
        display("You're in Yellow Tigers", target="output")


    elif grade == 8 and section == "Sapphire":
        display("You're in Green Hornets", target="output")
    elif grade == 8 and section == "Ruby":
        display("You're in Blue Bears", target="output")
    elif grade == 8 and section == "Topaz":
        display("You're in Red Bull Dogs", target="output")
    elif grade == 8 and section == "Emerald":
        display("You're in Yellow Tigers", target="output")

    elif grade == 9 and section == "Sapphire":
        display("You're in Green Hornets", target="output")
    elif grade == 9 and section == "Ruby":
        display("You're in Blue Bears", target="output")
    elif grade == 9 and section == "Topaz":
        display("You're in Red Bull Dogs", target="output")
    elif grade == 9 and section == "Emerald":
        display("You're in Yellow Tigers", target="output")


    elif grade == 10 and section == "Sapphire":
        display("You're in Green Hornets", target="output")
    elif grade == 10 and section == "Ruby":
        display("You're in Blue Bears", target="output")
    elif grade == 10 and section == "Topaz":
        display("You're in Red Bull Dogs", target="output")
    elif grade == 10 and section == "Emerald":
        display("You're in Yellow Tigers", target="output")

    else:
        display("Invalid input.", target="output")
