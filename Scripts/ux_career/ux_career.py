# ux_career.py — minimal script-side helpers for the UX Designer Career demo
try:
    import sims4
    import services
    from sims4.localization import LocalizationHelperTuning
except Exception:
    sims4 = None
    services = None

MOD_NAME = "UXDesignerCareer"

def log(msg):
    try:
        print(f"[{MOD_NAME}] {msg}")
    except Exception:
        pass

def show_basic_notification(title, text):
    # Show a simple notification in-game (called from XML loot via script).
    if services is None:
        return
    try:
        from ui.ui_dialog_notification import UiDialogNotification
        client = services.client_manager().get_first_client()
        if client is None:
            return
        title_loc = LocalizationHelperTuning.get_raw_text(title)
        text_loc = LocalizationHelperTuning.get_raw_text(text)
        dialog = UiDialogNotification.TunableFactory().default(client.active_sim, text=text_loc, title=title_loc)
        dialog.show_dialog()
    except Exception as e:
        log(f"Notification error: {e}")

def check_and_notify_promotion(sim_info, current_level):
    # Example hook to display promotions at levels 2/5/8.
    if services is None or sim_info is None:
        return
    try:
        if current_level in (2, 5, 8):
            tiers = {2: "Junior UX Designer", 5: "Mid-level UX Designer", 8: "Senior UX Designer"}
            tier = tiers.get(current_level, "UX Designer")
            show_basic_notification("Promotion!", f"You've been promoted to {tier}!")
    except Exception as e:
        log(f"Promotion check error: {e}")
