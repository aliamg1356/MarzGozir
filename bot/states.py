from aiogram.fsm.state import State, StatesGroup

class Form(StatesGroup):
    awaiting_panel_alias = State()
    awaiting_panel_url = State()
    awaiting_username = State()
    awaiting_password = State()
    awaiting_add_admin = State()
    awaiting_user_info = State()
    awaiting_delete_panel = State()
    awaiting_panel_selection = State()
    awaiting_action = State()
    awaiting_search_username = State()
    awaiting_create_username = State()
    awaiting_data_limit = State()
    awaiting_expire_time = State()
    awaiting_note = State()
    awaiting_protocol_selection = State()
    awaiting_inbounds_selection_for_existing_user = State()
    awaiting_new_data_limit = State()
    awaiting_new_expire_time = State()
    awaiting_log_channel = State()
    awaiting_user_action = State()

