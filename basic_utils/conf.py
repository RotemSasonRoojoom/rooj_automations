from typing import Literal
from pydantic import BaseModel, Field
from pydantic_settings import BaseSettings
from pathlib import Path

class CareLoginSettings(BaseSettings):
    username: str
    password: str
    url: str
    username_proxy: str
    password_proxy: str
    port: int
    server: str

class CareSettings(BaseSettings):
    login_info: CareLoginSettings = Field(default_factory=CareLoginSettings)
    env: Literal['draft', 'staging', 'Production','test'] = Field(default='Staging')
    test_env: Literal['vf-qa', 'vf-prod', 'bytel-qa','bytel-prod'] = Field(default='vf-prod')
    channel: Literal['web', 'IVR_NLU','CHATBOT','agent','TOBI'] = Field(default='web')
    cid: str
    simulator_path: str
    business_line: str
    logs_path: str
    screenshots_path: str

    class Config:
        env_file = Path(__file__).parent / '.env'
        env_nested_delimiter = '__'


settings = CareSettings()





