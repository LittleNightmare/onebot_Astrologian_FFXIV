from pydantic import BaseSettings


class Config(BaseSettings):

    # 暂时没用，但先留着
    plugin_setting: str = "default"
    # 强制个人与群组格式保持一致（好像没啥大用）
    same_message_structure: bool = False

    class Config:
        extra = "ignore"