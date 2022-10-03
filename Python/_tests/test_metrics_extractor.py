import os
import sys

script_dir = os.path.dirname(__file__)
mymodule_dir = os.path.join(script_dir, '..', 'src')
sys.path.append(mymodule_dir)

import pytest
import metrics_extractor 

def test_station_list():
    stations_list = metrics_extractor.extract_data(
        '../../_samples/case1-london.stations.csv')
    
    assert stations_list == [['1', '51.5028', '-0.2801', 'Acton Town', 'Acton<br />Town', '1', '2', '0'], ['2', '51.5143', '-0.0755', 'Aldgate', 'NULL', '1', '2', '0'], ['3', '51.5154', '-0.0726', 'Aldgate East', 'Aldgate<br />East', '1', '2', '0'], ['4', '51.5107', '-0.013', 'All Saints', 'All<br />Saints', '1', '1', '0'], [
        '5', '51.5407', '-0.2997', 'Alperton', 'NULL', '2.5', '1', '0'], ['7', '51.5322', '-0.1058', 'Angel', 'NULL', '2', '1', '0'], ['8', '51.5653', '-0.1353', 'Archway', 'NULL', '3', '1', '0'], ['9', '51.6164', '-0.1331', 'Arnos Grove', 'Arnos<br />Grove', '2', '1', '0'], ['6', '51.6736', '-0.607', 'Amersham', 'NULL', '2', '1', '1']]

def test_line_list():
    lines_list = metrics_extractor.extract_data(
        '../../_samples/case1-london.lines.csv')

    assert lines_list == [
        ['13', 'Docklands Light Railway', '00A77E', 'FFFFFF']]

def test_connections_list():
    connections_list = metrics_extractor.extract_data(
        '../../_samples/case1-london.connections.csv')

    assert connections_list == [['1', '2', '13', '14'], ['1', '4', '13', '34'], ['1', '5', '13', '24'], ['2', '3', '13', '14'], [
        '3', '4', '13', '34'], ['3', '7', '13', '24'], ['4', '9', '13', '14'], ['5', '6', '13', '34'], ['7', '8', '13', '24'], ['8', '9', '13', '14']]

