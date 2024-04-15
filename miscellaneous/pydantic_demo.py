from pydantic import ValidationError
from typing import Optional
import string

class User(pydantic.BaseModel):
    username: str
    password: str
    age: int
    score: float
    email: Optional[str] = None
    phone_number: Optional[str]= None
    
    def __repr__(self):
        return f"User(username={self.username})"
        
    # @pydantic.root_validator(skip_on_failure=True)
    # @classmethod
    # def validate_phone_email(cls,values):
    #     if "email" in values or "phone_number" in values:
    #         return values
    #     else:
    #         raise ValidationError("Add atleast one number or email")
    
    @pydantic.field_validator("username")
    @classmethod
    def validate_username(cls, user):
        if any(p in user for p in string.punctuation):
            raise ValidationError("Username cant have punctuation")
        else:
            return user
    
    @pydantic.field_validator("password")
    @classmethod
    def validate_password(cls, password):
        if len(password)<8:
            raise ValueError("Password can't be less than 8 char.")
        if any(p in password for p in string.punctuation):
            if any(p in password for p in string.digits):
                if any(p in password for p in string.ascii_lowercase):
                     return password
        else:
            raise ValidationError("Password need atleast punc, digit and lowercase")
    
    @pydantic.field_validator("age","score")
    @classmethod
    def valid_number(cls, n):
        if n<=0:
            raise ValidationError("Value should be non-negative")
        else:
            return n


candidate = {
    "username": "lakhotia",
    "password": "abcdes@123",
    "age": 21,
    "score": 24.1,
    "email":"abc",
    "phone_number":"7597572378"
}
        
u1 = User(**candidate)

print(u1)

    