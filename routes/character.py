from flask import Blueprint, render_template, request, url_for, redirect, session
from utils.Results import Results
from services.character_service import CharacterService

character_customization_bp = Blueprint(
    "character_customization", __name__, url_prefix="/customization"
)

@character_customization_bp.route("", methods=["GET"])
def customization():
    mode = "create"
    characters = CharacterService.list_all_characters()

    form_errors = session.pop("form_errors", {})
    old_input = session.pop("old_input", {})

    return render_template(
        "character_customization.html",
        characters=characters.data,
        mode=mode,
        errors=characters.errors,
        form_errors = form_errors,
        old_input = old_input
    )


@character_customization_bp.route("/create", methods=["POST"])
def create():
    mode = "create"
    # quando tiver muitos atributos, passar o objeto inteiro
   
    results = CharacterService.create_character(request.form.get("name"), request.form.get("hair"), request.form.get("clothes"))

    if results.errors:
        
        session["form_errors"] = results.errors
        session["old_input"] = request.form
        
    return redirect(url_for("character_customization.customization"))


@character_customization_bp.route("/edit/<int:id>", methods=["GET"])
def edit(id):
    mode = "edit"

    results = CharacterService.get_character(id)
    characters = CharacterService.list_all_characters()

    return render_template(
        "character_customization.html",
        mode=mode,
        character=results.data,
        characters=characters.data,
        form_errors=results.errors,
    )
    
    # se tiver erro precisa fazer redirect pro get customization


@character_customization_bp.route("/update/<int:id>", methods=["POST"])
def update(id):
    

    name = request.form.get("name")
    hair = request.form.get("hair")
    clothes = request.form.get("clothes")

    results = CharacterService.update_character(id, name, hair, clothes)

    if results.errors:
        mode = "edit"
        
        character = CharacterService.get_character(id)
        
        characters = CharacterService.list_all_characters()
        
        return render_template(
            "character_customization.html",
            character=character.data,
            characters=characters.data,
            errors=results.errors,
            mode=mode,
        )
    return redirect(url_for("character_customization.customization"))


@character_customization_bp.route("/delete/<int:id>", methods=["POST"])
def delete(id):

    CharacterService.delete_character(id)

    return redirect(url_for("character_customization.customization"))
