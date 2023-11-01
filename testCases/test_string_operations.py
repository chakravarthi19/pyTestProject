import pytest
import re


@pytest.mark.smoke
@pytest.mark.regression
# Test string equality
def test_string_equality():
    assert "hello" == "hello"


@pytest.mark.smoke
@pytest.mark.regression
# Test string concatenation
def test_string_concatenation():
    assert "hello" + "world" == "helloworld"


@pytest.mark.smoke
@pytest.mark.regression
# Test string length
def test_string_length():
    assert len("hello") == 5


@pytest.mark.smoke
@pytest.mark.regression
# Test substring
def test_substring():
    assert "world" in "helloworld"


@pytest.mark.smoke
@pytest.mark.regression
# Test string contains
def test_string_contains():
    assert "apple" in "pineapple"


@pytest.mark.regression
# Test string case
def test_string_case():
    assert "hello".upper() == "HELLO"


@pytest.mark.regression
# Test string split
def test_string_split():
    assert "apple,banana,cherry".split(",") == ["apple", "banana", "cherry"]


@pytest.mark.regression
@pytest.mark.sanity
# Test string strip
def test_string_strip():
    assert "   hello   ".strip() == "hello"

@pytest.mark.regression
@pytest.mark.sanity
# Test string replace
def test_string_replace():
    assert "pineapple".replace("pine", "straw") == "strawapple"


@pytest.mark.regression
@pytest.mark.sanity
# Test string format
def test_string_format():
    assert "{} is {} years old".format("Alice", 30) == "Alice is 30 years old"


@pytest.mark.regression
# Test string encoding/decoding
def test_string_encoding_decoding():
    text = "Hello, 你好"
    encoded_text = text.encode("utf-8")
    decoded_text = encoded_text.decode("utf-8")
    assert text == decoded_text


@pytest.mark.regression
# Test regular expression
def test_regular_expression():
    pattern = r'\d+'  # Match one or more digits
    text = "There are 123 apples and 456 bananas."
    assert re.findall(pattern, text) == ['123', '456']


@pytest.mark.regression
# Test string uppercase
def test_string_uppercase():
    assert "hello".upper() == "HELLO"


@pytest.mark.regression
# Test string lowercase
def test_string_lowercase():
    assert "WORLD".lower() == "world"


@pytest.mark.regression
# Test string title case
def test_string_title_case():
    assert "the quick brown fox".title() == "The Quick Brown Fox"


@pytest.mark.regression
# Test string startswith
def test_string_startswith():
    assert "apple pie".startswith("apple")


@pytest.mark.regression
# Test string endswith
def test_string_endswith():
    assert "apple pie".endswith("pie")


@pytest.mark.regression
# Test string isdigit
def test_string_isdigit():
    assert "12345".isdigit()


@pytest.mark.regression
# Test string isalpha
def test_string_isalpha():
    assert "abc".isalpha()


@pytest.mark.regression
# Test string isalnum
def test_string_isalnum():
    assert "abc123".isalnum()


@pytest.mark.regression
# Test string count
def test_string_count():
    assert "mississippi".count("s") == 4


@pytest.mark.regression
# Test string find
def test_string_find():
    assert "hello world".find("world") == 6


@pytest.mark.xfail
# @pytest.mark.regression
# Test string splitlines
def test_string_splitlines():
    text = "Line 1\nLine 2\nLine 3"
    assert text.splitlines() == ["Line 1", "Line 2", "Line 3"]


@pytest.mark.xfail
# @pytest.mark.regression
# Test string join
def test_string_join():
    words = ["apple", "banana", "cherry"]
    assert ",".join(words) == "apple,banana,cherry"


@pytest.mark.xfail
# @pytest.mark.regression
# Test string reverse
def test_string_reverse():
    assert "hello"[::-1] == "olleh"
