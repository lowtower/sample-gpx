"""Modify existing gpx tracks"""

import os
from datetime import timedelta, timezone

import gpxpy

files = [
    "1_Roscoff_Morlaix_A_parcours.gpx",
    "Lannion_Plestin_parcours24.4RE.gpx",
    "parcours-morlaix-plougasnou.gpx",
    "Perros-Guirec_Trebeurden_parcours23.6RE.gpx",
    "Plougasou-plestin-parcours.gpx",
    "Roscoff_Perros-Guirec.gpx",
    "Trebeurden_Lannion_parcours13.2RE.gpx",
]
for file in files:
    file_name = os.path.join("RoscoffCoastal", file)
    with open(file_name, 'r', encoding='utf-8') as gpx_file:
        gpx = gpxpy.parse(gpx_file)
        time = gpx.time
        for track in gpx.tracks:
            for segment in track.segments:
                time = time.replace(tzinfo=timezone.utc)
                for point in segment.points:
                    time = time + timedelta(seconds=10)
                    point.time = time
                    print(point)
        with open(file_name, "w", encoding='utf-8') as f:
            f.write(gpx.to_xml())
