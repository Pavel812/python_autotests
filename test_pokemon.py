import requests
import pytest

host = 'https://api.pokemonbattle.me:9104'

def test_status_code():
    checkstatuscode = requests.get(f'{host}/trainers', params={'trainer_id' : 2636 })
    assert checkstatuscode.status_code == 200

def test_checkname():
        
        checkname = requests.get(f'{host}/trainers', params={'trainer_id': 2636 })

        assert checkname.json()["trainer_name"] == "PAUL812"