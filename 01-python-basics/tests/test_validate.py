from csv2json import validate

def test_validate_pass():
    rows = [{"nama": "Andi", "umur": 20}, {"nama": "Budi", "umur": 25}]
    result = validate(rows, ["nama", "umur"])
    assert result == rows