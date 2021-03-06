from unittest import mock
import pytest
import requests

import astropy.units as u
from poliastro.twobody.angles import nu_to_M
from poliastro.neos import neows


@mock.patch('poliastro.neos.neows.requests.Response')
@mock.patch('poliastro.neos.neows.requests.get')
def test_orbit_from_spk_id_has_proper_values(mock_get, mock_response):
    mock_orbital_data = {
        'orbital_data': {
            'eccentricity': '.2225889698301071',
            'semi_major_axis': '1.457940027185708',
            'inclination': '10.82759100494802',
            'ascending_node_longitude': '304.3221633898424',
            'perihelion_argument': '178.8165910886752',
            'mean_anomaly': '71.28027812836476',
            "orbit_determination_date": "2017-06-06 06:20:43",
        }
    }

    mock_response.json.return_value = mock_orbital_data
    mock_get.return_value = mock_response
    ss = neows.orbit_from_spk_id('')

    assert ss.ecc == mock_orbital_data['orbital_data']['eccentricity'] * u.one
    assert ss.a == mock_orbital_data['orbital_data']['semi_major_axis'] * u.AU
    assert ss.inc == mock_orbital_data['orbital_data']['inclination'] * u.deg
    assert ss.raan == mock_orbital_data['orbital_data']['ascending_node_longitude'] * u.deg
    assert ss.argp == mock_orbital_data['orbital_data']['perihelion_argument'] * u.deg
    assert nu_to_M(ss.nu, ss.ecc) == mock_orbital_data['orbital_data']['mean_anomaly'] * u.deg


@mock.patch('poliastro.neos.neows.requests.get')
def test_orbit_from_spk_id_raises_when_error(mock_get):
    resp = requests.Response()

    resp.status_code = 404
    mock_get.return_value = resp   
    with pytest.raises(requests.HTTPError):
        ss = neows.orbit_from_spk_id('')


@mock.patch('poliastro.neos.neows.requests.get')
def test_spk_id_from_name_raises_when_error(mock_get):
    resp = requests.Response()

    resp.status_code = 404
    mock_get.return_value = resp
    with pytest.raises(requests.HTTPError):
        ss = neows.spk_id_from_name('')


@mock.patch('poliastro.neos.neows.requests.Response')
@mock.patch('poliastro.neos.neows.requests.get')
def test_spk_id_from_name_parses_body(mock_get, mock_response):
    with open('src/poliastro/tests/table.html', 'r') as demo_html:
        html = demo_html.read().replace('\n', '')
    
    mock_response.text = html
    mock_get.return_value = mock_response
    assert '2000433' == neows.spk_id_from_name('')


@mock.patch('poliastro.neos.neows.requests.Response')
@mock.patch('poliastro.neos.neows.requests.get')
def test_spk_id_from_name_parses_object_list_and_raises(mock_get, mock_response):
    with open('src/poliastro/tests/center.html', 'r') as demo_html:
        html = demo_html.read().replace('\n', '')

    mock_response.text = html
    mock_get.return_value = mock_response
    with pytest.raises(ValueError) as e_msg:
        neows.spk_id_from_name('')
        assert 'different bodies found' in str(e_msg)


@mock.patch('poliastro.neos.neows.requests.Response')
@mock.patch('poliastro.neos.neows.requests.get')
def test_spk_id_from_name_raises_when_not_found(mock_get, mock_response):
    with open('src/poliastro/tests/none.html', 'r') as demo_html:
        html = demo_html.read().replace('\n', '')
    mock_response.text = html
    mock_get.return_value = mock_response
    with pytest.raises(ValueError) as e_msg:
        neows.spk_id_from_name('')
        assert 'Object could not be found' in str(e_msg)
