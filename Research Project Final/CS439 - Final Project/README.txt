### How to Rerun This Notebook

1. Prepare your files  
Ensure the following files are in the notebook’s working directory:  
- `tiktok_dog_urls.txt` (the list of 100 scraped TikTok URLs)  
- `tiktok_dog_metrics.csv` (raw metrics after dropping unreliable fields)  
- `tiktok_dog_metrics_cleaned.csv` (abbreviations parsed, zeros removed)  
- `tiktok_dog_metrics_features.csv` (feature‐engineered dataset)  

2. **Install Python dependencies**  
import sys
!{sys.executable} -m pip install playwright
!{sys.executable} -m playwright install chromium
!{sys.executable} -m pip install wordcloud
!{sys.executable} -m pip install pandas
!{sys.executable} -m pip install matplotlib
!{sys.executable} -m pip install yt-dlp

Note: If you run the Playwright scraper inside this notebook, you’ll need playwright and to execute playwright install chromium once.

4. Execute all cells
In a fresh kernel, click Kernel → Restart & Run All, so each step (cleaning, EDA, feature engineering, clustering, modeling) runs in order.

5. Review outputs

Cleaned & feature CSVs:
tiktok_dog_metrics_pruned.csv
tiktok_dog_metrics_cleaned.csv
tiktok_dog_metrics_features.csv


Adjust file names or paths throughout if your directory structure differs!
