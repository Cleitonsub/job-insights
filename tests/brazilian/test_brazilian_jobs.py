from src.pre_built.brazilian_jobs import read_brazilian_file


file = 'tests/mocks/brazilians_jobs.csv'


def test_brazilian_jobs():
    assert isinstance(read_brazilian_file(file), list)
    assert read_brazilian_file(file)[0] == {
        'title': 'Maquinista',
        'salary': '2000',
        'type': 'trainee'
    }
