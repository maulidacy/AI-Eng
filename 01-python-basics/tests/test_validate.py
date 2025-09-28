from CLI_Sederhana.csv2json import validate

def test_validate_pass():
    rows = [{"nama": "Andi", "umur": 20}, {"nama": "Budi", "umur": 25}]
    result = validate(rows, ["nama", "umur"])
    assert result is True # harus lolos validasi

def test_validate_missing():
    rows = [{"nama": "Siti"}]
    result = validate(rows, ["nama", "umur"])
    assert result is False # harus gagal validasi