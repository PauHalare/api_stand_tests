import sender_stand_request
import data

def get_user_body(first_name):
    current_body = data.user_body.copy()
    current_body["firstName"] = first_name
    return current_body


def test_create_user_2_letter_in_first_name_get_success_response():
    user_body = get_user_body("Aa")
    user_response = sender_stand_request.post_new_user(user_body)
    assert user_response.status_code == 201
    assert user_response.json()["authToken"] != ""

    users_table_response = sender_stand_request.get_users_table()
    str_user = user_body["firstName"] + "," + user_body["phone"] + "," \
               + user_body["address"] + ",,," + user_response.json()["authToken"]
    assert users_table_response.text.count(str_user) == 1



# Función de prueba positiva
def positive_assert(first_name):
    # El cuerpo de la solicitud actualizada se guarda en la variable user_body
    user_body = get_user_body(first_name)
    user_response = sender_stand_request.post_new_user(user_body)
    assert user_response.status_code == 201
    assert user_response.json()["authToken"] != ""

    users_table_response = sender_stand_request.get_users_table()
    # String que debe estar en el cuerpo de respuesta
    str_user = user_body["firstName"] + "," + user_body["phone"] + "," \
               + user_body["address"] + ",,," + user_response.json()["authToken"]

# Comprueba si el usuario o usuaria existe y es único/a
    assert users_table_response.text.count(str_user) == 1


    # Prueba 1. Creación de un nuevo usuario o usuaria
    # El parámetro "firstName" contiene dos caracteres
    def test_create_user_2_letter_in_first_name_get_success_response():
        positive_assert("Aa")




#Prueba 2. Creación de un nuevo usuario o usuaria
    # El parámetro "firstName" contiene 15 caracteres
    def test_create_user_15_letter_in_first_name_get_success_response():
        positive_assert("Aaaaaaaaaaaaaaa")


 # Prueba 3 Preparación Negative assert
def negative_assert_symbol(first_name):
    user_body = get_user_body(first_name)
    response = get_user_body(first_name)
    assert response.status_code == 400
    assert response.json()["message"] == "El nombre que ingresaste es incorrecto. "  \
            "Los nombres solo pueden contener caracteres latinos,  " \
            "los nombres deben tener al menos 2 caracteres y no más de 15 caracteres"


# Prueba 3. Error
# El parámetro "firstName" contiene un carácter
def test_create_user_1_letter_in_first_name_get_error_response():
    negative_assert_symbol("A")

# Prueba 4. Error
# El parámetro "firstName" contiene 16 carácteres
def test_create_user_16_letter_in_first_name_get_error_response():
    negative_assert_symbol("Аааааааааааааааа")


# Prueba 5. Error
# El parámetro "firstName" contiene  un espacio
def test_create_user_has_space_in_first_name_get_error_response():
    negative_assert_symbol("A Aaa")


# Prueba 6. Error
# El parámetro "firstName" contiene  un caracter especial
def test_create_user_has_special_symbol_in_first_name_get_error_response():
    negative_assert_symbol("№%@")


# Prueba 7. Error
# El parámetro "firstName" contiene  un numero
def test_create_user_has_number_in_first_name_get_error_response():
    negative_assert_symbol("123")


#Pruebas 8 y 9 preparación
def negative_assert_no_firstname(user_body):
    response = sender_stand_request.post_new_user(user_body)
    assert response.status_code == 400
    assert response.json()["code"] == 400
    assert response.json()["message"] == "No se enviaron todos los parámetros requeridos"


def test_create_user_no_first_name_get_error_response():
    user_body = data.user_body.copy()
    user_body.pop("firstName")
    negative_assert_no_firstname(user_body)


    # Prueba 9. Error
    # El parámetro "firstName" contiene un string vacío
def test_create_user_empty_first_name_get_error_response():
        # El cuerpo de la solicitud actualizada se guarda en la variable user_body
        user_body = get_user_body("")
        # Comprueba la respuesta
        negative_assert_no_firstname(user_body)

def test_create_user_number_type_first_name_get_error_response():
    user_body = get_user_body(12)
    response = sender_stand_request.post_new_user(user_body)
    assert response.status_code == 400
    assert response.json()['code'] == 400
