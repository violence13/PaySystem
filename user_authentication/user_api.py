from main import app
from database import get_user_cards_by_phone_number_db,register_user_db, check_password_db, get_user_cabinet_db
from datetime import datetime


# Регистрация пользователя
@app.post('/register_user')
async def register_user_api(phone_number:int, name:str, pincode:int, password:str):
    result = register_user_db(phone_number=phone_number, name=name, password=password, pincode=pincode)
    return {'status':1, "message":result}

# Вход в аккаунт
@app.get('/login')
async def login_user_api(phone_number:int, password:str):
    result = check_password_db(phone_number=phone_number, password=password)
    return {'status': 1, "message": result}

# Вывод информации пользователя
@app.get('/user_cabinet')
async def get_user_cabinet_api(user_id:int):
    result = get_user_cabinet_db(user_id=user_id)
    return {'status': 1, "message": result}

# Получить карты по номеру телефона
@app.get('/get_user_cards_by_phone')
async def get_user_cards_by_phone_number_api(phone_number:int):
    result = get_user_cards_by_phone_number_db(phone_number)
    return {'status': 1, "message": result}
