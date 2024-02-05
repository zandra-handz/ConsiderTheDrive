import pytest
from project import menu_create_distance_object, menu_add_additional_friend, menu_print_results, Distance

api_key = "AIzaSyBAW09hdzlszciQ4fTiZjfxcVMlEkF5Iqk"

@pytest.fixture
def mock_user_input(monkeypatch):
    inputs = ["14 N Preston Street, Philadelphia, PA, 19104", "1234 Custer Creek Dr, Missouri City, TX", "Tim", "142 Turkey Hill Rd, Merrimack, NH", "Sarah", "n"]
    monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))


def test_menu_create_distance_object(mock_user_input):

    distance_object = menu_create_distance_object()

    assert isinstance(distance_object, Distance)

def test_menu_add_additional_friend(monkeypatch):

    inputs = ["120 River Road, Concord, NH", "Ashley", "n"]
    monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))
    
    friends = {"John": "1234 Custer Creek Drive, Missouri City, TX"}
    distance_object = Distance(api_key, origin_a="14 N Preston Street, Philadelphia, PA, 19104", destination="142 Turkey Hill Rd, Merrimack, NH", **friends)

    result = menu_add_additional_friend(distance_object)
    assert result is True  

def test_menu_print_results(capsys):
    friends = {"John": "1234 Custer Creek Drive, Missouri City, TX", "Sarah": "142 Turkey Hill Rd, Merrimack, NH"}
    distance_object = Distance(api_key, origin_a="14 N Preston Street, Philadelphia, PA, 19104", destination="142 Turkey Hill Rd, Merrimack, NH", **friends)
    distance_object.compare_directions = lambda many: {"John": {"duration": "1 hour", "distance": 10.5}, "Sarah": {"duration": "45 minutes", "distance": 8.0}}

    menu_print_results(distance_object)
    captured = capsys.readouterr()

    assert "Destination:" in captured.out
    assert "1: John - 1 hour" in captured.out
    assert "2: Sarah - 45 minutes" in captured.out