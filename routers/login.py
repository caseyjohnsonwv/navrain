import re
from fastapi import APIRouter, HTTPException


phone_number_regex = '^(?:\+\d{1,2})?[\s\-\.]*\(?(\d{3})\)?[\s\-\.]*(\d{3})[\s\-\.]*(\d{4})$'
def normalize_phone(phone):
    matches = re.findall(phone_number_regex, phone)
    print(matches)
    if len(matches) != 1:
        raise ValueError('Not a valid 10 digit phone number')
    return ''.join(matches[0])


router = APIRouter()

@router.get('/{phone}')
async def login_user(phone: str):
    try:
        phone = normalize_phone(phone)
    except ValueError as ex:
        raise HTTPException(status_code=422, detail=str(ex))
    return {"phone":phone}
