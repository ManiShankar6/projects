# Spotify Song Popularity Analysis

## 🎵 Objective
To understand the key audio features that influence a song's popularity on Spotify, using data extracted from the Spotify API and analyzing it through statistical, exploratory, and regression techniques.

## ❓ Research Question
**"What factors influence the popularity of songs on Spotify, and how can these factors be leveraged to improve song recommendations?"**

## 📊 Dataset Overview
We collected data for **18,000 songs** released between **January 2023 and present**, including:
- **Track Metadata**: Name, Artist, Track ID, Release Date, Popularity Score
- **Audio Features**: Danceability, Energy, Loudness, Speechiness, Acousticness, Instrumentalness, Liveness, Valence, Tempo, Duration

## ⚙️ Data Collection Process
- Used **Spotify API** with the `spotipy` Python library to extract metadata.
- Extracted audio features using manual API requests (bypassing Spotipy's `audio_features()` due to rate limits).
- Overcame **rate limiting (429 errors)** by chunking track IDs, rotating client credentials, and waiting strategically.

## 🧪 Analysis Conducted
1. **Descriptive Analysis**: Mean popularity score was 44.
2. **Distribution Plots**: Normal distributions for Danceability, Energy, and Tempo.
3. **Scatter Plots**:
   - Positive correlation: Danceability, Loudness → Popularity
   - Negative correlation: Instrumentalness, Valence → Popularity
4. **Correlation Heatmap**: Verified relationships between features.
5. **Regression Analysis**:
   - Significant predictors: Danceability (+), Loudness (+), Instrumentalness (−), Valence (−)
   - R² ≈ 0.14 → Suggests additional external factors influence popularity (e.g., artist fame).

## 🧠 Conclusion
- **Positive Impact**: Danceability, Loudness
- **Negative Impact**: Instrumentalness, Valence
- Recommendations can be improved by prioritizing high danceability/loudness and low instrumentalness/valence.

## 🔮 Future Work
- Integrate additional metadata (e.g., artist popularity, genre, playlist inclusion).
- Leverage ML models and clustering for mood/genre analysis.
- Incorporate user behavior and sentiment analysis.


## 📁 Files in This Repository
- `data_fetch.ipynb` → Spotify data extraction code
- `EDA.ipynb` → EDA and regression analysis
- `final_audio_features_dataset.csv` → Merged dataset used for analysis
- `README.md` → Project overview and documentation

---

## 🚀 How to Run This Project in Jupyter Notebook

Follow these steps to set up and run the project locally using Jupyter Notebook.

### 📥 Clone the Repository

```bash
git clone https://github.com/ManiShankar6/Projects.git
cd projects/spotify-popularity-analysis
```

### 🛠️ Set Up the Environment
**a. Create a Virtual Environment (Recommended)**

```bash
python -m venv venv
.\venv\Scripts\activate        # Windows PowerShell
# OR
source venv/bin/activate       # macOS/Linux
```

**b. Install Required Dependencies**

```bash
pip install -r requirements.txt
```

**📓 Launch Jupyter Notebook**
```bash
jupyter notebook
```

This will open Jupyter in your browser. Now:

- Open **`data_fetch.ipynb`**  
  ➤ Run this notebook to collect track metadata and audio features using the Spotify API.

- Open **`EDA.ipynb`**  
  ➤ Run this notebook to explore the dataset, visualize patterns, and perform regression analysis.
