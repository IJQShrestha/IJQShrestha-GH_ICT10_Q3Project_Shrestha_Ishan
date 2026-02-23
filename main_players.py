from pyscript import display, document


def show_players(e):
    document.getElementById("output").innerHTML = ""

    section = document.getElementById("section").value

    players = []


    if section == "Sapphire":
        players = [
            "Tessa Aseo", "Anakin Batac", "Neriza Calanglang",
            "Aaron Dee", "Vito De Guzman", "Harvey Dolor",
            "Adrianna Garces", "Selena Galvez", "Jillian Grospe",
            "Eduardo Hizon", "Margo Intalan", "Atasha Ko",
            "Alijah Lagman", "Marcus Law", "Sittie Macabago",
            "Euan Martinez", "Kelsey Medina", "Michaela Mendoza",
            "Manuel Mergal", "Seth Ngo", "Sofia Padojinog",
            "Jennifer Uy", "Ishan Shrestha", "Francesca Yao"
        ]


    elif section == "Ruby":
        players = [
            "Agena, Vada", "Ala, Zipporah Alvarado", "Baring, Jaiyanah",
            "Baylon, Koby Martin Eusebio", "Brodhagen, Alexandria Dominic",
            "Cabatingan, Jade Louisse Castro",
            "Cañete, Tarcisius John Coballes",
            "Dimaculangan, Zakari Dwayne U.",
            "Evangelista, Dwayne Kyle",
            "Galang, Charlize Liana Maceda",
            "Garabiles, Shalanie Lanette",
            "Gonzales, Amanda Mathea",
            "Jamet, Frances Hailey Almoro",
            "Ledesma, Aisha Ashley Opallia",
            "Nacino, Samantha Gabrielle",
            "Nardo, Kaitlyn Francesca",
            "Oliveros, Joaquin Rafael",
            "Olmedo, Cerinne Kimberlee",
            "Ong, Raiden Bryce Chan",
            "Rebadulla, Samantha Erin",
            "Reyes, David Miguel A.",
            "Sangreo, Vanna Marie",
            "Villafuerte, Lauren Mary",
            "Villegas, Enzo Kelsey",
            "Yao, Amanda Praise Kho"
        ]


    elif section == "Emerald":
        players = [
            "Andrian Joseph Abayon", "Erin Gayle Antes",
            "Caitlyn Apostol", "Kyla Limuelle Banaag",
            "Oscar Robert Barrientos", "Clarisse Yvonne Casal",
            "Thomas Taylor Coeli", "Ivan Kelly David",
            "Aurelia De Mata", "Franzeska Adienna Dela Cruz",
            "Jalena Rhein Dela Cruz", "Keisha May Dellejero",
            "Hikary Fukuda", "Ashley Rose Gozum",
            "Juanico Matthew Ibay", "Angela Bridget Lim",
            "Maria Julie Ann Lozano", "James Micah Mamauag",
            "Sofia Navarro", "Yciar Precones",
            "Gino Benedict Ramos", "Gurnoor Singh Sidhu",
            "Julia Ysabel Tiu", "Erich Jasmine Villamayor",
            "Annika Coleen Zaragoza"
        ]


    else:
        players = ["No list available yet."]


    for name in players:
        display(name, target="output")
