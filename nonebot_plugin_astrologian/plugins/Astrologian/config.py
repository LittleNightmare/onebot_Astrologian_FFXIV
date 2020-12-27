from pydantic import BaseSettings


class Config(BaseSettings):

    # plugin custom config
    plugin_setting: str = "default"
    same_message_structure: bool = False

    class Config:
        extra = "ignore"