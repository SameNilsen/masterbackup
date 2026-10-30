def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]



METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def test_check():
    assert filter_by_prefix([], 'john') == []
    assert filter_by_prefix(['xxx', 'asd', 'xxy', 'john doe', 'xxxAAA', 'xxx'], 'xxx') == ['xxx', 'xxxAAA', 'xxx']


