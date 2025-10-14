# Implementation Guide — UX Designer Career

## 1) IDs & Strings in Sims 4 Studio
- Open each XML in `Tuning/` with Sims 4 Studio.
- Assign a unique **Instance ID** to every resource. Replace the `TBD_INSTANCE_ID` placeholders accordingly.
- Create **String Table (STBL)** entries:
  - `UXC_PIE_CATEGORY_CAREER` → "Career"
  - `UXC_INTERACTION_DESIGN_WIREFRAMES` → "Design Wireframes"
  - `UXC_INTERACTION_RUN_USABILITY_TEST` → "Run Usability Test"
  - `UXC_INTERACTION_REMOTE_STANDUP` → "Remote Standup"
  - Notifications like: "Promoted to Junior UX Designer!"

## 2) Package XML
- Save XMLs into a new `.package` (e.g., `UXDesignerCareer_Tuning.package`). Place in Mods folder.
- Clear `localthumbcache.package` before tests.

## 3) Python Script (.ts4script)
- Place `Scripts/ux_career/ux_career.py` in a zip named `UXDesignerCareer.ts4script` while **preserving folders**.
- Compile to `.pyc` with EA's Python version to avoid mismatches.

## 4) Test
- In-game: Computer/Tablet → **Career** pie menu → try the 3 actions.
- Verify payouts/stat gains. Adjust as needed.

## 5) Enhancements
- Work-from-home vs Office toggle (buff/trait gating which interactions appear).
- Daily tasks/objectives to simulate job requirements.
- Promotion notifications at stat thresholds (2/5/8).
