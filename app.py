from flask import Flask, render_template
import folium

app = Flask(__name__)

# ข้อมูลสถานที่และพิกัด
locations = [
    {
        "name": "ดอยสุเทพ",
        "lat": 18.818615919415542,
        "lon": 98.89227498790338,
        "description": "ปูชนียสถานคู่บ้านคู่เมืองเชียงใหม่ ตั้งตระหง่านบนดอยสูง จุดชมวิวเมืองเชียงใหม่แบบพาโนรามาที่สวยงามที่สุด",
        "image_url": "https://images.unsplash.com/photo-1574886617066-879796e95c1c?auto=format&fit=crop&q=80&w=800",
        "gmaps_url": "https://www.google.com/maps/dir/?api=1&destination=18.818615919415542,98.89227498790338"
    },
    {
        "name": "ประตูท่าแพ",
        "lat": 18.788534672245962,
        "lon": 98.99266598551255,
        "description": "แลนด์มาร์กประวัติศาสตร์ จุดถ่ายรูปยอดฮิตกับกำแพงอิฐสีส้มเก่าแก่และลานกว้างที่เป็นหัวใจของเมือง",
        "image_url": "https://images.unsplash.com/photo-1619888941706-0b1a0391d4e0?auto=format&fit=crop&q=80&w=800",
        "gmaps_url": "https://www.google.com/maps/dir/?api=1&destination=18.788534672245962,98.99266598551255"
    },
    {
        "name": "วัดพระธาตุดอยคำ",
        "lat": 18.761899053964935,
        "lon": 98.91836751432969,
        "description": "วัดเก่าแก่อายุกว่าพันปี โด่งดังเรื่ององค์หลวงพ่อทันใจและสถาปัตยกรรมล้านนาที่วิจิตรงดงาม",
        "image_url": "https://images.unsplash.com/photo-1596773347146-248dbfa0b9be?auto=format&fit=crop&q=80&w=800",
        "gmaps_url": "https://www.google.com/maps/dir/?api=1&destination=18.761899053964935,98.91836751432969"
    },
    {
        "name": "อ่างแก้ว มช.",
        "lat": 18.807957541756373,
        "lon": 98.95168771880381,
        "description": "อ่างเก็บน้ำในมหาวิทยาลัยเชียงใหม่ พื้นที่สีเขียวสุดชิลล์ บรรยากาศโรแมนติกที่เหมาะกับการพักผ่อนยามเย็น",
        "image_url": "https://images.unsplash.com/photo-1606132717834-318e95e8fc27?auto=format&fit=crop&q=80&w=800",
        "gmaps_url": "https://www.google.com/maps/dir/?api=1&destination=18.807957541756373,98.95168771880381"
    },
    {
        "name": "สวนสัตว์เชียงใหม่",
        "lat": 18.81144296067999,
        "lon": 98.9474780047453,
        "description": "แหล่งเรียนรู้และสัมผัสชีวิตสัตว์ป่านานาชนิด ท่ามกลางธรรมชาติที่ร่มรื่นบริเวณเชิงดอยสุเทพ",
        "image_url": "https://images.unsplash.com/photo-1564750247657-3a133dfd5975?auto=format&fit=crop&q=80&w=800",
        "gmaps_url": "https://www.google.com/maps/dir/?api=1&destination=18.81144296067999,98.9474780047453"
    }
]

@app.route('/')
def index():
    # กำหนดจุดศูนย์กลางแผนที่ (ค่าเฉลี่ยของพิกัดในเชียงใหม่)
    center_lat = sum([loc['lat'] for loc in locations]) / len(locations)
    center_lon = sum([loc['lon'] for loc in locations]) / len(locations)
    
    # สร้างแผนที่ Folium ในธีม Dark Mode
    m = folium.Map(
        location=[center_lat, center_lon], 
        zoom_start=12, 
        tiles='CartoDB dark_matter', # ธีมสีดำ ล้ำสมัย
        control_scale=True
    )

    # ปักหมุดลงบนแผนที่
    for loc in locations:
        folium.Marker(
            location=[loc['lat'], loc['lon']],
            popup=folium.Popup(f"<b style='font-family:sans-serif;'>{loc['name']}</b>", max_width=200),
            tooltip=loc['name'],
            icon=folium.Icon(color='black', icon_color='white', icon='info-sign')
        ).add_to(m)

    # แปลงแผนที่เป็น HTML
    map_html = m._repr_html_()

    return render_template('index.html', locations=locations, map_html=map_html)

if __name__ == '__main__':
    app.run(debug=True)