rm output.html
rm *.csv 

python3 koeri-scraper.py 
python3 folium-heatmap.py 
firefox output.html
