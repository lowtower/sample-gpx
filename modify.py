"""Modify existing gpx tracks"""
from datetime import datetime, timedelta, timezone

import gpxpy

files = [
    "BrittanyJura/Alt_Portsmouth.gpx",
    "BrittanyJura/Basel_St-Brevin_Eurovelo6.gpx",
    "BrittanyJura/Courgenay_Ballon-DAlsace.gpx",
    "BrittanyJura/Dole_Langres.gpx",
    "BrittanyJura/Dole_Salin-les-Bains.gpx",
    "BrittanyJura/JuraRoute72011.gpx",
    "BrittanyJura/MoselradwegAusWiki.gpx",
    "BrittanyJura/Newhaven_Brighton.gpx",
    "BrittanyJura/Ouistreham_Caen.gpx",
    "BrittanyJura/Reims-VitryLeFrancois.gpx",
    "BrittanyJura/Salins-les-Bains_Fleurier.gpx",
    "BrittanyJura/Serqueaux_Dieppe.gpx",
    "BrittanyJura/Southampton_Portsmouth.gpx",
    "BrittanyJura/Vitry-le-Francois_Langres.gpx",
    "BrittanyJura/VoieVerteHauteVosges.gpx",
    "RoscoffCoastal/1_Roscoff_Morlaix_A_parcours.gpx",
    "RoscoffCoastal/Lannion_Plestin_parcours24.4RE.gpx",
    "RoscoffCoastal/parcours-morlaix-plougasnou.gpx",
    "RoscoffCoastal/Perros-Guirec_Trebeurden_parcours23.6RE.gpx",
    "RoscoffCoastal/Plougasou-plestin-parcours.gpx",
    "RoscoffCoastal/Roscoff_Perros-Guirec.gpx",
    "RoscoffCoastal/Trebeurden_Lannion_parcours13.2RE.gpx",
]
for file_name in files:
    with open(file_name, 'r', encoding='utf-8') as gpx_file:
        gpx = gpxpy.parse(gpx_file)
        time = datetime.now()
        if gpx.time:
            time = gpx.time.replace(tzinfo=timezone.utc)
        gpx.time = time
        for track in gpx.tracks:
            for segment in track.segments:
                for point in segment.points:
                    point.time = time
                    time = time + timedelta(seconds=10)
        with open(file_name, "w", encoding='utf-8') as f:
            f.write(gpx.to_xml())
