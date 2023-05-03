import folium
import branca
import random

# 지도 생성 (초기 위치: 서울시청, 줌 레벨: 15)
map_center = [37.5665, 126.9780]
my_map = folium.Map(location=map_center, zoom_start=15)

# 랜덤 좌표 및 범주 생성
num_points = 50
categories = ['실내', '실외']

locations = [
    ([37.5665 + random.uniform(-0.01, 0.01), 126.9780 + random.uniform(-0.01, 0.01)], random.choice(categories))
    for _ in range(num_points)
]

# 실내 및 실외 FeatureGroup 생성
indoor_group = folium.FeatureGroup(name="실내")
outdoor_group = folium.FeatureGroup(name="실외")

# 지도에 마커 추가
for location, category in locations:
    if category == '실내':
        folium.Marker(location, icon=folium.Icon(color='blue'), popup=category).add_to(indoor_group)
    elif category == '실외':
        folium.Marker(location, icon=folium.Icon(color='red'), popup=category).add_to(outdoor_group)

indoor_group.add_to(my_map)
outdoor_group.add_to(my_map)

# 범례 생성
legend_html = '''
<div style="position: fixed; bottom: 50px; left: 50px; width: 100px; height: 100px; border:2px solid grey; z-index:9999; font-size:14px;">
    &nbsp;<b>Legend</b><br>
    &nbsp;<i class="fa fa-circle" style="color: blue;"></i>&nbsp;실내<br>
    &nbsp;<i class="fa fa-circle" style="color: red;"></i>&nbsp;실외<br>
</div>
'''

# 범례 추가
legend = branca.element.Html(legend_html, script=True)
my_map.get_root().html.add_child(legend)

# LayerControl 추가
folium.LayerControl().add_to(my_map)

# 지도를 HTML 파일로 저장
my_map.save('my_map_with_categories_and_filter.html')
