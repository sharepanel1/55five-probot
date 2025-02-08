import requests
from bs4 import BeautifulSoup
import random
import time

import logging
logger = logging.getLogger(__name__)

class Scraper:
    def get_live_data(self):
        try:
            logger.info("🔄 Mencoba mengambil data dari 55Five...")
            response = requests.get('https://551au.com/live', timeout=10)
            response.raise_for_status()  # Ini akan throw error jika response != 200
            logger.info("✅ Berhasil mengambil data")
            # ... (ekstrak data)
        except Exception as e:
            logger.error(f"🚨 Gagal scraping: {str(e)}")
            return []

class FiveScraper:
    def __init__(self):
        self.user_agents = [
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15'
        ]
    
    def get_live_data(self):
        try:
            headers = {'User-Agent': random.choice(self.user_agents)}
            response = requests.get('https://551au.com/live', headers=headers, timeout=10)
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Ekstrak data
            results = []
            for row in soup.select('.result-table tr'):
                cols = row.select('td')
                if len(cols) >= 3:
                    results.append({
                        'period': cols[0].text.strip(),
                        'numbers': cols[1].text.strip(),
                        'time': cols[2].text.strip()
                    })
            return results
        except:
            return self._fallback_api()

    def _fallback_api(self):
        # Jika scraping gagal, pakai API
        response = requests.post('https://551au.com/api/live', json={'page':1})
        return response.json()['data']
headers = {
       "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
       "Referer": "https://551au.com/"
   }
   response = requests.get(url, headers=headers)
