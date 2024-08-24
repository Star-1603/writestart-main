from pydantic import BaseModel
import uuid
import time


class UserInfo(BaseModel):
    id: str
    company_name: str
    product_name: str
    ideal_user: str

    @classmethod
    def attach_random_id(cls, company_name, product_name, ideal_user):
        random_id = cls.generate_timestamp_id()
        return cls(id=random_id, company_name=company_name, product_name=product_name, ideal_user=ideal_user)

    @staticmethod
    def generate_timestamp_id():
        timestamp = int(time.time() * 1000)  # Convert current time to milliseconds
        random_component = str(uuid.uuid4()).replace('-', '')  # Generate a random component
        unique_id = f'{timestamp}{random_component}'  # Combine timestamp and random component
        return unique_id

user_table = "table"