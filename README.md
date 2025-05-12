# WMATA Live Train Tracker

A simple web app to display live train arrival times using the WMATA API.

## 🚀 Setup Instructions

1. Clone this repository:
   ```
   git clone https://github.com/your-username/wmata-tracker.git
   cd wmata-tracker
   ```

2. Create your environment file:
   ```
   cp .env.example .env
   ```

3. Edit the `.env` file and add your real WMATA API key:
   ```
   WMATA_API_KEY=your_real_key_here
   ```

4. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

5. Run the app:
   ```
   python app.py
   ```

6. Open a browser and visit [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

🛡️ **Note**: `.env` is in `.gitignore` to protect your API key.
