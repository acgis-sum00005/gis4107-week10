# ------------------------------------------------------------------------------
# Name:        water_stn_converter.py
#
# Purpose:
#    Converts the provided JSON file to CSV or KML.
#    For the CSV, the output columns will be:
#      {Station_Number}, {Station_Name}, {Longitude}, {Latitude}, LINK
#
#    where LINK is
#    https://wateroffice.ec.gc.ca/report/real_time_e.html?stn={Station_Number}
#
#    Header for CSV will be:
#      StationNumber, StationName, Longitude, Latitude, WaterOfficeLink
#
#    For the KML, the <Placemark> element will have the following sub-elements:
#              <name>{Station_Name}</name>
#              <description>
#                 link
#              </description>
#              <Point>
#                <coordinates>{Longitude},{Latitude},0</coordinates>
#              </Point>
#
#   Items enclosed by { } are the keys in the dictionary associated with
#   each feature (a key:value dictionary of values).
#
# Author:      Your name(s)
#
# Created:     dd/mm/yyyy
# ------------------------------------------------------------------------------

import csv
import json

def json_to_csv(in_json_filename, out_csv_filename):
    """Converts a JSON file created using the water_stn_downloader module
    to CSV"""
    dict = load_json_file_to_dict(in_json_filename)

    with open(out_csv_filename, 'w', newline='') as out:

        features = dict['features']

        # Write the header to the CSV file
        #
        writer = csv.writer(out)
        writer.writerow(['StationNumber', 'StationName', 'Longitude', 'Latitude', 'WaterOfficeLink'])

        fields = ('Station_Number', 'Station_Name', 'Longitude', 'Latitude')
        # Loop through all the features and write the results to the CSV file
        #
        for feature in features:
            attrs = feature['attributes']
            values = [attrs[field] for field in fields]
            values.append(get_wateroffice_link(attrs['Station_Number']))
            writer.writerow(values)


def json_to_kml(in_json_filename, out_kml_filename):
    """Converts a JSON file created using the water_stn_downloader module
    to KML"""
    json_data = load_json_file_to_dict(in_json_filename)
    with open(out_kml_filename, 'w', newline='') as outfile:
        outfile.write(get_kml_header())
        for feature in json_data['features']:
            attrs = feature['attributes']
            wo_link = get_wateroffice_link(attrs['Station_Number'])
            placemark = get_placemark(attrs['Station_Name'], attrs['Longitude'], attrs['Latitude'], wo_link)
            outfile.write(placemark)
        outfile.write(get_kml_footer())


def load_json_file_to_dict(filename):
    """Use json.load(file_object) to convert the contents of in_json_filename
    to a Python dictionary.  Return the resulting dictionary.
    """
    # Use with to open in_json_filename and use that file object as an
    # argument to json.load.  This will return a Python dict with nested
    # lists and dictionaries
    with open(filename) as file:
        return json.load(file)


def get_values_from_feature(feature):
    """Given a dictionary of feature attributes, return the following:
        Station_Number, Station_name, Longitude, Latitude  """
    return feature['Station_Number'], feature['Station_Name'], feature['Longitude'], feature['Latitude']


def get_wateroffice_link(station_number):
    """Given a station_number, return the English wateroffice link"""
    return "https://wateroffice.ec.gc.ca/report/real_time_e.html?stn=" + station_number


def get_kml_header():
    """Return the xml header including the Document start tag
    """
    return '''<?xml version="1.0" encoding="UTF-8"?>
<kml xmlns="http://www.opengis.net/kml/2.2">
<Document>
'''


def get_kml_footer():
    """Return the document and kml end tags
    """
    return '''</Document>
</kml>
'''


def get_placemark(name, longitude, latitude, wateroffice_link):
    """Return the KML Placemark element including start and end tags
    """
    return f'''<Placemark>
    <name>{name}</name>
    <description>
        {wateroffice_link}
    </description>
    <Point>
        <coordinates>{longitude},{latitude},0</coordinates>
    </Point>
  </Placemark>
'''