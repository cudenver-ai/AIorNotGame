
# AI or Not? — Local 3‑Level Guessing Game

A tiny Flask app you can run locally. Each level shows multiple images; click the one you think is **AI‑generated**. Get all three right to win.

## Quick Start
1. Make sure you have Python 3.9+ installed.
2. In a terminal:
   ```bash
   cd ai_or_not_game
   python -m venv .venv
   # Windows: .venv\Scripts\activate
   # macOS/Linux: source .venv/bin/activate
   pip install flask pillow
   python app.py
   ```
3. Open http://127.0.0.1:5000 in your browser.

## Add Your Own Images
- Place your images in `static/images/`. Any common format works (`.jpg`, `.png`, `.webp`).
- Edit `static/game_data.json` to describe each level. Example:

  ```json
  {
    "levels": [
      {
        "id": 1,
        "prompt": "Pick the AI‑generated image.",
        "options": [
          {"src": "/static/images/your_photo_1.jpg", "is_ai": false, "label": "A", "alt": "Photo A"},
          {"src": "/static/images/your_photo_2.jpg", "is_ai": true,  "label": "B", "alt": "Photo B"}
        ]
      }
    ]
  }
  ```

- `is_ai: true` marks the *correct* choice for that level.
- You can have 2–4 (or more) options per level.
- Keep three levels for the classic mode, or add more — the app adapts automatically.

## Tips
- Images should be reasonably sized (under a few MB) to keep loading snappy.
- You can rename the prompt per level to add hints or themes.
- If you change the folder or filenames, make sure the JSON `src` paths match (they should start with `/static/...`).

## Keyboard & Accessibility
- Use Tab/Shift+Tab to focus options, Enter/Space to pick.
- Feedback appears in the status bar; correct answers get a green outline.
- Buttons are disabled appropriately to prevent double clicks.

Have fun challenging your friends!
