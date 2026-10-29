from database import session
from models.Character import Character
from sqlalchemy import select
from utils.Results import Results


class CharacterService:

    @staticmethod
    def create_character(name, hair, clothes):

        character = Character(name=name, clothes=clothes, hair=hair)

        errors = CharacterService._validate_character(character)
        
        if errors:
            return Results(success=False, data=character, errors=errors)

        try:
            session.add(character)
            session.commit()
            return Results(success=True, data=character, errors={})

        except Exception as e:
            return Results(success=False, data=None, errors=e)

        finally:
            session.close()

    @staticmethod
    def list_all_characters():

        statement = select(Character)

        try:
            get_all_characters = session.scalars(statement).all()
            
            return Results(success=True, data=get_all_characters, errors={})
        
        except Exception as e:
            return Results(success=False, data=None, errors=e)
        finally:
            session.close()

         

    @staticmethod
    def get_character(id):

        try:
            get_character = session.get(Character, id)

            if not get_character:
                error = "This character doesn't exist on the database"
                return Results(success=False, data=None, errors=error)

            return Results(success=True, data=get_character, errors={})

        except Exception as e:
            return Results(success=False, data=None, errors=e)
        finally:
            session.close()

    @staticmethod
    def delete_character(id):

        try:
            character_to_delete = session.get(Character, id)

            if not character_to_delete:
                errors = {}
                errors["character_doesnt_exist"] = "This character doesn't exist on the database"
                return Results(success=False, data=None, errors=errors)

            session.delete(character_to_delete)
            session.commit()
            return Results(success=True, data=None, errors={})

        except Exception as e:
            return Results(success=False, data=None, errors=e)
        finally:
            session.close()

    @staticmethod
    def update_character(id, name, hair, clothes):
        
        character = Character(name=name, clothes=clothes, hair=hair)
        
        errors = CharacterService._validate_character(character)
        
        if errors:
            return Results(success=False, data=character, errors=errors)

        try:
            character_to_update = session.get(Character, id)

            if not character_to_update:
                errors = {}
                errors["character_doesnt_exist"] = "This character doesn't exist on the database"
                return Results(success=False, data=None, errors=errors)

            character_to_update.name = name
            character_to_update.hair = hair
            character_to_update.clothes = clothes

            session.commit()
            return Results(success=True, data=character_to_update.name, errors={})

        except Exception as e:
            return Results(success=False, data=None, errors=e)
        finally:
            session.close()

    @staticmethod
    def _validate_character(character):
        errors = {}

        hair = ["blue", "red"]
        clothes = ["t-shirt", "pants"]  

        if not character.name:
            errors["empty_name"] = "Required field name is empty!"

        if not character.hair:
            errors["empty_hair"] = "Required field hair is empty!"

        if not character.clothes:
            errors["empty_clothes"] = "Required field clothes is empty!"

        if character.hair not in hair:
            errors["invalid_hair"] = "Invalid Hair!"

        if character.clothes not in clothes:
            errors["invalid_clothes"] = "Invalid Clothes!"

        if errors:
            return errors
        
        
        